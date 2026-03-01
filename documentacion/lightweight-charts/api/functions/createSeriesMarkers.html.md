- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Functions]{.breadcrumbs__link}
- [createSeriesMarkers]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Function: createSeriesMarkers()

> **createSeriesMarkers**\<`HorzScaleItem`\>(`series`, `markers`?,
> `options`?):
> [`ISeriesMarkersPluginApi`](../interfaces/ISeriesMarkersPluginApi.html)\<`HorzScaleItem`\>

A function to create a series markers primitive.

## Type parameters[​](createSeriesMarkers.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem**

## Parameters[​](createSeriesMarkers.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **series**: [`ISeriesApi`](../interfaces/ISeriesApi.html)\<keyof
[`SeriesOptionsMap`](../interfaces/SeriesOptionsMap.html),
`HorzScaleItem`,
[`AreaData`](../interfaces/AreaData.html)\<`HorzScaleItem`\> \|
[`WhitespaceData`](../interfaces/WhitespaceData.html)\<`HorzScaleItem`\>
\| [`BarData`](../interfaces/BarData.html)\<`HorzScaleItem`\> \|
[`CandlestickData`](../interfaces/CandlestickData.html)\<`HorzScaleItem`\>
\| [`BaselineData`](../interfaces/BaselineData.html)\<`HorzScaleItem`\>
\| [`LineData`](../interfaces/LineData.html)\<`HorzScaleItem`\> \|
[`HistogramData`](../interfaces/HistogramData.html)\<`HorzScaleItem`\>
\| [`CustomData`](../interfaces/CustomData.html)\<`HorzScaleItem`\> \|
[`CustomSeriesWhitespaceData`](../interfaces/CustomSeriesWhitespaceData.html)\<`HorzScaleItem`\>,
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

The series to which the primitive will be attached.

• **markers?**:
[`SeriesMarker`](../type-aliases/SeriesMarker.html)\<`HorzScaleItem`\>\[\]

An array of markers to be displayed on the series.

• **options?**: [`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`SeriesMarkersOptions`](../interfaces/SeriesMarkersOptions.html)\>

Options for the series markers plugin.

## Returns[​](createSeriesMarkers.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesMarkersPluginApi`](../interfaces/ISeriesMarkersPluginApi.html)\<`HorzScaleItem`\>

## Example[​](createSeriesMarkers.html#example "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}

    const seriesMarkers = createSeriesMarkers(
        series,
        [
            {
                color: 'green',
                position: 'inBar',
                shape: 'arrowDown',
                time: 1556880900,
            },
        ]
    );
 // and then you can modify the markers
 // set it to empty array to remove all markers
 seriesMarkers.setMarkers([]);

 // `seriesMarkers.markers()` returns current markers
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

- [Type
  parameters](createSeriesMarkers.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Parameters](createSeriesMarkers.html#parameters){.table-of-contents__link
  .toc-highlight}
- [Returns](createSeriesMarkers.html#returns){.table-of-contents__link
  .toc-highlight}
- [Example](createSeriesMarkers.html#example){.table-of-contents__link
  .toc-highlight}
