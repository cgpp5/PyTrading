# Issue — Indicator Pane Switch Failure

## Estado

Pendiente.

No se resuelve en esta iteracion. Se documenta para que un agente enfocado en UI lo tome despues.

---

## Resumen

La UI falla al cambiar desde un indicador en panel separado como ATR hacia un indicador overlay como Bollinger Bands.

El fallo ocurre en el frontend al limpiar el indicador actual antes de cargar el nuevo.

---

## Reproduccion

1. Ejecutar `python -m trading_ui.visual_test`.
2. Abrir la app en el navegador.
3. Cargar `AAPL / 1d`.
4. Seleccionar `ATR (14)`.
5. Cambiar a `Bollinger Bands (20, 2)`.

Resultado actual:

```text
Uncaught (in promise) Error: Assertion failed: Invalid pane index
    r https://unpkg.com/lightweight-charts@5.0/dist/lightweight-charts.standalone.production.js:7
    fc https://unpkg.com/lightweight-charts@5.0/dist/lightweight-charts.standalone.production.js:7
    removePane https://unpkg.com/lightweight-charts@5.0/dist/lightweight-charts.standalone.production.js:7
    clearIndicatorSeries http://localhost:8000/static/app.js:185
    loadIndicator http://localhost:8000/static/app.js:197
```

Resultado esperado:

* La UI debe remover ATR correctamente.
* La UI debe renderizar Bollinger Bands sin excepciones en consola.
* El cambio entre indicadores overlay y separate-pane debe ser seguro en ambas direcciones.

---

## Alcance funcional

El problema esta en la gestion del ciclo de vida de panes y series en Lightweight Charts v5.

Casos que deben funcionar:

* separate pane -> overlay
* overlay -> separate pane
* separate pane -> separate pane
* overlay -> overlay
* indicator -> ninguno

---

## Area sospechosa

Archivo principal:

* `frontend/app.js`

Funciones relevantes:

* `clearIndicatorSeries()`
* `loadIndicator()`

Variables de estado relevantes:

* `indicatorPane`
* `indicatorSeries`

La evidencia actual sugiere que el frontend conserva o intenta remover un pane con un indice que Lightweight Charts ya considera invalido.

---

## Contexto tecnico

TradingUI hoy mezcla dos modos de render:

* indicadores overlay en el pane principal del precio,
* indicadores en pane separado como ATR y MACD.

El bug aparece especificamente al cambiar entre esos modos.

Hay una alta probabilidad de que el problema no sea ATR en si, sino el contrato de limpieza y recreacion de panes en la capa frontend.

---

## Hipotesis a validar

1. `indicatorPane` queda referenciando un pane ya destruido o reindexado.
2. El frontend usa `chart.removePane(...)` en un momento en que la libreria ya removio implicitamente el pane al quitar series.
3. El pane se crea, pero las series no siempre quedan realmente asociadas al pane esperado.
4. El cambio de indicador ocurre con estado parcial cuando una promesa anterior termina tarde.

---

## Sugerencia de investigacion para el agente UI

1. Instrumentar temporalmente `frontend/app.js` con logs de:
   * `chart.panes().length`
   * `indicatorPane?.paneIndex()`
   * cantidad de `indicatorSeries`
   * `data.pane` recibido desde `/api/indicator`
2. Confirmar el contrato exacto de Lightweight Charts v5 para:
   * `addPane(preserveEmptyPane?)`
   * `removePane(index)`
   * `addSeries(..., paneIndex)`
   * autoremocion de panes vacios
3. Verificar si el enfoque correcto es:
   * remover solo series y dejar que el pane desaparezca,
   * o preservar el pane vacio y reutilizarlo,
   * o crear series directamente con `pane.addSeries(...)` en vez de `chart.addSeries(..., paneIndex)`.
4. Revisar condiciones de carrera entre cambios rapidos de selector.

---

## Criterio de aceptacion

Se considera resuelto cuando:

* no hay excepciones en consola al alternar indicadores,
* ATR y MACD renderizan en panel separado consistentemente,
* Bollinger renderiza como overlay consistentemente,
* el visual test soporta cambios repetidos entre indicadores sin degradarse.

---

## Archivos relacionados

* `frontend/app.js`
* `frontend/index.html`
* `trading_ui/server.py`
* `trading_ui/visual_test.py`
* `tests/test_trading_ui_api.py`

---

## Nota

Este issue se documenta para trabajo posterior. No se debe seguir iterando el debug en esta tarea.