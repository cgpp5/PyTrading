/**
 * TradingUI — Frontend application
 *
 * Fetches OHLCV + features from the FastAPI backend and renders
 * them using Lightweight Charts v5.
 */

const {
    createChart,
    CandlestickSeries,
    HistogramSeries,
    LineSeries,
} = LightweightCharts;

// ── DOM refs ──

const symbolSelect    = document.getElementById('symbol');
const timeframeSelect = document.getElementById('timeframe');
const featureSelect   = document.getElementById('feature');
const loadBtn         = document.getElementById('load-btn');
const statusEl        = document.getElementById('status');
const container       = document.getElementById('chart-container');

// ── Chart state ──

let chart         = null;
let candleSeries  = null;
let volumeSeries  = null;
let volumePane    = null;
let indicatorPane = null;
let indicatorSeries = [];

// ── Helpers ──

function setStatus(msg) {
    statusEl.textContent = msg;
}

async function fetchJSON(url) {
    const resp = await fetch(url);
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    return resp.json();
}

// ── Populate dropdowns ──

async function populateSymbols() {
    const data = await fetchJSON('/api/symbols');
    symbolSelect.innerHTML = '';
    data.symbols.forEach(s => {
        const opt = document.createElement('option');
        opt.value = s;
        opt.textContent = s;
        symbolSelect.appendChild(opt);
    });
}

async function populateTimeframes() {
    const data = await fetchJSON('/api/timeframes');
    timeframeSelect.innerHTML = '';
    data.timeframes.forEach(tf => {
        const opt = document.createElement('option');
        opt.value = tf;
        opt.textContent = tf;
        // Default to 1d
        if (tf === '1d') opt.selected = true;
        timeframeSelect.appendChild(opt);
    });
}

async function populateIndicators(symbol, timeframe) {
    const data = await fetchJSON(
        `/api/available-indicators?symbol=${encodeURIComponent(symbol)}&timeframe=${encodeURIComponent(timeframe)}`
    );
    featureSelect.innerHTML = '<option value="">(ninguno)</option>';
    data.indicators.forEach(indicator => {
        const opt = document.createElement('option');
        opt.value = indicator.key;
        opt.textContent = indicator.name;
        featureSelect.appendChild(opt);
    });
}

// ── Chart creation / teardown ──

function destroyChart() {
    if (chart) {
        chart.remove();
        chart = null;
        candleSeries = null;
        volumeSeries = null;
        volumePane = null;
        indicatorPane = null;
        indicatorSeries = [];
    }
}

function createChartInstance() {
    chart = createChart(container, {
        width: container.clientWidth,
        height: container.clientHeight,
        layout: {
            background: { color: '#1e1e2e' },
            textColor: '#cdd6f4',
        },
        grid: {
            vertLines: { color: '#313244' },
            horzLines: { color: '#313244' },
        },
        timeScale: {
            timeVisible: true,
            secondsVisible: false,
        },
        crosshair: {
            mode: 0, // Normal
        },
    });
}

// ── Load OHLCV + Volume ──

async function loadOHLCV() {
    const symbol = symbolSelect.value;
    const timeframe = timeframeSelect.value;

    if (!symbol || !timeframe) return;

    setStatus('Cargando...');

    try {
        const data = await fetchJSON(
            `/api/ohlcv?symbol=${encodeURIComponent(symbol)}&timeframe=${encodeURIComponent(timeframe)}`
        );

        if (data.candles.length === 0) {
            setStatus('Sin datos para esta combinación');
            destroyChart();
            return;
        }

        // Recreate chart fresh
        destroyChart();
        createChartInstance();

        // Candlestick series (main pane)
        candleSeries = chart.addSeries(CandlestickSeries, {
            upColor: '#a6e3a1',
            downColor: '#f38ba8',
            borderUpColor: '#a6e3a1',
            borderDownColor: '#f38ba8',
            wickUpColor: '#a6e3a1',
            wickDownColor: '#f38ba8',
        });
        candleSeries.setData(data.candles);

        // Volume histogram (separate pane)
        volumePane = chart.addPane();
        volumePane.setHeight(120);
        const paneIdx = volumePane.paneIndex();

        volumeSeries = chart.addSeries(HistogramSeries, {
            color: '#89b4fa',
            priceFormat: { type: 'volume' },
        }, paneIdx);
        volumeSeries.setData(data.volume);

        chart.timeScale().fitContent();

        setStatus(`${symbol} / ${timeframe} — ${data.candles.length} velas`);

        // Populate indicators dropdown for this symbol/timeframe
        await populateIndicators(symbol, timeframe);

    } catch (err) {
        setStatus(`Error: ${err.message}`);
        console.error(err);
    }
}

function clearIndicatorSeries() {
    if (!chart || indicatorSeries.length === 0) return;
    indicatorSeries.forEach(series => chart.removeSeries(series));
    indicatorSeries = [];
    if (indicatorPane) {
        chart.removePane(indicatorPane.paneIndex());
        indicatorPane = null;
    }
}

// ── Load indicator overlay ──

async function loadIndicator() {
    const symbol = symbolSelect.value;
    const timeframe = timeframeSelect.value;
    const indicator = featureSelect.value;

    clearIndicatorSeries();

    if (!indicator || !chart) return;

    try {
        const data = await fetchJSON(
            `/api/indicator?symbol=${encodeURIComponent(symbol)}&timeframe=${encodeURIComponent(timeframe)}&indicator=${encodeURIComponent(indicator)}`
        );

        if (data.series.length === 0) {
            setStatus(`Indicator ${indicator}: sin datos`);
            return;
        }

        let paneIndex;
        if (data.pane === 'separate') {
            indicatorPane = chart.addPane();
            indicatorPane.setHeight(140);
            paneIndex = indicatorPane.paneIndex();
        }

        data.series.forEach(item => {
            const definition = item.seriesType === 'histogram' ? HistogramSeries : LineSeries;
            const options = item.seriesType === 'histogram'
                ? {
                    color: item.color,
                    priceLineVisible: false,
                    lastValueVisible: true,
                }
                : {
                    color: item.color,
                    lineWidth: item.lineWidth,
                    lastValueVisible: true,
                    priceLineVisible: false,
                };
            const series = chart.addSeries(definition, options, paneIndex);
            const seriesData = item.seriesType === 'histogram'
                ? item.data.map(point => ({
                    ...point,
                    color: point.value >= 0 ? item.color : item.negativeColor,
                }))
                : item.data;
            series.setData(seriesData);
            indicatorSeries.push(series);
        });

        setStatus(`${symbol} / ${timeframe} + ${data.name}`);

    } catch (err) {
        setStatus(`Error indicator: ${err.message}`);
        console.error(err);
    }
}

// ── Resize handler ──

window.addEventListener('resize', () => {
    if (chart) {
        chart.resize(container.clientWidth, container.clientHeight);
    }
});

// ── Event bindings ──

loadBtn.addEventListener('click', loadOHLCV);
featureSelect.addEventListener('change', loadIndicator);

// ── Init ──

(async () => {
    try {
        await Promise.all([populateSymbols(), populateTimeframes()]);
        setStatus('Listo — selecciona un símbolo y pulsa Cargar');
    } catch (err) {
        setStatus(`Error al inicializar: ${err.message}`);
        console.error(err);
    }
})();
