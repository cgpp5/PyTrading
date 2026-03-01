- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [LocalizationOptionsBase]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: LocalizationOptionsBase

Represents basic localization options

## Extended by[​](LocalizationOptionsBase.html#extended-by "Direct link to Extended by"){.hash-link aria-label="Direct link to Extended by"} {#extended-by .anchor .anchorWithStickyNavbar_LWe7}

- [`LocalizationOptions`](LocalizationOptions.html)

## Properties[​](LocalizationOptionsBase.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### locale[​](LocalizationOptionsBase.html#locale "Direct link to locale"){.hash-link aria-label="Direct link to locale"} {#locale .anchor .anchorWithStickyNavbar_LWe7}

> **locale**: `string`

Current locale used to format dates. Uses the browser\'s language
settings by default.

#### See[​](LocalizationOptionsBase.html#see "Direct link to See"){.hash-link aria-label="Direct link to See"} {#see .anchor .anchorWithStickyNavbar_LWe7}

[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation){target="_blank"
rel="noopener noreferrer"}

#### Default Value[​](LocalizationOptionsBase.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`navigator.language`

------------------------------------------------------------------------

### priceFormatter?[​](LocalizationOptionsBase.html#priceformatter "Direct link to priceFormatter?"){.hash-link aria-label="Direct link to priceFormatter?"} {#priceformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **priceFormatter**:
> [`PriceFormatterFn`](../type-aliases/PriceFormatterFn.html)

Override formatting of the price scale tick marks, labels and crosshair
labels. Can be used for cases that can\'t be covered with built-in price
formats.

#### See[​](LocalizationOptionsBase.html#see-1 "Direct link to See"){.hash-link aria-label="Direct link to See"} {#see-1 .anchor .anchorWithStickyNavbar_LWe7}

[PriceFormatCustom](PriceFormatCustom.html)

#### Default Value[​](LocalizationOptionsBase.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

------------------------------------------------------------------------

### tickmarksPriceFormatter?[​](LocalizationOptionsBase.html#tickmarkspriceformatter "Direct link to tickmarksPriceFormatter?"){.hash-link aria-label="Direct link to tickmarksPriceFormatter?"} {#tickmarkspriceformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **tickmarksPriceFormatter**:
> [`TickmarksPriceFormatterFn`](../type-aliases/TickmarksPriceFormatterFn.html)

Overrides the formatting of price scale tick marks. Use this to define
formatting rules based on all provided price values.

#### Default Value[​](LocalizationOptionsBase.html#default-value-2 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-2 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

------------------------------------------------------------------------

### percentageFormatter?[​](LocalizationOptionsBase.html#percentageformatter "Direct link to percentageFormatter?"){.hash-link aria-label="Direct link to percentageFormatter?"} {#percentageformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **percentageFormatter**:
> [`PercentageFormatterFn`](../type-aliases/PercentageFormatterFn.html)

Overrides the formatting of percentage scale tick marks.

#### Default Value[​](LocalizationOptionsBase.html#default-value-3 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-3 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

------------------------------------------------------------------------

### tickmarksPercentageFormatter?[​](LocalizationOptionsBase.html#tickmarkspercentageformatter "Direct link to tickmarksPercentageFormatter?"){.hash-link aria-label="Direct link to tickmarksPercentageFormatter?"} {#tickmarkspercentageformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **tickmarksPercentageFormatter**:
> [`TickmarksPercentageFormatterFn`](../type-aliases/TickmarksPercentageFormatterFn.html)

Override formatting of the percentage scale tick marks. Can be used if
formatting should be adjusted based on all the values being formatted

#### Default Value[​](LocalizationOptionsBase.html#default-value-4 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-4 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

- [Extended
  by](LocalizationOptionsBase.html#extended-by){.table-of-contents__link
  .toc-highlight}
- [Properties](LocalizationOptionsBase.html#properties){.table-of-contents__link
  .toc-highlight}
  - [locale](LocalizationOptionsBase.html#locale){.table-of-contents__link
    .toc-highlight}
  - [priceFormatter?](LocalizationOptionsBase.html#priceformatter){.table-of-contents__link
    .toc-highlight}
  - [tickmarksPriceFormatter?](LocalizationOptionsBase.html#tickmarkspriceformatter){.table-of-contents__link
    .toc-highlight}
  - [percentageFormatter?](LocalizationOptionsBase.html#percentageformatter){.table-of-contents__link
    .toc-highlight}
  - [tickmarksPercentageFormatter?](LocalizationOptionsBase.html#tickmarkspercentageformatter){.table-of-contents__link
    .toc-highlight}
