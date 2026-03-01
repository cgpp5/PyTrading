- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [PriceChartLocalizationOptions]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: PriceChartLocalizationOptions

Extends LocalizationOptions for price-based charts. Includes settings
specific to formatting price values on the horizontal scale.

## Extends[​](PriceChartLocalizationOptions.html#extends "Direct link to Extends"){.hash-link aria-label="Direct link to Extends"} {#extends .anchor .anchorWithStickyNavbar_LWe7}

- [`LocalizationOptions`](LocalizationOptions.html)
  \<[`HorzScalePriceItem`](../type-aliases/HorzScalePriceItem.html)\>

## Properties[​](PriceChartLocalizationOptions.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### timeFormatter?[​](PriceChartLocalizationOptions.html#timeformatter "Direct link to timeFormatter?"){.hash-link aria-label="Direct link to timeFormatter?"} {#timeformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **timeFormatter**:
> [`TimeFormatterFn`](../type-aliases/TimeFormatterFn.html)\<`number`\>

Override formatting of the time scale crosshair label.

#### Default Value[​](PriceChartLocalizationOptions.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

#### Inherited from[​](PriceChartLocalizationOptions.html#inherited-from "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from .anchor .anchorWithStickyNavbar_LWe7}

[`LocalizationOptions`](LocalizationOptions.html) .
[`timeFormatter`](LocalizationOptions.html#timeformatter)

------------------------------------------------------------------------

### dateFormat[​](PriceChartLocalizationOptions.html#dateformat "Direct link to dateFormat"){.hash-link aria-label="Direct link to dateFormat"} {#dateformat .anchor .anchorWithStickyNavbar_LWe7}

> **dateFormat**: `string`

Date formatting string.

Can contain `yyyy`, `yy`, `MMMM`, `MMM`, `MM` and `dd` literals which
will be replaced with corresponding date\'s value.

Ignored if [timeFormatter](LocalizationOptions.html#timeformatter) has
been specified.

#### Default Value[​](PriceChartLocalizationOptions.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

`'dd MMM \'yy'`

#### Inherited from[​](PriceChartLocalizationOptions.html#inherited-from-1 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-1 .anchor .anchorWithStickyNavbar_LWe7}

[`LocalizationOptions`](LocalizationOptions.html) .
[`dateFormat`](LocalizationOptions.html#dateformat)

------------------------------------------------------------------------

### locale[​](PriceChartLocalizationOptions.html#locale "Direct link to locale"){.hash-link aria-label="Direct link to locale"} {#locale .anchor .anchorWithStickyNavbar_LWe7}

> **locale**: `string`

Current locale used to format dates. Uses the browser\'s language
settings by default.

#### See[​](PriceChartLocalizationOptions.html#see "Direct link to See"){.hash-link aria-label="Direct link to See"} {#see .anchor .anchorWithStickyNavbar_LWe7}

[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation){target="_blank"
rel="noopener noreferrer"}

#### Default Value[​](PriceChartLocalizationOptions.html#default-value-2 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-2 .anchor .anchorWithStickyNavbar_LWe7}

`navigator.language`

#### Inherited from[​](PriceChartLocalizationOptions.html#inherited-from-2 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-2 .anchor .anchorWithStickyNavbar_LWe7}

[`LocalizationOptions`](LocalizationOptions.html) .
[`locale`](LocalizationOptions.html#locale)

------------------------------------------------------------------------

### priceFormatter?[​](PriceChartLocalizationOptions.html#priceformatter "Direct link to priceFormatter?"){.hash-link aria-label="Direct link to priceFormatter?"} {#priceformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **priceFormatter**:
> [`PriceFormatterFn`](../type-aliases/PriceFormatterFn.html)

Override formatting of the price scale tick marks, labels and crosshair
labels. Can be used for cases that can\'t be covered with built-in price
formats.

#### See[​](PriceChartLocalizationOptions.html#see-1 "Direct link to See"){.hash-link aria-label="Direct link to See"} {#see-1 .anchor .anchorWithStickyNavbar_LWe7}

[PriceFormatCustom](PriceFormatCustom.html)

#### Default Value[​](PriceChartLocalizationOptions.html#default-value-3 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-3 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

#### Inherited from[​](PriceChartLocalizationOptions.html#inherited-from-3 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-3 .anchor .anchorWithStickyNavbar_LWe7}

[`LocalizationOptions`](LocalizationOptions.html) .
[`priceFormatter`](LocalizationOptions.html#priceformatter)

------------------------------------------------------------------------

### tickmarksPriceFormatter?[​](PriceChartLocalizationOptions.html#tickmarkspriceformatter "Direct link to tickmarksPriceFormatter?"){.hash-link aria-label="Direct link to tickmarksPriceFormatter?"} {#tickmarkspriceformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **tickmarksPriceFormatter**:
> [`TickmarksPriceFormatterFn`](../type-aliases/TickmarksPriceFormatterFn.html)

Overrides the formatting of price scale tick marks. Use this to define
formatting rules based on all provided price values.

#### Default Value[​](PriceChartLocalizationOptions.html#default-value-4 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-4 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

#### Inherited from[​](PriceChartLocalizationOptions.html#inherited-from-4 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-4 .anchor .anchorWithStickyNavbar_LWe7}

[`LocalizationOptions`](LocalizationOptions.html) .
[`tickmarksPriceFormatter`](LocalizationOptions.html#tickmarkspriceformatter)

------------------------------------------------------------------------

### percentageFormatter?[​](PriceChartLocalizationOptions.html#percentageformatter "Direct link to percentageFormatter?"){.hash-link aria-label="Direct link to percentageFormatter?"} {#percentageformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **percentageFormatter**:
> [`PercentageFormatterFn`](../type-aliases/PercentageFormatterFn.html)

Overrides the formatting of percentage scale tick marks.

#### Default Value[​](PriceChartLocalizationOptions.html#default-value-5 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-5 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

#### Inherited from[​](PriceChartLocalizationOptions.html#inherited-from-5 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-5 .anchor .anchorWithStickyNavbar_LWe7}

[`LocalizationOptions`](LocalizationOptions.html) .
[`percentageFormatter`](LocalizationOptions.html#percentageformatter)

------------------------------------------------------------------------

### tickmarksPercentageFormatter?[​](PriceChartLocalizationOptions.html#tickmarkspercentageformatter "Direct link to tickmarksPercentageFormatter?"){.hash-link aria-label="Direct link to tickmarksPercentageFormatter?"} {#tickmarkspercentageformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **tickmarksPercentageFormatter**:
> [`TickmarksPercentageFormatterFn`](../type-aliases/TickmarksPercentageFormatterFn.html)

Override formatting of the percentage scale tick marks. Can be used if
formatting should be adjusted based on all the values being formatted

#### Default Value[​](PriceChartLocalizationOptions.html#default-value-6 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-6 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

#### Inherited from[​](PriceChartLocalizationOptions.html#inherited-from-6 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-6 .anchor .anchorWithStickyNavbar_LWe7}

[`LocalizationOptions`](LocalizationOptions.html) .
[`tickmarksPercentageFormatter`](LocalizationOptions.html#tickmarkspercentageformatter)

------------------------------------------------------------------------

### precision[​](PriceChartLocalizationOptions.html#precision "Direct link to precision"){.hash-link aria-label="Direct link to precision"} {#precision .anchor .anchorWithStickyNavbar_LWe7}

> **precision**: `number`

The number of decimal places to display for price values on the
horizontal scale.

- [Extends](PriceChartLocalizationOptions.html#extends){.table-of-contents__link
  .toc-highlight}
- [Properties](PriceChartLocalizationOptions.html#properties){.table-of-contents__link
  .toc-highlight}
  - [timeFormatter?](PriceChartLocalizationOptions.html#timeformatter){.table-of-contents__link
    .toc-highlight}
  - [dateFormat](PriceChartLocalizationOptions.html#dateformat){.table-of-contents__link
    .toc-highlight}
  - [locale](PriceChartLocalizationOptions.html#locale){.table-of-contents__link
    .toc-highlight}
  - [priceFormatter?](PriceChartLocalizationOptions.html#priceformatter){.table-of-contents__link
    .toc-highlight}
  - [tickmarksPriceFormatter?](PriceChartLocalizationOptions.html#tickmarkspriceformatter){.table-of-contents__link
    .toc-highlight}
  - [percentageFormatter?](PriceChartLocalizationOptions.html#percentageformatter){.table-of-contents__link
    .toc-highlight}
  - [tickmarksPercentageFormatter?](PriceChartLocalizationOptions.html#tickmarkspercentageformatter){.table-of-contents__link
    .toc-highlight}
  - [precision](PriceChartLocalizationOptions.html#precision){.table-of-contents__link
    .toc-highlight}
