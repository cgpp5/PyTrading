- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [PriceFormatCustom]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: PriceFormatCustom

Represents series value formatting options.

## Properties[​](PriceFormatCustom.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### type[​](PriceFormatCustom.html#type "Direct link to type"){.hash-link aria-label="Direct link to type"} {#type .anchor .anchorWithStickyNavbar_LWe7}

> **type**: `"custom"`

The custom price format.

------------------------------------------------------------------------

### formatter[​](PriceFormatCustom.html#formatter "Direct link to formatter"){.hash-link aria-label="Direct link to formatter"} {#formatter .anchor .anchorWithStickyNavbar_LWe7}

> **formatter**:
> [`PriceFormatterFn`](../type-aliases/PriceFormatterFn.html)

Override price formatting behaviour. Can be used for cases that can\'t
be covered with built-in price formats.

------------------------------------------------------------------------

### tickmarksFormatter?[​](PriceFormatCustom.html#tickmarksformatter "Direct link to tickmarksFormatter?"){.hash-link aria-label="Direct link to tickmarksFormatter?"} {#tickmarksformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **tickmarksFormatter**:
> [`TickmarksPriceFormatterFn`](../type-aliases/TickmarksPriceFormatterFn.html)

Override price formatting for multiple prices. Can be used if formatter
should be adjusted based of all values being formatted.

------------------------------------------------------------------------

### minMove[​](PriceFormatCustom.html#minmove "Direct link to minMove"){.hash-link aria-label="Direct link to minMove"} {#minmove .anchor .anchorWithStickyNavbar_LWe7}

> **minMove**: `number`

The minimum possible step size for price value movement.

#### Default Value[​](PriceFormatCustom.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`0.01`

------------------------------------------------------------------------

### base?[​](PriceFormatCustom.html#base "Direct link to base?"){.hash-link aria-label="Direct link to base?"} {#base .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **base**: `number`

The base value for the price format. It should equal to 1 /
[minMove](PriceFormatCustom.html#minmove). If this option is specified,
we ignore the [minMove](PriceFormatCustom.html#minmove) option. It can
be useful for cases with very small price movements like `1e-18` where
we can reach limitations of floating point precision.

- [Properties](PriceFormatCustom.html#properties){.table-of-contents__link
  .toc-highlight}
  - [type](PriceFormatCustom.html#type){.table-of-contents__link
    .toc-highlight}
  - [formatter](PriceFormatCustom.html#formatter){.table-of-contents__link
    .toc-highlight}
  - [tickmarksFormatter?](PriceFormatCustom.html#tickmarksformatter){.table-of-contents__link
    .toc-highlight}
  - [minMove](PriceFormatCustom.html#minmove){.table-of-contents__link
    .toc-highlight}
  - [base?](PriceFormatCustom.html#base){.table-of-contents__link
    .toc-highlight}
