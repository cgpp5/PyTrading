- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [CustomData]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: CustomData\<HorzScaleItem\>

Base structure describing a single item of data for a custom series.

This type allows for any properties to be defined within the interface.
It is recommended that you extend this interface with the required data
structure.

## Extends[​](CustomData.html#extends "Direct link to Extends"){.hash-link aria-label="Direct link to Extends"} {#extends .anchor .anchorWithStickyNavbar_LWe7}

- [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.html)\<`HorzScaleItem`\>

## Type parameters[​](CustomData.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem** = [`Time`](../type-aliases/Time.html)

## Properties[​](CustomData.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### color?[​](CustomData.html#color "Direct link to color?"){.hash-link aria-label="Direct link to color?"} {#color .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **color**: `string`

If defined then this color will be used for the price line and price
scale line for this specific data item of the custom series.

------------------------------------------------------------------------

### time[​](CustomData.html#time "Direct link to time"){.hash-link aria-label="Direct link to time"} {#time .anchor .anchorWithStickyNavbar_LWe7}

> **time**: `HorzScaleItem`

The time of the data.

#### Inherited from[​](CustomData.html#inherited-from "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from .anchor .anchorWithStickyNavbar_LWe7}

[`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.html) .
[`time`](CustomSeriesWhitespaceData.html#time)

------------------------------------------------------------------------

### customValues?[​](CustomData.html#customvalues "Direct link to customValues?"){.hash-link aria-label="Direct link to customValues?"} {#customvalues .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **customValues**: `Record`\<`string`, `unknown`\>

Additional custom values which will be ignored by the library, but could
be used by plugins.

#### Inherited from[​](CustomData.html#inherited-from-1 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-1 .anchor .anchorWithStickyNavbar_LWe7}

[`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.html) .
[`customValues`](CustomSeriesWhitespaceData.html#customvalues)

- [Extends](CustomData.html#extends){.table-of-contents__link
  .toc-highlight}
- [Type
  parameters](CustomData.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](CustomData.html#properties){.table-of-contents__link
  .toc-highlight}
  - [color?](CustomData.html#color){.table-of-contents__link
    .toc-highlight}
  - [time](CustomData.html#time){.table-of-contents__link
    .toc-highlight}
  - [customValues?](CustomData.html#customvalues){.table-of-contents__link
    .toc-highlight}
