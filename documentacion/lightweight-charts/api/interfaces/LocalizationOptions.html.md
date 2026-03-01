- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [LocalizationOptions]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: LocalizationOptions\<HorzScaleItem\>

Represents options for formatting dates, times, and prices according to
a locale.

## Extends[​](LocalizationOptions.html#extends "Direct link to Extends"){.hash-link aria-label="Direct link to Extends"} {#extends .anchor .anchorWithStickyNavbar_LWe7}

- [`LocalizationOptionsBase`](LocalizationOptionsBase.html)

## Extended by[​](LocalizationOptions.html#extended-by "Direct link to Extended by"){.hash-link aria-label="Direct link to Extended by"} {#extended-by .anchor .anchorWithStickyNavbar_LWe7}

- [`PriceChartLocalizationOptions`](PriceChartLocalizationOptions.html)

## Type parameters[​](LocalizationOptions.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem**

## Properties[​](LocalizationOptions.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### timeFormatter?[​](LocalizationOptions.html#timeformatter "Direct link to timeFormatter?"){.hash-link aria-label="Direct link to timeFormatter?"} {#timeformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **timeFormatter**:
> [`TimeFormatterFn`](../type-aliases/TimeFormatterFn.html)\<`HorzScaleItem`\>

Override formatting of the time scale crosshair label.

#### Default Value[​](LocalizationOptions.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

------------------------------------------------------------------------

### dateFormat[​](LocalizationOptions.html#dateformat "Direct link to dateFormat"){.hash-link aria-label="Direct link to dateFormat"} {#dateformat .anchor .anchorWithStickyNavbar_LWe7}

> **dateFormat**: `string`

Date formatting string.

Can contain `yyyy`, `yy`, `MMMM`, `MMM`, `MM` and `dd` literals which
will be replaced with corresponding date\'s value.

Ignored if [timeFormatter](LocalizationOptions.html#timeformatter) has
been specified.

#### Default Value[​](LocalizationOptions.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

`'dd MMM \'yy'`

------------------------------------------------------------------------

### locale[​](LocalizationOptions.html#locale "Direct link to locale"){.hash-link aria-label="Direct link to locale"} {#locale .anchor .anchorWithStickyNavbar_LWe7}

> **locale**: `string`

Current locale used to format dates. Uses the browser\'s language
settings by default.

#### See[​](LocalizationOptions.html#see "Direct link to See"){.hash-link aria-label="Direct link to See"} {#see .anchor .anchorWithStickyNavbar_LWe7}

[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#Locale_identification_and_negotiation){target="_blank"
rel="noopener noreferrer"}

#### Default Value[​](LocalizationOptions.html#default-value-2 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-2 .anchor .anchorWithStickyNavbar_LWe7}

`navigator.language`

#### Inherited from[​](LocalizationOptions.html#inherited-from "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from .anchor .anchorWithStickyNavbar_LWe7}

[`LocalizationOptionsBase`](LocalizationOptionsBase.html) .
[`locale`](LocalizationOptionsBase.html#locale)

------------------------------------------------------------------------

### priceFormatter?[​](LocalizationOptions.html#priceformatter "Direct link to priceFormatter?"){.hash-link aria-label="Direct link to priceFormatter?"} {#priceformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **priceFormatter**:
> [`PriceFormatterFn`](../type-aliases/PriceFormatterFn.html)

Override formatting of the price scale tick marks, labels and crosshair
labels. Can be used for cases that can\'t be covered with built-in price
formats.

#### See[​](LocalizationOptions.html#see-1 "Direct link to See"){.hash-link aria-label="Direct link to See"} {#see-1 .anchor .anchorWithStickyNavbar_LWe7}

[PriceFormatCustom](PriceFormatCustom.html)

#### Default Value[​](LocalizationOptions.html#default-value-3 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-3 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

#### Inherited from[​](LocalizationOptions.html#inherited-from-1 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-1 .anchor .anchorWithStickyNavbar_LWe7}

[`LocalizationOptionsBase`](LocalizationOptionsBase.html) .
[`priceFormatter`](LocalizationOptionsBase.html#priceformatter)

------------------------------------------------------------------------

### tickmarksPriceFormatter?[​](LocalizationOptions.html#tickmarkspriceformatter "Direct link to tickmarksPriceFormatter?"){.hash-link aria-label="Direct link to tickmarksPriceFormatter?"} {#tickmarkspriceformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **tickmarksPriceFormatter**:
> [`TickmarksPriceFormatterFn`](../type-aliases/TickmarksPriceFormatterFn.html)

Overrides the formatting of price scale tick marks. Use this to define
formatting rules based on all provided price values.

#### Default Value[​](LocalizationOptions.html#default-value-4 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-4 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

#### Inherited from[​](LocalizationOptions.html#inherited-from-2 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-2 .anchor .anchorWithStickyNavbar_LWe7}

[`LocalizationOptionsBase`](LocalizationOptionsBase.html) .
[`tickmarksPriceFormatter`](LocalizationOptionsBase.html#tickmarkspriceformatter)

------------------------------------------------------------------------

### percentageFormatter?[​](LocalizationOptions.html#percentageformatter "Direct link to percentageFormatter?"){.hash-link aria-label="Direct link to percentageFormatter?"} {#percentageformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **percentageFormatter**:
> [`PercentageFormatterFn`](../type-aliases/PercentageFormatterFn.html)

Overrides the formatting of percentage scale tick marks.

#### Default Value[​](LocalizationOptions.html#default-value-5 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-5 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

#### Inherited from[​](LocalizationOptions.html#inherited-from-3 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-3 .anchor .anchorWithStickyNavbar_LWe7}

[`LocalizationOptionsBase`](LocalizationOptionsBase.html) .
[`percentageFormatter`](LocalizationOptionsBase.html#percentageformatter)

------------------------------------------------------------------------

### tickmarksPercentageFormatter?[​](LocalizationOptions.html#tickmarkspercentageformatter "Direct link to tickmarksPercentageFormatter?"){.hash-link aria-label="Direct link to tickmarksPercentageFormatter?"} {#tickmarkspercentageformatter .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **tickmarksPercentageFormatter**:
> [`TickmarksPercentageFormatterFn`](../type-aliases/TickmarksPercentageFormatterFn.html)

Override formatting of the percentage scale tick marks. Can be used if
formatting should be adjusted based on all the values being formatted

#### Default Value[​](LocalizationOptions.html#default-value-6 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-6 .anchor .anchorWithStickyNavbar_LWe7}

`undefined`

#### Inherited from[​](LocalizationOptions.html#inherited-from-4 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-4 .anchor .anchorWithStickyNavbar_LWe7}

[`LocalizationOptionsBase`](LocalizationOptionsBase.html) .
[`tickmarksPercentageFormatter`](LocalizationOptionsBase.html#tickmarkspercentageformatter)

- [Extends](LocalizationOptions.html#extends){.table-of-contents__link
  .toc-highlight}
- [Extended
  by](LocalizationOptions.html#extended-by){.table-of-contents__link
  .toc-highlight}
- [Type
  parameters](LocalizationOptions.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](LocalizationOptions.html#properties){.table-of-contents__link
  .toc-highlight}
  - [timeFormatter?](LocalizationOptions.html#timeformatter){.table-of-contents__link
    .toc-highlight}
  - [dateFormat](LocalizationOptions.html#dateformat){.table-of-contents__link
    .toc-highlight}
  - [locale](LocalizationOptions.html#locale){.table-of-contents__link
    .toc-highlight}
  - [priceFormatter?](LocalizationOptions.html#priceformatter){.table-of-contents__link
    .toc-highlight}
  - [tickmarksPriceFormatter?](LocalizationOptions.html#tickmarkspriceformatter){.table-of-contents__link
    .toc-highlight}
  - [percentageFormatter?](LocalizationOptions.html#percentageformatter){.table-of-contents__link
    .toc-highlight}
  - [tickmarksPercentageFormatter?](LocalizationOptions.html#tickmarkspercentageformatter){.table-of-contents__link
    .toc-highlight}
