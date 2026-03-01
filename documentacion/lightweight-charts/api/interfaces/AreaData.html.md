- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [AreaData]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: AreaData\<HorzScaleItem\>

Structure describing a single item of data for area series

## Extends[​](AreaData.html#extends "Direct link to Extends"){.hash-link aria-label="Direct link to Extends"} {#extends .anchor .anchorWithStickyNavbar_LWe7}

- [`SingleValueData`](SingleValueData.html)\<`HorzScaleItem`\>

## Type parameters[​](AreaData.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem** = [`Time`](../type-aliases/Time.html)

## Properties[​](AreaData.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### lineColor?[​](AreaData.html#linecolor "Direct link to lineColor?"){.hash-link aria-label="Direct link to lineColor?"} {#linecolor .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **lineColor**: `string`

Optional line color value for certain data item. If missed, color from
options is used

------------------------------------------------------------------------

### topColor?[​](AreaData.html#topcolor "Direct link to topColor?"){.hash-link aria-label="Direct link to topColor?"} {#topcolor .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **topColor**: `string`

Optional top color value for certain data item. If missed, color from
options is used

------------------------------------------------------------------------

### bottomColor?[​](AreaData.html#bottomcolor "Direct link to bottomColor?"){.hash-link aria-label="Direct link to bottomColor?"} {#bottomcolor .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **bottomColor**: `string`

Optional bottom color value for certain data item. If missed, color from
options is used

------------------------------------------------------------------------

### time[​](AreaData.html#time "Direct link to time"){.hash-link aria-label="Direct link to time"} {#time .anchor .anchorWithStickyNavbar_LWe7}

> **time**: `HorzScaleItem`

The time of the data.

#### Inherited from[​](AreaData.html#inherited-from "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from .anchor .anchorWithStickyNavbar_LWe7}

[`SingleValueData`](SingleValueData.html) .
[`time`](SingleValueData.html#time)

------------------------------------------------------------------------

### value[​](AreaData.html#value "Direct link to value"){.hash-link aria-label="Direct link to value"} {#value .anchor .anchorWithStickyNavbar_LWe7}

> **value**: `number`

Price value of the data.

#### Inherited from[​](AreaData.html#inherited-from-1 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-1 .anchor .anchorWithStickyNavbar_LWe7}

[`SingleValueData`](SingleValueData.html) .
[`value`](SingleValueData.html#value)

------------------------------------------------------------------------

### customValues?[​](AreaData.html#customvalues "Direct link to customValues?"){.hash-link aria-label="Direct link to customValues?"} {#customvalues .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **customValues**: `Record`\<`string`, `unknown`\>

Additional custom values which will be ignored by the library, but could
be used by plugins.

#### Inherited from[​](AreaData.html#inherited-from-2 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-2 .anchor .anchorWithStickyNavbar_LWe7}

[`SingleValueData`](SingleValueData.html) .
[`customValues`](SingleValueData.html#customvalues)

- [Extends](AreaData.html#extends){.table-of-contents__link
  .toc-highlight}
- [Type
  parameters](AreaData.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](AreaData.html#properties){.table-of-contents__link
  .toc-highlight}
  - [lineColor?](AreaData.html#linecolor){.table-of-contents__link
    .toc-highlight}
  - [topColor?](AreaData.html#topcolor){.table-of-contents__link
    .toc-highlight}
  - [bottomColor?](AreaData.html#bottomcolor){.table-of-contents__link
    .toc-highlight}
  - [time](AreaData.html#time){.table-of-contents__link .toc-highlight}
  - [value](AreaData.html#value){.table-of-contents__link
    .toc-highlight}
  - [customValues?](AreaData.html#customvalues){.table-of-contents__link
    .toc-highlight}
