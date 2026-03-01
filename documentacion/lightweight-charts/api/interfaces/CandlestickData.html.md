- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [CandlestickData]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: CandlestickData\<HorzScaleItem\>

Structure describing a single item of data for candlestick series

## Extends[​](CandlestickData.html#extends "Direct link to Extends"){.hash-link aria-label="Direct link to Extends"} {#extends .anchor .anchorWithStickyNavbar_LWe7}

- [`OhlcData`](OhlcData.html)\<`HorzScaleItem`\>

## Type parameters[​](CandlestickData.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem** = [`Time`](../type-aliases/Time.html)

## Properties[​](CandlestickData.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### color?[​](CandlestickData.html#color "Direct link to color?"){.hash-link aria-label="Direct link to color?"} {#color .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **color**: `string`

Optional color value for certain data item. If missed, color from
options is used

------------------------------------------------------------------------

### borderColor?[​](CandlestickData.html#bordercolor "Direct link to borderColor?"){.hash-link aria-label="Direct link to borderColor?"} {#bordercolor .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **borderColor**: `string`

Optional border color value for certain data item. If missed, color from
options is used

------------------------------------------------------------------------

### wickColor?[​](CandlestickData.html#wickcolor "Direct link to wickColor?"){.hash-link aria-label="Direct link to wickColor?"} {#wickcolor .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **wickColor**: `string`

Optional wick color value for certain data item. If missed, color from
options is used

------------------------------------------------------------------------

### time[​](CandlestickData.html#time "Direct link to time"){.hash-link aria-label="Direct link to time"} {#time .anchor .anchorWithStickyNavbar_LWe7}

> **time**: `HorzScaleItem`

The bar time.

#### Inherited from[​](CandlestickData.html#inherited-from "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from .anchor .anchorWithStickyNavbar_LWe7}

[`OhlcData`](OhlcData.html) . [`time`](OhlcData.html#time)

------------------------------------------------------------------------

### open[​](CandlestickData.html#open "Direct link to open"){.hash-link aria-label="Direct link to open"} {#open .anchor .anchorWithStickyNavbar_LWe7}

> **open**: `number`

The open price.

#### Inherited from[​](CandlestickData.html#inherited-from-1 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-1 .anchor .anchorWithStickyNavbar_LWe7}

[`OhlcData`](OhlcData.html) . [`open`](OhlcData.html#open)

------------------------------------------------------------------------

### high[​](CandlestickData.html#high "Direct link to high"){.hash-link aria-label="Direct link to high"} {#high .anchor .anchorWithStickyNavbar_LWe7}

> **high**: `number`

The high price.

#### Inherited from[​](CandlestickData.html#inherited-from-2 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-2 .anchor .anchorWithStickyNavbar_LWe7}

[`OhlcData`](OhlcData.html) . [`high`](OhlcData.html#high)

------------------------------------------------------------------------

### low[​](CandlestickData.html#low "Direct link to low"){.hash-link aria-label="Direct link to low"} {#low .anchor .anchorWithStickyNavbar_LWe7}

> **low**: `number`

The low price.

#### Inherited from[​](CandlestickData.html#inherited-from-3 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-3 .anchor .anchorWithStickyNavbar_LWe7}

[`OhlcData`](OhlcData.html) . [`low`](OhlcData.html#low)

------------------------------------------------------------------------

### close[​](CandlestickData.html#close "Direct link to close"){.hash-link aria-label="Direct link to close"} {#close .anchor .anchorWithStickyNavbar_LWe7}

> **close**: `number`

The close price.

#### Inherited from[​](CandlestickData.html#inherited-from-4 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-4 .anchor .anchorWithStickyNavbar_LWe7}

[`OhlcData`](OhlcData.html) . [`close`](OhlcData.html#close)

------------------------------------------------------------------------

### customValues?[​](CandlestickData.html#customvalues "Direct link to customValues?"){.hash-link aria-label="Direct link to customValues?"} {#customvalues .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **customValues**: `Record`\<`string`, `unknown`\>

Additional custom values which will be ignored by the library, but could
be used by plugins.

#### Inherited from[​](CandlestickData.html#inherited-from-5 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-5 .anchor .anchorWithStickyNavbar_LWe7}

[`OhlcData`](OhlcData.html) .
[`customValues`](OhlcData.html#customvalues)

- [Extends](CandlestickData.html#extends){.table-of-contents__link
  .toc-highlight}
- [Type
  parameters](CandlestickData.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](CandlestickData.html#properties){.table-of-contents__link
  .toc-highlight}
  - [color?](CandlestickData.html#color){.table-of-contents__link
    .toc-highlight}
  - [borderColor?](CandlestickData.html#bordercolor){.table-of-contents__link
    .toc-highlight}
  - [wickColor?](CandlestickData.html#wickcolor){.table-of-contents__link
    .toc-highlight}
  - [time](CandlestickData.html#time){.table-of-contents__link
    .toc-highlight}
  - [open](CandlestickData.html#open){.table-of-contents__link
    .toc-highlight}
  - [high](CandlestickData.html#high){.table-of-contents__link
    .toc-highlight}
  - [low](CandlestickData.html#low){.table-of-contents__link
    .toc-highlight}
  - [close](CandlestickData.html#close){.table-of-contents__link
    .toc-highlight}
  - [customValues?](CandlestickData.html#customvalues){.table-of-contents__link
    .toc-highlight}
