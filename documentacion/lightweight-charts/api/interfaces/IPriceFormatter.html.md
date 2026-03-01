- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [IPriceFormatter]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: IPriceFormatter

Interface to be implemented by the object in order to be used as a price
formatter

## Methods[​](IPriceFormatter.html#methods "Direct link to Methods"){.hash-link aria-label="Direct link to Methods"} {#methods .anchor .anchorWithStickyNavbar_LWe7}

### format()[​](IPriceFormatter.html#format "Direct link to format()"){.hash-link aria-label="Direct link to format()"} {#format .anchor .anchorWithStickyNavbar_LWe7}

> **format**(`price`): `string`

Formatting function

#### Parameters[​](IPriceFormatter.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **price**: `number`

Original price to be formatted

#### Returns[​](IPriceFormatter.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`string`

Formatted price

------------------------------------------------------------------------

### formatTickmarks()[​](IPriceFormatter.html#formattickmarks "Direct link to formatTickmarks()"){.hash-link aria-label="Direct link to formatTickmarks()"} {#formattickmarks .anchor .anchorWithStickyNavbar_LWe7}

> **formatTickmarks**(`prices`): `string`\[\]

A formatting function for price scale tick marks. Use this function to
define formatting rules based on all provided price values.

#### Parameters[​](IPriceFormatter.html#parameters-1 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **prices**: readonly `number`\[\]

Prices to be formatted

#### Returns[​](IPriceFormatter.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

`string`\[\]

Formatted prices

- [Methods](IPriceFormatter.html#methods){.table-of-contents__link
  .toc-highlight}
  - [format()](IPriceFormatter.html#format){.table-of-contents__link
    .toc-highlight}
  - [formatTickmarks()](IPriceFormatter.html#formattickmarks){.table-of-contents__link
    .toc-highlight}
