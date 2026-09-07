const { useState, useEffect, useRef, useCallback, useId } = React;
const { createChart, CandlestickSeries, HistogramSeries, LineSeries, LineStyle } = LightweightCharts;

const THEMES = {
  blue: "bg-[#0044FF]/20 text-[#0044FF] border-[#0044FF]/30",
  blueDim: "bg-[#0044FF]/10 text-[#0044FF] border-[#0044FF]/20",
  teal: "bg-[#009D88]/20 text-[#009D88] border-[#009D88]/30",
  tealDim: "bg-[#009D88]/10 text-[#009D88] border-[#009D88]/20",
  red: "bg-[#BD1A27]/20 text-[#BD1A27] border-[#BD1A27]/30",
  sage: "bg-[#99C69B]/20 text-[#99C69B] border-[#99C69B]/30",
  slate: "bg-slate-800 text-slate-400 border-white/10"
};

const Badge = ({ text, themeClass, onClick }) => (
  <span 
    onClick={onClick} 
    title="Click to remove"
    className={`text-[8px] px-[6px] py-[0.5px] rounded-full uppercase font-bold border inline-flex items-center cursor-pointer hover:opacity-70 ${themeClass}`}>
    {text}
  </span>
);

async function fetchJSON(url) {
    const resp = await fetch(url);
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    return resp.json();
}

// ---------------------------------------------------------------------------
// SymbolInput — combobox de símbolo.
//
// Es un <input> con un <datalist> de símbolos ya cacheados (autocompletado),
// pero permite escribir CUALQUIER ticker.  El símbolo sólo se "confirma" al
// pulsar Enter o al salir del campo (blur): así no disparamos una descarga
// por cada tecla.  El backend auto-descarga el símbolo si no está cacheado.
// ---------------------------------------------------------------------------
const SymbolInput = ({ value, onChange, symbols = [], className = "" }) => {
    const [open, setOpen] = useState(false);
    const [text, setText] = useState(value);
    const [query, setQuery] = useState("");
    const [active, setActive] = useState(-1);
    const [dropPos, setDropPos] = useState(null); // {top, left, width}
    const rootRef = useRef(null);
    const inputRef = useRef(null);

    const filtered = (symbols || []).filter(s => s.includes(query));
    const known = symbols.includes(value);

    // Cerrar el desplegable al hacer clic fuera.
    useEffect(() => {
        const onDocClick = (e) => {
            if (rootRef.current && !rootRef.current.contains(e.target)) setOpen(false);
        };
        document.addEventListener('mousedown', onDocClick);
        return () => document.removeEventListener('mousedown', onDocClick);
    }, []);

    // Calcula la posición (viewport) del desplegable. Usamos `position: fixed`
    // para que ningún ancestro con `overflow-hidden` (p. ej. la cabecera del
    // ChartCard) lo recorte.
    const openDropdown = () => {
        const el = inputRef.current;
        if (!el) return;
        const rect = el.getBoundingClientRect();
        const width = Math.max(rect.width, 180);
        const left = Math.max(4, Math.min(rect.left, window.innerWidth - width - 4));
        setDropPos({ top: rect.bottom + 4, left, width });
        setOpen(true);
    };

    const commit = (raw) => {
        const next = (raw === undefined ? text : raw).trim().toUpperCase();
        setOpen(false);
        setActive(-1);
        setText(next);
        setQuery("");
        if (next && next !== value) onChange(next);
    };

    const onKeyDown = (e) => {
        if (e.key === 'ArrowDown') {
            e.preventDefault();
            openDropdown();
            setActive(a => Math.min(a + 1, filtered.length - 1));
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            setActive(a => Math.max(a - 1, -1));
        } else if (e.key === 'Enter') {
            e.preventDefault();
            if (active >= 0 && active < filtered.length) commit(filtered[active]);
            else commit();
        } else if (e.key === 'Escape') {
            setOpen(false);
        }
    };

    return (
        <div className={`relative ${className}`} ref={rootRef}>
            {/* Símbolo + chevron-down (SVG real) */}
            <div className="flex items-center gap-1">
                <input
                    ref={inputRef}
                    className="font-headline font-bold text-[9px] tracking-tight uppercase bg-transparent min-w-0 h-6 focus:outline-none focus:ring-0 border-none outline-none"
                    value={open ? text : value}
                    placeholder="SYMBOL"
                    spellCheck={false}
                    autoComplete="off"
                    title="Escribe cualquier ticker o elige de los cacheados"
                    onFocus={e => {
                        // Al enfocar: muestra todos los cacheados y selecciona el
                        // texto actual para reemplazarlo al teclear.
                        setText(value);
                        setQuery("");
                        setActive(-1);
                        openDropdown();
                        try { e.target.select(); } catch { /* noop */ }
                    }}
                    onChange={e => {
                        setText(e.target.value);
                        setQuery(e.target.value.trim().toUpperCase());
                        setActive(-1);
                        openDropdown();
                    }}
                    onKeyDown={onKeyDown}
                    onBlur={() => setTimeout(() => setOpen(false), 120)}
                />
                {/* Chevron SVGs real: verde = en caché, ámbar = se descargará.
                    Rota 180° cuando el desplegable está abierto. */}
                <button
                    type="button"
                    aria-label="Seleccionar símbolo"
                    aria-expanded={open}
                    onClick={() => { openDropdown(); inputRef.current?.focus(); }}
                    className="shrink-0 flex items-center justify-center transition-colors text-white/60 hover:text-white"
                    title={value && known ? 'En caché' : value ? 'No en caché (se descargará)' : 'Seleccionar símbolo'}
                >
                    <svg
                        className={`transition-transform duration-150 ${open ? 'rotate-180' : ''}`}
                        width="10"
                        height="10"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2.5"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        aria-hidden="true"
                    >
                        <polyline points="6 9 12 15 18 9" />
                    </svg>
                </button>
            </div>

            {/* Desplegable de tickers cacheados (posición fija: escapa del clipping) */}
            {open && dropPos && (
                <div
                    className="fixed z-[200] bg-[#0F0F0F] border border-white/20 rounded shadow-xl overflow-y-auto"
                    style={{ top: dropPos.top, left: dropPos.left, width: dropPos.width, maxHeight: 208 }}
                >
                    {filtered.length === 0 ? (
                        <div className="px-2 py-1.5 text-[8px] uppercase tracking-widest text-amber-400/80">
                            {query ? `"${query}" no está en caché` : 'No hay símbolos en caché'}
                        </div>
                    ) : (
                        filtered.map((s, i) => (
                            <button
                                key={s}
                                type="button"
                                onMouseDown={(e) => { e.preventDefault(); commit(s); }}
                                className={`block w-full text-left px-2 py-1 text-[9px] font-mono uppercase tracking-wide ${i === active ? 'bg-white/10 text-white' : 'text-slate-300 hover:bg-white/5'}`}
                            >
                                {s}
                            </button>
                        ))
                    )}
                </div>
            )}
        </div>
    );
};

// ---------------------------------------------------------------------------
// TimeframeSelect — selector de resolución con chevron blanco bien posicionado.
//
// Usa `<select appearance-none bg-none>` y reserva padding a la derecha
// (`pr-3`) para que el texto NO quede debajo del chevron. Sin esto, el plugin
// de Tailwind inyecta un chevron como `background-image` que se solapa con el
// texto cuando el select es estrecho y no tiene padding.
// ---------------------------------------------------------------------------
const TimeframeSelect = ({ value, onChange, timeframes = [], className = "" }) => (
    <div className={`relative inline-flex items-center ${className}`}>
        <select
            className="bg-transparent appearance-none bg-none text-terminal text-slate-400 font-mono border-none cursor-pointer p-0 h-6 focus:outline-none focus:ring-0 pr-3"
            value={value}
            onChange={e => onChange(e.target.value)}
            title="Change Timeframe"
        >
            {timeframes.map(tf => <option key={tf} value={tf}>{tf}</option>)}
        </select>
        {/* Chevron blanco (SVG real), posicionado a la derecha sin solaparse. */}
        <svg
            className="pointer-events-none absolute right-0 text-white/60"
            width="9"
            height="9"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.5"
            strokeLinecap="round"
            strokeLinejoin="round"
            aria-hidden="true"
        >
            <polyline points="6 9 12 15 18 9" />
        </svg>
    </div>
);

// ---------------------------------------------------------------------------
// Sincronización de escalas de tiempo entre gráficos de un mismo grupo.
//
// En la Detail Screen, el gráfico principal y los sub-panes deben compartir el
// mismo eje temporal: si haces zoom o pan en uno, el resto debe seguirlo.
// Lightweight Charts v5 expone `timeScale().subscribeVisibleLogicalRangeChange`
// (cambio de rango lógico = índice de barras) y `timeScale().setVisibleLogicalRange`.
//
// Usamos rangos LÓGICOS (índices de barras) en lugar de timestamps. Como todos
// los gráficos del grupo cargan el mismo OHLCV (misma cantidad de barras), el
// rango lógico es directamente comparable entre ellos.
//
// Un flag `lock` evita el bucle infinito: al propagar un rango, el
// `setVisibleLogicalRange` vuelve a disparar el callback del propio gráfico,
// que se ignora mientras `lock` está activo.
// ---------------------------------------------------------------------------
const timeScaleSyncGroups = {};

function _getOrCreateSyncGroup(syncId) {
    if (!timeScaleSyncGroups[syncId]) {
        timeScaleSyncGroups[syncId] = { charts: [], lock: false };
    }
    return timeScaleSyncGroups[syncId];
}

function linkChartToSyncGroup(syncId, chart) {
    const group = _getOrCreateSyncGroup(syncId);
    if (group.charts.includes(chart)) return;

    // Si el grupo ya tiene un gráfico (p. ej. el principal), el nuevo
    // sub-pane adopta su rango visible actual en lugar de resetear a fit-all.
    const existing = group.charts[0];
    if (existing) {
        const range = existing.timeScale().getVisibleLogicalRange();
        if (range) chart.timeScale().setVisibleLogicalRange(range);
    }

    group.charts.push(chart);
    chart.timeScale().subscribeVisibleLogicalRangeChange(range => {
        if (!range || group.lock) return;
        group.lock = true;
        try {
            group.charts.forEach(c => {
                if (c !== chart) c.timeScale().setVisibleLogicalRange(range);
            });
        } finally {
            group.lock = false;
        }
    });
}

function unlinkChartFromSyncGroup(syncId, chart) {
    const group = timeScaleSyncGroups[syncId];
    if (!group) return;
    const idx = group.charts.indexOf(chart);
    if (idx >= 0) group.charts.splice(idx, 1);
    if (group.charts.length === 0) delete timeScaleSyncGroups[syncId];
}

// ---------------------------------------------------------------------------
// Gestión de panes (sub-panes separados) de Lightweight Charts v5.
//
// En v5 cada `addPane()` crea un panel con su propio divisor. Si añades un
// indicador de panel separado (MACD, ADX, ATR, SMA Osc) y luego lo quitas, hay
// que eliminar también su panel, no solo sus series. `removePane` espera un
// ÍNDICE numérico (no el objeto de panel), así que lo resolvemos con
// `chart.panes().indexOf(pane)`.
// ---------------------------------------------------------------------------
function removePaneByApi(chart, pane) {
    if (!chart || !pane) return;
    const idx = chart.panes().indexOf(pane);
    if (idx >= 0) chart.removePane(idx);
}

// Elimina todas las series y panes de indicadores registrados en *refs*.
function clearIndicatorRefs(chart, seriesRef, paneRef) {
    if (!chart) return;
    Object.keys(seriesRef.current).forEach(key => {
        seriesRef.current[key].forEach(s => chart.removeSeries(s));
        removePaneByApi(chart, paneRef.current[key]);
    });
    seriesRef.current = {};
    paneRef.current = {};
}

// ---------------------------------------------------------------------------
// PriceChart — gráfico reutilizable (velas + volumen + indicadores)
// Compartido por el Wall Monitor (ChartCard) y la Detail Screen.
//
// `syncId`: si se proporciona, este gráfico se sincroniza (zoom/pan) con todos
// los demás gráficos que usan el mismo `syncId` (p. ej. en un futuro layout de
// varios gráficos enlazados). Hoy ningún componente lo usa (la Detail Screen
// es un único gráfico y la Wall Monitor mantiene ventanas independientes), por
// lo que queda como utilidad para layouts multi-gráfico.
// ---------------------------------------------------------------------------
const PriceChart = ({ symbol, timeframe, indicators = [], onPrice, syncId }) => {
    const chartContainerRef = useRef(null);
    const chartRef = useRef(null);
    const candleSeriesRef = useRef(null);
    const volumeSeriesRef = useRef(null);
    const indicatorSeriesRefs = useRef({});
    const indicatorPaneRefs = useRef({});
    // Clave de símbolo|timeframe para saber cuándo reiniciar todo (evita
    // paneles huérfanos al cambiar de instrumento).
    const lastKeyRef = useRef('');

    const [status, setStatus] = useState("Loading...");
    // Mensaje cuando el símbolo no tiene datos (ticker inexistente / sin datos).
    const [emptyMsg, setEmptyMsg] = useState(null);

    // 1. Initialize the Lightweight Chart
    //
    // Importante (bug corregido): el contenedor del gráfico debe quedar SIN
    // hijos gestionados por React. Lightweight Charts inyecta su propio DOM
    // (canvas) imperativamente; si React reconcilia hijos dentro de ese
    // contenedor (p. ej. un <span> de estado), borra el DOM del gráfico al
    // re-renderizar. Por eso el estado se pinta como *hermano*, no como hijo.
    //
    // También: con `autoSize: true` NO se debe llamar manualmente a
    // `chart.applyOptions({ width, height })` (el código antiguo lo hacía con
    // un ResizeObserver propio y desmontaba el gráfico al cambiar de tamaño).
    useEffect(() => {
        const c = chartContainerRef.current;
        if (!c) return;

        const chart = createChart(c, {
            autoSize: true,
            layout: {
                // Design System: fondo TRANSPARENTE (la superficie del
                // ChartCard es la que aporta el color `#0F0F0F`; en la
                // Detail Screen el fondo general `#000`).
                background: { type: 'solid', color: 'transparent' },
                // Texto de ejes en Slate 400 (datos secundarios del sistema).
                textColor: '#94a3b8',
                fontFamily: 'JetBrains Mono',
                fontSize: 9
            },
            // Design System: SIN gridlines.
            grid: {
                vertLines: { color: 'transparent' },
                horzLines: { color: 'transparent' }
            },
            timeScale: {
                timeVisible: true,
                secondsVisible: false,
                borderColor: 'rgba(255,255,255,0.1)'
            },
            rightPriceScale: {
                borderColor: 'rgba(255,255,255,0.1)'
            },
            crosshair: { mode: 0 }
        });

        chartRef.current = chart;
        if (syncId) linkChartToSyncGroup(syncId, chart);

        return () => {
            if (syncId) unlinkChartFromSyncGroup(syncId, chart);
            chart.remove();
            chartRef.current = null;
        };
    }, [syncId]);

    // 4. Load OHLCV data
    useEffect(() => {
        if (!chartRef.current || !symbol || !timeframe) return;

        // Clear existing OHLCV series
        if (candleSeriesRef.current) chartRef.current.removeSeries(candleSeriesRef.current);
        if (volumeSeriesRef.current) chartRef.current.removeSeries(volumeSeriesRef.current);

        candleSeriesRef.current = chartRef.current.addSeries(CandlestickSeries, {
            upColor: '#4DFF54', 
            downColor: '#BD1A27',
            borderUpColor: '#4DFF54', 
            borderDownColor: '#BD1A27',
            wickUpColor: '#4DFF54', 
            wickDownColor: '#BD1A27',
        });

        // El volumen se superpone en el panel principal (no se crea un panel
        // separado): así no aparece un divisor innecesario entre precio y
        // volumen. Se dibuja en la franja inferior mediante su propia escala
        // de precios y `scaleMargins`.
        volumeSeriesRef.current = chartRef.current.addSeries(HistogramSeries, {
            color: '#1e293b',
            priceFormat: { type: 'volume' },
            priceScaleId: 'volume',
        });

        volumeSeriesRef.current.priceScale().applyOptions({
            scaleMargins: { top: 0.8, bottom: 0 }
        });

        setStatus("Fetching data...");
        setEmptyMsg(null);
        fetchJSON(`/api/ohlcv?symbol=${symbol}&timeframe=${timeframe}`)
            .then(data => {
                candleSeriesRef.current.setData(data.candles);
                volumeSeriesRef.current.setData(data.volume);
                if (data.candles.length > 0) chartRef.current.timeScale().fitContent();

                const ok = data.status === "ok" && data.candles.length > 0;
                setEmptyMsg(ok ? null : (data.message || `No data available for ${symbol}`));

                if (onPrice && data.candles.length > 0) {
                    const last = data.candles[data.candles.length - 1];
                    const prev = data.candles.length > 1 ? data.candles[data.candles.length - 2] : null;
                    const change = prev ? ((last.close - prev.close) / prev.close) * 100 : 0;
                    onPrice(last.close, change);
                }
                setStatus("");
            })
            .catch(err => setStatus(`Error: ${err.message}`));

    }, [symbol, timeframe]);

    // 5. Load and synchronize Indicators
    //
    // Gestión de paneles separados:
    //   - Un indicador de panel separado (MACD/ADX/ATR/SMA Osc) crea UN único
    //     panel (no uno por serie). Se guarda en `indicatorPaneRefs`.
    //   - Al quitar el indicador se eliminan sus series Y su panel (para que no
    //     queden divisores huérfanos).
    //   - Al cambiar de símbolo/timeframe se limpian todos los paneles/series
    //     de indicadores para evitar basura al recargar.
    useEffect(() => {
        if (!chartRef.current || !symbol || !timeframe) return;
        const chart = chartRef.current;

        const key = `${symbol}|${timeframe}`;
        if (lastKeyRef.current !== key) {
            // Cambió el instrumento → limpiar indicadores y paneles antiguos.
            clearIndicatorRefs(chart, indicatorSeriesRefs, indicatorPaneRefs);
            lastKeyRef.current = key;
        }

        // Clean up indicators that were removed
        Object.keys(indicatorSeriesRefs.current).forEach(key2 => {
            if (!indicators.includes(key2)) {
                indicatorSeriesRefs.current[key2].forEach(s => chart.removeSeries(s));
                removePaneByApi(chart, indicatorPaneRefs.current[key2]);
                delete indicatorSeriesRefs.current[key2];
                delete indicatorPaneRefs.current[key2];
            }
        });

        // Fetch and add new indicators
        indicators.forEach(indicatorKey => {
            if (!indicatorSeriesRefs.current[indicatorKey]) {
                fetchJSON(`/api/indicator?symbol=${symbol}&timeframe=${timeframe}&indicator=${indicatorKey}`)
                    .then(data => {
                        if (!data.series) return;

                        const isSeparatePane = data.overlay === false || data.pane !== 'overlay';
                        const createdSeries = [];

                        // Crear el panel UNA sola vez por indicador.
                        let targetPane = chart;
                        if (isSeparatePane && chart.addPane) {
                            targetPane = chart.addPane({ height: 120 });
                            indicatorPaneRefs.current[indicatorKey] = targetPane;
                        }

                        data.series.forEach(sConfig => {
                            let seriesOptions = {
                                color: sConfig.color || '#fff',
                                lineWidth: sConfig.lineWidth || 2
                            };

                            // Map a semantic lineStyle string to the
                            // Lightweight Charts LineStyle enum.
                            if (sConfig.lineStyle === 'dotted') {
                                seriesOptions.lineStyle = LineStyle.Dotted;
                            } else if (sConfig.lineStyle === 'dashed') {
                                seriesOptions.lineStyle = LineStyle.Dashed;
                            }

                            // Determine series type
                            let isHistogram = false;
                            if (sConfig.seriesType === 'histogram' || (data.kind === 'macd' && sConfig.label.toLowerCase() === 'histogram')) {
                                isHistogram = true;
                            }

                            if (isSeparatePane) {
                                // El panel separado tiene su propia escala de precios.
                                seriesOptions.priceScaleId = data.kind;
                            }

                            let s;
                            if (isHistogram) {
                                s = targetPane.addSeries(HistogramSeries, seriesOptions);
                            } else {
                                s = targetPane.addSeries(LineSeries, seriesOptions);
                            }

                            s.setData(sConfig.data);
                            createdSeries.push(s);

                            // Apply scale margins if it's a sub-pane
                            if (isSeparatePane) {
                                s.priceScale().applyOptions({
                                    scaleMargins: { top: 0.2, bottom: 0.05 }
                                });
                            }
                        });
                        indicatorSeriesRefs.current[indicatorKey] = createdSeries;
                    })
                    .catch(console.error);
            }
        });

    }, [symbol, timeframe, indicators]);

    return (
        <div className="relative flex-1 min-h-0 overflow-hidden">
            {/* Contenedor del gráfico: vacío (sin hijos de React) para que LWC
                sea su único gestor y no se pierda al re-renderizar. */}
            <div ref={chartContainerRef} className="absolute inset-0" />
            {/* Estado como hermano superpuesto, nunca dentro del contenedor. */}
            {status && (
                <span className="absolute top-1 left-2 z-20 text-[8px] text-slate-500 animate-pulse">{status}</span>
            )}
            {/* Feedback de ticker sin datos (no encontrado / sin datos). */}
            {emptyMsg && (
                <div className="absolute inset-0 z-20 flex items-center justify-center pointer-events-none">
                    <div className="text-center px-4">
                        <div className="material-symbols-outlined text-3xl text-slate-600 mb-2">search_off</div>
                        <div className="font-headline text-xs uppercase tracking-widest text-slate-300">{symbol}</div>
                        <div className="text-[10px] text-slate-500 mt-1 max-w-[260px]">{emptyMsg}</div>
                    </div>
                </div>
            )}
        </div>
    );
};

// ---------------------------------------------------------------------------
// ChartCard — ventana del Wall Monitor (cabecera interactiva + PriceChart)
// ---------------------------------------------------------------------------
const ChartCard = ({ window, updateWindow, onClose, addWindowFrom, onMaximize }) => {
    const [symbols, setSymbols] = useState([]);
    const [timeframes, setTimeframes] = useState([]);
    const [availableIndicators, setAvailableIndicators] = useState([]);

    const [lastPrice, setLastPrice] = useState(0);
    const [priceChange, setPriceChange] = useState(0);

    // 1. Fetch available symbols and timeframes
    useEffect(() => {
        fetchJSON('/api/symbols').then(d => setSymbols(d.symbols || [])).catch(console.error);
        fetchJSON('/api/timeframes').then(d => setTimeframes(d.timeframes || [])).catch(console.error);
    }, []);

    // 2. Fetch available indicators when symbol/timeframe changes
    useEffect(() => {
        if (window.symbol && window.timeframe) {
            fetchJSON(`/api/available-indicators?symbol=${window.symbol}&timeframe=${window.timeframe}`)
                .then(d => setAvailableIndicators(d.indicators || []))
                .catch(console.error);
        }
    }, [window.symbol, window.timeframe]);

    const priceColor = priceChange >= 0 ? "text-[#4DFF54]" : "text-[#BD1A27]";
    const priceStr = lastPrice.toFixed(2);
    const changeStr = (priceChange >= 0 ? "+" : "") + priceChange.toFixed(2) + "%";

    return (
        <div className="bg-[#0F0F0F] border-[0.5px] border-white/30 flex flex-col overflow-hidden relative shadow-xl h-full w-full min-h-0 min-w-0">
            {/* Cabecera del Gráfico */}
            <div className="flex justify-between items-center px-2 py-1 bg-black/40 border-b-[0.5px] border-white/10 z-10">
                <div className="flex items-center space-x-2 overflow-hidden">

                    {/* Símbolo (combobox: escribe cualquier ticker o elige de los cacheados) */}
                    <SymbolInput
                        value={window.symbol}
                        onChange={v => updateWindow({ symbol: v })}
                        symbols={symbols}
                        className="font-headline font-bold text-terminal tracking-tight whitespace-nowrap text-white border-none cursor-text hover:bg-white/10 px-1 focus:ring-0 focus:outline-none w-20"
                    />

                    {/* Timeframe */}
                    <TimeframeSelect
                        value={window.timeframe}
                        onChange={v => updateWindow({ timeframe: v })}
                        timeframes={timeframes}
                    />

                    {/* Active Indicators */}
                    <div className="flex space-x-1 items-center">
                        {window.indicators.map(ind => {
                            const name = ind.split('@')[0].replace(/_/g, ' ');
                            return (
                                <Badge
                                    key={ind}
                                    text={name}
                                    themeClass={THEMES.blue}
                                    onClick={() => {
                                        updateWindow({ indicators: window.indicators.filter(i => i !== ind) });
                                    }}
                                />
                            );
                        })}

                        {/* Add Indicator Select */}
                        <select
                            className="bg-transparent text-terminal text-slate-500 border-none opacity-50 hover:opacity-100 hover:text-white p-0 cursor-pointer focus:ring-0 text-[8px] appearance-none h-6"
                            value=""
                            onChange={e => {
                                if(e.target.value && !window.indicators.includes(e.target.value)) {
                                    updateWindow({ indicators: [...window.indicators, e.target.value] });
                                }
                            }}
                            title="Add Indicator"
                        >
                            <option value="">+ ADD</option>
                            {availableIndicators.filter(i => !window.indicators.includes(i.key)).map(i => (
                                <option key={i.key} value={i.key}>{i.name}</option>
                            ))}
                        </select>
                    </div>

                </div>

                <div className="flex items-center space-x-2">
                    {/* Precio en vivo: alineado a la derecha, Mono, coloreado dinámicamente */}
                    <span className={`font-mono text-terminal h-6 flex items-center ${priceColor}`}>
                        {priceStr} ({changeStr})
                    </span>
                    <div className="flex items-center space-x-1">
                        <button className="material-symbols-outlined flex items-center justify-center h-6 w-6 text-slate-400 hover:text-white transition-colors" onClick={() => onMaximize && onMaximize(window)} title="Open Detail Screen">fullscreen</button>
                        <button className="material-symbols-outlined flex items-center justify-center h-6 w-6 text-slate-400 hover:text-white transition-colors" onClick={() => addWindowFrom(window)} title="Clone Window">add_box</button>
                        <button className="material-symbols-outlined flex items-center justify-center h-6 w-6 text-slate-400 hover:text-white transition-colors" onClick={onClose} title="Close Window">close</button>
                    </div>
                </div>
            </div>

            {/* Gráfico */}
            <PriceChart
                symbol={window.symbol}
                timeframe={window.timeframe}
                indicators={window.indicators}
                onPrice={(price, change) => { setLastPrice(price); setPriceChange(change); }}
            />
        </div>
    );
};

// ---------------------------------------------------------------------------
// DetailScreen — Instrument Monitor (Paso 5)
// Gráfico principal + sub-ventanas apilables (scroll) + Side Panel con
// log de trading, observabilidad y métricas operativas persistentes.
// ---------------------------------------------------------------------------
const DetailScreen = ({ initialWindow, onBack }) => {
    const [symbol, setSymbol] = useState(initialWindow.symbol);
    const [timeframe, setTimeframe] = useState(initialWindow.timeframe);
    const [indicators, setIndicators] = useState(initialWindow.indicators || []);

    const [symbols, setSymbols] = useState([]);
    const [timeframes, setTimeframes] = useState([]);
    const [availableIndicators, setAvailableIndicators] = useState([]);

    const [lastPrice, setLastPrice] = useState(0);
    const [priceChange, setPriceChange] = useState(0);

    // Side panel: log de trading + posiciones + métricas
    const [logEvents, setLogEvents] = useState([]);
    const [positions, setPositions] = useState([]);
    const [openPositions, setOpenPositions] = useState(0);
    const [totalPl, setTotalPl] = useState(0);
    const [lastClose, setLastClose] = useState(null);

    // 1. Símbolos y timeframes
    useEffect(() => {
        fetchJSON('/api/symbols').then(d => setSymbols(d.symbols || [])).catch(console.error);
        fetchJSON('/api/timeframes').then(d => setTimeframes(d.timeframes || [])).catch(console.error);
    }, []);

    // 2. Indicadores disponibles
    useEffect(() => {
        if (symbol && timeframe) {
            fetchJSON(`/api/available-indicators?symbol=${symbol}&timeframe=${timeframe}`)
                .then(d => setAvailableIndicators(d.indicators || []))
                .catch(console.error);
        }
    }, [symbol, timeframe]);

    // 3. Log de trading
    useEffect(() => {
        if (!symbol) return;
        fetchJSON(`/api/trading-log?symbol=${symbol}`)
            .then(d => setLogEvents(d.events || []))
            .catch(console.error);
    }, [symbol]);

    // 4. Posiciones + métricas operativas
    useEffect(() => {
        if (!symbol) return;
        fetchJSON(`/api/positions?symbol=${symbol}`)
            .then(d => {
                setPositions(d.positions || []);
                setOpenPositions(d.open_positions || 0);
                setTotalPl(d.total_pl || 0);
                setLastClose(d.last_close ?? null);
            })
            .catch(console.error);
    }, [symbol]);

    const plColor = totalPl >= 0 ? "text-[#4DFF54]" : "text-[#BD1A27]";
    const priceColor = priceChange >= 0 ? "text-[#4DFF54]" : "text-[#BD1A27]";

    return (
        <div className="bg-[#000000] text-[#e5e2e1] font-body h-screen w-screen overflow-hidden flex flex-col">
            {/* Barra superior */}
            <div className="flex items-center justify-between px-3 py-2 bg-black/60 border-b-[0.5px] border-white/10 z-20">
                <div className="flex items-center space-x-3">
                    <button className="material-symbols-outlined flex items-center justify-center h-6 w-6 text-slate-400 hover:text-white transition-colors" onClick={onBack} title="Back to Wall Monitor">arrow_back</button>
                    <span className="font-headline font-bold tracking-widest text-xs uppercase text-white">Instrument Monitor</span>

                    <SymbolInput
                        value={symbol}
                        onChange={v => setSymbol(v)}
                        symbols={symbols}
                        className="font-headline font-bold text-terminal tracking-tight whitespace-nowrap text-white border-none cursor-text hover:bg-white/10 px-1 focus:ring-0 focus:outline-none w-20"
                    />

                    <TimeframeSelect
                        value={timeframe}
                        onChange={setTimeframe}
                        timeframes={timeframes}
                    />

                    {/* Indicadores del gráfico principal */}
                    <div className="flex space-x-1 items-center">
                        {indicators.map(ind => (
                            <Badge
                                key={ind}
                                text={ind.split('@')[0].replace(/_/g, ' ')}
                                themeClass={THEMES.blue}
                                onClick={() => setIndicators(indicators.filter(i => i !== ind))}
                            />
                        ))}
                        <select
                            className="bg-transparent text-terminal text-slate-500 border-none opacity-50 hover:opacity-100 hover:text-white p-0 cursor-pointer focus:ring-0 text-[8px] appearance-none h-6"
                            value=""
                            onChange={e => {
                                if (e.target.value && !indicators.includes(e.target.value)) {
                                    setIndicators([...indicators, e.target.value]);
                                }
                            }}
                            title="Add Indicator"
                        >
                            <option value="">+ ADD</option>
                            {availableIndicators.filter(i => !indicators.includes(i.key)).map(i => (
                                <option key={i.key} value={i.key}>{i.name}</option>
                            ))}
                        </select>
                    </div>

                </div>

                <div className="flex items-center space-x-3">
                    {/* Precio en vivo: alineado a la derecha, Mono, coloreado dinámicamente */}
                    <span className={`font-mono text-terminal h-6 flex items-center ${priceColor}`}>
                        {lastPrice.toFixed(2)} ({(priceChange >= 0 ? "+" : "") + priceChange.toFixed(2)}%)
                    </span>
                    <button className="material-symbols-outlined flex items-center justify-center h-6 w-6 text-slate-400 hover:text-white transition-colors" onClick={onBack} title="Close">close</button>
                </div>
            </div>

            {/* Cuerpo: gráfico (con sub-ventanas) + side panel */}
            <div className="flex flex-1 min-h-0">
                {/* Sector central: gráfico principal + sub-ventanas apilables */}
                <div className="flex-1 flex flex-col min-w-0 min-h-0">
                    {/* Gráfico principal con el mismo sistema de sub-paneles que
                        la Wall Monitor: los indicadores de panel separado
                        (MACD, ADX, ATR, SMA Osc) se apilan como panes dentro
                        de este único gráfico al añadirlos desde "Add Indicator". */}
                    <div className="flex-1 min-h-0 flex flex-col">
                        <PriceChart
                            symbol={symbol}
                            timeframe={timeframe}
                            indicators={indicators}
                            onPrice={(price, change) => { setLastPrice(price); setPriceChange(change); }}
                        />
                    </div>
                </div>

                {/* Sector derecho: Side Panel */}
                <div className="w-[320px] shrink-0 border-l-[0.5px] border-white/10 bg-[#0A0A0A] flex flex-col min-h-0 overflow-y-auto">
                    {/* Métricas operativas principales */}
                    <div className="p-3 border-b-[0.5px] border-white/10">
                        <div className="text-[8px] uppercase tracking-widest text-slate-500 mb-2">Operative Metrics</div>
                        <div className="grid grid-cols-2 gap-2">
                            <div className="bg-white/5 rounded p-2">
                                <div className="text-[8px] uppercase text-slate-500">Total P/L</div>
                                <div className={`font-mono text-sm font-bold ${plColor}`}>
                                    {totalPl >= 0 ? "+" : ""}{totalPl.toFixed(2)}
                                </div>
                            </div>
                            <div className="bg-white/5 rounded p-2">
                                <div className="text-[8px] uppercase text-slate-500">Open Positions</div>
                                <div className="font-mono text-sm font-bold text-white">{openPositions}</div>
                            </div>
                        </div>
                        {lastClose !== null && (
                            <div className="mt-2 text-[9px] text-slate-500">Last close: <span className="text-slate-300 font-mono">{lastClose.toFixed(2)}</span></div>
                        )}
                    </div>

                    {/* Posiciones abiertas */}
                    <div className="p-3 border-b-[0.5px] border-white/10">
                        <div className="text-[8px] uppercase tracking-widest text-slate-500 mb-2">Open Positions</div>
                        {positions.length === 0 ? (
                            <div className="text-[9px] text-slate-600">No open positions</div>
                        ) : (
                            <div className="space-y-1">
                                {positions.map(p => (
                                    <div key={p.id} className="flex items-center justify-between bg-white/5 rounded px-2 py-1 text-[9px]">
                                        <span className="uppercase font-bold text-white">{p.side}</span>
                                        <span className="font-mono text-slate-400">{p.qty} @ {p.entry_price}</span>
                                        <button
                                            className="material-symbols-outlined text-slate-500 hover:text-[#BD1A27]"
                                            title="Close position"
                                            onClick={() => fetchJSON(`/api/positions/${p.id}?symbol=${symbol}`, { method: 'DELETE' }).then(() => {
                                                setPositions(positions.filter(x => x.id !== p.id));
                                                setOpenPositions(openPositions - 1);
                                            }).catch(console.error)}
                                        >close</button>
                                    </div>
                                ))}
                            </div>
                        )}
                    </div>

                    {/* Log de trading */}
                    <div className="p-3 flex-1">
                        <div className="text-[8px] uppercase tracking-widest text-slate-500 mb-2">Trading Log</div>
                        {logEvents.length === 0 ? (
                            <div className="text-[9px] text-slate-600">No signals or executions yet</div>
                        ) : (
                            <div className="space-y-1">
                                {[...logEvents].reverse().map((ev, i) => {
                                    const isBuy = (ev.action || "").toUpperCase() === "BUY";
                                    const isSell = (ev.action || "").toUpperCase() === "SELL";
                                    const color = ev.type === "execution"
                                        ? (isBuy ? "text-[#4DFF54]" : isSell ? "text-[#BD1A27]" : "text-slate-300")
                                        : "text-slate-400";
                                    return (
                                        <div key={i} className="bg-white/5 rounded px-2 py-1 text-[9px]">
                                            <div className="flex items-center justify-between">
                                                <span className={`font-bold uppercase ${color}`}>
                                                    {ev.type === "execution" ? "EXEC" : "SIGNAL"} · {ev.action || "—"}
                                                </span>
                                                <span className="text-slate-600 font-mono">{(ev.timestamp || "").replace("T", " ").slice(0, 16)}</span>
                                            </div>
                                            {ev.strategy && <div className="text-slate-500">{ev.strategy}</div>}
                                        </div>
                                    );
                                })}
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
};

const App = () => {
    // Initial state: 1 window
    const [windows, setWindows] = useState([
        { id: 1, symbol: 'AAPL', timeframe: '1d', indicators: [] }
    ]);

    // Ventana maximizada → Detail Screen (Instrument Monitor)
    const [detailWindow, setDetailWindow] = useState(null);

    const addWindow = () => {
        if (windows.length >= 6) return;
        const newId = windows.length ? Math.max(...windows.map(w => w.id)) + 1 : 1;
        // Clone the state of the first window for convenience, or defaults
        const refWindow = windows[0] || {};
        setWindows([...windows, { 
            id: newId, 
            symbol: refWindow.symbol || 'AAPL', 
            timeframe: refWindow.timeframe || '1d', 
            indicators: [] 
        }]);
    };

    const updateWindow = (id, updates) => {
        setWindows(windows.map(w => w.id === id ? { ...w, ...updates } : w));
    };

    const removeWindow = id => {
        setWindows(windows.filter(w => w.id !== id));
    };

    // Calculate grid layout based on number of windows (Tiling Manager)
    let cols = 1;
    let rows = 1;
    const count = windows.length;
    
    if (count === 2) { cols = 2; rows = 1; }
    else if (count === 3 || count === 4) { cols = 2; rows = 2; }
    else if (count >= 5) { cols = 3; rows = 2; }

    // Si hay una ventana maximizada → Detail Screen (Instrument Monitor)
    if (detailWindow) {
        return (
            <DetailScreen
                initialWindow={detailWindow}
                onBack={() => setDetailWindow(null)}
            />
        );
    }

    return (
        <div className="bg-[#000000] text-[#e5e2e1] font-body selection:bg-blue-600 selection:text-white h-screen w-screen overflow-hidden relative flex flex-col">
            
            {/* Global Toolbar / Add Window Button */}
            {count < 6 && (
                <button 
                    onClick={addWindow} 
                    className="absolute z-50 bottom-4 right-4 material-symbols-outlined text-white hover:text-gray-300 transition-colors drop-shadow-lg text-3xl"
                    title="Add Chart Window"
                >
                    add
                </button>
            )}

            {/* Grid Principal */}
            <main 
                className="gap-1 p-1 bg-[#000000] h-full w-full min-h-0" 
                style={{ 
                    display: 'grid',
                    gridTemplateColumns: `repeat(${cols}, 1fr)`, 
                    gridTemplateRows: `repeat(${rows}, 1fr)` 
                }}
            >
                {windows.map((w, index) => {
                    let gridStyle = {};
                    if (count === 3) {
                        if (index === 0) gridStyle = { gridColumn: '1', gridRow: '1' };
                        else if (index === 1) gridStyle = { gridColumn: '1', gridRow: '2' };
                        else if (index === 2) gridStyle = { gridColumn: '2', gridRow: '1 / span 2' };
                    }
                    return (
                    <div 
                        key={w.id} 
                        className="flex flex-col min-h-0 min-w-0"
                        style={gridStyle}
                    >
                        <ChartCard
                            window={w}
                            updateWindow={updates => updateWindow(w.id, updates)}
                            onClose={() => removeWindow(w.id)}
                            onMaximize={(win) => setDetailWindow(win)}
                            addWindowFrom={(sourceWindow) => {
                                if (windows.length >= 6) return;
                                const newId = Math.max(...windows.map(x => x.id)) + 1;
                                setWindows([...windows, { 
                                    id: newId, 
                                    symbol: sourceWindow.symbol, 
                                    timeframe: sourceWindow.timeframe, 
                                    indicators: [...sourceWindow.indicators] 
                                }]);
                            }}
                        />
                    </div>
                    );
                })}
                
                {windows.length === 0 && (
                    <div className="col-span-full row-span-full flex flex-col items-center justify-center text-slate-600">
                        <span className="material-symbols-outlined text-4xl mb-2">monitoring</span>
                        <p className="font-headline tracking-widest text-xs uppercase">No active windows</p>
                        <button onClick={addWindow} className="mt-4 px-4 py-2 bg-white/5 hover:bg-white/10 rounded border border-white/10 text-xs font-bold uppercase">
                            Add Window
                        </button>
                    </div>
                )}
            </main>
        </div>
    );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);