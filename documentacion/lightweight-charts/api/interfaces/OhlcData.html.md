- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [OhlcData]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: OhlcData\<HorzScaleItem\>

Represents a bar with a [Time](../type-aliases/Time.html) and open,
high, low, and close prices.

## Extends[​](OhlcData.html#extends "Direct link to Extends"){.hash-link aria-label="Direct link to Extends"} {#extends .anchor .anchorWithStickyNavbar_LWe7}

- [`WhitespaceData`](WhitespaceData.html)\<`HorzScaleItem`\>

## Extended by[​](OhlcData.html#extended-by "Direct link to Extended by"){.hash-link aria-label="Direct link to Extended by"} {#extended-by .anchor .anchorWithStickyNavbar_LWe7}

- [`BarData`](BarData.html)
- [`CandlestickData`](CandlestickData.html)

## Type parameters[​](OhlcData.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem** = [`Time`](../type-aliases/Time.html)

## Properties[​](OhlcData.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### time[​](OhlcData.html#time "Direct link to time"){.hash-link aria-label="Direct link to time"} {#time .anchor .anchorWithStickyNavbar_LWe7}

> **time**: `HorzScaleItem`

The bar time.

#### Overrides[​](OhlcData.html#overrides "Direct link to Overrides"){.hash-link aria-label="Direct link to Overrides"} {#overrides .anchor .anchorWithStickyNavbar_LWe7}

[`WhitespaceData`](WhitespaceData.html) .
[`time`](WhitespaceData.html#time)

------------------------------------------------------------------------

### open[​](OhlcData.html#open "Direct link to open"){.hash-link aria-label="Direct link to open"} {#open .anchor .anchorWithStickyNavbar_LWe7}

> **open**: `number`

The open price.

------------------------------------------------------------------------

### high[​](OhlcData.html#high "Direct link to high"){.hash-link aria-label="Direct link to high"} {#high .anchor .anchorWithStickyNavbar_LWe7}

> **high**: `number`

The high price.

------------------------------------------------------------------------

### low[​](OhlcData.html#low "Direct link to low"){.hash-link aria-label="Direct link to low"} {#low .anchor .anchorWithStickyNavbar_LWe7}

> **low**: `number`

The low price.

------------------------------------------------------------------------

### close[​](OhlcData.html#close "Direct link to close"){.hash-link aria-label="Direct link to close"} {#close .anchor .anchorWithStickyNavbar_LWe7}

> **close**: `number`

The close price.

------------------------------------------------------------------------

### customValues?[​](OhlcData.html#customvalues "Direct link to customValues?"){.hash-link aria-label="Direct link to customValues?"} {#customvalues .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **customValues**: `Record`\<`string`, `unknown`\>

Additional custom values which will be ignored by the library, but could
be used by plugins.

#### Inherited from[​](OhlcData.html#inherited-from "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from .anchor .anchorWithStickyNavbar_LWe7}

[`WhitespaceData`](WhitespaceData.html) .
[`customValues`](WhitespaceData.html#customvalues)

- [Extends](OhlcData.html#extends){.table-of-contents__link
  .toc-highlight}
- [Extended by](OhlcData.html#extended-by){.table-of-contents__link
  .toc-highlight}
- [Type
  parameters](OhlcData.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](OhlcData.html#properties){.table-of-contents__link
  .toc-highlight}
  - [time](OhlcData.html#time){.table-of-contents__link .toc-highlight}
  - [open](OhlcData.html#open){.table-of-contents__link .toc-highlight}
  - [high](OhlcData.html#high){.table-of-contents__link .toc-highlight}
  - [low](OhlcData.html#low){.table-of-contents__link .toc-highlight}
  - [close](OhlcData.html#close){.table-of-contents__link
    .toc-highlight}
  - [customValues?](OhlcData.html#customvalues){.table-of-contents__link
    .toc-highlight}
