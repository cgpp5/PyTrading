- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Functions]{.breadcrumbs__link}
- [createUpDownMarkers]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Function: createUpDownMarkers()

> **createUpDownMarkers**\<`T`\>(`series`, `options`?):
> [`ISeriesUpDownMarkerPluginApi`](../interfaces/ISeriesUpDownMarkerPluginApi.html)\<`T`\>

Creates and attaches the Series Up Down Markers Plugin.

## Type parameters[​](createUpDownMarkers.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **T**

## Parameters[​](createUpDownMarkers.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **series**: [`ISeriesApi`](../interfaces/ISeriesApi.html)\<keyof
[`SeriesOptionsMap`](../interfaces/SeriesOptionsMap.html), `T`,
[`AreaData`](../interfaces/AreaData.html)\<`T`\> \|
[`WhitespaceData`](../interfaces/WhitespaceData.html)\<`T`\> \|
[`BarData`](../interfaces/BarData.html)\<`T`\> \|
[`CandlestickData`](../interfaces/CandlestickData.html)\<`T`\> \|
[`BaselineData`](../interfaces/BaselineData.html)\<`T`\> \|
[`LineData`](../interfaces/LineData.html)\<`T`\> \|
[`HistogramData`](../interfaces/HistogramData.html)\<`T`\> \|
[`CustomData`](../interfaces/CustomData.html)\<`T`\> \|
[`CustomSeriesWhitespaceData`](../interfaces/CustomSeriesWhitespaceData.html)\<`T`\>,
[`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.html) \|
[`AreaSeriesOptions`](../type-aliases/AreaSeriesOptions.html) \|
[`BarSeriesOptions`](../type-aliases/BarSeriesOptions.html) \|
[`CandlestickSeriesOptions`](../type-aliases/CandlestickSeriesOptions.html)
\| [`BaselineSeriesOptions`](../type-aliases/BaselineSeriesOptions.html)
\| [`LineSeriesOptions`](../type-aliases/LineSeriesOptions.html) \|
[`HistogramSeriesOptions`](../type-aliases/HistogramSeriesOptions.html),
[`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`AreaStyleOptions`](../interfaces/AreaStyleOptions.html) &
[`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.html)\> \|
[`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`BarStyleOptions`](../interfaces/BarStyleOptions.html) &
[`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.html)\> \|
[`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`CandlestickStyleOptions`](../interfaces/CandlestickStyleOptions.html)
& [`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.html)\> \|
[`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`BaselineStyleOptions`](../interfaces/BaselineStyleOptions.html) &
[`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.html)\> \|
[`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`LineStyleOptions`](../interfaces/LineStyleOptions.html) &
[`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.html)\> \|
[`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`HistogramStyleOptions`](../interfaces/HistogramStyleOptions.html) &
[`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.html)\> \|
[`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`CustomStyleOptions`](../interfaces/CustomStyleOptions.html) &
[`SeriesOptionsCommon`](../interfaces/SeriesOptionsCommon.html)\>\>

Series to which attach the Up Down Markers Plugin

• **options?**: `Partial`
\<[`UpDownMarkersPluginOptions`](../interfaces/UpDownMarkersPluginOptions.html)\>

options for the Up Down Markers Plugin

## Returns[​](createUpDownMarkers.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesUpDownMarkerPluginApi`](../interfaces/ISeriesUpDownMarkerPluginApi.html)\<`T`\>

Api for Series Up Down Marker Plugin.
[ISeriesUpDownMarkerPluginApi](../interfaces/ISeriesUpDownMarkerPluginApi.html)

## Example[​](createUpDownMarkers.html#example "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}

const chart = createChart('container');
const lineSeries = chart.addSeries(LineSeries);
const upDownMarkers = createUpDownMarkers(lineSeries, {
    positiveColor: '#22AB94',
    negativeColor: '#F7525F',
    updateVisibilityDuration: 5000,
});
// to add some data
upDownMarkers.setData(
    [
        { time: '2020-02-02', value: 12.34 },
        //... more line series data
    ]
);
// ... Update some values
upDownMarkers.update({ time: '2020-02-02', value: 13.54 }, true);
// to remove plugin from the series
upDownMarkers.detach();
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

- [Type
  parameters](createUpDownMarkers.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Parameters](createUpDownMarkers.html#parameters){.table-of-contents__link
  .toc-highlight}
- [Returns](createUpDownMarkers.html#returns){.table-of-contents__link
  .toc-highlight}
- [Example](createUpDownMarkers.html#example){.table-of-contents__link
  .toc-highlight}
