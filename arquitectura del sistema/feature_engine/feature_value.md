feature\_value

domingo, 1 de marzo de 2026

20:47

**Entidad conceptual: FeatureValue**

Un FeatureValue representa **el valor de una feature en un timestamp concreto**, junto con el contexto mínimo necesario para interpretarlo correctamente.

Debe contener:

* **identidad semántica** (qué feature es),
* **valor numérico**,
* **estado de calidad**,
* **versión semántica**.

**Contrato de serialización (forma canónica)**

Cada feature se serializa en el JSON del DataStore como una entrada independiente, con esta estructura:

{
 "mcclellan\_oscillator@1.0": {
 "value": -123.45,
 "quality": "ready"
 }
}

**Invariantes**

* La clave **siempre** es name@version.
* value es escalar (float | int).
* quality es un valor de FeatureQuality.
* No se permiten estructuras anidadas arbitrarias.
* No se permite omitir quality.

Esto convierte el JSON en un **registro semántico**, no en un simple diccionario de columnas.

**Cómo encaja con tu DataStore actual**

Cambia el contenido del campo features:

{
 "rsi\_14@1.0": {"value": 42.3, "quality": "ready"},
 "sma\_50@1.0": {"value": 398.1, "quality": "warmup"}
}

Esto mantiene:

* esquema híbrido,
* UPSERT,
* compatibilidad con SQLite,
* flexibilidad futura.

Y añade:

* versionado,
* auditabilidad,
* trazabilidad de degradación.

**Responsabilidades por capa (muy importante)**

**FeatureEngine**

* Produce FeatureValue (valor + calidad).
* Conoce FeatureSpec.
* Decide quality.

**DataStore**

* **No interpreta** features.
* Valida estructura mínima.
* Persiste y reconstruye fielmente.

**Consumidores (StrategyLogic, UI)**

* Reciben DataFrame reconstruido.
* Pueden:
  + usar solo valores READY,
  + o reaccionar a DEGRADED.

**Validaciones mínimas en DataStore (recomendadas)**

Antes de escribir el JSON:

* La clave debe contener @.
* El valor debe ser un dict con:
  + value,
  + quality.
* quality debe ser un string válido de FeatureQuality.

Si no se cumple, se falla **antes de escribir**.

Esto evita corrupción silenciosa del SSOT.

**Reconstrucción al leer**

Al hacer load\_market\_data:

* El DataFrame puede:
  + exponer solo value como columna (modo simple),
  + o exponer columnas paralelas:
    - rsi\_14@1.0,
    - rsi\_14@1.0\_\_quality.

Esto se puede decidir más adelante sin cambiar el contrato en disco.