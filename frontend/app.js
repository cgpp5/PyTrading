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
let featureSeries = null;

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

async function populateFeatures(symbol, timeframe) {
    const data = await fetchJSON(
        `/api/available-features?symbol=${encodeURIComponent(symbol)}&timeframe=${encodeURIComponent(timeframe)}`
    );
    featureSelect.innerHTML = '<option value="">(ninguno)</option>';
    data.features.forEach(f => {
        const opt = document.createElement('option');
        opt.value = f;
        opt.textContent = f;
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
        featureSeries = null;
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

        // Populate features dropdown for this symbol/timeframe
        await populateFeatures(symbol, timeframe);

    } catch (err) {
        setStatus(`Error: ${err.message}`);
        console.error(err);
    }
}

// ── Load feature overlay ──

async function loadFeature() {
    const symbol = symbolSelect.value;
    const timeframe = timeframeSelect.value;
    const feature = featureSelect.value;

    // Remove previous feature overlay
    if (featureSeries && chart) {
        chart.removeSeries(featureSeries);
        featureSeries = null;
    }

    if (!feature || !chart) return;

    try {
        const data = await fetchJSON(
            `/api/features?symbol=${encodeURIComponent(symbol)}&timeframe=${encodeURIComponent(timeframe)}&feature=${encodeURIComponent(feature)}`
        );

        if (data.data.length === 0) {
            setStatus(`Feature ${feature}: sin datos`);
            return;
        }

        featureSeries = chart.addSeries(LineSeries, {
            color: '#fab387',
            lineWidth: 2,
        });
        featureSeries.setData(data.data);

        setStatus(`${symbol} / ${timeframe} + ${feature}`);

    } catch (err) {
        setStatus(`Error feature: ${err.message}`);
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
featureSelect.addEventListener('change', loadFeature);

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
