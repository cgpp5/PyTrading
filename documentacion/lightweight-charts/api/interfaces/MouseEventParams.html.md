- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [MouseEventParams]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: MouseEventParams\<HorzScaleItem\>

Represents a mouse event.

## Type parameters[​](MouseEventParams.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem** = [`Time`](../type-aliases/Time.html)

## Properties[​](MouseEventParams.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### time?[​](MouseEventParams.html#time "Direct link to time?"){.hash-link aria-label="Direct link to time?"} {#time .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **time**: `HorzScaleItem`

Time of the data at the location of the mouse event.

The value will be `undefined` if the location of the event in the chart
is outside the range of available data.

------------------------------------------------------------------------

### logical?[​](MouseEventParams.html#logical "Direct link to logical?"){.hash-link aria-label="Direct link to logical?"} {#logical .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **logical**: [`Logical`](../type-aliases/Logical.html)

Logical index

------------------------------------------------------------------------

### point?[​](MouseEventParams.html#point "Direct link to point?"){.hash-link aria-label="Direct link to point?"} {#point .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **point**: [`Point`](Point.html)

Location of the event in the chart.

The value will be `undefined` if the event is fired outside the chart,
for example a mouse leave event.

------------------------------------------------------------------------

### paneIndex?[​](MouseEventParams.html#paneindex "Direct link to paneIndex?"){.hash-link aria-label="Direct link to paneIndex?"} {#paneindex .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **paneIndex**: `number`

The index of the Pane

------------------------------------------------------------------------

### seriesData[​](MouseEventParams.html#seriesdata "Direct link to seriesData"){.hash-link aria-label="Direct link to seriesData"} {#seriesdata .anchor .anchorWithStickyNavbar_LWe7}

> **seriesData**: `Map` \<[`ISeriesApi`](ISeriesApi.html)\<keyof
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
> [`SeriesOptionsCommon`](SeriesOptionsCommon.html)\>\>,
> [`BarData`](BarData.html)\<`HorzScaleItem`\> \|
> [`LineData`](LineData.html)\<`HorzScaleItem`\> \|
> [`HistogramData`](HistogramData.html)\<`HorzScaleItem`\> \|
> [`CustomData`](CustomData.html)\<`HorzScaleItem`\>\>

Data of all series at the location of the event in the chart.

Keys of the map are [ISeriesApi](ISeriesApi.html) instances. Values are
prices. Values of the map are original data items

------------------------------------------------------------------------

### hoveredSeries?[​](MouseEventParams.html#hoveredseries "Direct link to hoveredSeries?"){.hash-link aria-label="Direct link to hoveredSeries?"} {#hoveredseries .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **hoveredSeries**: [`ISeriesApi`](ISeriesApi.html)\<keyof
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

The [ISeriesApi](ISeriesApi.html) for the series at the point of the
mouse event.

------------------------------------------------------------------------

### hoveredObjectId?[​](MouseEventParams.html#hoveredobjectid "Direct link to hoveredObjectId?"){.hash-link aria-label="Direct link to hoveredObjectId?"} {#hoveredobjectid .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **hoveredObjectId**: `unknown`

The ID of the object at the point of the mouse event.

------------------------------------------------------------------------

### sourceEvent?[​](MouseEventParams.html#sourceevent "Direct link to sourceEvent?"){.hash-link aria-label="Direct link to sourceEvent?"} {#sourceevent .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **sourceEvent**:
> [`TouchMouseEventData`](TouchMouseEventData.html)

The underlying source mouse or touch event data, if available

- [Type
  parameters](MouseEventParams.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](MouseEventParams.html#properties){.table-of-contents__link
  .toc-highlight}
  - [time?](MouseEventParams.html#time){.table-of-contents__link
    .toc-highlight}
  - [logical?](MouseEventParams.html#logical){.table-of-contents__link
    .toc-highlight}
  - [point?](MouseEventParams.html#point){.table-of-contents__link
    .toc-highlight}
  - [paneIndex?](MouseEventParams.html#paneindex){.table-of-contents__link
    .toc-highlight}
  - [seriesData](MouseEventParams.html#seriesdata){.table-of-contents__link
    .toc-highlight}
  - [hoveredSeries?](MouseEventParams.html#hoveredseries){.table-of-contents__link
    .toc-highlight}
  - [hoveredObjectId?](MouseEventParams.html#hoveredobjectid){.table-of-contents__link
    .toc-highlight}
  - [sourceEvent?](MouseEventParams.html#sourceevent){.table-of-contents__link
    .toc-highlight}
