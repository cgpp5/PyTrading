- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [IHorzScaleBehavior]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: IHorzScaleBehavior\<HorzScaleItem\>

Class interface for Horizontal scale behavior

## Type parameters[​](IHorzScaleBehavior.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem**

## Methods[​](IHorzScaleBehavior.html#methods "Direct link to Methods"){.hash-link aria-label="Direct link to Methods"} {#methods .anchor .anchorWithStickyNavbar_LWe7}

### options()[​](IHorzScaleBehavior.html#options "Direct link to options()"){.hash-link aria-label="Direct link to options()"} {#options .anchor .anchorWithStickyNavbar_LWe7}

> **options**():
> [`ChartOptionsImpl`](ChartOptionsImpl.html)\<`HorzScaleItem`\>

Structure describing options of the chart.

#### Returns[​](IHorzScaleBehavior.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

[`ChartOptionsImpl`](ChartOptionsImpl.html)\<`HorzScaleItem`\>

ChartOptionsBase

------------------------------------------------------------------------

### setOptions()[​](IHorzScaleBehavior.html#setoptions "Direct link to setOptions()"){.hash-link aria-label="Direct link to setOptions()"} {#setoptions .anchor .anchorWithStickyNavbar_LWe7}

> **setOptions**(`options`): `void`

Set the chart options. Note that this is different to `applyOptions`
since the provided options will overwrite the current options instead of
merging with the current options.

#### Parameters[​](IHorzScaleBehavior.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **options**:
[`ChartOptionsImpl`](ChartOptionsImpl.html)\<`HorzScaleItem`\>

Chart options to be set

#### Returns[​](IHorzScaleBehavior.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

`void`

void

------------------------------------------------------------------------

### preprocessData()[​](IHorzScaleBehavior.html#preprocessdata "Direct link to preprocessData()"){.hash-link aria-label="Direct link to preprocessData()"} {#preprocessdata .anchor .anchorWithStickyNavbar_LWe7}

> **preprocessData**(`data`): `void`

Method to preprocess the data.

#### Parameters[​](IHorzScaleBehavior.html#parameters-1 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **data**:
[`DataItem`](../type-aliases/DataItem.html)\<`HorzScaleItem`\> \|
[`DataItem`](../type-aliases/DataItem.html)\<`HorzScaleItem`\>\[\]

Data items for the series

#### Returns[​](IHorzScaleBehavior.html#returns-2 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-2 .anchor .anchorWithStickyNavbar_LWe7}

`void`

void

------------------------------------------------------------------------

### convertHorzItemToInternal()[​](IHorzScaleBehavior.html#converthorzitemtointernal "Direct link to convertHorzItemToInternal()"){.hash-link aria-label="Direct link to convertHorzItemToInternal()"} {#converthorzitemtointernal .anchor .anchorWithStickyNavbar_LWe7}

> **convertHorzItemToInternal**(`item`): `object`

Convert horizontal scale item into an internal horizontal scale item.

#### Parameters[​](IHorzScaleBehavior.html#parameters-2 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-2 .anchor .anchorWithStickyNavbar_LWe7}

• **item**: `HorzScaleItem`

item to be converted

#### Returns[​](IHorzScaleBehavior.html#returns-3 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-3 .anchor .anchorWithStickyNavbar_LWe7}

`object`

InternalHorzScaleItem

##### \[species\][​](IHorzScaleBehavior.html#species "Direct link to [species]"){.hash-link aria-label="Direct link to [species]"} {#species .anchor .anchorWithStickyNavbar_LWe7}

> **\[species\]**: `"InternalHorzScaleItem"`

The \'name\' or species of the nominal.

------------------------------------------------------------------------

### createConverterToInternalObj()[​](IHorzScaleBehavior.html#createconvertertointernalobj "Direct link to createConverterToInternalObj()"){.hash-link aria-label="Direct link to createConverterToInternalObj()"} {#createconvertertointernalobj .anchor .anchorWithStickyNavbar_LWe7}

> **createConverterToInternalObj**(`data`):
> [`HorzScaleItemConverterToInternalObj`](../type-aliases/HorzScaleItemConverterToInternalObj.html)\<`HorzScaleItem`\>

Creates and returns a converter for changing series data into internal
horizontal scale items.

#### Parameters[​](IHorzScaleBehavior.html#parameters-3 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-3 .anchor .anchorWithStickyNavbar_LWe7}

• **data**: ([`AreaData`](AreaData.html)\<`HorzScaleItem`\> \|
[`WhitespaceData`](WhitespaceData.html)\<`HorzScaleItem`\> \|
[`BarData`](BarData.html)\<`HorzScaleItem`\> \|
[`CandlestickData`](CandlestickData.html)\<`HorzScaleItem`\> \|
[`BaselineData`](BaselineData.html)\<`HorzScaleItem`\> \|
[`LineData`](LineData.html)\<`HorzScaleItem`\> \|
[`HistogramData`](HistogramData.html)\<`HorzScaleItem`\> \|
[`CustomData`](CustomData.html)\<`HorzScaleItem`\> \|
[`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.html)\<`HorzScaleItem`\>)\[\]

series data

#### Returns[​](IHorzScaleBehavior.html#returns-4 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-4 .anchor .anchorWithStickyNavbar_LWe7}

[`HorzScaleItemConverterToInternalObj`](../type-aliases/HorzScaleItemConverterToInternalObj.html)\<`HorzScaleItem`\>

HorzScaleItemConverterToInternalObj

------------------------------------------------------------------------

### key()[​](IHorzScaleBehavior.html#key "Direct link to key()"){.hash-link aria-label="Direct link to key()"} {#key .anchor .anchorWithStickyNavbar_LWe7}

> **key**(`internalItem`):
> [`InternalHorzScaleItemKey`](../type-aliases/InternalHorzScaleItemKey.html)

Returns the key for the specified horizontal scale item.

#### Parameters[​](IHorzScaleBehavior.html#parameters-4 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-4 .anchor .anchorWithStickyNavbar_LWe7}

• **internalItem**: `HorzScaleItem` \| `object`

horizontal scale item for which the key should be returned

#### Returns[​](IHorzScaleBehavior.html#returns-5 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-5 .anchor .anchorWithStickyNavbar_LWe7}

[`InternalHorzScaleItemKey`](../type-aliases/InternalHorzScaleItemKey.html)

InternalHorzScaleItemKey

------------------------------------------------------------------------

### cacheKey()[​](IHorzScaleBehavior.html#cachekey "Direct link to cacheKey()"){.hash-link aria-label="Direct link to cacheKey()"} {#cachekey .anchor .anchorWithStickyNavbar_LWe7}

> **cacheKey**(`internalItem`): `number`

Returns the cache key for the specified horizontal scale item.

#### Parameters[​](IHorzScaleBehavior.html#parameters-5 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-5 .anchor .anchorWithStickyNavbar_LWe7}

• **internalItem**

horizontal scale item for which the cache key should be returned

• **internalItem.\[species\]**: `"InternalHorzScaleItem"`

The \'name\' or species of the nominal.

#### Returns[​](IHorzScaleBehavior.html#returns-6 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-6 .anchor .anchorWithStickyNavbar_LWe7}

`number`

number

------------------------------------------------------------------------

### updateFormatter()[​](IHorzScaleBehavior.html#updateformatter "Direct link to updateFormatter()"){.hash-link aria-label="Direct link to updateFormatter()"} {#updateformatter .anchor .anchorWithStickyNavbar_LWe7}

> **updateFormatter**(`options`): `void`

Update the formatter with the localization options.

#### Parameters[​](IHorzScaleBehavior.html#parameters-6 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-6 .anchor .anchorWithStickyNavbar_LWe7}

• **options**:
[`LocalizationOptions`](LocalizationOptions.html)\<`HorzScaleItem`\>

Localization options

#### Returns[​](IHorzScaleBehavior.html#returns-7 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-7 .anchor .anchorWithStickyNavbar_LWe7}

`void`

void

------------------------------------------------------------------------

### formatHorzItem()[​](IHorzScaleBehavior.html#formathorzitem "Direct link to formatHorzItem()"){.hash-link aria-label="Direct link to formatHorzItem()"} {#formathorzitem .anchor .anchorWithStickyNavbar_LWe7}

> **formatHorzItem**(`item`): `string`

Format the horizontal scale item into a display string.

#### Parameters[​](IHorzScaleBehavior.html#parameters-7 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-7 .anchor .anchorWithStickyNavbar_LWe7}

• **item**

horizontal scale item to be formatted as a string

• **item.\[species\]**: `"InternalHorzScaleItem"`

The \'name\' or species of the nominal.

#### Returns[​](IHorzScaleBehavior.html#returns-8 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-8 .anchor .anchorWithStickyNavbar_LWe7}

`string`

string

------------------------------------------------------------------------

### formatTickmark()[​](IHorzScaleBehavior.html#formattickmark "Direct link to formatTickmark()"){.hash-link aria-label="Direct link to formatTickmark()"} {#formattickmark .anchor .anchorWithStickyNavbar_LWe7}

> **formatTickmark**(`item`, `localizationOptions`): `string`

Format the horizontal scale tickmark into a display string.

#### Parameters[​](IHorzScaleBehavior.html#parameters-8 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-8 .anchor .anchorWithStickyNavbar_LWe7}

• **item**: [`TickMark`](TickMark.html)

tickmark item

• **localizationOptions**:
[`LocalizationOptions`](LocalizationOptions.html)\<`HorzScaleItem`\>

Localization options

#### Returns[​](IHorzScaleBehavior.html#returns-9 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-9 .anchor .anchorWithStickyNavbar_LWe7}

`string`

string

------------------------------------------------------------------------

### maxTickMarkWeight()[​](IHorzScaleBehavior.html#maxtickmarkweight "Direct link to maxTickMarkWeight()"){.hash-link aria-label="Direct link to maxTickMarkWeight()"} {#maxtickmarkweight .anchor .anchorWithStickyNavbar_LWe7}

> **maxTickMarkWeight**(`marks`):
> [`TickMarkWeightValue`](../type-aliases/TickMarkWeightValue.html)

Returns the maximum tickmark weight value for the specified tickmarks on
the time scale.

#### Parameters[​](IHorzScaleBehavior.html#parameters-9 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-9 .anchor .anchorWithStickyNavbar_LWe7}

• **marks**: [`TimeMark`](TimeMark.html)\[\]

Timescale tick marks

#### Returns[​](IHorzScaleBehavior.html#returns-10 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-10 .anchor .anchorWithStickyNavbar_LWe7}

[`TickMarkWeightValue`](../type-aliases/TickMarkWeightValue.html)

TickMarkWeightValue

------------------------------------------------------------------------

### fillWeightsForPoints()[​](IHorzScaleBehavior.html#fillweightsforpoints "Direct link to fillWeightsForPoints()"){.hash-link aria-label="Direct link to fillWeightsForPoints()"} {#fillweightsforpoints .anchor .anchorWithStickyNavbar_LWe7}

> **fillWeightsForPoints**(`sortedTimePoints`, `startIndex`): `void`

Fill the weights for the sorted time scale points.

#### Parameters[​](IHorzScaleBehavior.html#parameters-10 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-10 .anchor .anchorWithStickyNavbar_LWe7}

• **sortedTimePoints**: readonly
[`Mutable`](../type-aliases/Mutable.html)
\<[`TimeScalePoint`](TimeScalePoint.html)\>\[\]

sorted time scale points

• **startIndex**: `number`

starting index

#### Returns[​](IHorzScaleBehavior.html#returns-11 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-11 .anchor .anchorWithStickyNavbar_LWe7}

`void`

void

------------------------------------------------------------------------

### shouldResetTickmarkLabels()?[​](IHorzScaleBehavior.html#shouldresettickmarklabels "Direct link to shouldResetTickmarkLabels()?"){.hash-link aria-label="Direct link to shouldResetTickmarkLabels()?"} {#shouldresettickmarklabels .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **shouldResetTickmarkLabels**(`tickMarks`): `boolean`

If returns true, then the tick mark formatter will be called for all the
visible tick marks even if the formatter has previously been called for
a specific tick mark. This allows you to change the formatting on all
the tick marks.

#### Parameters[​](IHorzScaleBehavior.html#parameters-11 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-11 .anchor .anchorWithStickyNavbar_LWe7}

• **tickMarks**: readonly [`TickMark`](TickMark.html)\[\]

array of tick marks

#### Returns[​](IHorzScaleBehavior.html#returns-12 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-12 .anchor .anchorWithStickyNavbar_LWe7}

`boolean`

boolean

- [Type
  parameters](IHorzScaleBehavior.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Methods](IHorzScaleBehavior.html#methods){.table-of-contents__link
  .toc-highlight}
  - [options()](IHorzScaleBehavior.html#options){.table-of-contents__link
    .toc-highlight}
  - [setOptions()](IHorzScaleBehavior.html#setoptions){.table-of-contents__link
    .toc-highlight}
  - [preprocessData()](IHorzScaleBehavior.html#preprocessdata){.table-of-contents__link
    .toc-highlight}
  - [convertHorzItemToInternal()](IHorzScaleBehavior.html#converthorzitemtointernal){.table-of-contents__link
    .toc-highlight}
  - [createConverterToInternalObj()](IHorzScaleBehavior.html#createconvertertointernalobj){.table-of-contents__link
    .toc-highlight}
  - [key()](IHorzScaleBehavior.html#key){.table-of-contents__link
    .toc-highlight}
  - [cacheKey()](IHorzScaleBehavior.html#cachekey){.table-of-contents__link
    .toc-highlight}
  - [updateFormatter()](IHorzScaleBehavior.html#updateformatter){.table-of-contents__link
    .toc-highlight}
  - [formatHorzItem()](IHorzScaleBehavior.html#formathorzitem){.table-of-contents__link
    .toc-highlight}
  - [formatTickmark()](IHorzScaleBehavior.html#formattickmark){.table-of-contents__link
    .toc-highlight}
  - [maxTickMarkWeight()](IHorzScaleBehavior.html#maxtickmarkweight){.table-of-contents__link
    .toc-highlight}
  - [fillWeightsForPoints()](IHorzScaleBehavior.html#fillweightsforpoints){.table-of-contents__link
    .toc-highlight}
  - [shouldResetTickmarkLabels()?](IHorzScaleBehavior.html#shouldresettickmarklabels){.table-of-contents__link
    .toc-highlight}
