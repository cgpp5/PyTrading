- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [PriceScaleOptions]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: PriceScaleOptions

Structure that describes price scale options

## Properties[​](PriceScaleOptions.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### autoScale[​](PriceScaleOptions.html#autoscale "Direct link to autoScale"){.hash-link aria-label="Direct link to autoScale"} {#autoscale .anchor .anchorWithStickyNavbar_LWe7}

> **autoScale**: `boolean`

Autoscaling is a feature that automatically adjusts a price scale to fit
the visible range of data. Note that overlay price scales are always
auto-scaled.

#### Default Value[​](PriceScaleOptions.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`true`

------------------------------------------------------------------------

### mode[​](PriceScaleOptions.html#mode "Direct link to mode"){.hash-link aria-label="Direct link to mode"} {#mode .anchor .anchorWithStickyNavbar_LWe7}

> **mode**: [`PriceScaleMode`](../enumerations/PriceScaleMode.html)

Price scale mode.

#### Default Value[​](PriceScaleOptions.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
{@link PriceScaleMode.Normal}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### invertScale[​](PriceScaleOptions.html#invertscale "Direct link to invertScale"){.hash-link aria-label="Direct link to invertScale"} {#invertscale .anchor .anchorWithStickyNavbar_LWe7}

> **invertScale**: `boolean`

Invert the price scale, so that a upwards trend is shown as a downwards
trend and vice versa. Affects both the price scale and the data on the
chart.

#### Default Value[​](PriceScaleOptions.html#default-value-2 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-2 .anchor .anchorWithStickyNavbar_LWe7}

`false`

------------------------------------------------------------------------

### alignLabels[​](PriceScaleOptions.html#alignlabels "Direct link to alignLabels"){.hash-link aria-label="Direct link to alignLabels"} {#alignlabels .anchor .anchorWithStickyNavbar_LWe7}

> **alignLabels**: `boolean`

Align price scale labels to prevent them from overlapping.

#### Default Value[​](PriceScaleOptions.html#default-value-3 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-3 .anchor .anchorWithStickyNavbar_LWe7}

`true`

------------------------------------------------------------------------

### scaleMargins[​](PriceScaleOptions.html#scalemargins "Direct link to scaleMargins"){.hash-link aria-label="Direct link to scaleMargins"} {#scalemargins .anchor .anchorWithStickyNavbar_LWe7}

> **scaleMargins**: [`PriceScaleMargins`](PriceScaleMargins.html)

Price scale margins.

#### Default Value[​](PriceScaleOptions.html#default-value-4 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-4 .anchor .anchorWithStickyNavbar_LWe7}

`{ bottom: 0.1, top: 0.2 }`

#### Example[​](PriceScaleOptions.html#example "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
chart.priceScale('right').applyOptions({
    scaleMargins: {
        top: 0.8,
        bottom: 0,
    },
});
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### borderVisible[​](PriceScaleOptions.html#bordervisible "Direct link to borderVisible"){.hash-link aria-label="Direct link to borderVisible"} {#bordervisible .anchor .anchorWithStickyNavbar_LWe7}

> **borderVisible**: `boolean`

Set true to draw a border between the price scale and the chart area.

#### Default Value[​](PriceScaleOptions.html#default-value-5 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-5 .anchor .anchorWithStickyNavbar_LWe7}

`true`

------------------------------------------------------------------------

### borderColor[​](PriceScaleOptions.html#bordercolor "Direct link to borderColor"){.hash-link aria-label="Direct link to borderColor"} {#bordercolor .anchor .anchorWithStickyNavbar_LWe7}

> **borderColor**: `string`

Price scale border color.

#### Default Value[​](PriceScaleOptions.html#default-value-6 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-6 .anchor .anchorWithStickyNavbar_LWe7}

`'#2B2B43'`

------------------------------------------------------------------------

### textColor?[​](PriceScaleOptions.html#textcolor "Direct link to textColor?"){.hash-link aria-label="Direct link to textColor?"} {#textcolor .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **textColor**: `string`

Price scale text color. If not provided
[LayoutOptions.textColor](LayoutOptions.html#textcolor) is used.

#### Default Value[​](PriceScaleOptions.html#default-value-7 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-7 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

------------------------------------------------------------------------

### entireTextOnly[​](PriceScaleOptions.html#entiretextonly "Direct link to entireTextOnly"){.hash-link aria-label="Direct link to entireTextOnly"} {#entiretextonly .anchor .anchorWithStickyNavbar_LWe7}

> **entireTextOnly**: `boolean`

Show top and bottom corner labels only if entire text is visible.

#### Default Value[​](PriceScaleOptions.html#default-value-8 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-8 .anchor .anchorWithStickyNavbar_LWe7}

`false`

------------------------------------------------------------------------

### visible[​](PriceScaleOptions.html#visible "Direct link to visible"){.hash-link aria-label="Direct link to visible"} {#visible .anchor .anchorWithStickyNavbar_LWe7}

> **visible**: `boolean`

Indicates if this price scale visible. Ignored by overlay price scales.

#### Default Value[​](PriceScaleOptions.html#default-value-9 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-9 .anchor .anchorWithStickyNavbar_LWe7}

`true` for the right price scale and `false` for the left. For the yield
curve chart, the default is for the left scale to be visible.

------------------------------------------------------------------------

### ticksVisible[​](PriceScaleOptions.html#ticksvisible "Direct link to ticksVisible"){.hash-link aria-label="Direct link to ticksVisible"} {#ticksvisible .anchor .anchorWithStickyNavbar_LWe7}

> **ticksVisible**: `boolean`

Draw small horizontal line on price axis labels.

#### Default Value[​](PriceScaleOptions.html#default-value-10 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-10 .anchor .anchorWithStickyNavbar_LWe7}

`false`

------------------------------------------------------------------------

### minimumWidth[​](PriceScaleOptions.html#minimumwidth "Direct link to minimumWidth"){.hash-link aria-label="Direct link to minimumWidth"} {#minimumwidth .anchor .anchorWithStickyNavbar_LWe7}

> **minimumWidth**: `number`

Define a minimum width for the price scale. Note: This value will be
exceeded if the price scale needs more space to display it\'s contents.

Setting a minimum width could be useful for ensuring that multiple
charts positioned in a vertical stack each have an identical price scale
width, or for plugins which require a bit more space within the price
scale pane.

#### Default Value[​](PriceScaleOptions.html#default-value-11 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-11 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
0
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### ensureEdgeTickMarksVisible[​](PriceScaleOptions.html#ensureedgetickmarksvisible "Direct link to ensureEdgeTickMarksVisible"){.hash-link aria-label="Direct link to ensureEdgeTickMarksVisible"} {#ensureedgetickmarksvisible .anchor .anchorWithStickyNavbar_LWe7}

> **ensureEdgeTickMarksVisible**: `boolean`

Ensures that tick marks are always visible at the very top and bottom of
the price scale, regardless of the data range. When enabled, a tick mark
will be drawn at both edges of the scale, providing clear boundary
indicators.

#### Default Value[​](PriceScaleOptions.html#default-value-12 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-12 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
false
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

- [Properties](PriceScaleOptions.html#properties){.table-of-contents__link
  .toc-highlight}
  - [autoScale](PriceScaleOptions.html#autoscale){.table-of-contents__link
    .toc-highlight}
  - [mode](PriceScaleOptions.html#mode){.table-of-contents__link
    .toc-highlight}
  - [invertScale](PriceScaleOptions.html#invertscale){.table-of-contents__link
    .toc-highlight}
  - [alignLabels](PriceScaleOptions.html#alignlabels){.table-of-contents__link
    .toc-highlight}
  - [scaleMargins](PriceScaleOptions.html#scalemargins){.table-of-contents__link
    .toc-highlight}
  - [borderVisible](PriceScaleOptions.html#bordervisible){.table-of-contents__link
    .toc-highlight}
  - [borderColor](PriceScaleOptions.html#bordercolor){.table-of-contents__link
    .toc-highlight}
  - [textColor?](PriceScaleOptions.html#textcolor){.table-of-contents__link
    .toc-highlight}
  - [entireTextOnly](PriceScaleOptions.html#entiretextonly){.table-of-contents__link
    .toc-highlight}
  - [visible](PriceScaleOptions.html#visible){.table-of-contents__link
    .toc-highlight}
  - [ticksVisible](PriceScaleOptions.html#ticksvisible){.table-of-contents__link
    .toc-highlight}
  - [minimumWidth](PriceScaleOptions.html#minimumwidth){.table-of-contents__link
    .toc-highlight}
  - [ensureEdgeTickMarksVisible](PriceScaleOptions.html#ensureedgetickmarksvisible){.table-of-contents__link
    .toc-highlight}
