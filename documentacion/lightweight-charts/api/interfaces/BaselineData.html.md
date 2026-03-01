- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [BaselineData]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: BaselineData\<HorzScaleItem\>

Structure describing a single item of data for baseline series

## Extends[​](BaselineData.html#extends "Direct link to Extends"){.hash-link aria-label="Direct link to Extends"} {#extends .anchor .anchorWithStickyNavbar_LWe7}

- [`SingleValueData`](SingleValueData.html)\<`HorzScaleItem`\>

## Type parameters[​](BaselineData.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem** = [`Time`](../type-aliases/Time.html)

## Properties[​](BaselineData.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### topFillColor1?[​](BaselineData.html#topfillcolor1 "Direct link to topFillColor1?"){.hash-link aria-label="Direct link to topFillColor1?"} {#topfillcolor1 .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **topFillColor1**: `string`

Optional top area top fill color value for certain data item. If missed,
color from options is used

------------------------------------------------------------------------

### topFillColor2?[​](BaselineData.html#topfillcolor2 "Direct link to topFillColor2?"){.hash-link aria-label="Direct link to topFillColor2?"} {#topfillcolor2 .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **topFillColor2**: `string`

Optional top area bottom fill color value for certain data item. If
missed, color from options is used

------------------------------------------------------------------------

### topLineColor?[​](BaselineData.html#toplinecolor "Direct link to topLineColor?"){.hash-link aria-label="Direct link to topLineColor?"} {#toplinecolor .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **topLineColor**: `string`

Optional top area line color value for certain data item. If missed,
color from options is used

------------------------------------------------------------------------

### bottomFillColor1?[​](BaselineData.html#bottomfillcolor1 "Direct link to bottomFillColor1?"){.hash-link aria-label="Direct link to bottomFillColor1?"} {#bottomfillcolor1 .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **bottomFillColor1**: `string`

Optional bottom area top fill color value for certain data item. If
missed, color from options is used

------------------------------------------------------------------------

### bottomFillColor2?[​](BaselineData.html#bottomfillcolor2 "Direct link to bottomFillColor2?"){.hash-link aria-label="Direct link to bottomFillColor2?"} {#bottomfillcolor2 .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **bottomFillColor2**: `string`

Optional bottom area bottom fill color value for certain data item. If
missed, color from options is used

------------------------------------------------------------------------

### bottomLineColor?[​](BaselineData.html#bottomlinecolor "Direct link to bottomLineColor?"){.hash-link aria-label="Direct link to bottomLineColor?"} {#bottomlinecolor .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **bottomLineColor**: `string`

Optional bottom area line color value for certain data item. If missed,
color from options is used

------------------------------------------------------------------------

### time[​](BaselineData.html#time "Direct link to time"){.hash-link aria-label="Direct link to time"} {#time .anchor .anchorWithStickyNavbar_LWe7}

> **time**: `HorzScaleItem`

The time of the data.

#### Inherited from[​](BaselineData.html#inherited-from "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from .anchor .anchorWithStickyNavbar_LWe7}

[`SingleValueData`](SingleValueData.html) .
[`time`](SingleValueData.html#time)

------------------------------------------------------------------------

### value[​](BaselineData.html#value "Direct link to value"){.hash-link aria-label="Direct link to value"} {#value .anchor .anchorWithStickyNavbar_LWe7}

> **value**: `number`

Price value of the data.

#### Inherited from[​](BaselineData.html#inherited-from-1 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-1 .anchor .anchorWithStickyNavbar_LWe7}

[`SingleValueData`](SingleValueData.html) .
[`value`](SingleValueData.html#value)

------------------------------------------------------------------------

### customValues?[​](BaselineData.html#customvalues "Direct link to customValues?"){.hash-link aria-label="Direct link to customValues?"} {#customvalues .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **customValues**: `Record`\<`string`, `unknown`\>

Additional custom values which will be ignored by the library, but could
be used by plugins.

#### Inherited from[​](BaselineData.html#inherited-from-2 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-2 .anchor .anchorWithStickyNavbar_LWe7}

[`SingleValueData`](SingleValueData.html) .
[`customValues`](SingleValueData.html#customvalues)

- [Extends](BaselineData.html#extends){.table-of-contents__link
  .toc-highlight}
- [Type
  parameters](BaselineData.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](BaselineData.html#properties){.table-of-contents__link
  .toc-highlight}
  - [topFillColor1?](BaselineData.html#topfillcolor1){.table-of-contents__link
    .toc-highlight}
  - [topFillColor2?](BaselineData.html#topfillcolor2){.table-of-contents__link
    .toc-highlight}
  - [topLineColor?](BaselineData.html#toplinecolor){.table-of-contents__link
    .toc-highlight}
  - [bottomFillColor1?](BaselineData.html#bottomfillcolor1){.table-of-contents__link
    .toc-highlight}
  - [bottomFillColor2?](BaselineData.html#bottomfillcolor2){.table-of-contents__link
    .toc-highlight}
  - [bottomLineColor?](BaselineData.html#bottomlinecolor){.table-of-contents__link
    .toc-highlight}
  - [time](BaselineData.html#time){.table-of-contents__link
    .toc-highlight}
  - [value](BaselineData.html#value){.table-of-contents__link
    .toc-highlight}
  - [customValues?](BaselineData.html#customvalues){.table-of-contents__link
    .toc-highlight}
