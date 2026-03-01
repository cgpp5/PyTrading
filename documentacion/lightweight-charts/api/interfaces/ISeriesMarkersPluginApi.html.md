- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [ISeriesMarkersPluginApi]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: ISeriesMarkersPluginApi\<HorzScaleItem\>

Interface for a series markers plugin

## Extends[​](ISeriesMarkersPluginApi.html#extends "Direct link to Extends"){.hash-link aria-label="Direct link to Extends"} {#extends .anchor .anchorWithStickyNavbar_LWe7}

- [`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.html)\<`HorzScaleItem`\>

## Type parameters[​](ISeriesMarkersPluginApi.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem**

## Properties[​](ISeriesMarkersPluginApi.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### setMarkers()[​](ISeriesMarkersPluginApi.html#setmarkers "Direct link to setMarkers()"){.hash-link aria-label="Direct link to setMarkers()"} {#setmarkers .anchor .anchorWithStickyNavbar_LWe7}

> **setMarkers**: (`markers`) =\> `void`

Set markers to the series.

#### Parameters[​](ISeriesMarkersPluginApi.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **markers**:
[`SeriesMarker`](../type-aliases/SeriesMarker.html)\<`HorzScaleItem`\>\[\]

An array of markers to be displayed on the series.

#### Returns[​](ISeriesMarkersPluginApi.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### markers()[​](ISeriesMarkersPluginApi.html#markers "Direct link to markers()"){.hash-link aria-label="Direct link to markers()"} {#markers .anchor .anchorWithStickyNavbar_LWe7}

> **markers**: () =\> readonly
> [`SeriesMarker`](../type-aliases/SeriesMarker.html)\<`HorzScaleItem`\>\[\]

Returns current markers.

#### Returns[​](ISeriesMarkersPluginApi.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

readonly
[`SeriesMarker`](../type-aliases/SeriesMarker.html)\<`HorzScaleItem`\>\[\]

------------------------------------------------------------------------

### detach()[​](ISeriesMarkersPluginApi.html#detach "Direct link to detach()"){.hash-link aria-label="Direct link to detach()"} {#detach .anchor .anchorWithStickyNavbar_LWe7}

> **detach**: () =\> `void`

Detaches the plugin from the series.

#### Returns[​](ISeriesMarkersPluginApi.html#returns-2 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-2 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Overrides[​](ISeriesMarkersPluginApi.html#overrides "Direct link to Overrides"){.hash-link aria-label="Direct link to Overrides"} {#overrides .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.html) .
[`detach`](ISeriesPrimitiveWrapper.html#detach)

------------------------------------------------------------------------

### getSeries()[​](ISeriesMarkersPluginApi.html#getseries "Direct link to getSeries()"){.hash-link aria-label="Direct link to getSeries()"} {#getseries .anchor .anchorWithStickyNavbar_LWe7}

> **getSeries**: () =\> [`ISeriesApi`](ISeriesApi.html)\<keyof
> [`SeriesOptionsMap`](SeriesOptionsMap.html), `HorzScaleItem`,
> [`AreaData`](AreaData.html)\<`HorzScaleItem`\> \|
> [`WhitespaceData`](WhitespaceData.html)\<`HorzScaleItem`\> \|
> [`BarData`](BarData.html)\<`HorzScaleItem`\> \|
> [`CandlestickData`](CandlestickData.html)\<`HorzScaleItem`\> \|
> [`BaselineData`](BaselineData.html)\<`HorzScaleItem`\> \|
> [`LineData`](LineData.html)\<`HorzScaleItem`\> \|
> [`HistogramData`](HistogramData.html)\<`HorzScaleItem`\> \|
> [`CustomData`](CustomData.html)\<`HorzScaleItem`\> \|
> [`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.html)\<`HorzScaleItem`\>,
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

#### Returns[​](ISeriesMarkersPluginApi.html#returns-3 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-3 .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesApi`](ISeriesApi.html)\<keyof
[`SeriesOptionsMap`](SeriesOptionsMap.html), `HorzScaleItem`,
[`AreaData`](AreaData.html)\<`HorzScaleItem`\> \|
[`WhitespaceData`](WhitespaceData.html)\<`HorzScaleItem`\> \|
[`BarData`](BarData.html)\<`HorzScaleItem`\> \|
[`CandlestickData`](CandlestickData.html)\<`HorzScaleItem`\> \|
[`BaselineData`](BaselineData.html)\<`HorzScaleItem`\> \|
[`LineData`](LineData.html)\<`HorzScaleItem`\> \|
[`HistogramData`](HistogramData.html)\<`HorzScaleItem`\> \|
[`CustomData`](CustomData.html)\<`HorzScaleItem`\> \|
[`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.html)\<`HorzScaleItem`\>,
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

#### Inherited from[​](ISeriesMarkersPluginApi.html#inherited-from "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.html) .
[`getSeries`](ISeriesPrimitiveWrapper.html#getseries)

------------------------------------------------------------------------

### applyOptions()?[​](ISeriesMarkersPluginApi.html#applyoptions "Direct link to applyOptions()?"){.hash-link aria-label="Direct link to applyOptions()?"} {#applyoptions .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **applyOptions**: (`options`) =\> `void`

Applies options to the primitive.

#### Parameters[​](ISeriesMarkersPluginApi.html#parameters-1 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **options**:
[`DeepPartial`](../type-aliases/DeepPartial.html)\<`unknown`\>

Options to apply. The options are deeply merged with the current
options.

#### Returns[​](ISeriesMarkersPluginApi.html#returns-4 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-4 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](ISeriesMarkersPluginApi.html#inherited-from-1 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-1 .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.html) .
[`applyOptions`](ISeriesPrimitiveWrapper.html#applyoptions)

- [Extends](ISeriesMarkersPluginApi.html#extends){.table-of-contents__link
  .toc-highlight}
- [Type
  parameters](ISeriesMarkersPluginApi.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](ISeriesMarkersPluginApi.html#properties){.table-of-contents__link
  .toc-highlight}
  - [setMarkers()](ISeriesMarkersPluginApi.html#setmarkers){.table-of-contents__link
    .toc-highlight}
  - [markers()](ISeriesMarkersPluginApi.html#markers){.table-of-contents__link
    .toc-highlight}
  - [detach()](ISeriesMarkersPluginApi.html#detach){.table-of-contents__link
    .toc-highlight}
  - [getSeries()](ISeriesMarkersPluginApi.html#getseries){.table-of-contents__link
    .toc-highlight}
  - [applyOptions()?](ISeriesMarkersPluginApi.html#applyoptions){.table-of-contents__link
    .toc-highlight}
