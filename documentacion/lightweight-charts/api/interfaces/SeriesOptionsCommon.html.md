- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [SeriesOptionsCommon]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: SeriesOptionsCommon

Represents options common for all types of series

## Properties[​](SeriesOptionsCommon.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### lastValueVisible[​](SeriesOptionsCommon.html#lastvaluevisible "Direct link to lastValueVisible"){.hash-link aria-label="Direct link to lastValueVisible"} {#lastvaluevisible .anchor .anchorWithStickyNavbar_LWe7}

> **lastValueVisible**: `boolean`

Visibility of the label with the latest visible price on the price
scale.

#### Default Value[​](SeriesOptionsCommon.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`true`, `false` for yield curve charts

------------------------------------------------------------------------

### title[​](SeriesOptionsCommon.html#title "Direct link to title"){.hash-link aria-label="Direct link to title"} {#title .anchor .anchorWithStickyNavbar_LWe7}

> **title**: `string`

You can name series when adding it to a chart. This name will be
displayed on the label next to the last value label.

#### Default Value[​](SeriesOptionsCommon.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

`''`

------------------------------------------------------------------------

### priceScaleId?[​](SeriesOptionsCommon.html#pricescaleid "Direct link to priceScaleId?"){.hash-link aria-label="Direct link to priceScaleId?"} {#pricescaleid .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **priceScaleId**: `string`

Target price scale to bind new series to.

#### Default Value[​](SeriesOptionsCommon.html#default-value-2 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-2 .anchor .anchorWithStickyNavbar_LWe7}

`'right'` if right scale is visible and `'left'` otherwise

------------------------------------------------------------------------

### visible[​](SeriesOptionsCommon.html#visible "Direct link to visible"){.hash-link aria-label="Direct link to visible"} {#visible .anchor .anchorWithStickyNavbar_LWe7}

> **visible**: `boolean`

Visibility of the series. If the series is hidden, everything including
price lines, baseline, price labels and markers, will also be hidden.
Please note that hiding a series is not equivalent to deleting it, since
hiding does not affect the timeline at all, unlike deleting where the
timeline can be changed (some points can be deleted).

#### Default Value[​](SeriesOptionsCommon.html#default-value-3 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-3 .anchor .anchorWithStickyNavbar_LWe7}

`true`

------------------------------------------------------------------------

### priceLineVisible[​](SeriesOptionsCommon.html#pricelinevisible "Direct link to priceLineVisible"){.hash-link aria-label="Direct link to priceLineVisible"} {#pricelinevisible .anchor .anchorWithStickyNavbar_LWe7}

> **priceLineVisible**: `boolean`

Show the price line. Price line is a horizontal line indicating the last
price of the series.

#### Default Value[​](SeriesOptionsCommon.html#default-value-4 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-4 .anchor .anchorWithStickyNavbar_LWe7}

`true`, `false` for yield curve charts

------------------------------------------------------------------------

### priceLineSource[​](SeriesOptionsCommon.html#pricelinesource "Direct link to priceLineSource"){.hash-link aria-label="Direct link to priceLineSource"} {#pricelinesource .anchor .anchorWithStickyNavbar_LWe7}

> **priceLineSource**:
> [`PriceLineSource`](../enumerations/PriceLineSource.html)

The source to use for the value of the price line.

#### Default Value[​](SeriesOptionsCommon.html#default-value-5 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-5 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
{@link PriceLineSource.LastBar}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### priceLineWidth[​](SeriesOptionsCommon.html#pricelinewidth "Direct link to priceLineWidth"){.hash-link aria-label="Direct link to priceLineWidth"} {#pricelinewidth .anchor .anchorWithStickyNavbar_LWe7}

> **priceLineWidth**: [`LineWidth`](../type-aliases/LineWidth.html)

Width of the price line.

#### Default Value[​](SeriesOptionsCommon.html#default-value-6 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-6 .anchor .anchorWithStickyNavbar_LWe7}

`1`

------------------------------------------------------------------------

### priceLineColor[​](SeriesOptionsCommon.html#pricelinecolor "Direct link to priceLineColor"){.hash-link aria-label="Direct link to priceLineColor"} {#pricelinecolor .anchor .anchorWithStickyNavbar_LWe7}

> **priceLineColor**: `string`

Color of the price line. By default, its color is set by the last bar
color (or by line color on Line and Area charts).

#### Default Value[​](SeriesOptionsCommon.html#default-value-7 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-7 .anchor .anchorWithStickyNavbar_LWe7}

`''`

------------------------------------------------------------------------

### priceLineStyle[​](SeriesOptionsCommon.html#pricelinestyle "Direct link to priceLineStyle"){.hash-link aria-label="Direct link to priceLineStyle"} {#pricelinestyle .anchor .anchorWithStickyNavbar_LWe7}

> **priceLineStyle**: [`LineStyle`](../enumerations/LineStyle.html)

Price line style.

#### Default Value[​](SeriesOptionsCommon.html#default-value-8 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-8 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
{@link LineStyle.Dashed}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### priceFormat[​](SeriesOptionsCommon.html#priceformat "Direct link to priceFormat"){.hash-link aria-label="Direct link to priceFormat"} {#priceformat .anchor .anchorWithStickyNavbar_LWe7}

> **priceFormat**: [`PriceFormat`](../type-aliases/PriceFormat.html)

Price format.

#### Default Value[​](SeriesOptionsCommon.html#default-value-9 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-9 .anchor .anchorWithStickyNavbar_LWe7}

`{ type: 'price', precision: 2, minMove: 0.01 }`

------------------------------------------------------------------------

### baseLineVisible[​](SeriesOptionsCommon.html#baselinevisible "Direct link to baseLineVisible"){.hash-link aria-label="Direct link to baseLineVisible"} {#baselinevisible .anchor .anchorWithStickyNavbar_LWe7}

> **baseLineVisible**: `boolean`

Visibility of base line. Suitable for percentage and `IndexedTo100`
scales.

#### Default Value[​](SeriesOptionsCommon.html#default-value-10 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-10 .anchor .anchorWithStickyNavbar_LWe7}

`true`

------------------------------------------------------------------------

### baseLineColor[​](SeriesOptionsCommon.html#baselinecolor "Direct link to baseLineColor"){.hash-link aria-label="Direct link to baseLineColor"} {#baselinecolor .anchor .anchorWithStickyNavbar_LWe7}

> **baseLineColor**: `string`

Color of the base line in `IndexedTo100` mode.

#### Default Value[​](SeriesOptionsCommon.html#default-value-11 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-11 .anchor .anchorWithStickyNavbar_LWe7}

`'#B2B5BE'`

------------------------------------------------------------------------

### baseLineWidth[​](SeriesOptionsCommon.html#baselinewidth "Direct link to baseLineWidth"){.hash-link aria-label="Direct link to baseLineWidth"} {#baselinewidth .anchor .anchorWithStickyNavbar_LWe7}

> **baseLineWidth**: [`LineWidth`](../type-aliases/LineWidth.html)

Base line width. Suitable for percentage and `IndexedTo10` scales.

#### Default Value[​](SeriesOptionsCommon.html#default-value-12 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-12 .anchor .anchorWithStickyNavbar_LWe7}

`1`

------------------------------------------------------------------------

### baseLineStyle[​](SeriesOptionsCommon.html#baselinestyle "Direct link to baseLineStyle"){.hash-link aria-label="Direct link to baseLineStyle"} {#baselinestyle .anchor .anchorWithStickyNavbar_LWe7}

> **baseLineStyle**: [`LineStyle`](../enumerations/LineStyle.html)

Base line style. Suitable for percentage and indexedTo100 scales.

#### Default Value[​](SeriesOptionsCommon.html#default-value-13 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-13 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
{@link LineStyle.Solid}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### autoscaleInfoProvider?[​](SeriesOptionsCommon.html#autoscaleinfoprovider "Direct link to autoscaleInfoProvider?"){.hash-link aria-label="Direct link to autoscaleInfoProvider?"} {#autoscaleinfoprovider .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **autoscaleInfoProvider**:
> [`AutoscaleInfoProvider`](../type-aliases/AutoscaleInfoProvider.html)

Override the default [AutoscaleInfo](AutoscaleInfo.html) provider. By
default, the chart scales data automatically based on visible data
range. However, for some reasons one could require overriding this
behavior.

#### Default Value[​](SeriesOptionsCommon.html#default-value-14 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-14 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

#### Examples[​](SeriesOptionsCommon.html#examples "Direct link to Examples"){.hash-link aria-label="Direct link to Examples"} {#examples .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const firstSeries = chart.addSeries(LineSeries, {
    autoscaleInfoProvider: () => ({
        priceRange: {
            minValue: 0,
            maxValue: 100,
        },
    }),
});
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const firstSeries = chart.addSeries(LineSeries, {
    autoscaleInfoProvider: () => ({
        priceRange: {
            minValue: 0,
            maxValue: 100,
        },
        margins: {
            above: 10,
            below: 10,
        },
    }),
});
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const firstSeries = chart.addSeries(LineSeries, {
    autoscaleInfoProvider: original => {
        const res = original();
        if (res !== null) {
            res.priceRange.minValue -= 10;
            res.priceRange.maxValue += 10;
        }
        return res;
    },
});
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### conflationThresholdFactor?[​](SeriesOptionsCommon.html#conflationthresholdfactor "Direct link to conflationThresholdFactor?"){.hash-link aria-label="Direct link to conflationThresholdFactor?"} {#conflationthresholdfactor .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **conflationThresholdFactor**: `number`

Conflation smoothing factor for this series. Overrides the global time
scale option. Controls how aggressively conflation is applied
specifically to this series.

- 1.0 = conflate only when display can\'t show detail (default,
  performance-focused)
- 2.0 = conflate at 2x the display threshold (moderate smoothing)
- 4.0 = conflate at 4x the display threshold (strong smoothing)
- 8.0+ = very aggressive smoothing for very small charts

Higher values result in fewer data points being displayed for this
series, creating smoother but less detailed charts. This allows
different series on the same chart to have different conflation levels.

#### Default Value[​](SeriesOptionsCommon.html#default-value-15 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-15 .anchor .anchorWithStickyNavbar_LWe7}

`undefined` (uses global time scale option)

- [Properties](SeriesOptionsCommon.html#properties){.table-of-contents__link
  .toc-highlight}
  - [lastValueVisible](SeriesOptionsCommon.html#lastvaluevisible){.table-of-contents__link
    .toc-highlight}
  - [title](SeriesOptionsCommon.html#title){.table-of-contents__link
    .toc-highlight}
  - [priceScaleId?](SeriesOptionsCommon.html#pricescaleid){.table-of-contents__link
    .toc-highlight}
  - [visible](SeriesOptionsCommon.html#visible){.table-of-contents__link
    .toc-highlight}
  - [priceLineVisible](SeriesOptionsCommon.html#pricelinevisible){.table-of-contents__link
    .toc-highlight}
  - [priceLineSource](SeriesOptionsCommon.html#pricelinesource){.table-of-contents__link
    .toc-highlight}
  - [priceLineWidth](SeriesOptionsCommon.html#pricelinewidth){.table-of-contents__link
    .toc-highlight}
  - [priceLineColor](SeriesOptionsCommon.html#pricelinecolor){.table-of-contents__link
    .toc-highlight}
  - [priceLineStyle](SeriesOptionsCommon.html#pricelinestyle){.table-of-contents__link
    .toc-highlight}
  - [priceFormat](SeriesOptionsCommon.html#priceformat){.table-of-contents__link
    .toc-highlight}
  - [baseLineVisible](SeriesOptionsCommon.html#baselinevisible){.table-of-contents__link
    .toc-highlight}
  - [baseLineColor](SeriesOptionsCommon.html#baselinecolor){.table-of-contents__link
    .toc-highlight}
  - [baseLineWidth](SeriesOptionsCommon.html#baselinewidth){.table-of-contents__link
    .toc-highlight}
  - [baseLineStyle](SeriesOptionsCommon.html#baselinestyle){.table-of-contents__link
    .toc-highlight}
  - [autoscaleInfoProvider?](SeriesOptionsCommon.html#autoscaleinfoprovider){.table-of-contents__link
    .toc-highlight}
  - [conflationThresholdFactor?](SeriesOptionsCommon.html#conflationthresholdfactor){.table-of-contents__link
    .toc-highlight}
