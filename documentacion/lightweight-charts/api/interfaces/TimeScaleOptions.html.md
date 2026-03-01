- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [TimeScaleOptions]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: TimeScaleOptions

Extended time scale options for time-based horizontal scale

## Extends[​](TimeScaleOptions.html#extends "Direct link to Extends"){.hash-link aria-label="Direct link to Extends"} {#extends .anchor .anchorWithStickyNavbar_LWe7}

- [`HorzScaleOptions`](HorzScaleOptions.html)

## Properties[​](TimeScaleOptions.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### rightOffset[​](TimeScaleOptions.html#rightoffset "Direct link to rightOffset"){.hash-link aria-label="Direct link to rightOffset"} {#rightoffset .anchor .anchorWithStickyNavbar_LWe7}

> **rightOffset**: `number`

The margin space in bars from the right side of the chart.

#### Default Value[​](TimeScaleOptions.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`0`

#### Inherited from[​](TimeScaleOptions.html#inherited-from "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`rightOffset`](HorzScaleOptions.html#rightoffset)

------------------------------------------------------------------------

### rightOffsetPixels?[​](TimeScaleOptions.html#rightoffsetpixels "Direct link to rightOffsetPixels?"){.hash-link aria-label="Direct link to rightOffsetPixels?"} {#rightoffsetpixels .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **rightOffsetPixels**: `number`

The margin space in pixels from the right side of the chart. This option
has priority over `rightOffset`.

#### Default Value[​](TimeScaleOptions.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-1 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-1 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`rightOffsetPixels`](HorzScaleOptions.html#rightoffsetpixels)

------------------------------------------------------------------------

### barSpacing[​](TimeScaleOptions.html#barspacing "Direct link to barSpacing"){.hash-link aria-label="Direct link to barSpacing"} {#barspacing .anchor .anchorWithStickyNavbar_LWe7}

> **barSpacing**: `number`

The space between bars in pixels.

#### Default Value[​](TimeScaleOptions.html#default-value-2 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-2 .anchor .anchorWithStickyNavbar_LWe7}

`6`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-2 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-2 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`barSpacing`](HorzScaleOptions.html#barspacing)

------------------------------------------------------------------------

### minBarSpacing[​](TimeScaleOptions.html#minbarspacing "Direct link to minBarSpacing"){.hash-link aria-label="Direct link to minBarSpacing"} {#minbarspacing .anchor .anchorWithStickyNavbar_LWe7}

> **minBarSpacing**: `number`

The minimum space between bars in pixels.

#### Default Value[​](TimeScaleOptions.html#default-value-3 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-3 .anchor .anchorWithStickyNavbar_LWe7}

`0.5`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-3 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-3 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`minBarSpacing`](HorzScaleOptions.html#minbarspacing)

------------------------------------------------------------------------

### maxBarSpacing[​](TimeScaleOptions.html#maxbarspacing "Direct link to maxBarSpacing"){.hash-link aria-label="Direct link to maxBarSpacing"} {#maxbarspacing .anchor .anchorWithStickyNavbar_LWe7}

> **maxBarSpacing**: `number`

The maximum space between bars in pixels.

Has no effect if value is set to `0`.

#### Default Value[​](TimeScaleOptions.html#default-value-4 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-4 .anchor .anchorWithStickyNavbar_LWe7}

`0`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-4 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-4 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`maxBarSpacing`](HorzScaleOptions.html#maxbarspacing)

------------------------------------------------------------------------

### fixLeftEdge[​](TimeScaleOptions.html#fixleftedge "Direct link to fixLeftEdge"){.hash-link aria-label="Direct link to fixLeftEdge"} {#fixleftedge .anchor .anchorWithStickyNavbar_LWe7}

> **fixLeftEdge**: `boolean`

Prevent scrolling to the left of the first bar.

#### Default Value[​](TimeScaleOptions.html#default-value-5 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-5 .anchor .anchorWithStickyNavbar_LWe7}

`false`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-5 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-5 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`fixLeftEdge`](HorzScaleOptions.html#fixleftedge)

------------------------------------------------------------------------

### fixRightEdge[​](TimeScaleOptions.html#fixrightedge "Direct link to fixRightEdge"){.hash-link aria-label="Direct link to fixRightEdge"} {#fixrightedge .anchor .anchorWithStickyNavbar_LWe7}

> **fixRightEdge**: `boolean`

Prevent scrolling to the right of the most recent bar.

#### Default Value[​](TimeScaleOptions.html#default-value-6 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-6 .anchor .anchorWithStickyNavbar_LWe7}

`false`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-6 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-6 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`fixRightEdge`](HorzScaleOptions.html#fixrightedge)

------------------------------------------------------------------------

### lockVisibleTimeRangeOnResize[​](TimeScaleOptions.html#lockvisibletimerangeonresize "Direct link to lockVisibleTimeRangeOnResize"){.hash-link aria-label="Direct link to lockVisibleTimeRangeOnResize"} {#lockvisibletimerangeonresize .anchor .anchorWithStickyNavbar_LWe7}

> **lockVisibleTimeRangeOnResize**: `boolean`

Prevent changing the visible time range during chart resizing.

#### Default Value[​](TimeScaleOptions.html#default-value-7 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-7 .anchor .anchorWithStickyNavbar_LWe7}

`false`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-7 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-7 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`lockVisibleTimeRangeOnResize`](HorzScaleOptions.html#lockvisibletimerangeonresize)

------------------------------------------------------------------------

### rightBarStaysOnScroll[​](TimeScaleOptions.html#rightbarstaysonscroll "Direct link to rightBarStaysOnScroll"){.hash-link aria-label="Direct link to rightBarStaysOnScroll"} {#rightbarstaysonscroll .anchor .anchorWithStickyNavbar_LWe7}

> **rightBarStaysOnScroll**: `boolean`

Prevent the hovered bar from moving when scrolling.

#### Default Value[​](TimeScaleOptions.html#default-value-8 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-8 .anchor .anchorWithStickyNavbar_LWe7}

`false`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-8 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-8 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`rightBarStaysOnScroll`](HorzScaleOptions.html#rightbarstaysonscroll)

------------------------------------------------------------------------

### borderVisible[​](TimeScaleOptions.html#bordervisible "Direct link to borderVisible"){.hash-link aria-label="Direct link to borderVisible"} {#bordervisible .anchor .anchorWithStickyNavbar_LWe7}

> **borderVisible**: `boolean`

Show the time scale border.

#### Default Value[​](TimeScaleOptions.html#default-value-9 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-9 .anchor .anchorWithStickyNavbar_LWe7}

`true`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-9 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-9 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`borderVisible`](HorzScaleOptions.html#bordervisible)

------------------------------------------------------------------------

### borderColor[​](TimeScaleOptions.html#bordercolor "Direct link to borderColor"){.hash-link aria-label="Direct link to borderColor"} {#bordercolor .anchor .anchorWithStickyNavbar_LWe7}

> **borderColor**: `string`

The time scale border color.

#### Default Value[​](TimeScaleOptions.html#default-value-10 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-10 .anchor .anchorWithStickyNavbar_LWe7}

`'#2B2B43'`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-10 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-10 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`borderColor`](HorzScaleOptions.html#bordercolor)

------------------------------------------------------------------------

### visible[​](TimeScaleOptions.html#visible "Direct link to visible"){.hash-link aria-label="Direct link to visible"} {#visible .anchor .anchorWithStickyNavbar_LWe7}

> **visible**: `boolean`

Show the time scale.

#### Default Value[​](TimeScaleOptions.html#default-value-11 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-11 .anchor .anchorWithStickyNavbar_LWe7}

`true`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-11 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-11 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`visible`](HorzScaleOptions.html#visible)

------------------------------------------------------------------------

### timeVisible[​](TimeScaleOptions.html#timevisible "Direct link to timeVisible"){.hash-link aria-label="Direct link to timeVisible"} {#timevisible .anchor .anchorWithStickyNavbar_LWe7}

> **timeVisible**: `boolean`

Show the time, not just the date, in the time scale and vertical
crosshair label.

#### Default Value[​](TimeScaleOptions.html#default-value-12 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-12 .anchor .anchorWithStickyNavbar_LWe7}

`false`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-12 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-12 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`timeVisible`](HorzScaleOptions.html#timevisible)

------------------------------------------------------------------------

### secondsVisible[​](TimeScaleOptions.html#secondsvisible "Direct link to secondsVisible"){.hash-link aria-label="Direct link to secondsVisible"} {#secondsvisible .anchor .anchorWithStickyNavbar_LWe7}

> **secondsVisible**: `boolean`

Show seconds in the time scale and vertical crosshair label in
`hh:mm:ss` format for intraday data.

#### Default Value[​](TimeScaleOptions.html#default-value-13 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-13 .anchor .anchorWithStickyNavbar_LWe7}

`true`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-13 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-13 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`secondsVisible`](HorzScaleOptions.html#secondsvisible)

------------------------------------------------------------------------

### shiftVisibleRangeOnNewBar[​](TimeScaleOptions.html#shiftvisiblerangeonnewbar "Direct link to shiftVisibleRangeOnNewBar"){.hash-link aria-label="Direct link to shiftVisibleRangeOnNewBar"} {#shiftvisiblerangeonnewbar .anchor .anchorWithStickyNavbar_LWe7}

> **shiftVisibleRangeOnNewBar**: `boolean`

Shift the visible range to the right (into the future) by the number of
new bars when new data is added.

Note that this only applies when the last bar is visible.

#### Default Value[​](TimeScaleOptions.html#default-value-14 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-14 .anchor .anchorWithStickyNavbar_LWe7}

`true`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-14 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-14 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`shiftVisibleRangeOnNewBar`](HorzScaleOptions.html#shiftvisiblerangeonnewbar)

------------------------------------------------------------------------

### allowShiftVisibleRangeOnWhitespaceReplacement[​](TimeScaleOptions.html#allowshiftvisiblerangeonwhitespacereplacement "Direct link to allowShiftVisibleRangeOnWhitespaceReplacement"){.hash-link aria-label="Direct link to allowShiftVisibleRangeOnWhitespaceReplacement"} {#allowshiftvisiblerangeonwhitespacereplacement .anchor .anchorWithStickyNavbar_LWe7}

> **allowShiftVisibleRangeOnWhitespaceReplacement**: `boolean`

Allow the visible range to be shifted to the right when a new bar is
added which is replacing an existing whitespace time point on the chart.

Note that this only applies when the last bar is visible &
`shiftVisibleRangeOnNewBar` is enabled.

#### Default Value[​](TimeScaleOptions.html#default-value-15 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-15 .anchor .anchorWithStickyNavbar_LWe7}

`false`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-15 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-15 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`allowShiftVisibleRangeOnWhitespaceReplacement`](HorzScaleOptions.html#allowshiftvisiblerangeonwhitespacereplacement)

------------------------------------------------------------------------

### ticksVisible[​](TimeScaleOptions.html#ticksvisible "Direct link to ticksVisible"){.hash-link aria-label="Direct link to ticksVisible"} {#ticksvisible .anchor .anchorWithStickyNavbar_LWe7}

> **ticksVisible**: `boolean`

Draw small vertical line on time axis labels.

#### Default Value[​](TimeScaleOptions.html#default-value-16 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-16 .anchor .anchorWithStickyNavbar_LWe7}

`false`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-16 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-16 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`ticksVisible`](HorzScaleOptions.html#ticksvisible)

------------------------------------------------------------------------

### tickMarkMaxCharacterLength?[​](TimeScaleOptions.html#tickmarkmaxcharacterlength "Direct link to tickMarkMaxCharacterLength?"){.hash-link aria-label="Direct link to tickMarkMaxCharacterLength?"} {#tickmarkmaxcharacterlength .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **tickMarkMaxCharacterLength**: `number`

Maximum tick mark label length. Used to override the default 8 character
maximum length.

#### Default Value[​](TimeScaleOptions.html#default-value-17 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-17 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

#### Inherited from[​](TimeScaleOptions.html#inherited-from-17 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-17 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`tickMarkMaxCharacterLength`](HorzScaleOptions.html#tickmarkmaxcharacterlength)

------------------------------------------------------------------------

### uniformDistribution[​](TimeScaleOptions.html#uniformdistribution "Direct link to uniformDistribution"){.hash-link aria-label="Direct link to uniformDistribution"} {#uniformdistribution .anchor .anchorWithStickyNavbar_LWe7}

> **uniformDistribution**: `boolean`

Changes horizontal scale marks generation. With this flag equal to
`true`, marks of the same weight are either all drawn or none are drawn
at all.

#### Inherited from[​](TimeScaleOptions.html#inherited-from-18 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-18 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`uniformDistribution`](HorzScaleOptions.html#uniformdistribution)

------------------------------------------------------------------------

### minimumHeight[​](TimeScaleOptions.html#minimumheight "Direct link to minimumHeight"){.hash-link aria-label="Direct link to minimumHeight"} {#minimumheight .anchor .anchorWithStickyNavbar_LWe7}

> **minimumHeight**: `number`

Define a minimum height for the time scale. Note: This value will be
exceeded if the time scale needs more space to display it\'s contents.

Setting a minimum height could be useful for ensuring that multiple
charts positioned in a horizontal stack each have an identical time
scale height, or for plugins which require a bit more space within the
time scale pane.

#### Default Value[​](TimeScaleOptions.html#default-value-18 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-18 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
0
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

#### Inherited from[​](TimeScaleOptions.html#inherited-from-19 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-19 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`minimumHeight`](HorzScaleOptions.html#minimumheight)

------------------------------------------------------------------------

### allowBoldLabels[​](TimeScaleOptions.html#allowboldlabels "Direct link to allowBoldLabels"){.hash-link aria-label="Direct link to allowBoldLabels"} {#allowboldlabels .anchor .anchorWithStickyNavbar_LWe7}

> **allowBoldLabels**: `boolean`

Allow major time scale labels to be rendered in a bolder font weight.

#### Default Value[​](TimeScaleOptions.html#default-value-19 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-19 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
true
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

#### Inherited from[​](TimeScaleOptions.html#inherited-from-20 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-20 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`allowBoldLabels`](HorzScaleOptions.html#allowboldlabels)

------------------------------------------------------------------------

### ignoreWhitespaceIndices[​](TimeScaleOptions.html#ignorewhitespaceindices "Direct link to ignoreWhitespaceIndices"){.hash-link aria-label="Direct link to ignoreWhitespaceIndices"} {#ignorewhitespaceindices .anchor .anchorWithStickyNavbar_LWe7}

> **ignoreWhitespaceIndices**: `boolean`

Ignore time scale points containing only whitespace (for all series)
when drawing grid lines, tick marks, and snapping the crosshair to time
scale points.

For the yield curve chart type it defaults to `true`.

#### Default Value[​](TimeScaleOptions.html#default-value-20 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-20 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
false
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

#### Inherited from[​](TimeScaleOptions.html#inherited-from-21 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-21 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`ignoreWhitespaceIndices`](HorzScaleOptions.html#ignorewhitespaceindices)

------------------------------------------------------------------------

### enableConflation[​](TimeScaleOptions.html#enableconflation "Direct link to enableConflation"){.hash-link aria-label="Direct link to enableConflation"} {#enableconflation .anchor .anchorWithStickyNavbar_LWe7}

> **enableConflation**: `boolean`

Enable data conflation for performance optimization when bar spacing is
very small. When enabled, multiple data points are automatically
combined into single points when they would be rendered in less than 0.5
pixels of screen space. This significantly improves rendering
performance for large datasets when zoomed out.

#### Default Value[​](TimeScaleOptions.html#default-value-21 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-21 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
false
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

#### Inherited from[​](TimeScaleOptions.html#inherited-from-22 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-22 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`enableConflation`](HorzScaleOptions.html#enableconflation)

------------------------------------------------------------------------

### conflationThresholdFactor?[​](TimeScaleOptions.html#conflationthresholdfactor "Direct link to conflationThresholdFactor?"){.hash-link aria-label="Direct link to conflationThresholdFactor?"} {#conflationthresholdfactor .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **conflationThresholdFactor**: `number`

Smoothing factor for conflation thresholds. Controls how aggressively
conflation is applied. This can be used to create smoother-looking
charts, especially useful for sparklines and small charts.

- 1.0 = conflate only when display can\'t show detail (default,
  performance-focused)
- 2.0 = conflate at 2x the display threshold (moderate smoothing)
- 4.0 = conflate at 4x the display threshold (strong smoothing)
- 8.0+ = very aggressive smoothing for very small charts

Higher values result in fewer data points being displayed, creating
smoother but less detailed charts. This is particularly useful for
sparklines and small charts where smooth appearance is prioritized over
showing every data point.

Note: Should be used with continuous series types (line, area, baseline)
for best visual results. Candlestick and bar series may look less
natural with high smoothing factors.

#### Default Value[​](TimeScaleOptions.html#default-value-22 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-22 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
1.0
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

#### Inherited from[​](TimeScaleOptions.html#inherited-from-23 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-23 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`conflationThresholdFactor`](HorzScaleOptions.html#conflationthresholdfactor)

------------------------------------------------------------------------

### precomputeConflationOnInit[​](TimeScaleOptions.html#precomputeconflationoninit "Direct link to precomputeConflationOnInit"){.hash-link aria-label="Direct link to precomputeConflationOnInit"} {#precomputeconflationoninit .anchor .anchorWithStickyNavbar_LWe7}

> **precomputeConflationOnInit**: `boolean`

Precompute conflation chunks for common levels right after data load.
When enabled, the system will precompute conflation data in the
background, which improves performance when zooming out but increases
initial load time and memory usage.

Performance impact:

- Initial load: +100-500ms depending on dataset size
- Memory usage: +20-50% of original dataset size
- Zoom performance: Significant improvement (10-100x faster)

Recommended for: Large datasets (\>10K points) on machines with
sufficient memory

#### Default Value[​](TimeScaleOptions.html#default-value-23 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-23 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
false
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

#### Inherited from[​](TimeScaleOptions.html#inherited-from-24 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-24 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`precomputeConflationOnInit`](HorzScaleOptions.html#precomputeconflationoninit)

------------------------------------------------------------------------

### precomputeConflationPriority[​](TimeScaleOptions.html#precomputeconflationpriority "Direct link to precomputeConflationPriority"){.hash-link aria-label="Direct link to precomputeConflationPriority"} {#precomputeconflationpriority .anchor .anchorWithStickyNavbar_LWe7}

> **precomputeConflationPriority**: `"background"` \| `"user-visible"`
> \| `"user-blocking"`

Priority used for background precompute tasks when the Prioritized Task
Scheduling API is available.

Options:

- \'background\': Lowest priority, tasks run only when the browser is
  idle
- \'user-visible\': Medium priority, tasks run when they might affect
  visible content
- \'user-blocking\': Highest priority, tasks run immediately and may
  block user interaction

Recommendation: Use \'background\' for most cases to avoid impacting
user experience. Only use higher priorities if conflation is critical
for your application\'s functionality.

#### Default Value[​](TimeScaleOptions.html#default-value-24 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-24 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
'background'
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

#### Inherited from[​](TimeScaleOptions.html#inherited-from-25 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-25 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleOptions`](HorzScaleOptions.html) .
[`precomputeConflationPriority`](HorzScaleOptions.html#precomputeconflationpriority)

------------------------------------------------------------------------

### tickMarkFormatter?[​](TimeScaleOptions.html#tickmarkformatter "Direct link to tickMarkFormatter?"){.hash-link aria-label="Direct link to tickMarkFormatter?"} {#tickmarkformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **tickMarkFormatter**:
> [`TickMarkFormatter`](../type-aliases/TickMarkFormatter.html)

Tick marks formatter can be used to customize tick marks labels on the
time axis.

#### Default Value[​](TimeScaleOptions.html#default-value-25 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-25 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

- [Extends](TimeScaleOptions.html#extends){.table-of-contents__link
  .toc-highlight}
- [Properties](TimeScaleOptions.html#properties){.table-of-contents__link
  .toc-highlight}
  - [rightOffset](TimeScaleOptions.html#rightoffset){.table-of-contents__link
    .toc-highlight}
  - [rightOffsetPixels?](TimeScaleOptions.html#rightoffsetpixels){.table-of-contents__link
    .toc-highlight}
  - [barSpacing](TimeScaleOptions.html#barspacing){.table-of-contents__link
    .toc-highlight}
  - [minBarSpacing](TimeScaleOptions.html#minbarspacing){.table-of-contents__link
    .toc-highlight}
  - [maxBarSpacing](TimeScaleOptions.html#maxbarspacing){.table-of-contents__link
    .toc-highlight}
  - [fixLeftEdge](TimeScaleOptions.html#fixleftedge){.table-of-contents__link
    .toc-highlight}
  - [fixRightEdge](TimeScaleOptions.html#fixrightedge){.table-of-contents__link
    .toc-highlight}
  - [lockVisibleTimeRangeOnResize](TimeScaleOptions.html#lockvisibletimerangeonresize){.table-of-contents__link
    .toc-highlight}
  - [rightBarStaysOnScroll](TimeScaleOptions.html#rightbarstaysonscroll){.table-of-contents__link
    .toc-highlight}
  - [borderVisible](TimeScaleOptions.html#bordervisible){.table-of-contents__link
    .toc-highlight}
  - [borderColor](TimeScaleOptions.html#bordercolor){.table-of-contents__link
    .toc-highlight}
  - [visible](TimeScaleOptions.html#visible){.table-of-contents__link
    .toc-highlight}
  - [timeVisible](TimeScaleOptions.html#timevisible){.table-of-contents__link
    .toc-highlight}
  - [secondsVisible](TimeScaleOptions.html#secondsvisible){.table-of-contents__link
    .toc-highlight}
  - [shiftVisibleRangeOnNewBar](TimeScaleOptions.html#shiftvisiblerangeonnewbar){.table-of-contents__link
    .toc-highlight}
  - [allowShiftVisibleRangeOnWhitespaceReplacement](TimeScaleOptions.html#allowshiftvisiblerangeonwhitespacereplacement){.table-of-contents__link
    .toc-highlight}
  - [ticksVisible](TimeScaleOptions.html#ticksvisible){.table-of-contents__link
    .toc-highlight}
  - [tickMarkMaxCharacterLength?](TimeScaleOptions.html#tickmarkmaxcharacterlength){.table-of-contents__link
    .toc-highlight}
  - [uniformDistribution](TimeScaleOptions.html#uniformdistribution){.table-of-contents__link
    .toc-highlight}
  - [minimumHeight](TimeScaleOptions.html#minimumheight){.table-of-contents__link
    .toc-highlight}
  - [allowBoldLabels](TimeScaleOptions.html#allowboldlabels){.table-of-contents__link
    .toc-highlight}
  - [ignoreWhitespaceIndices](TimeScaleOptions.html#ignorewhitespaceindices){.table-of-contents__link
    .toc-highlight}
  - [enableConflation](TimeScaleOptions.html#enableconflation){.table-of-contents__link
    .toc-highlight}
  - [conflationThresholdFactor?](TimeScaleOptions.html#conflationthresholdfactor){.table-of-contents__link
    .toc-highlight}
  - [precomputeConflationOnInit](TimeScaleOptions.html#precomputeconflationoninit){.table-of-contents__link
    .toc-highlight}
  - [precomputeConflationPriority](TimeScaleOptions.html#precomputeconflationpriority){.table-of-contents__link
    .toc-highlight}
  - [tickMarkFormatter?](TimeScaleOptions.html#tickmarkformatter){.table-of-contents__link
    .toc-highlight}
