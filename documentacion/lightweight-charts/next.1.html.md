This is unreleased documentation for Lightweight Charts **Next**
version.

For up-to-date documentation, see the **[latest
version](https://tradingview.github.io/lightweight-charts/docs)** (5.1).

- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Getting started]{.breadcrumbs__link itemprop="name"}

[Version: Next]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Getting started

## Requirements[​](next.1.html#requirements "Direct link to Requirements"){.hash-link aria-label="Direct link to Requirements"} {#requirements .anchor .anchorWithStickyNavbar_LWe7}

Lightweight Charts™ is *a client-side* library that is not designed to
work on the server side, for example, with Node.js.

The library code targets the [*ES2020* language
specification](https://262.ecma-international.org/11.0/){target="_blank"
rel="noopener noreferrer"}. Therefore, the browsers you work with should
support this language revision. Consider the following
[table](https://compat-table.github.io/compat-table/es2016plus/){target="_blank"
rel="noopener noreferrer"} to ensure the browser compatibility.

To support previous revisions, you can set up a transpilation process
for the `lightweight-charts` package in your build system using tools
such as Babel. If you encounter any issues, open a [GitHub
issue](https://github.com/tradingview/lightweight-charts/issues){target="_blank"
rel="noopener noreferrer"} with detailed information, and we will
investigate potential solutions.

## Installation[​](next.1.html#installation "Direct link to Installation"){.hash-link aria-label="Direct link to Installation"} {#installation .anchor .anchorWithStickyNavbar_LWe7}

To set up the library, install the
[`lightweight-charts`](https://www.npmjs.com/package/lightweight-charts){target="_blank"
rel="noopener noreferrer"} npm package:

``` {.prism-code .language-console .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
npm install --save lightweight-charts
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

The package includes TypeScript declarations, enabling seamless
integration within TypeScript projects.

### Build variants[​](next.1.html#build-variants "Direct link to Build variants"){.hash-link aria-label="Direct link to Build variants"} {#build-variants .anchor .anchorWithStickyNavbar_LWe7}

The library ships with the following build variants:

Dependencies included

Mode

ES module

IIFE (`window.LightweightCharts`)

No

PROD

`lightweight-charts.production.mjs`

N/A

No

DEV

`lightweight-charts.development.mjs`

N/A

Yes (standalone)

PROD

`lightweight-charts.standalone.production.mjs`

`lightweight-charts.standalone.production.js`

Yes (standalone)

DEV

`lightweight-charts.standalone.development.mjs`

`lightweight-charts.standalone.development.js`

## License and attribution[​](next.1.html#license-and-attribution "Direct link to License and attribution"){.hash-link aria-label="Direct link to License and attribution"} {#license-and-attribution .anchor .anchorWithStickyNavbar_LWe7}

The Lightweight Charts™ license **requires** specifying TradingView as
the product creator. You should add the following attributes to a public
page of your website or mobile application:

- Attribution notice from the
  [`NOTICE`](https://github.com/tradingview/lightweight-charts/blob/master/NOTICE){target="_blank"
  rel="noopener noreferrer"} file
- The
  [https://www.tradingview.com](https://www.tradingview.com){target="_blank"
  rel="noopener noreferrer"} link

## Creating a chart[​](next.1.html#creating-a-chart "Direct link to Creating a chart"){.hash-link aria-label="Direct link to Creating a chart"} {#creating-a-chart .anchor .anchorWithStickyNavbar_LWe7}

As a first step, import the library to your file:

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

To create a chart, use the
[`createChart`](next/api/functions/createChart.html) function. You can
call the function multiple times to create as many charts as needed:

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}

// ...
const firstChart = createChart(document.getElementById('firstContainer'));
const secondChart = createChart(document.getElementById('secondContainer'));
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

As a result, `createChart` returns an
[`IChartApi`](next/api/interfaces/IChartApi.html) object that allows you
to interact with the created chart.

## Creating a series[​](next.1.html#creating-a-series "Direct link to Creating a series"){.hash-link aria-label="Direct link to Creating a series"} {#creating-a-series .anchor .anchorWithStickyNavbar_LWe7}

When the chart is created, you can display data on it.

The basic primitive to display data is a
[series](next/api/interfaces/ISeriesApi.html). The library supports the
following series types:

- Area
- Bar
- Baseline
- Candlestick
- Histogram
- Line

To create a series, use the
[`addSeries`](next/api/interfaces/IChartApi.html#addseries) method from
[`IChartApi`](next/api/interfaces/IChartApi.html). As a parameter,
specify a [series type](next/series-types.html) you would like to
create:

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}

const chart = createChart(container);

const areaSeries = chart.addSeries(AreaSeries);
const barSeries = chart.addSeries(BarSeries);
const baselineSeries = chart.addSeries(BaselineSeries);
// ...
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

Note that a series **cannot be transferred** from one type to another
one, since different series types require different data and options
types.

## Setting and updating a data[​](next.1.html#setting-and-updating-a-data "Direct link to Setting and updating a data"){.hash-link aria-label="Direct link to Setting and updating a data"} {#setting-and-updating-a-data .anchor .anchorWithStickyNavbar_LWe7}

When the series is created, you can populate it with data. Note that the
API calls remain the same regardless of the series type, although the
data format may vary.

### Setting the data to a series[​](next.1.html#setting-the-data-to-a-series "Direct link to Setting the data to a series"){.hash-link aria-label="Direct link to Setting the data to a series"} {#setting-the-data-to-a-series .anchor .anchorWithStickyNavbar_LWe7}

To set the data to a series, you should call the
[`ISeriesApi.setData`](next/api/interfaces/ISeriesApi.html#setdata)
method:

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const chartOptions = { layout: { textColor: 'black', background: { type: 'solid', color: 'white' } } };
const chart = createChart(document.getElementById('container'), chartOptions);
const areaSeries = chart.addSeries(AreaSeries, {
    lineColor: '#2962FF', topColor: '#2962FF',
    bottomColor: 'rgba(41, 98, 255, 0.28)',
});
areaSeries.setData([
    { time: '2018-12-22', value: 32.51 },
    { time: '2018-12-23', value: 31.11 },
    { time: '2018-12-24', value: 27.02 },
    { time: '2018-12-25', value: 27.32 },
    { time: '2018-12-26', value: 25.17 },
    { time: '2018-12-27', value: 28.89 },
    { time: '2018-12-28', value: 25.46 },
    { time: '2018-12-29', value: 23.92 },
    { time: '2018-12-30', value: 22.68 },
    { time: '2018-12-31', value: 22.67 },
]);

const candlestickSeries = chart.addSeries(CandlestickSeries, {
    upColor: '#26a69a', downColor: '#ef5350', borderVisible: false,
    wickUpColor: '#26a69a', wickDownColor: '#ef5350',
});
candlestickSeries.setData([
    { time: '2018-12-22', open: 75.16, high: 82.84, low: 36.16, close: 45.72 },
    { time: '2018-12-23', open: 45.12, high: 53.90, low: 45.12, close: 48.09 },
    { time: '2018-12-24', open: 60.71, high: 60.71, low: 53.39, close: 59.29 },
    { time: '2018-12-25', open: 68.26, high: 68.26, low: 59.04, close: 60.50 },
    { time: '2018-12-26', open: 67.71, high: 105.85, low: 66.67, close: 91.04 },
    { time: '2018-12-27', open: 91.04, high: 121.40, low: 82.70, close: 111.40 },
    { time: '2018-12-28', open: 111.51, high: 142.83, low: 103.34, close: 131.25 },
    { time: '2018-12-29', open: 131.33, high: 151.17, low: 77.68, close: 96.43 },
    { time: '2018-12-30', open: 106.33, high: 110.20, low: 90.39, close: 98.10 },
    { time: '2018-12-31', open: 109.87, high: 114.69, low: 85.66, close: 111.26 },
]);

chart.timeScale().fitContent();
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

 

You can also use `setData` to replace all data items.

### Updating the data in a series[​](next.1.html#updating-the-data-in-a-series "Direct link to Updating the data in a series"){.hash-link aria-label="Direct link to Updating the data in a series"} {#updating-the-data-in-a-series .anchor .anchorWithStickyNavbar_LWe7}

If your data is updated, for example in real-time, you may also need to
refresh the chart accordingly. To do this, call the
[`ISeriesApi.update`](next/api/interfaces/ISeriesApi.html#update) method
that allows you to update the last data item or add a new one.

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}

const chart = createChart(container);

const areaSeries = chart.addSeries(AreaSeries);
areaSeries.setData([
    // Other data items
    { time: '2018-12-31', value: 22.67 },
]);

const candlestickSeries = chart.addSeries(CandlestickSeries);
candlestickSeries.setData([
    // Other data items
    { time: '2018-12-31', open: 109.87, high: 114.69, low: 85.66, close: 111.26 },
]);

// ...

// Update the most recent bar
areaSeries.update({ time: '2018-12-31', value: 25 });
candlestickSeries.update({ time: '2018-12-31', open: 109.87, high: 114.69, low: 85.66, close: 112 });

// Creating the new bar
areaSeries.update({ time: '2019-01-01', value: 20 });
candlestickSeries.update({ time: '2019-01-01', open: 112, high: 112, low: 100, close: 101 });
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

We do not recommend calling
[`ISeriesApi.setData`](next/api/interfaces/ISeriesApi.html#setdata) to
update the chart, as this method replaces all series data and can
significantly affect the performance.

[](next/series-types.html){.pagination-nav__link
.pagination-nav__link--next}

Next

Series

- [Requirements](next.1.html#requirements){.table-of-contents__link
  .toc-highlight}
- [Installation](next.1.html#installation){.table-of-contents__link
  .toc-highlight}
  - [Build
    variants](next.1.html#build-variants){.table-of-contents__link
    .toc-highlight}
- [License and
  attribution](next.1.html#license-and-attribution){.table-of-contents__link
  .toc-highlight}
- [Creating a
  chart](next.1.html#creating-a-chart){.table-of-contents__link
  .toc-highlight}
- [Creating a
  series](next.1.html#creating-a-series){.table-of-contents__link
  .toc-highlight}
- [Setting and updating a
  data](next.1.html#setting-and-updating-a-data){.table-of-contents__link
  .toc-highlight}
  - [Setting the data to a
    series](next.1.html#setting-the-data-to-a-series){.table-of-contents__link
    .toc-highlight}
  - [Updating the data in a
    series](next.1.html#updating-the-data-in-a-series){.table-of-contents__link
    .toc-highlight}
