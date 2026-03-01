- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [PriceChartOptions]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: PriceChartOptions

Configuration options specific to price-based charts. Extends the base
chart options and includes localization settings for price formatting.

## Extends[​](PriceChartOptions.html#extends "Direct link to Extends"){.hash-link aria-label="Direct link to Extends"} {#extends .anchor .anchorWithStickyNavbar_LWe7}

- [`ChartOptionsImpl`](ChartOptionsImpl.html)\<`number`\>

## Properties[​](PriceChartOptions.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### width[​](PriceChartOptions.html#width "Direct link to width"){.hash-link aria-label="Direct link to width"} {#width .anchor .anchorWithStickyNavbar_LWe7}

> **width**: `number`

Width of the chart in pixels

#### Default Value[​](PriceChartOptions.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

If `0` (default) or none value provided, then a size of the widget will
be calculated based its container\'s size.

#### Inherited from[​](PriceChartOptions.html#inherited-from "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`width`](ChartOptionsImpl.html#width)

------------------------------------------------------------------------

### height[​](PriceChartOptions.html#height "Direct link to height"){.hash-link aria-label="Direct link to height"} {#height .anchor .anchorWithStickyNavbar_LWe7}

> **height**: `number`

Height of the chart in pixels

#### Default Value[​](PriceChartOptions.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

If `0` (default) or none value provided, then a size of the widget will
be calculated based its container\'s size.

#### Inherited from[​](PriceChartOptions.html#inherited-from-1 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-1 .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`height`](ChartOptionsImpl.html#height)

------------------------------------------------------------------------

### autoSize[​](PriceChartOptions.html#autosize "Direct link to autoSize"){.hash-link aria-label="Direct link to autoSize"} {#autosize .anchor .anchorWithStickyNavbar_LWe7}

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

#### Inherited from[​](PriceChartOptions.html#inherited-from-2 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-2 .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`autoSize`](ChartOptionsImpl.html#autosize)

------------------------------------------------------------------------

### layout[​](PriceChartOptions.html#layout "Direct link to layout"){.hash-link aria-label="Direct link to layout"} {#layout .anchor .anchorWithStickyNavbar_LWe7}

> **layout**: [`LayoutOptions`](LayoutOptions.html)

Layout options

#### Inherited from[​](PriceChartOptions.html#inherited-from-3 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-3 .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`layout`](ChartOptionsImpl.html#layout)

------------------------------------------------------------------------

### leftPriceScale[​](PriceChartOptions.html#leftpricescale "Direct link to leftPriceScale"){.hash-link aria-label="Direct link to leftPriceScale"} {#leftpricescale .anchor .anchorWithStickyNavbar_LWe7}

> **leftPriceScale**: [`PriceScaleOptions`](PriceScaleOptions.html)

Left price scale options

#### Inherited from[​](PriceChartOptions.html#inherited-from-4 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-4 .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`leftPriceScale`](ChartOptionsImpl.html#leftpricescale)

------------------------------------------------------------------------

### rightPriceScale[​](PriceChartOptions.html#rightpricescale "Direct link to rightPriceScale"){.hash-link aria-label="Direct link to rightPriceScale"} {#rightpricescale .anchor .anchorWithStickyNavbar_LWe7}

> **rightPriceScale**: [`PriceScaleOptions`](PriceScaleOptions.html)

Right price scale options

#### Inherited from[​](PriceChartOptions.html#inherited-from-5 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-5 .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`rightPriceScale`](ChartOptionsImpl.html#rightpricescale)

------------------------------------------------------------------------

### overlayPriceScales[​](PriceChartOptions.html#overlaypricescales "Direct link to overlayPriceScales"){.hash-link aria-label="Direct link to overlayPriceScales"} {#overlaypricescales .anchor .anchorWithStickyNavbar_LWe7}

> **overlayPriceScales**:
> [`OverlayPriceScaleOptions`](../type-aliases/OverlayPriceScaleOptions.html)

Overlay price scale options

#### Inherited from[​](PriceChartOptions.html#inherited-from-6 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-6 .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`overlayPriceScales`](ChartOptionsImpl.html#overlaypricescales)

------------------------------------------------------------------------

### timeScale[​](PriceChartOptions.html#timescale "Direct link to timeScale"){.hash-link aria-label="Direct link to timeScale"} {#timescale .anchor .anchorWithStickyNavbar_LWe7}

> **timeScale**: [`HorzScaleOptions`](HorzScaleOptions.html)

Time scale options

#### Inherited from[​](PriceChartOptions.html#inherited-from-7 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-7 .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`timeScale`](ChartOptionsImpl.html#timescale)

------------------------------------------------------------------------

### crosshair[​](PriceChartOptions.html#crosshair "Direct link to crosshair"){.hash-link aria-label="Direct link to crosshair"} {#crosshair .anchor .anchorWithStickyNavbar_LWe7}

> **crosshair**: [`CrosshairOptions`](CrosshairOptions.html)

The crosshair shows the intersection of the price and time scale values
at any point on the chart.

#### Inherited from[​](PriceChartOptions.html#inherited-from-8 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-8 .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`crosshair`](ChartOptionsImpl.html#crosshair)

------------------------------------------------------------------------

### grid[​](PriceChartOptions.html#grid "Direct link to grid"){.hash-link aria-label="Direct link to grid"} {#grid .anchor .anchorWithStickyNavbar_LWe7}

> **grid**: [`GridOptions`](GridOptions.html)

A grid is represented in the chart background as a vertical and
horizontal lines drawn at the levels of visible marks of price and the
time scales.

#### Inherited from[​](PriceChartOptions.html#inherited-from-9 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-9 .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`grid`](ChartOptionsImpl.html#grid)

------------------------------------------------------------------------

### handleScroll[​](PriceChartOptions.html#handlescroll "Direct link to handleScroll"){.hash-link aria-label="Direct link to handleScroll"} {#handlescroll .anchor .anchorWithStickyNavbar_LWe7}

> **handleScroll**: `boolean` \|
> [`HandleScrollOptions`](HandleScrollOptions.html)

Scroll options, or a boolean flag that enables/disables scrolling

#### Inherited from[​](PriceChartOptions.html#inherited-from-10 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-10 .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`handleScroll`](ChartOptionsImpl.html#handlescroll)

------------------------------------------------------------------------

### handleScale[​](PriceChartOptions.html#handlescale "Direct link to handleScale"){.hash-link aria-label="Direct link to handleScale"} {#handlescale .anchor .anchorWithStickyNavbar_LWe7}

> **handleScale**: `boolean` \|
> [`HandleScaleOptions`](HandleScaleOptions.html)

Scale options, or a boolean flag that enables/disables scaling

#### Inherited from[​](PriceChartOptions.html#inherited-from-11 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-11 .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`handleScale`](ChartOptionsImpl.html#handlescale)

------------------------------------------------------------------------

### kineticScroll[​](PriceChartOptions.html#kineticscroll "Direct link to kineticScroll"){.hash-link aria-label="Direct link to kineticScroll"} {#kineticscroll .anchor .anchorWithStickyNavbar_LWe7}

> **kineticScroll**: [`KineticScrollOptions`](KineticScrollOptions.html)

Kinetic scroll options

#### Inherited from[​](PriceChartOptions.html#inherited-from-12 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-12 .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`kineticScroll`](ChartOptionsImpl.html#kineticscroll)

------------------------------------------------------------------------

### trackingMode[​](PriceChartOptions.html#trackingmode "Direct link to trackingMode"){.hash-link aria-label="Direct link to trackingMode"} {#trackingmode .anchor .anchorWithStickyNavbar_LWe7}

> **trackingMode**: [`TrackingModeOptions`](TrackingModeOptions.html)

Represent options for the tracking mode\'s behavior.

Mobile users will not have the ability to see the values/dates like they
do on desktop. To see it, they should enter the tracking mode. The
tracking mode will deactivate the scrolling and make it possible to
check values and dates.

#### Inherited from[​](PriceChartOptions.html#inherited-from-13 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-13 .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`trackingMode`](ChartOptionsImpl.html#trackingmode)

------------------------------------------------------------------------

### addDefaultPane[​](PriceChartOptions.html#adddefaultpane "Direct link to addDefaultPane"){.hash-link aria-label="Direct link to addDefaultPane"} {#adddefaultpane .anchor .anchorWithStickyNavbar_LWe7}

> **addDefaultPane**: `boolean`

Whether to add a default pane to the chart Disable this option when you
want to create a chart with no panes and add them manually

#### Default Value[​](PriceChartOptions.html#default-value-2 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-2 .anchor .anchorWithStickyNavbar_LWe7}

`true`

#### Inherited from[​](PriceChartOptions.html#inherited-from-14 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-14 .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`addDefaultPane`](ChartOptionsImpl.html#adddefaultpane)

------------------------------------------------------------------------

### localization[​](PriceChartOptions.html#localization "Direct link to localization"){.hash-link aria-label="Direct link to localization"} {#localization .anchor .anchorWithStickyNavbar_LWe7}

> **localization**:
> [`PriceChartLocalizationOptions`](PriceChartLocalizationOptions.html)

Localization options for formatting price values and other chart
elements.

#### Overrides[​](PriceChartOptions.html#overrides "Direct link to Overrides"){.hash-link aria-label="Direct link to Overrides"} {#overrides .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html) .
[`localization`](ChartOptionsImpl.html#localization)

- [Extends](PriceChartOptions.html#extends){.table-of-contents__link
  .toc-highlight}
- [Properties](PriceChartOptions.html#properties){.table-of-contents__link
  .toc-highlight}
  - [width](PriceChartOptions.html#width){.table-of-contents__link
    .toc-highlight}
  - [height](PriceChartOptions.html#height){.table-of-contents__link
    .toc-highlight}
  - [autoSize](PriceChartOptions.html#autosize){.table-of-contents__link
    .toc-highlight}
  - [layout](PriceChartOptions.html#layout){.table-of-contents__link
    .toc-highlight}
  - [leftPriceScale](PriceChartOptions.html#leftpricescale){.table-of-contents__link
    .toc-highlight}
  - [rightPriceScale](PriceChartOptions.html#rightpricescale){.table-of-contents__link
    .toc-highlight}
  - [overlayPriceScales](PriceChartOptions.html#overlaypricescales){.table-of-contents__link
    .toc-highlight}
  - [timeScale](PriceChartOptions.html#timescale){.table-of-contents__link
    .toc-highlight}
  - [crosshair](PriceChartOptions.html#crosshair){.table-of-contents__link
    .toc-highlight}
  - [grid](PriceChartOptions.html#grid){.table-of-contents__link
    .toc-highlight}
  - [handleScroll](PriceChartOptions.html#handlescroll){.table-of-contents__link
    .toc-highlight}
  - [handleScale](PriceChartOptions.html#handlescale){.table-of-contents__link
    .toc-highlight}
  - [kineticScroll](PriceChartOptions.html#kineticscroll){.table-of-contents__link
    .toc-highlight}
  - [trackingMode](PriceChartOptions.html#trackingmode){.table-of-contents__link
    .toc-highlight}
  - [addDefaultPane](PriceChartOptions.html#adddefaultpane){.table-of-contents__link
    .toc-highlight}
  - [localization](PriceChartOptions.html#localization){.table-of-contents__link
    .toc-highlight}
