- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Plugins]{.breadcrumbs__link}
- [Overview]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Plugins

Plugins allow you to extend the library\'s functionality and render
custom elements, such as new series, drawing tools, indicators, and
watermarks.

You can create plugins of the following types:

- [Custom series](intro.html#custom-series) --- define new types of
  series.
- [Primitives](intro.html#primitives) --- define custom visualizations,
  drawing tools, and chart annotations that can be attached to an
  existing series ([series primitives](intro.html#series-primitives)) or
  chart pane ([pane primitives](intro.html#pane-primitives)).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]{.admonitionIcon_Rf37}Tips

- Use the
  [create-lwc-plugin](https://www.npmjs.com/package/create-lwc-plugin){target="_blank"
  rel="noopener noreferrer"} npm package to quickly scaffold a project
  for your custom plugin.
- Explore the [Plugin Examples
  Demo](https://tradingview.github.io/lightweight-charts/plugin-examples){target="_blank"
  rel="noopener noreferrer"} page that hosts interactive examples of
  heatmaps, alerts, watermarks, and tooltips implemented with plugins.
  You can find the code of these examples in the
  [`plugin-examples`](https://github.com/tradingview/lightweight-charts/tree/master/plugin-examples){target="_blank"
  rel="noopener noreferrer"} folder in the Lightweight Charts™
  repository.

## Custom series[​](intro.html#custom-series "Direct link to Custom series"){.hash-link aria-label="Direct link to Custom series"} {#custom-series .anchor .anchorWithStickyNavbar_LWe7}

Custom series allow you to define new types of series with custom data
structures and rendering logic. For implementation details, refer to the
[Custom Series Types](custom_series.html) article.

Use the
[`addCustomSeries`](../api/interfaces/IChartApi.html#addcustomseries)
method to add a custom series to the chart. Then, you can manage it
through the same API available for built-in series. For example, call
the [`setData`](../api/interfaces/ISeriesApi.html#setdata) method to
populate the series with data.

javascript

``` {.prism-code .language-javascript .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
class MyCustomSeries {
    /* Class implementing the ICustomSeriesPaneView interface */
}

// Create an instantiated custom series
const customSeriesInstance = new MyCustomSeries();

const chart = createChart(document.getElementById('container'));
const myCustomSeries = chart.addCustomSeries(customSeriesInstance, {
    // Options for MyCustomSeries
    customOption: 10,
});

const data = [
    { time: 1642425322, value: 123, customValue: 456 },
    /* ... more data */
];

myCustomSeries.setData(data);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

## Primitives[​](intro.html#primitives "Direct link to Primitives"){.hash-link aria-label="Direct link to Primitives"} {#primitives .anchor .anchorWithStickyNavbar_LWe7}

Primitives allow you to define custom visualizations, drawing tools, and
chart annotations. You can render them at different levels in the visual
stack to create complex, layered compositions.

### Series primitives[​](intro.html#series-primitives "Direct link to Series primitives"){.hash-link aria-label="Direct link to Series primitives"} {#series-primitives .anchor .anchorWithStickyNavbar_LWe7}

Series primitives are attached to a specific series and can render on
the main pane, price and time scales. For implementation details, refer
to the [Series Primitives](series-primitives.html) article.

Use the
[`attachPrimitive`](../api/interfaces/ISeriesApi.html#attachprimitive)
method to add a primitive to the chart and attach it to the series.

javascript

``` {.prism-code .language-javascript .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
class MyCustomPrimitive {
    /* Class implementing the ISeriesPrimitive interface */
}

// Create an instantiated series primitive
const myCustomPrimitive = new MyCustomPrimitive();

const chart = createChart(document.getElementById('container'));
const lineSeries = chart.addSeries(LineSeries);

const data = [
    { time: 1642425322, value: 123 },
    /* ... more data */
];

// Attach the primitive to the series
lineSeries.attachPrimitive(myCustomPrimitive);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

### Pane primitives[​](intro.html#pane-primitives "Direct link to Pane primitives"){.hash-link aria-label="Direct link to Pane primitives"} {#pane-primitives .anchor .anchorWithStickyNavbar_LWe7}

Pane primitives are attached to a chart pane rather than a specific
series. You can use them to create chart-wide annotations and features
like watermarks. For implementation details, refer to the [Pane
Primitives](pane-primitives.html) article.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]{.admonitionIcon_Rf37}caution

Note that pane primitives cannot render on the price or time scale.

Use the
[`attachPrimitive`](../api/interfaces/IPaneApi.html#attachprimitive)
method to add a primitive to the chart and attach it to the pane.

``` {.prism-code .language-javascript .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
class MyCustomPanePrimitive {
    /* Class implementing the IPanePrimitive interface */
}

// Create an instantiated pane primitive
const myCustomPanePrimitive = new MyCustomPanePrimitive();

const chart = createChart(document.getElementById('container'));
// Get the main pane
const mainPane = chart.panes()[0];

// Attach the primitive to the pane
mainPane.attachPrimitive(myCustomPanePrimitive);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

[](../time-zones.html){.pagination-nav__link
.pagination-nav__link--prev}

Previous

Time zones

[](series-primitives.html){.pagination-nav__link
.pagination-nav__link--next}

Next

Series Primitives

- [Custom series](intro.html#custom-series){.table-of-contents__link
  .toc-highlight}
- [Primitives](intro.html#primitives){.table-of-contents__link
  .toc-highlight}
  - [Series
    primitives](intro.html#series-primitives){.table-of-contents__link
    .toc-highlight}
  - [Pane
    primitives](intro.html#pane-primitives){.table-of-contents__link
    .toc-highlight}
