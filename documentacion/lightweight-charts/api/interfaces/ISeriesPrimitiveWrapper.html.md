- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [ISeriesPrimitiveWrapper]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: ISeriesPrimitiveWrapper\<T, Options\>

Interface for a series primitive.

## Extended by[​](ISeriesPrimitiveWrapper.html#extended-by "Direct link to Extended by"){.hash-link aria-label="Direct link to Extended by"} {#extended-by .anchor .anchorWithStickyNavbar_LWe7}

- [`ISeriesMarkersPluginApi`](ISeriesMarkersPluginApi.html)
- [`ISeriesUpDownMarkerPluginApi`](ISeriesUpDownMarkerPluginApi.html)

## Type parameters[​](ISeriesPrimitiveWrapper.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **T**

• **Options** = `unknown`

## Properties[​](ISeriesPrimitiveWrapper.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### detach()[​](ISeriesPrimitiveWrapper.html#detach "Direct link to detach()"){.hash-link aria-label="Direct link to detach()"} {#detach .anchor .anchorWithStickyNavbar_LWe7}

> **detach**: () =\> `void`

Detaches the plugin from the series.

#### Returns[​](ISeriesPrimitiveWrapper.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### getSeries()[​](ISeriesPrimitiveWrapper.html#getseries "Direct link to getSeries()"){.hash-link aria-label="Direct link to getSeries()"} {#getseries .anchor .anchorWithStickyNavbar_LWe7}

> **getSeries**: () =\> [`ISeriesApi`](ISeriesApi.html)\<keyof
> [`SeriesOptionsMap`](SeriesOptionsMap.html), `T`,
> [`AreaData`](AreaData.html)\<`T`\> \|
> [`WhitespaceData`](WhitespaceData.html)\<`T`\> \|
> [`BarData`](BarData.html)\<`T`\> \|
> [`CandlestickData`](CandlestickData.html)\<`T`\> \|
> [`BaselineData`](BaselineData.html)\<`T`\> \|
> [`LineData`](LineData.html)\<`T`\> \|
> [`HistogramData`](HistogramData.html)\<`T`\> \|
> [`CustomData`](CustomData.html)\<`T`\> \|
> [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.html)\<`T`\>,
> [`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.html) \|
> [`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.html) \|
> [`BarSeriesOptions`](../type-aliases/BarSeriesOptions.html) \|
> [`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.html)
> \|
> [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.html)
> \| [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.html) \|
> [`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.html),
> [`DeepPartial`](../type-aliases/DeepPartial.html)
> \<[`AreaStyleOptions`](AreaStyleOptions.html) &
> [`SeriesOptionsCommon`](SeriesOptionsCommon.html)\> \|
> [`DeepPartial`](../type-aliases/DeepPartial.html)
> \<[`BarStyleOptions`](BarStyleOptions.html) &
> [`SeriesOptionsCommon`](SeriesOptionsCommon.html)\> \|
> [`DeepPartial`](../type-aliases/DeepPartial.html)
> \<[`CandlestickStyleOptions`](CandlestickStyleOptions.html) &
> [`SeriesOptionsCommon`](SeriesOptionsCommon.html)\> \|
> [`DeepPartial`](../type-aliases/DeepPartial.html)
> \<[`BaselineStyleOptions`](BaselineStyleOptions.html) &
> [`SeriesOptionsCommon`](SeriesOptionsCommon.html)\> \|
> [`DeepPartial`](../type-aliases/DeepPartial.html)
> \<[`LineStyleOptions`](LineStyleOptions.html) &
> [`SeriesOptionsCommon`](SeriesOptionsCommon.html)\> \|
> [`DeepPartial`](../type-aliases/DeepPartial.html)
> \<[`HistogramStyleOptions`](HistogramStyleOptions.html) &
> [`SeriesOptionsCommon`](SeriesOptionsCommon.html)\> \|
> [`DeepPartial`](../type-aliases/DeepPartial.html)
> \<[`CustomStyleOptions`](CustomStyleOptions.html) &
> [`SeriesOptionsCommon`](SeriesOptionsCommon.html)\>\>

Returns the current series.

#### Returns[​](ISeriesPrimitiveWrapper.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesApi`](ISeriesApi.html)\<keyof
[`SeriesOptionsMap`](SeriesOptionsMap.html), `T`,
[`AreaData`](AreaData.html)\<`T`\> \|
[`WhitespaceData`](WhitespaceData.html)\<`T`\> \|
[`BarData`](BarData.html)\<`T`\> \|
[`CandlestickData`](CandlestickData.html)\<`T`\> \|
[`BaselineData`](BaselineData.html)\<`T`\> \|
[`LineData`](LineData.html)\<`T`\> \|
[`HistogramData`](HistogramData.html)\<`T`\> \|
[`CustomData`](CustomData.html)\<`T`\> \|
[`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.html)\<`T`\>,
[`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.html) \|
[`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.html) \|
[`BarSeriesOptions`](../type-aliases/BarSeriesOptions.html) \|
[`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.html)
\| [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.html)
\| [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.html) \|
[`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.html),
[`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`AreaStyleOptions`](AreaStyleOptions.html) &
[`SeriesOptionsCommon`](SeriesOptionsCommon.html)\> \|
[`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`BarStyleOptions`](BarStyleOptions.html) &
[`SeriesOptionsCommon`](SeriesOptionsCommon.html)\> \|
[`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`CandlestickStyleOptions`](CandlestickStyleOptions.html) &
[`SeriesOptionsCommon`](SeriesOptionsCommon.html)\> \|
[`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`BaselineStyleOptions`](BaselineStyleOptions.html) &
[`SeriesOptionsCommon`](SeriesOptionsCommon.html)\> \|
[`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`LineStyleOptions`](LineStyleOptions.html) &
[`SeriesOptionsCommon`](SeriesOptionsCommon.html)\> \|
[`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`HistogramStyleOptions`](HistogramStyleOptions.html) &
[`SeriesOptionsCommon`](SeriesOptionsCommon.html)\> \|
[`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`CustomStyleOptions`](CustomStyleOptions.html) &
[`SeriesOptionsCommon`](SeriesOptionsCommon.html)\>\>

------------------------------------------------------------------------

### applyOptions()?[​](ISeriesPrimitiveWrapper.html#applyoptions "Direct link to applyOptions()?"){.hash-link aria-label="Direct link to applyOptions()?"} {#applyoptions .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **applyOptions**: (`options`) =\> `void`

Applies options to the primitive.

#### Parameters[​](ISeriesPrimitiveWrapper.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **options**:
[`DeepPartial`](../type-aliases/DeepPartial.html)\<`Options`\>

Options to apply. The options are deeply merged with the current
options.

#### Returns[​](ISeriesPrimitiveWrapper.html#returns-2 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-2 .anchor .anchorWithStickyNavbar_LWe7}

`void`

- [Extended
  by](ISeriesPrimitiveWrapper.html#extended-by){.table-of-contents__link
  .toc-highlight}
- [Type
  parameters](ISeriesPrimitiveWrapper.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](ISeriesPrimitiveWrapper.html#properties){.table-of-contents__link
  .toc-highlight}
  - [detach()](ISeriesPrimitiveWrapper.html#detach){.table-of-contents__link
    .toc-highlight}
  - [getSeries()](ISeriesPrimitiveWrapper.html#getseries){.table-of-contents__link
    .toc-highlight}
  - [applyOptions()?](ISeriesPrimitiveWrapper.html#applyoptions){.table-of-contents__link
    .toc-highlight}
