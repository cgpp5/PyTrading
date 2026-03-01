- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [AreaStyleOptions]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: AreaStyleOptions

Represents style options for an area series.

## Properties[​](AreaStyleOptions.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### topColor[​](AreaStyleOptions.html#topcolor "Direct link to topColor"){.hash-link aria-label="Direct link to topColor"} {#topcolor .anchor .anchorWithStickyNavbar_LWe7}

> **topColor**: `string`

Color of the top part of the area.

#### Default Value[​](AreaStyleOptions.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`'rgba( 46, 220, 135, 0.4)'`

------------------------------------------------------------------------

### bottomColor[​](AreaStyleOptions.html#bottomcolor "Direct link to bottomColor"){.hash-link aria-label="Direct link to bottomColor"} {#bottomcolor .anchor .anchorWithStickyNavbar_LWe7}

> **bottomColor**: `string`

Color of the bottom part of the area.

#### Default Value[​](AreaStyleOptions.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

`'rgba( 40, 221, 100, 0)'`

------------------------------------------------------------------------

### relativeGradient[​](AreaStyleOptions.html#relativegradient "Direct link to relativeGradient"){.hash-link aria-label="Direct link to relativeGradient"} {#relativegradient .anchor .anchorWithStickyNavbar_LWe7}

> **relativeGradient**: `boolean`

Gradient is relative to the base value and the currently visible range.
If it is false, the gradient is relative to the top and bottom of the
chart.

#### Default Value[​](AreaStyleOptions.html#default-value-2 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-2 .anchor .anchorWithStickyNavbar_LWe7}

`false`

------------------------------------------------------------------------

### invertFilledArea[​](AreaStyleOptions.html#invertfilledarea "Direct link to invertFilledArea"){.hash-link aria-label="Direct link to invertFilledArea"} {#invertfilledarea .anchor .anchorWithStickyNavbar_LWe7}

> **invertFilledArea**: `boolean`

Invert the filled area. Fills the area above the line if set to true.

#### Default Value[​](AreaStyleOptions.html#default-value-3 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-3 .anchor .anchorWithStickyNavbar_LWe7}

`false`

------------------------------------------------------------------------

### lineColor[​](AreaStyleOptions.html#linecolor "Direct link to lineColor"){.hash-link aria-label="Direct link to lineColor"} {#linecolor .anchor .anchorWithStickyNavbar_LWe7}

> **lineColor**: `string`

Line color.

#### Default Value[​](AreaStyleOptions.html#default-value-4 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-4 .anchor .anchorWithStickyNavbar_LWe7}

`'#33D778'`

------------------------------------------------------------------------

### lineStyle[​](AreaStyleOptions.html#linestyle "Direct link to lineStyle"){.hash-link aria-label="Direct link to lineStyle"} {#linestyle .anchor .anchorWithStickyNavbar_LWe7}

> **lineStyle**: [`LineStyle`](../enumerations/LineStyle.html)

Line style.

#### Default Value[​](AreaStyleOptions.html#default-value-5 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-5 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
{@link LineStyle.Solid}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### lineWidth[​](AreaStyleOptions.html#linewidth "Direct link to lineWidth"){.hash-link aria-label="Direct link to lineWidth"} {#linewidth .anchor .anchorWithStickyNavbar_LWe7}

> **lineWidth**: [`LineWidth`](../type-aliases/LineWidth.html)

Line width in pixels.

#### Default Value[​](AreaStyleOptions.html#default-value-6 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-6 .anchor .anchorWithStickyNavbar_LWe7}

`3`

------------------------------------------------------------------------

### lineType[​](AreaStyleOptions.html#linetype "Direct link to lineType"){.hash-link aria-label="Direct link to lineType"} {#linetype .anchor .anchorWithStickyNavbar_LWe7}

> **lineType**: [`LineType`](../enumerations/LineType.html)

Line type.

#### Default Value[​](AreaStyleOptions.html#default-value-7 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-7 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
{@link LineType.Simple}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### lineVisible[​](AreaStyleOptions.html#linevisible "Direct link to lineVisible"){.hash-link aria-label="Direct link to lineVisible"} {#linevisible .anchor .anchorWithStickyNavbar_LWe7}

> **lineVisible**: `boolean`

Show series line.

#### Default Value[​](AreaStyleOptions.html#default-value-8 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-8 .anchor .anchorWithStickyNavbar_LWe7}

`true`

------------------------------------------------------------------------

### pointMarkersVisible[​](AreaStyleOptions.html#pointmarkersvisible "Direct link to pointMarkersVisible"){.hash-link aria-label="Direct link to pointMarkersVisible"} {#pointmarkersvisible .anchor .anchorWithStickyNavbar_LWe7}

> **pointMarkersVisible**: `boolean`

Show circle markers on each point.

#### Default Value[​](AreaStyleOptions.html#default-value-9 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-9 .anchor .anchorWithStickyNavbar_LWe7}

`false`

------------------------------------------------------------------------

### pointMarkersRadius?[​](AreaStyleOptions.html#pointmarkersradius "Direct link to pointMarkersRadius?"){.hash-link aria-label="Direct link to pointMarkersRadius?"} {#pointmarkersradius .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **pointMarkersRadius**: `number`

Circle markers radius in pixels.

#### Default Value[​](AreaStyleOptions.html#default-value-10 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-10 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

------------------------------------------------------------------------

### crosshairMarkerVisible[​](AreaStyleOptions.html#crosshairmarkervisible "Direct link to crosshairMarkerVisible"){.hash-link aria-label="Direct link to crosshairMarkerVisible"} {#crosshairmarkervisible .anchor .anchorWithStickyNavbar_LWe7}

> **crosshairMarkerVisible**: `boolean`

Show the crosshair marker.

#### Default Value[​](AreaStyleOptions.html#default-value-11 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-11 .anchor .anchorWithStickyNavbar_LWe7}

`true`

------------------------------------------------------------------------

### crosshairMarkerRadius[​](AreaStyleOptions.html#crosshairmarkerradius "Direct link to crosshairMarkerRadius"){.hash-link aria-label="Direct link to crosshairMarkerRadius"} {#crosshairmarkerradius .anchor .anchorWithStickyNavbar_LWe7}

> **crosshairMarkerRadius**: `number`

Crosshair marker radius in pixels.

#### Default Value[​](AreaStyleOptions.html#default-value-12 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-12 .anchor .anchorWithStickyNavbar_LWe7}

`4`

------------------------------------------------------------------------

### crosshairMarkerBorderColor[​](AreaStyleOptions.html#crosshairmarkerbordercolor "Direct link to crosshairMarkerBorderColor"){.hash-link aria-label="Direct link to crosshairMarkerBorderColor"} {#crosshairmarkerbordercolor .anchor .anchorWithStickyNavbar_LWe7}

> **crosshairMarkerBorderColor**: `string`

Crosshair marker border color. An empty string falls back to the color
of the series under the crosshair.

#### Default Value[​](AreaStyleOptions.html#default-value-13 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-13 .anchor .anchorWithStickyNavbar_LWe7}

`''`

------------------------------------------------------------------------

### crosshairMarkerBackgroundColor[​](AreaStyleOptions.html#crosshairmarkerbackgroundcolor "Direct link to crosshairMarkerBackgroundColor"){.hash-link aria-label="Direct link to crosshairMarkerBackgroundColor"} {#crosshairmarkerbackgroundcolor .anchor .anchorWithStickyNavbar_LWe7}

> **crosshairMarkerBackgroundColor**: `string`

The crosshair marker background color. An empty string falls back to the
color of the series under the crosshair.

#### Default Value[​](AreaStyleOptions.html#default-value-14 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-14 .anchor .anchorWithStickyNavbar_LWe7}

`''`

------------------------------------------------------------------------

### crosshairMarkerBorderWidth[​](AreaStyleOptions.html#crosshairmarkerborderwidth "Direct link to crosshairMarkerBorderWidth"){.hash-link aria-label="Direct link to crosshairMarkerBorderWidth"} {#crosshairmarkerborderwidth .anchor .anchorWithStickyNavbar_LWe7}

> **crosshairMarkerBorderWidth**: `number`

Crosshair marker border width in pixels.

#### Default Value[​](AreaStyleOptions.html#default-value-15 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-15 .anchor .anchorWithStickyNavbar_LWe7}

`2`

------------------------------------------------------------------------

### lastPriceAnimation[​](AreaStyleOptions.html#lastpriceanimation "Direct link to lastPriceAnimation"){.hash-link aria-label="Direct link to lastPriceAnimation"} {#lastpriceanimation .anchor .anchorWithStickyNavbar_LWe7}

> **lastPriceAnimation**:
> [`LastPriceAnimationMode`](../enumerations/LastPriceAnimationMode.html)

Last price animation mode.

#### Default Value[​](AreaStyleOptions.html#default-value-16 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-16 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
{@link LastPriceAnimationMode.Disabled}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

- [Properties](AreaStyleOptions.html#properties){.table-of-contents__link
  .toc-highlight}
  - [topColor](AreaStyleOptions.html#topcolor){.table-of-contents__link
    .toc-highlight}
  - [bottomColor](AreaStyleOptions.html#bottomcolor){.table-of-contents__link
    .toc-highlight}
  - [relativeGradient](AreaStyleOptions.html#relativegradient){.table-of-contents__link
    .toc-highlight}
  - [invertFilledArea](AreaStyleOptions.html#invertfilledarea){.table-of-contents__link
    .toc-highlight}
  - [lineColor](AreaStyleOptions.html#linecolor){.table-of-contents__link
    .toc-highlight}
  - [lineStyle](AreaStyleOptions.html#linestyle){.table-of-contents__link
    .toc-highlight}
  - [lineWidth](AreaStyleOptions.html#linewidth){.table-of-contents__link
    .toc-highlight}
  - [lineType](AreaStyleOptions.html#linetype){.table-of-contents__link
    .toc-highlight}
  - [lineVisible](AreaStyleOptions.html#linevisible){.table-of-contents__link
    .toc-highlight}
  - [pointMarkersVisible](AreaStyleOptions.html#pointmarkersvisible){.table-of-contents__link
    .toc-highlight}
  - [pointMarkersRadius?](AreaStyleOptions.html#pointmarkersradius){.table-of-contents__link
    .toc-highlight}
  - [crosshairMarkerVisible](AreaStyleOptions.html#crosshairmarkervisible){.table-of-contents__link
    .toc-highlight}
  - [crosshairMarkerRadius](AreaStyleOptions.html#crosshairmarkerradius){.table-of-contents__link
    .toc-highlight}
  - [crosshairMarkerBorderColor](AreaStyleOptions.html#crosshairmarkerbordercolor){.table-of-contents__link
    .toc-highlight}
  - [crosshairMarkerBackgroundColor](AreaStyleOptions.html#crosshairmarkerbackgroundcolor){.table-of-contents__link
    .toc-highlight}
  - [crosshairMarkerBorderWidth](AreaStyleOptions.html#crosshairmarkerborderwidth){.table-of-contents__link
    .toc-highlight}
  - [lastPriceAnimation](AreaStyleOptions.html#lastpriceanimation){.table-of-contents__link
    .toc-highlight}
