- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [ChartOptionsBase]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: ChartOptionsBase

Represents common chart options

## Extended by[​](ChartOptionsBase.html#extended-by "Direct link to Extended by"){.hash-link aria-label="Direct link to Extended by"} {#extended-by .anchor .anchorWithStickyNavbar_LWe7}

- [`ChartOptionsImpl`](ChartOptionsImpl.html)

## Properties[​](ChartOptionsBase.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### width[​](ChartOptionsBase.html#width "Direct link to width"){.hash-link aria-label="Direct link to width"} {#width .anchor .anchorWithStickyNavbar_LWe7}

> **width**: `number`

Width of the chart in pixels

#### Default Value[​](ChartOptionsBase.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

If `0` (default) or none value provided, then a size of the widget will
be calculated based its container\'s size.

------------------------------------------------------------------------

### height[​](ChartOptionsBase.html#height "Direct link to height"){.hash-link aria-label="Direct link to height"} {#height .anchor .anchorWithStickyNavbar_LWe7}

> **height**: `number`

Height of the chart in pixels

#### Default Value[​](ChartOptionsBase.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

If `0` (default) or none value provided, then a size of the widget will
be calculated based its container\'s size.

------------------------------------------------------------------------

### autoSize[​](ChartOptionsBase.html#autosize "Direct link to autoSize"){.hash-link aria-label="Direct link to autoSize"} {#autosize .anchor .anchorWithStickyNavbar_LWe7}

> **autoSize**: `boolean`

Setting this flag to `true` will make the chart watch the chart
container\'s size and automatically resize the chart to fit its
container whenever the size changes.

This feature requires
[`ResizeObserver`](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver){target="_blank"
rel="noopener noreferrer"} class to be available in the global scope.
Note that calling code is responsible for providing a polyfill if
required. If the global scope does not have `ResizeObserver`, a warning
will appear and the flag will be ignored.

Please pay attention that `autoSize` option and explicit sizes options
`width` and `height` don\'t conflict with one another. If you specify
`autoSize` flag, then `width` and `height` options will be ignored
unless `ResizeObserver` has failed. If it fails then the values will be
used as fallback.

The flag `autoSize` could also be set with and unset with `applyOptions`
function.

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const chart = LightweightCharts.createChart(document.body, {
    autoSize: true,
});
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### layout[​](ChartOptionsBase.html#layout "Direct link to layout"){.hash-link aria-label="Direct link to layout"} {#layout .anchor .anchorWithStickyNavbar_LWe7}

> **layout**: [`LayoutOptions`](LayoutOptions.html)

Layout options

------------------------------------------------------------------------

### leftPriceScale[​](ChartOptionsBase.html#leftpricescale "Direct link to leftPriceScale"){.hash-link aria-label="Direct link to leftPriceScale"} {#leftpricescale .anchor .anchorWithStickyNavbar_LWe7}

> **leftPriceScale**: [`PriceScaleOptions`](PriceScaleOptions.html)

Left price scale options

------------------------------------------------------------------------

### rightPriceScale[​](ChartOptionsBase.html#rightpricescale "Direct link to rightPriceScale"){.hash-link aria-label="Direct link to rightPriceScale"} {#rightpricescale .anchor .anchorWithStickyNavbar_LWe7}

> **rightPriceScale**: [`PriceScaleOptions`](PriceScaleOptions.html)

Right price scale options

------------------------------------------------------------------------

### overlayPriceScales[​](ChartOptionsBase.html#overlaypricescales "Direct link to overlayPriceScales"){.hash-link aria-label="Direct link to overlayPriceScales"} {#overlaypricescales .anchor .anchorWithStickyNavbar_LWe7}

> **overlayPriceScales**:
> [`OverlayPriceScaleOptions`](../type-aliases/OverlayPriceScaleOptions.html)

Overlay price scale options

------------------------------------------------------------------------

### timeScale[​](ChartOptionsBase.html#timescale "Direct link to timeScale"){.hash-link aria-label="Direct link to timeScale"} {#timescale .anchor .anchorWithStickyNavbar_LWe7}

> **timeScale**: [`HorzScaleOptions`](HorzScaleOptions.html)

Time scale options

------------------------------------------------------------------------

### crosshair[​](ChartOptionsBase.html#crosshair "Direct link to crosshair"){.hash-link aria-label="Direct link to crosshair"} {#crosshair .anchor .anchorWithStickyNavbar_LWe7}

> **crosshair**: [`CrosshairOptions`](CrosshairOptions.html)

The crosshair shows the intersection of the price and time scale values
at any point on the chart.

------------------------------------------------------------------------

### grid[​](ChartOptionsBase.html#grid "Direct link to grid"){.hash-link aria-label="Direct link to grid"} {#grid .anchor .anchorWithStickyNavbar_LWe7}

> **grid**: [`GridOptions`](GridOptions.html)

A grid is represented in the chart background as a vertical and
horizontal lines drawn at the levels of visible marks of price and the
time scales.

------------------------------------------------------------------------

### handleScroll[​](ChartOptionsBase.html#handlescroll "Direct link to handleScroll"){.hash-link aria-label="Direct link to handleScroll"} {#handlescroll .anchor .anchorWithStickyNavbar_LWe7}

> **handleScroll**: `boolean` \|
> [`HandleScrollOptions`](HandleScrollOptions.html)

Scroll options, or a boolean flag that enables/disables scrolling

------------------------------------------------------------------------

### handleScale[​](ChartOptionsBase.html#handlescale "Direct link to handleScale"){.hash-link aria-label="Direct link to handleScale"} {#handlescale .anchor .anchorWithStickyNavbar_LWe7}

> **handleScale**: `boolean` \|
> [`HandleScaleOptions`](HandleScaleOptions.html)

Scale options, or a boolean flag that enables/disables scaling

------------------------------------------------------------------------

### kineticScroll[​](ChartOptionsBase.html#kineticscroll "Direct link to kineticScroll"){.hash-link aria-label="Direct link to kineticScroll"} {#kineticscroll .anchor .anchorWithStickyNavbar_LWe7}

> **kineticScroll**: [`KineticScrollOptions`](KineticScrollOptions.html)

Kinetic scroll options

------------------------------------------------------------------------

### trackingMode[​](ChartOptionsBase.html#trackingmode "Direct link to trackingMode"){.hash-link aria-label="Direct link to trackingMode"} {#trackingmode .anchor .anchorWithStickyNavbar_LWe7}

> **trackingMode**: [`TrackingModeOptions`](TrackingModeOptions.html)

Represent options for the tracking mode\'s behavior.

Mobile users will not have the ability to see the values/dates like they
do on desktop. To see it, they should enter the tracking mode. The
tracking mode will deactivate the scrolling and make it possible to
check values and dates.

------------------------------------------------------------------------

### localization[​](ChartOptionsBase.html#localization "Direct link to localization"){.hash-link aria-label="Direct link to localization"} {#localization .anchor .anchorWithStickyNavbar_LWe7}

> **localization**:
> [`LocalizationOptionsBase`](LocalizationOptionsBase.html)

Basic localization options

------------------------------------------------------------------------

### addDefaultPane[​](ChartOptionsBase.html#adddefaultpane "Direct link to addDefaultPane"){.hash-link aria-label="Direct link to addDefaultPane"} {#adddefaultpane .anchor .anchorWithStickyNavbar_LWe7}

> **addDefaultPane**: `boolean`

Whether to add a default pane to the chart Disable this option when you
want to create a chart with no panes and add them manually

#### Default Value[​](ChartOptionsBase.html#default-value-2 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-2 .anchor .anchorWithStickyNavbar_LWe7}

`true`

- [Extended
  by](ChartOptionsBase.html#extended-by){.table-of-contents__link
  .toc-highlight}
- [Properties](ChartOptionsBase.html#properties){.table-of-contents__link
  .toc-highlight}
  - [width](ChartOptionsBase.html#width){.table-of-contents__link
    .toc-highlight}
  - [height](ChartOptionsBase.html#height){.table-of-contents__link
    .toc-highlight}
  - [autoSize](ChartOptionsBase.html#autosize){.table-of-contents__link
    .toc-highlight}
  - [layout](ChartOptionsBase.html#layout){.table-of-contents__link
    .toc-highlight}
  - [leftPriceScale](ChartOptionsBase.html#leftpricescale){.table-of-contents__link
    .toc-highlight}
  - [rightPriceScale](ChartOptionsBase.html#rightpricescale){.table-of-contents__link
    .toc-highlight}
  - [overlayPriceScales](ChartOptionsBase.html#overlaypricescales){.table-of-contents__link
    .toc-highlight}
  - [timeScale](ChartOptionsBase.html#timescale){.table-of-contents__link
    .toc-highlight}
  - [crosshair](ChartOptionsBase.html#crosshair){.table-of-contents__link
    .toc-highlight}
  - [grid](ChartOptionsBase.html#grid){.table-of-contents__link
    .toc-highlight}
  - [handleScroll](ChartOptionsBase.html#handlescroll){.table-of-contents__link
    .toc-highlight}
  - [handleScale](ChartOptionsBase.html#handlescale){.table-of-contents__link
    .toc-highlight}
  - [kineticScroll](ChartOptionsBase.html#kineticscroll){.table-of-contents__link
    .toc-highlight}
  - [trackingMode](ChartOptionsBase.html#trackingmode){.table-of-contents__link
    .toc-highlight}
  - [localization](ChartOptionsBase.html#localization){.table-of-contents__link
    .toc-highlight}
  - [addDefaultPane](ChartOptionsBase.html#adddefaultpane){.table-of-contents__link
    .toc-highlight}
