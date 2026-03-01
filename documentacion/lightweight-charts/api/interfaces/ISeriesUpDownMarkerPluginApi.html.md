- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [ISeriesUpDownMarkerPluginApi]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: ISeriesUpDownMarkerPluginApi\<HorzScaleItem, TData\>

UpDownMarkersPrimitive Plugin for showing the direction of price changes
on the chart. This plugin can only be used with Line and Area series
types.

1.  Manual control:

- Use the `setMarkers` method to manually add markers to the chart. This
  will replace any existing markers.
- Use `clearMarkers` to remove all markers.

2.  Automatic updates:

Use `setData` and `update` from this primitive instead of the those on
the series to let the primitive handle the creation of price change
markers automatically.

- Use `setData` to initialize or replace all data points.
- Use `update` to modify individual data points. This will automatically
  create markers for price changes on existing data points.
- The `updateVisibilityDuration` option controls how long markers remain
  visible.

## Extends[​](ISeriesUpDownMarkerPluginApi.html#extends "Direct link to Extends"){.hash-link aria-label="Direct link to Extends"} {#extends .anchor .anchorWithStickyNavbar_LWe7}

- [`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.html)\<`HorzScaleItem`\>

## Type parameters[​](ISeriesUpDownMarkerPluginApi.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem**

• **TData** *extends*
[`SeriesDataItemTypeMap`](SeriesDataItemTypeMap.html)\<`HorzScaleItem`\>\[[`UpDownMarkersSupportedSeriesTypes`](../type-aliases/UpDownMarkersSupportedSeriesTypes.html)\]
=
[`SeriesDataItemTypeMap`](SeriesDataItemTypeMap.html)\<`HorzScaleItem`\>\[`"Line"`\]

## Properties[​](ISeriesUpDownMarkerPluginApi.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### detach()[​](ISeriesUpDownMarkerPluginApi.html#detach "Direct link to detach()"){.hash-link aria-label="Direct link to detach()"} {#detach .anchor .anchorWithStickyNavbar_LWe7}

> **detach**: () =\> `void`

Detaches the plugin from the series.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](ISeriesUpDownMarkerPluginApi.html#inherited-from "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.html) .
[`detach`](ISeriesPrimitiveWrapper.html#detach)

------------------------------------------------------------------------

### getSeries()[​](ISeriesUpDownMarkerPluginApi.html#getseries "Direct link to getSeries()"){.hash-link aria-label="Direct link to getSeries()"} {#getseries .anchor .anchorWithStickyNavbar_LWe7}

> **getSeries**: () =\> [`ISeriesApi`](ISeriesApi.html)\<keyof
> [`SeriesOptionsMap`](SeriesOptionsMap.html), `HorzScaleItem`,
> [`WhitespaceData`](WhitespaceData.html)\<`HorzScaleItem`\> \|
> [`LineData`](LineData.html)\<`HorzScaleItem`\> \|
> [`AreaData`](AreaData.html)\<`HorzScaleItem`\> \|
> [`BarData`](BarData.html)\<`HorzScaleItem`\> \|
> [`CandlestickData`](CandlestickData.html)\<`HorzScaleItem`\> \|
> [`BaselineData`](BaselineData.html)\<`HorzScaleItem`\> \|
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

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesApi`](ISeriesApi.html)\<keyof
[`SeriesOptionsMap`](SeriesOptionsMap.html), `HorzScaleItem`,
[`WhitespaceData`](WhitespaceData.html)\<`HorzScaleItem`\> \|
[`LineData`](LineData.html)\<`HorzScaleItem`\> \|
[`AreaData`](AreaData.html)\<`HorzScaleItem`\> \|
[`BarData`](BarData.html)\<`HorzScaleItem`\> \|
[`CandlestickData`](CandlestickData.html)\<`HorzScaleItem`\> \|
[`BaselineData`](BaselineData.html)\<`HorzScaleItem`\> \|
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

#### Inherited from[​](ISeriesUpDownMarkerPluginApi.html#inherited-from-1 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-1 .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.html) .
[`getSeries`](ISeriesPrimitiveWrapper.html#getseries)

------------------------------------------------------------------------

### applyOptions()[​](ISeriesUpDownMarkerPluginApi.html#applyoptions "Direct link to applyOptions()"){.hash-link aria-label="Direct link to applyOptions()"} {#applyoptions .anchor .anchorWithStickyNavbar_LWe7}

> **applyOptions**: (`options`) =\> `void`

Applies new options to the plugin.

#### Parameters[​](ISeriesUpDownMarkerPluginApi.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **options**: `Partial`
\<[`UpDownMarkersPluginOptions`](UpDownMarkersPluginOptions.html)\>

Partial options to apply.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns-2 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-2 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Overrides[​](ISeriesUpDownMarkerPluginApi.html#overrides "Direct link to Overrides"){.hash-link aria-label="Direct link to Overrides"} {#overrides .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesPrimitiveWrapper`](ISeriesPrimitiveWrapper.html) .
[`applyOptions`](ISeriesPrimitiveWrapper.html#applyoptions)

------------------------------------------------------------------------

### setData()[​](ISeriesUpDownMarkerPluginApi.html#setdata "Direct link to setData()"){.hash-link aria-label="Direct link to setData()"} {#setdata .anchor .anchorWithStickyNavbar_LWe7}

> **setData**: (`data`) =\> `void`

Sets the data for the series and manages data points for marker updates.

#### Parameters[​](ISeriesUpDownMarkerPluginApi.html#parameters-1 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **data**: `TData`\[\]

Array of data points to set.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns-3 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-3 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### update()[​](ISeriesUpDownMarkerPluginApi.html#update "Direct link to update()"){.hash-link aria-label="Direct link to update()"} {#update .anchor .anchorWithStickyNavbar_LWe7}

> **update**: (`data`, `historicalUpdate`?) =\> `void`

Updates a single data point and manages marker updates for existing data
points.

#### Parameters[​](ISeriesUpDownMarkerPluginApi.html#parameters-2 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-2 .anchor .anchorWithStickyNavbar_LWe7}

• **data**: `TData`

The data point to update.

• **historicalUpdate?**: `boolean`

Optional flag for historical updates.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns-4 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-4 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### markers()[​](ISeriesUpDownMarkerPluginApi.html#markers "Direct link to markers()"){.hash-link aria-label="Direct link to markers()"} {#markers .anchor .anchorWithStickyNavbar_LWe7}

> **markers**: () =\> readonly
> [`SeriesUpDownMarker`](SeriesUpDownMarker.html)\<`HorzScaleItem`\>\[\]

Retrieves the current markers on the chart.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns-5 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-5 .anchor .anchorWithStickyNavbar_LWe7}

readonly
[`SeriesUpDownMarker`](SeriesUpDownMarker.html)\<`HorzScaleItem`\>\[\]

------------------------------------------------------------------------

### setMarkers()[​](ISeriesUpDownMarkerPluginApi.html#setmarkers "Direct link to setMarkers()"){.hash-link aria-label="Direct link to setMarkers()"} {#setmarkers .anchor .anchorWithStickyNavbar_LWe7}

> **setMarkers**: (`markers`) =\> `void`

Manually sets markers on the chart.

#### Parameters[​](ISeriesUpDownMarkerPluginApi.html#parameters-3 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-3 .anchor .anchorWithStickyNavbar_LWe7}

• **markers**:
[`SeriesUpDownMarker`](SeriesUpDownMarker.html)\<`HorzScaleItem`\>\[\]

Array of SeriesUpDownMarker to set.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns-6 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-6 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### clearMarkers()[​](ISeriesUpDownMarkerPluginApi.html#clearmarkers "Direct link to clearMarkers()"){.hash-link aria-label="Direct link to clearMarkers()"} {#clearmarkers .anchor .anchorWithStickyNavbar_LWe7}

> **clearMarkers**: () =\> `void`

Clears all markers from the chart.

#### Returns[​](ISeriesUpDownMarkerPluginApi.html#returns-7 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-7 .anchor .anchorWithStickyNavbar_LWe7}

`void`

- [Extends](ISeriesUpDownMarkerPluginApi.html#extends){.table-of-contents__link
  .toc-highlight}
- [Type
  parameters](ISeriesUpDownMarkerPluginApi.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](ISeriesUpDownMarkerPluginApi.html#properties){.table-of-contents__link
  .toc-highlight}
  - [detach()](ISeriesUpDownMarkerPluginApi.html#detach){.table-of-contents__link
    .toc-highlight}
  - [getSeries()](ISeriesUpDownMarkerPluginApi.html#getseries){.table-of-contents__link
    .toc-highlight}
  - [applyOptions()](ISeriesUpDownMarkerPluginApi.html#applyoptions){.table-of-contents__link
    .toc-highlight}
  - [setData()](ISeriesUpDownMarkerPluginApi.html#setdata){.table-of-contents__link
    .toc-highlight}
  - [update()](ISeriesUpDownMarkerPluginApi.html#update){.table-of-contents__link
    .toc-highlight}
  - [markers()](ISeriesUpDownMarkerPluginApi.html#markers){.table-of-contents__link
    .toc-highlight}
  - [setMarkers()](ISeriesUpDownMarkerPluginApi.html#setmarkers){.table-of-contents__link
    .toc-highlight}
  - [clearMarkers()](ISeriesUpDownMarkerPluginApi.html#clearmarkers){.table-of-contents__link
    .toc-highlight}
