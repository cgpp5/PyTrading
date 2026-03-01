- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [SingleValueData]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: SingleValueData\<HorzScaleItem\>

A base interface for a data point of single-value series.

## Extends[​](SingleValueData.html#extends "Direct link to Extends"){.hash-link aria-label="Direct link to Extends"} {#extends .anchor .anchorWithStickyNavbar_LWe7}

- [`WhitespaceData`](WhitespaceData.html)\<`HorzScaleItem`\>

## Extended by[​](SingleValueData.html#extended-by "Direct link to Extended by"){.hash-link aria-label="Direct link to Extended by"} {#extended-by .anchor .anchorWithStickyNavbar_LWe7}

- [`AreaData`](AreaData.html)
- [`BaselineData`](BaselineData.html)
- [`HistogramData`](HistogramData.html)
- [`LineData`](LineData.html)

## Type parameters[​](SingleValueData.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem** = [`Time`](../type-aliases/Time.html)

## Properties[​](SingleValueData.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### time[​](SingleValueData.html#time "Direct link to time"){.hash-link aria-label="Direct link to time"} {#time .anchor .anchorWithStickyNavbar_LWe7}

> **time**: `HorzScaleItem`

The time of the data.

#### Overrides[​](SingleValueData.html#overrides "Direct link to Overrides"){.hash-link aria-label="Direct link to Overrides"} {#overrides .anchor .anchorWithStickyNavbar_LWe7}

[`WhitespaceData`](WhitespaceData.html) .
[`time`](WhitespaceData.html#time)

------------------------------------------------------------------------

### value[​](SingleValueData.html#value "Direct link to value"){.hash-link aria-label="Direct link to value"} {#value .anchor .anchorWithStickyNavbar_LWe7}

> **value**: `number`

Price value of the data.

------------------------------------------------------------------------

### customValues?[​](SingleValueData.html#customvalues "Direct link to customValues?"){.hash-link aria-label="Direct link to customValues?"} {#customvalues .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **customValues**: `Record`\<`string`, `unknown`\>

Additional custom values which will be ignored by the library, but could
be used by plugins.

#### Inherited from[​](SingleValueData.html#inherited-from "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from .anchor .anchorWithStickyNavbar_LWe7}

[`WhitespaceData`](WhitespaceData.html) .
[`customValues`](WhitespaceData.html#customvalues)

- [Extends](SingleValueData.html#extends){.table-of-contents__link
  .toc-highlight}
- [Extended
  by](SingleValueData.html#extended-by){.table-of-contents__link
  .toc-highlight}
- [Type
  parameters](SingleValueData.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](SingleValueData.html#properties){.table-of-contents__link
  .toc-highlight}
  - [time](SingleValueData.html#time){.table-of-contents__link
    .toc-highlight}
  - [value](SingleValueData.html#value){.table-of-contents__link
    .toc-highlight}
  - [customValues?](SingleValueData.html#customvalues){.table-of-contents__link
    .toc-highlight}
