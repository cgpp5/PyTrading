- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [IYieldCurveChartApi]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: IYieldCurveChartApi

The main interface of a single yield curve chart.

## Extends[​](IYieldCurveChartApi.html#extends "Direct link to Extends"){.hash-link aria-label="Direct link to Extends"} {#extends .anchor .anchorWithStickyNavbar_LWe7}

- `Omit` \<[`IChartApiBase`](IChartApiBase.html)\<`number`\>,
  `"addSeries"`\>

## Methods[​](IYieldCurveChartApi.html#methods "Direct link to Methods"){.hash-link aria-label="Direct link to Methods"} {#methods .anchor .anchorWithStickyNavbar_LWe7}

### remove()[​](IYieldCurveChartApi.html#remove "Direct link to remove()"){.hash-link aria-label="Direct link to remove()"} {#remove .anchor .anchorWithStickyNavbar_LWe7}

> **remove**(): `void`

Removes the chart object including all DOM elements. This is an
irreversible operation, you cannot do anything with the chart after
removing it.

#### Returns[​](IYieldCurveChartApi.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from .anchor .anchorWithStickyNavbar_LWe7}

`Omit.remove`

------------------------------------------------------------------------

### resize()[​](IYieldCurveChartApi.html#resize "Direct link to resize()"){.hash-link aria-label="Direct link to resize()"} {#resize .anchor .anchorWithStickyNavbar_LWe7}

> **resize**(`width`, `height`, `forceRepaint`?): `void`

Sets fixed size of the chart. By default chart takes up 100% of its
container.

If chart has the `autoSize` option enabled, and the ResizeObserver is
available then the width and height values will be ignored.

#### Parameters[​](IYieldCurveChartApi.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **width**: `number`

Target width of the chart.

• **height**: `number`

Target height of the chart.

• **forceRepaint?**: `boolean`

True to initiate resize immediately. One could need this to get
screenshot immediately after resize.

#### Returns[​](IYieldCurveChartApi.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-1 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-1 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.resize`

------------------------------------------------------------------------

### addCustomSeries()[​](IYieldCurveChartApi.html#addcustomseries "Direct link to addCustomSeries()"){.hash-link aria-label="Direct link to addCustomSeries()"} {#addcustomseries .anchor .anchorWithStickyNavbar_LWe7}

> **addCustomSeries**\<`TData`, `TOptions`,
> `TPartialOptions`\>(`customPaneView`, `customOptions`?, `paneIndex`?):
> [`ISeriesApi`](ISeriesApi.html)\<`"Custom"`, `number`,
> [`WhitespaceData`](WhitespaceData.html)\<`number`\> \| `TData`,
> `TOptions`, `TPartialOptions`\>

Creates a custom series with specified parameters.

A custom series is a generic series which can be extended with a custom
renderer to implement chart types which the library doesn\'t support by
default.

#### Type parameters[​](IYieldCurveChartApi.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **TData** *extends* [`CustomData`](CustomData.html)\<`number`\>

• **TOptions** *extends*
[`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.html)

• **TPartialOptions** *extends*
[`DeepPartial`](../type-aliases/DeepPartial.html)\<`TOptions` &
[`SeriesOptionsCommon`](SeriesOptionsCommon.html)\> =
[`DeepPartial`](../type-aliases/DeepPartial.html)\<`TOptions` &
[`SeriesOptionsCommon`](SeriesOptionsCommon.html)\>

#### Parameters[​](IYieldCurveChartApi.html#parameters-1 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **customPaneView**:
[`ICustomSeriesPaneView`](ICustomSeriesPaneView.html)\<`number`,
`TData`, `TOptions`\>

A custom series pane view which implements the custom renderer.

• **customOptions?**:
[`DeepPartial`](../type-aliases/DeepPartial.html)\<`TOptions` &
[`SeriesOptionsCommon`](SeriesOptionsCommon.html)\>

Customization parameters of the series being created.

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const series = chart.addCustomSeries(myCustomPaneView);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

• **paneIndex?**: `number`

#### Returns[​](IYieldCurveChartApi.html#returns-2 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-2 .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesApi`](ISeriesApi.html)\<`"Custom"`, `number`,
[`WhitespaceData`](WhitespaceData.html)\<`number`\> \| `TData`,
`TOptions`, `TPartialOptions`\>

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-2 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-2 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.addCustomSeries`

------------------------------------------------------------------------

### removeSeries()[​](IYieldCurveChartApi.html#removeseries "Direct link to removeSeries()"){.hash-link aria-label="Direct link to removeSeries()"} {#removeseries .anchor .anchorWithStickyNavbar_LWe7}

> **removeSeries**(`seriesApi`): `void`

Removes a series of any type. This is an irreversible operation, you
cannot do anything with the series after removing it.

#### Parameters[​](IYieldCurveChartApi.html#parameters-2 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-2 .anchor .anchorWithStickyNavbar_LWe7}

• **seriesApi**: [`ISeriesApi`](ISeriesApi.html)\<keyof
[`SeriesOptionsMap`](SeriesOptionsMap.html), `number`,
[`WhitespaceData`](WhitespaceData.html)\<`number`\> \|
[`LineData`](LineData.html)\<`number`\> \|
[`CustomData`](CustomData.html)\<`number`\> \|
[`AreaData`](AreaData.html)\<`number`\> \|
[`BarData`](BarData.html)\<`number`\> \|
[`CandlestickData`](CandlestickData.html)\<`number`\> \|
[`BaselineData`](BaselineData.html)\<`number`\> \|
[`HistogramData`](HistogramData.html)\<`number`\> \|
[`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.html)\<`number`\>,
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

#### Returns[​](IYieldCurveChartApi.html#returns-3 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-3 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-3 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-3 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.removeSeries`

#### Example[​](IYieldCurveChartApi.html#example "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
chart.removeSeries(series);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### subscribeClick()[​](IYieldCurveChartApi.html#subscribeclick "Direct link to subscribeClick()"){.hash-link aria-label="Direct link to subscribeClick()"} {#subscribeclick .anchor .anchorWithStickyNavbar_LWe7}

> **subscribeClick**(`handler`): `void`

Subscribe to the chart click event.

#### Parameters[​](IYieldCurveChartApi.html#parameters-3 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-3 .anchor .anchorWithStickyNavbar_LWe7}

• **handler**:
[`MouseEventHandler`](../type-aliases/MouseEventHandler.html)\<`number`\>

Handler to be called on mouse click.

#### Returns[​](IYieldCurveChartApi.html#returns-4 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-4 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-4 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-4 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.subscribeClick`

#### Example[​](IYieldCurveChartApi.html#example-1 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-1 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
function myClickHandler(param) {
    if (!param.point) {
        return;
    }

    console.log(`Click at ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);
}

chart.subscribeClick(myClickHandler);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### unsubscribeClick()[​](IYieldCurveChartApi.html#unsubscribeclick "Direct link to unsubscribeClick()"){.hash-link aria-label="Direct link to unsubscribeClick()"} {#unsubscribeclick .anchor .anchorWithStickyNavbar_LWe7}

> **unsubscribeClick**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using
[subscribeClick](IChartApiBase.html#subscribeclick).

#### Parameters[​](IYieldCurveChartApi.html#parameters-4 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-4 .anchor .anchorWithStickyNavbar_LWe7}

• **handler**:
[`MouseEventHandler`](../type-aliases/MouseEventHandler.html)\<`number`\>

Previously subscribed handler

#### Returns[​](IYieldCurveChartApi.html#returns-5 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-5 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-5 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-5 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.unsubscribeClick`

#### Example[​](IYieldCurveChartApi.html#example-2 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-2 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
chart.unsubscribeClick(myClickHandler);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### subscribeDblClick()[​](IYieldCurveChartApi.html#subscribedblclick "Direct link to subscribeDblClick()"){.hash-link aria-label="Direct link to subscribeDblClick()"} {#subscribedblclick .anchor .anchorWithStickyNavbar_LWe7}

> **subscribeDblClick**(`handler`): `void`

Subscribe to the chart double-click event.

#### Parameters[​](IYieldCurveChartApi.html#parameters-5 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-5 .anchor .anchorWithStickyNavbar_LWe7}

• **handler**:
[`MouseEventHandler`](../type-aliases/MouseEventHandler.html)\<`number`\>

Handler to be called on mouse double-click.

#### Returns[​](IYieldCurveChartApi.html#returns-6 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-6 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-6 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-6 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.subscribeDblClick`

#### Example[​](IYieldCurveChartApi.html#example-3 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-3 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
function myDblClickHandler(param) {
    if (!param.point) {
        return;
    }

    console.log(`Double Click at ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);
}

chart.subscribeDblClick(myDblClickHandler);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### unsubscribeDblClick()[​](IYieldCurveChartApi.html#unsubscribedblclick "Direct link to unsubscribeDblClick()"){.hash-link aria-label="Direct link to unsubscribeDblClick()"} {#unsubscribedblclick .anchor .anchorWithStickyNavbar_LWe7}

> **unsubscribeDblClick**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using
[subscribeDblClick](IChartApiBase.html#subscribedblclick).

#### Parameters[​](IYieldCurveChartApi.html#parameters-6 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-6 .anchor .anchorWithStickyNavbar_LWe7}

• **handler**:
[`MouseEventHandler`](../type-aliases/MouseEventHandler.html)\<`number`\>

Previously subscribed handler

#### Returns[​](IYieldCurveChartApi.html#returns-7 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-7 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-7 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-7 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.unsubscribeDblClick`

#### Example[​](IYieldCurveChartApi.html#example-4 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-4 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
chart.unsubscribeDblClick(myDblClickHandler);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### subscribeCrosshairMove()[​](IYieldCurveChartApi.html#subscribecrosshairmove "Direct link to subscribeCrosshairMove()"){.hash-link aria-label="Direct link to subscribeCrosshairMove()"} {#subscribecrosshairmove .anchor .anchorWithStickyNavbar_LWe7}

> **subscribeCrosshairMove**(`handler`): `void`

Subscribe to the crosshair move event.

#### Parameters[​](IYieldCurveChartApi.html#parameters-7 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-7 .anchor .anchorWithStickyNavbar_LWe7}

• **handler**:
[`MouseEventHandler`](../type-aliases/MouseEventHandler.html)\<`number`\>

Handler to be called on crosshair move.

#### Returns[​](IYieldCurveChartApi.html#returns-8 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-8 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-8 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-8 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.subscribeCrosshairMove`

#### Example[​](IYieldCurveChartApi.html#example-5 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-5 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
function myCrosshairMoveHandler(param) {
    if (!param.point) {
        return;
    }

    console.log(`Crosshair moved to ${param.point.x}, ${param.point.y}. The time is ${param.time}.`);
}

chart.subscribeCrosshairMove(myCrosshairMoveHandler);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### unsubscribeCrosshairMove()[​](IYieldCurveChartApi.html#unsubscribecrosshairmove "Direct link to unsubscribeCrosshairMove()"){.hash-link aria-label="Direct link to unsubscribeCrosshairMove()"} {#unsubscribecrosshairmove .anchor .anchorWithStickyNavbar_LWe7}

> **unsubscribeCrosshairMove**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using
[subscribeCrosshairMove](IChartApiBase.html#subscribecrosshairmove).

#### Parameters[​](IYieldCurveChartApi.html#parameters-8 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-8 .anchor .anchorWithStickyNavbar_LWe7}

• **handler**:
[`MouseEventHandler`](../type-aliases/MouseEventHandler.html)\<`number`\>

Previously subscribed handler

#### Returns[​](IYieldCurveChartApi.html#returns-9 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-9 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-9 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-9 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.unsubscribeCrosshairMove`

#### Example[​](IYieldCurveChartApi.html#example-6 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-6 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
chart.unsubscribeCrosshairMove(myCrosshairMoveHandler);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### priceScale()[​](IYieldCurveChartApi.html#pricescale "Direct link to priceScale()"){.hash-link aria-label="Direct link to priceScale()"} {#pricescale .anchor .anchorWithStickyNavbar_LWe7}

> **priceScale**(`priceScaleId`, `paneIndex`?):
> [`IPriceScaleApi`](IPriceScaleApi.html)

Returns API to manipulate a price scale.

#### Parameters[​](IYieldCurveChartApi.html#parameters-9 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-9 .anchor .anchorWithStickyNavbar_LWe7}

• **priceScaleId**: `string`

ID of the price scale.

• **paneIndex?**: `number`

Index of the pane (default: 0)

#### Returns[​](IYieldCurveChartApi.html#returns-10 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-10 .anchor .anchorWithStickyNavbar_LWe7}

[`IPriceScaleApi`](IPriceScaleApi.html)

Price scale API.

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-10 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-10 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.priceScale`

------------------------------------------------------------------------

### timeScale()[​](IYieldCurveChartApi.html#timescale "Direct link to timeScale()"){.hash-link aria-label="Direct link to timeScale()"} {#timescale .anchor .anchorWithStickyNavbar_LWe7}

> **timeScale**(): [`ITimeScaleApi`](ITimeScaleApi.html)\<`number`\>

Returns API to manipulate the time scale

#### Returns[​](IYieldCurveChartApi.html#returns-11 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-11 .anchor .anchorWithStickyNavbar_LWe7}

[`ITimeScaleApi`](ITimeScaleApi.html)\<`number`\>

Target API

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-11 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-11 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.timeScale`

------------------------------------------------------------------------

### applyOptions()[​](IYieldCurveChartApi.html#applyoptions "Direct link to applyOptions()"){.hash-link aria-label="Direct link to applyOptions()"} {#applyoptions .anchor .anchorWithStickyNavbar_LWe7}

> **applyOptions**(`options`): `void`

Applies new options to the chart

#### Parameters[​](IYieldCurveChartApi.html#parameters-10 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-10 .anchor .anchorWithStickyNavbar_LWe7}

• **options**: [`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`ChartOptionsImpl`](ChartOptionsImpl.html)\<`number`\>\>

Any subset of options.

#### Returns[​](IYieldCurveChartApi.html#returns-12 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-12 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-12 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-12 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.applyOptions`

------------------------------------------------------------------------

### options()[​](IYieldCurveChartApi.html#options "Direct link to options()"){.hash-link aria-label="Direct link to options()"} {#options .anchor .anchorWithStickyNavbar_LWe7}

> **options**(): `Readonly`
> \<[`ChartOptionsImpl`](ChartOptionsImpl.html)\<`number`\>\>

Returns currently applied options

#### Returns[​](IYieldCurveChartApi.html#returns-13 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-13 .anchor .anchorWithStickyNavbar_LWe7}

`Readonly` \<[`ChartOptionsImpl`](ChartOptionsImpl.html)\<`number`\>\>

Full set of currently applied options, including defaults

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-13 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-13 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.options`

------------------------------------------------------------------------

### takeScreenshot()[​](IYieldCurveChartApi.html#takescreenshot "Direct link to takeScreenshot()"){.hash-link aria-label="Direct link to takeScreenshot()"} {#takescreenshot .anchor .anchorWithStickyNavbar_LWe7}

> **takeScreenshot**(`addTopLayer`?, `includeCrosshair`?):
> `HTMLCanvasElement`

Make a screenshot of the chart with all the elements excluding
crosshair.

#### Parameters[​](IYieldCurveChartApi.html#parameters-11 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-11 .anchor .anchorWithStickyNavbar_LWe7}

• **addTopLayer?**: `boolean`

if true, the top layer and primitives will be included in the screenshot
(default: false)

• **includeCrosshair?**: `boolean`

works only if addTopLayer is enabled. If true, the crosshair will be
included in the screenshot (default: false)

#### Returns[​](IYieldCurveChartApi.html#returns-14 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-14 .anchor .anchorWithStickyNavbar_LWe7}

`HTMLCanvasElement`

A canvas with the chart drawn on. Any `Canvas` methods like
`toDataURL()` or `toBlob()` can be used to serialize the result.

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-14 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-14 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.takeScreenshot`

------------------------------------------------------------------------

### addPane()[​](IYieldCurveChartApi.html#addpane "Direct link to addPane()"){.hash-link aria-label="Direct link to addPane()"} {#addpane .anchor .anchorWithStickyNavbar_LWe7}

> **addPane**(`preserveEmptyPane`?):
> [`IPaneApi`](IPaneApi.html)\<`number`\>

Add a pane to the chart

#### Parameters[​](IYieldCurveChartApi.html#parameters-12 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-12 .anchor .anchorWithStickyNavbar_LWe7}

• **preserveEmptyPane?**: `boolean`

Whether to preserve the empty pane

#### Returns[​](IYieldCurveChartApi.html#returns-15 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-15 .anchor .anchorWithStickyNavbar_LWe7}

[`IPaneApi`](IPaneApi.html)\<`number`\>

The pane API

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-15 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-15 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.addPane`

------------------------------------------------------------------------

### panes()[​](IYieldCurveChartApi.html#panes "Direct link to panes()"){.hash-link aria-label="Direct link to panes()"} {#panes .anchor .anchorWithStickyNavbar_LWe7}

> **panes**(): [`IPaneApi`](IPaneApi.html)\<`number`\>\[\]

Returns array of panes\' API

#### Returns[​](IYieldCurveChartApi.html#returns-16 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-16 .anchor .anchorWithStickyNavbar_LWe7}

[`IPaneApi`](IPaneApi.html)\<`number`\>\[\]

array of pane\'s Api

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-16 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-16 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.panes`

------------------------------------------------------------------------

### removePane()[​](IYieldCurveChartApi.html#removepane "Direct link to removePane()"){.hash-link aria-label="Direct link to removePane()"} {#removepane .anchor .anchorWithStickyNavbar_LWe7}

> **removePane**(`index`): `void`

Removes a pane with index

#### Parameters[​](IYieldCurveChartApi.html#parameters-13 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-13 .anchor .anchorWithStickyNavbar_LWe7}

• **index**: `number`

the pane to be removed

#### Returns[​](IYieldCurveChartApi.html#returns-17 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-17 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-17 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-17 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.removePane`

------------------------------------------------------------------------

### swapPanes()[​](IYieldCurveChartApi.html#swappanes "Direct link to swapPanes()"){.hash-link aria-label="Direct link to swapPanes()"} {#swappanes .anchor .anchorWithStickyNavbar_LWe7}

> **swapPanes**(`first`, `second`): `void`

swap the position of two panes.

#### Parameters[​](IYieldCurveChartApi.html#parameters-14 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-14 .anchor .anchorWithStickyNavbar_LWe7}

• **first**: `number`

the first index

• **second**: `number`

the second index

#### Returns[​](IYieldCurveChartApi.html#returns-18 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-18 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-18 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-18 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.swapPanes`

------------------------------------------------------------------------

### autoSizeActive()[​](IYieldCurveChartApi.html#autosizeactive "Direct link to autoSizeActive()"){.hash-link aria-label="Direct link to autoSizeActive()"} {#autosizeactive .anchor .anchorWithStickyNavbar_LWe7}

> **autoSizeActive**(): `boolean`

Returns the active state of the `autoSize` option. This can be used to
check whether the chart is handling resizing automatically with a
`ResizeObserver`.

#### Returns[​](IYieldCurveChartApi.html#returns-19 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-19 .anchor .anchorWithStickyNavbar_LWe7}

`boolean`

Whether the `autoSize` option is enabled and the active.

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-19 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-19 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.autoSizeActive`

------------------------------------------------------------------------

### chartElement()[​](IYieldCurveChartApi.html#chartelement "Direct link to chartElement()"){.hash-link aria-label="Direct link to chartElement()"} {#chartelement .anchor .anchorWithStickyNavbar_LWe7}

> **chartElement**(): `HTMLDivElement`

Returns the generated div element containing the chart. This can be used
for adding your own additional event listeners, or for measuring the
elements dimensions and position within the document.

#### Returns[​](IYieldCurveChartApi.html#returns-20 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-20 .anchor .anchorWithStickyNavbar_LWe7}

`HTMLDivElement`

generated div element containing the chart.

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-20 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-20 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.chartElement`

------------------------------------------------------------------------

### setCrosshairPosition()[​](IYieldCurveChartApi.html#setcrosshairposition "Direct link to setCrosshairPosition()"){.hash-link aria-label="Direct link to setCrosshairPosition()"} {#setcrosshairposition .anchor .anchorWithStickyNavbar_LWe7}

> **setCrosshairPosition**(`price`, `horizontalPosition`, `seriesApi`):
> `void`

Set the crosshair position within the chart.

Usually the crosshair position is set automatically by the user\'s
actions. However in some cases you may want to set it explicitly.

For example if you want to synchronise the crosshairs of two separate
charts.

#### Parameters[​](IYieldCurveChartApi.html#parameters-15 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-15 .anchor .anchorWithStickyNavbar_LWe7}

• **price**: `number`

The price (vertical coordinate) of the new crosshair position.

• **horizontalPosition**: `number`

The horizontal coordinate (time by default) of the new crosshair
position.

• **seriesApi**: [`ISeriesApi`](ISeriesApi.html)\<keyof
[`SeriesOptionsMap`](SeriesOptionsMap.html), `number`,
[`WhitespaceData`](WhitespaceData.html)\<`number`\> \|
[`LineData`](LineData.html)\<`number`\> \|
[`CustomData`](CustomData.html)\<`number`\> \|
[`AreaData`](AreaData.html)\<`number`\> \|
[`BarData`](BarData.html)\<`number`\> \|
[`CandlestickData`](CandlestickData.html)\<`number`\> \|
[`BaselineData`](BaselineData.html)\<`number`\> \|
[`HistogramData`](HistogramData.html)\<`number`\> \|
[`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.html)\<`number`\>,
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

#### Returns[​](IYieldCurveChartApi.html#returns-21 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-21 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-21 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-21 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.setCrosshairPosition`

------------------------------------------------------------------------

### clearCrosshairPosition()[​](IYieldCurveChartApi.html#clearcrosshairposition "Direct link to clearCrosshairPosition()"){.hash-link aria-label="Direct link to clearCrosshairPosition()"} {#clearcrosshairposition .anchor .anchorWithStickyNavbar_LWe7}

> **clearCrosshairPosition**(): `void`

Clear the crosshair position within the chart.

#### Returns[​](IYieldCurveChartApi.html#returns-22 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-22 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-22 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-22 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.clearCrosshairPosition`

------------------------------------------------------------------------

### paneSize()[​](IYieldCurveChartApi.html#panesize "Direct link to paneSize()"){.hash-link aria-label="Direct link to paneSize()"} {#panesize .anchor .anchorWithStickyNavbar_LWe7}

> **paneSize**(`paneIndex`?): [`PaneSize`](PaneSize.html)

Returns the dimensions of the chart pane (the plot surface which
excludes time and price scales). This would typically only be useful for
plugin development.

#### Parameters[​](IYieldCurveChartApi.html#parameters-16 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-16 .anchor .anchorWithStickyNavbar_LWe7}

• **paneIndex?**: `number`

The index of the pane

#### Returns[​](IYieldCurveChartApi.html#returns-23 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-23 .anchor .anchorWithStickyNavbar_LWe7}

[`PaneSize`](PaneSize.html)

Dimensions of the chart pane

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-23 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-23 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.paneSize`

#### Default Value[​](IYieldCurveChartApi.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`0`

------------------------------------------------------------------------

### horzBehaviour()[​](IYieldCurveChartApi.html#horzbehaviour "Direct link to horzBehaviour()"){.hash-link aria-label="Direct link to horzBehaviour()"} {#horzbehaviour .anchor .anchorWithStickyNavbar_LWe7}

> **horzBehaviour**():
> [`IHorzScaleBehavior`](IHorzScaleBehavior.html)\<`number`\>

Returns the horizontal scale behaviour.

#### Returns[​](IYieldCurveChartApi.html#returns-24 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-24 .anchor .anchorWithStickyNavbar_LWe7}

[`IHorzScaleBehavior`](IHorzScaleBehavior.html)\<`number`\>

#### Inherited from[​](IYieldCurveChartApi.html#inherited-from-24 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-24 .anchor .anchorWithStickyNavbar_LWe7}

`Omit.horzBehaviour`

------------------------------------------------------------------------

### addSeries()[​](IYieldCurveChartApi.html#addseries "Direct link to addSeries()"){.hash-link aria-label="Direct link to addSeries()"} {#addseries .anchor .anchorWithStickyNavbar_LWe7}

> **addSeries**\<`T`\>(`definition`, `options`?, `paneIndex`?):
> [`ISeriesApi`](ISeriesApi.html)\<`T`, `number`,
> [`WhitespaceData`](WhitespaceData.html)\<`number`\> \|
> [`LineData`](LineData.html)\<`number`\>,
> [`SeriesOptionsMap`](SeriesOptionsMap.html)\[`T`\],
> [`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.html)\[`T`\]\>

Creates a series with specified parameters.

Note that the Yield Curve chart only supports the Area and Line series
types.

#### Type parameters[​](IYieldCurveChartApi.html#type-parameters-1 "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **T** *extends*
[`YieldCurveSeriesType`](../type-aliases/YieldCurveSeriesType.html)

#### Parameters[​](IYieldCurveChartApi.html#parameters-17 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-17 .anchor .anchorWithStickyNavbar_LWe7}

• **definition**: [`SeriesDefinition`](SeriesDefinition.html)\<`T`\>

A series definition for either AreaSeries or LineSeries.

• **options?**:
[`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.html)\[`T`\]

Customization parameters of the series being created.

• **paneIndex?**: `number`

An index of the pane where the series should be created.

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const series = chart.addSeries(LineSeries, { lineWidth: 2 });
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

#### Returns[​](IYieldCurveChartApi.html#returns-25 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-25 .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesApi`](ISeriesApi.html)\<`T`, `number`,
[`WhitespaceData`](WhitespaceData.html)\<`number`\> \|
[`LineData`](LineData.html)\<`number`\>,
[`SeriesOptionsMap`](SeriesOptionsMap.html)\[`T`\],
[`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.html)\[`T`\]\>

- [Extends](IYieldCurveChartApi.html#extends){.table-of-contents__link
  .toc-highlight}
- [Methods](IYieldCurveChartApi.html#methods){.table-of-contents__link
  .toc-highlight}
  - [remove()](IYieldCurveChartApi.html#remove){.table-of-contents__link
    .toc-highlight}
  - [resize()](IYieldCurveChartApi.html#resize){.table-of-contents__link
    .toc-highlight}
  - [addCustomSeries()](IYieldCurveChartApi.html#addcustomseries){.table-of-contents__link
    .toc-highlight}
  - [removeSeries()](IYieldCurveChartApi.html#removeseries){.table-of-contents__link
    .toc-highlight}
  - [subscribeClick()](IYieldCurveChartApi.html#subscribeclick){.table-of-contents__link
    .toc-highlight}
  - [unsubscribeClick()](IYieldCurveChartApi.html#unsubscribeclick){.table-of-contents__link
    .toc-highlight}
  - [subscribeDblClick()](IYieldCurveChartApi.html#subscribedblclick){.table-of-contents__link
    .toc-highlight}
  - [unsubscribeDblClick()](IYieldCurveChartApi.html#unsubscribedblclick){.table-of-contents__link
    .toc-highlight}
  - [subscribeCrosshairMove()](IYieldCurveChartApi.html#subscribecrosshairmove){.table-of-contents__link
    .toc-highlight}
  - [unsubscribeCrosshairMove()](IYieldCurveChartApi.html#unsubscribecrosshairmove){.table-of-contents__link
    .toc-highlight}
  - [priceScale()](IYieldCurveChartApi.html#pricescale){.table-of-contents__link
    .toc-highlight}
  - [timeScale()](IYieldCurveChartApi.html#timescale){.table-of-contents__link
    .toc-highlight}
  - [applyOptions()](IYieldCurveChartApi.html#applyoptions){.table-of-contents__link
    .toc-highlight}
  - [options()](IYieldCurveChartApi.html#options){.table-of-contents__link
    .toc-highlight}
  - [takeScreenshot()](IYieldCurveChartApi.html#takescreenshot){.table-of-contents__link
    .toc-highlight}
  - [addPane()](IYieldCurveChartApi.html#addpane){.table-of-contents__link
    .toc-highlight}
  - [panes()](IYieldCurveChartApi.html#panes){.table-of-contents__link
    .toc-highlight}
  - [removePane()](IYieldCurveChartApi.html#removepane){.table-of-contents__link
    .toc-highlight}
  - [swapPanes()](IYieldCurveChartApi.html#swappanes){.table-of-contents__link
    .toc-highlight}
  - [autoSizeActive()](IYieldCurveChartApi.html#autosizeactive){.table-of-contents__link
    .toc-highlight}
  - [chartElement()](IYieldCurveChartApi.html#chartelement){.table-of-contents__link
    .toc-highlight}
  - [setCrosshairPosition()](IYieldCurveChartApi.html#setcrosshairposition){.table-of-contents__link
    .toc-highlight}
  - [clearCrosshairPosition()](IYieldCurveChartApi.html#clearcrosshairposition){.table-of-contents__link
    .toc-highlight}
  - [paneSize()](IYieldCurveChartApi.html#panesize){.table-of-contents__link
    .toc-highlight}
  - [horzBehaviour()](IYieldCurveChartApi.html#horzbehaviour){.table-of-contents__link
    .toc-highlight}
  - [addSeries()](IYieldCurveChartApi.html#addseries){.table-of-contents__link
    .toc-highlight}
