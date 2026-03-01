- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [IPaneApi]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: IPaneApi\<HorzScaleItem\>

Represents the interface for interacting with a pane in a lightweight
chart.

## Type parameters[​](IPaneApi.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem**

## Methods[​](IPaneApi.html#methods "Direct link to Methods"){.hash-link aria-label="Direct link to Methods"} {#methods .anchor .anchorWithStickyNavbar_LWe7}

### getHeight()[​](IPaneApi.html#getheight "Direct link to getHeight()"){.hash-link aria-label="Direct link to getHeight()"} {#getheight .anchor .anchorWithStickyNavbar_LWe7}

> **getHeight**(): `number`

Retrieves the height of the pane in pixels.

#### Returns[​](IPaneApi.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`number`

The height of the pane in pixels.

------------------------------------------------------------------------

### setHeight()[​](IPaneApi.html#setheight "Direct link to setHeight()"){.hash-link aria-label="Direct link to setHeight()"} {#setheight .anchor .anchorWithStickyNavbar_LWe7}

> **setHeight**(`height`): `void`

Sets the height of the pane.

#### Parameters[​](IPaneApi.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **height**: `number`

The number of pixels to set as the height of the pane.

#### Returns[​](IPaneApi.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### moveTo()[​](IPaneApi.html#moveto "Direct link to moveTo()"){.hash-link aria-label="Direct link to moveTo()"} {#moveto .anchor .anchorWithStickyNavbar_LWe7}

> **moveTo**(`paneIndex`): `void`

Moves the pane to a new position.

#### Parameters[​](IPaneApi.html#parameters-1 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **paneIndex**: `number`

The target index of the pane. Should be a number between 0 and the total
number of panes - 1.

#### Returns[​](IPaneApi.html#returns-2 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-2 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### paneIndex()[​](IPaneApi.html#paneindex "Direct link to paneIndex()"){.hash-link aria-label="Direct link to paneIndex()"} {#paneindex .anchor .anchorWithStickyNavbar_LWe7}

> **paneIndex**(): `number`

Retrieves the index of the pane.

#### Returns[​](IPaneApi.html#returns-3 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-3 .anchor .anchorWithStickyNavbar_LWe7}

`number`

The index of the pane. It is a number between 0 and the total number of
panes - 1.

------------------------------------------------------------------------

### getSeries()[​](IPaneApi.html#getseries "Direct link to getSeries()"){.hash-link aria-label="Direct link to getSeries()"} {#getseries .anchor .anchorWithStickyNavbar_LWe7}

> **getSeries**(): [`ISeriesApi`](ISeriesApi.html)\<keyof
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
> [`SeriesOptionsCommon`](SeriesOptionsCommon.html)\>\>\[\]

Retrieves the array of series for the current pane.

#### Returns[​](IPaneApi.html#returns-4 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-4 .anchor .anchorWithStickyNavbar_LWe7}

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
[`SeriesOptionsCommon`](SeriesOptionsCommon.html)\>\>\[\]

An array of series.

------------------------------------------------------------------------

### getHTMLElement()[​](IPaneApi.html#gethtmlelement "Direct link to getHTMLElement()"){.hash-link aria-label="Direct link to getHTMLElement()"} {#gethtmlelement .anchor .anchorWithStickyNavbar_LWe7}

> **getHTMLElement**(): `HTMLElement`

Retrieves the HTML element of the pane.

#### Returns[​](IPaneApi.html#returns-5 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-5 .anchor .anchorWithStickyNavbar_LWe7}

`HTMLElement`

The HTML element of the pane or null if pane wasn\'t created yet.

------------------------------------------------------------------------

### attachPrimitive()[​](IPaneApi.html#attachprimitive "Direct link to attachPrimitive()"){.hash-link aria-label="Direct link to attachPrimitive()"} {#attachprimitive .anchor .anchorWithStickyNavbar_LWe7}

> **attachPrimitive**(`primitive`): `void`

Attaches additional drawing primitive to the pane

#### Parameters[​](IPaneApi.html#parameters-2 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-2 .anchor .anchorWithStickyNavbar_LWe7}

• **primitive**:
[`IPanePrimitive`](../type-aliases/IPanePrimitive.html)\<`HorzScaleItem`\>

any implementation of IPanePrimitive interface

#### Returns[​](IPaneApi.html#returns-6 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-6 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### detachPrimitive()[​](IPaneApi.html#detachprimitive "Direct link to detachPrimitive()"){.hash-link aria-label="Direct link to detachPrimitive()"} {#detachprimitive .anchor .anchorWithStickyNavbar_LWe7}

> **detachPrimitive**(`primitive`): `void`

Detaches additional drawing primitive from the pane

#### Parameters[​](IPaneApi.html#parameters-3 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-3 .anchor .anchorWithStickyNavbar_LWe7}

• **primitive**:
[`IPanePrimitive`](../type-aliases/IPanePrimitive.html)\<`HorzScaleItem`\>

implementation of IPanePrimitive interface attached before Does nothing
if specified primitive was not attached

#### Returns[​](IPaneApi.html#returns-7 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-7 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### priceScale()[​](IPaneApi.html#pricescale "Direct link to priceScale()"){.hash-link aria-label="Direct link to priceScale()"} {#pricescale .anchor .anchorWithStickyNavbar_LWe7}

> **priceScale**(`priceScaleId`):
> [`IPriceScaleApi`](IPriceScaleApi.html)

Returns the price scale with the given id.

#### Parameters[​](IPaneApi.html#parameters-4 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-4 .anchor .anchorWithStickyNavbar_LWe7}

• **priceScaleId**: `string`

ID of the price scale to find

#### Returns[​](IPaneApi.html#returns-8 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-8 .anchor .anchorWithStickyNavbar_LWe7}

[`IPriceScaleApi`](IPriceScaleApi.html)

#### Throws[​](IPaneApi.html#throws "Direct link to Throws"){.hash-link aria-label="Direct link to Throws"} {#throws .anchor .anchorWithStickyNavbar_LWe7}

If the price scale with the given id is not found in this pane

------------------------------------------------------------------------

### setPreserveEmptyPane()[​](IPaneApi.html#setpreserveemptypane "Direct link to setPreserveEmptyPane()"){.hash-link aria-label="Direct link to setPreserveEmptyPane()"} {#setpreserveemptypane .anchor .anchorWithStickyNavbar_LWe7}

> **setPreserveEmptyPane**(`preserve`): `void`

Sets whether to preserve the empty pane

#### Parameters[​](IPaneApi.html#parameters-5 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-5 .anchor .anchorWithStickyNavbar_LWe7}

• **preserve**: `boolean`

Whether to preserve the empty pane

#### Returns[​](IPaneApi.html#returns-9 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-9 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### preserveEmptyPane()[​](IPaneApi.html#preserveemptypane "Direct link to preserveEmptyPane()"){.hash-link aria-label="Direct link to preserveEmptyPane()"} {#preserveemptypane .anchor .anchorWithStickyNavbar_LWe7}

> **preserveEmptyPane**(): `boolean`

Returns whether to preserve the empty pane

#### Returns[​](IPaneApi.html#returns-10 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-10 .anchor .anchorWithStickyNavbar_LWe7}

`boolean`

Whether to preserve the empty pane

------------------------------------------------------------------------

### getStretchFactor()[​](IPaneApi.html#getstretchfactor "Direct link to getStretchFactor()"){.hash-link aria-label="Direct link to getStretchFactor()"} {#getstretchfactor .anchor .anchorWithStickyNavbar_LWe7}

> **getStretchFactor**(): `number`

Returns the stretch factor of the pane. Stretch factor determines the
relative size of the pane compared to other panes.

#### Returns[​](IPaneApi.html#returns-11 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-11 .anchor .anchorWithStickyNavbar_LWe7}

`number`

The stretch factor of the pane. Default is 1

------------------------------------------------------------------------

### setStretchFactor()[​](IPaneApi.html#setstretchfactor "Direct link to setStretchFactor()"){.hash-link aria-label="Direct link to setStretchFactor()"} {#setstretchfactor .anchor .anchorWithStickyNavbar_LWe7}

> **setStretchFactor**(`stretchFactor`): `void`

Sets the stretch factor of the pane. When you creating a pane, the
stretch factor is 1 by default. So if you have three panes, and you want
to make the first pane twice as big as the second and third panes, you
can set the stretch factor of the first pane to 2000. Example:

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const pane1 = chart.addPane();
const pane2 = chart.addPane();
const pane3 = chart.addPane();
pane1.setStretchFactor(0.2);
pane2.setStretchFactor(0.3);
pane3.setStretchFactor(0.5);
// Now the first pane will be 20% of the total height, the second pane will be 30% of the total height, and the third pane will be 50% of the total height.
// Note: if you have one pane with default stretch factor of 1 and set other pane's stretch factor to 50,
// library will try to make second pane 50 times smaller than the first pane
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

#### Parameters[​](IPaneApi.html#parameters-6 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-6 .anchor .anchorWithStickyNavbar_LWe7}

• **stretchFactor**: `number`

The stretch factor of the pane.

#### Returns[​](IPaneApi.html#returns-12 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-12 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### addCustomSeries()[​](IPaneApi.html#addcustomseries "Direct link to addCustomSeries()"){.hash-link aria-label="Direct link to addCustomSeries()"} {#addcustomseries .anchor .anchorWithStickyNavbar_LWe7}

> **addCustomSeries**\<`TData`, `TOptions`,
> `TPartialOptions`\>(`customPaneView`, `customOptions`?):
> [`ISeriesApi`](ISeriesApi.html)\<`"Custom"`, `HorzScaleItem`,
> [`WhitespaceData`](WhitespaceData.html)\<`HorzScaleItem`\> \| `TData`,
> `TOptions`, `TPartialOptions`\>

Creates a custom series with specified parameters.

A custom series is a generic series which can be extended with a custom
renderer to implement chart types which the library doesn\'t support by
default.

#### Type parameters[​](IPaneApi.html#type-parameters-1 "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **TData** *extends* [`CustomData`](CustomData.html)\<`HorzScaleItem`\>

• **TOptions** *extends*
[`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.html)

• **TPartialOptions** *extends*
[`DeepPartial`](../type-aliases/DeepPartial.html)\<`TOptions` &
[`SeriesOptionsCommon`](SeriesOptionsCommon.html)\> =
[`DeepPartial`](../type-aliases/DeepPartial.html)\<`TOptions` &
[`SeriesOptionsCommon`](SeriesOptionsCommon.html)\>

#### Parameters[​](IPaneApi.html#parameters-7 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-7 .anchor .anchorWithStickyNavbar_LWe7}

• **customPaneView**:
[`ICustomSeriesPaneView`](ICustomSeriesPaneView.html)\<`HorzScaleItem`,
`TData`, `TOptions`\>

A custom series pane view which implements the custom renderer.

• **customOptions?**:
[`DeepPartial`](../type-aliases/DeepPartial.html)\<`TOptions` &
[`SeriesOptionsCommon`](SeriesOptionsCommon.html)\>

Customization parameters of the series being created.

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const series = pane.addCustomSeries(myCustomPaneView);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

#### Returns[​](IPaneApi.html#returns-13 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-13 .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesApi`](ISeriesApi.html)\<`"Custom"`, `HorzScaleItem`,
[`WhitespaceData`](WhitespaceData.html)\<`HorzScaleItem`\> \| `TData`,
`TOptions`, `TPartialOptions`\>

------------------------------------------------------------------------

### addSeries()[​](IPaneApi.html#addseries "Direct link to addSeries()"){.hash-link aria-label="Direct link to addSeries()"} {#addseries .anchor .anchorWithStickyNavbar_LWe7}

> **addSeries**\<`T`\>(`definition`, `options`?):
> [`ISeriesApi`](ISeriesApi.html)\<`T`, `HorzScaleItem`,
> [`SeriesDataItemTypeMap`](SeriesDataItemTypeMap.html)\<`HorzScaleItem`\>\[`T`\],
> [`SeriesOptionsMap`](SeriesOptionsMap.html)\[`T`\],
> [`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.html)\[`T`\]\>

Creates a series with specified parameters.

#### Type parameters[​](IPaneApi.html#type-parameters-2 "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters-2 .anchor .anchorWithStickyNavbar_LWe7}

• **T** *extends* keyof [`SeriesOptionsMap`](SeriesOptionsMap.html)

#### Parameters[​](IPaneApi.html#parameters-8 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-8 .anchor .anchorWithStickyNavbar_LWe7}

• **definition**: [`SeriesDefinition`](SeriesDefinition.html)\<`T`\>

A series definition.

• **options?**:
[`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.html)\[`T`\]

Customization parameters of the series being created.

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const series = pane.addSeries(LineSeries, { lineWidth: 2 });
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

#### Returns[​](IPaneApi.html#returns-14 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-14 .anchor .anchorWithStickyNavbar_LWe7}

[`ISeriesApi`](ISeriesApi.html)\<`T`, `HorzScaleItem`,
[`SeriesDataItemTypeMap`](SeriesDataItemTypeMap.html)\<`HorzScaleItem`\>\[`T`\],
[`SeriesOptionsMap`](SeriesOptionsMap.html)\[`T`\],
[`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.html)\[`T`\]\>

- [Type
  parameters](IPaneApi.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Methods](IPaneApi.html#methods){.table-of-contents__link
  .toc-highlight}
  - [getHeight()](IPaneApi.html#getheight){.table-of-contents__link
    .toc-highlight}
  - [setHeight()](IPaneApi.html#setheight){.table-of-contents__link
    .toc-highlight}
  - [moveTo()](IPaneApi.html#moveto){.table-of-contents__link
    .toc-highlight}
  - [paneIndex()](IPaneApi.html#paneindex){.table-of-contents__link
    .toc-highlight}
  - [getSeries()](IPaneApi.html#getseries){.table-of-contents__link
    .toc-highlight}
  - [getHTMLElement()](IPaneApi.html#gethtmlelement){.table-of-contents__link
    .toc-highlight}
  - [attachPrimitive()](IPaneApi.html#attachprimitive){.table-of-contents__link
    .toc-highlight}
  - [detachPrimitive()](IPaneApi.html#detachprimitive){.table-of-contents__link
    .toc-highlight}
  - [priceScale()](IPaneApi.html#pricescale){.table-of-contents__link
    .toc-highlight}
  - [setPreserveEmptyPane()](IPaneApi.html#setpreserveemptypane){.table-of-contents__link
    .toc-highlight}
  - [preserveEmptyPane()](IPaneApi.html#preserveemptypane){.table-of-contents__link
    .toc-highlight}
  - [getStretchFactor()](IPaneApi.html#getstretchfactor){.table-of-contents__link
    .toc-highlight}
  - [setStretchFactor()](IPaneApi.html#setstretchfactor){.table-of-contents__link
    .toc-highlight}
  - [addCustomSeries()](IPaneApi.html#addcustomseries){.table-of-contents__link
    .toc-highlight}
  - [addSeries()](IPaneApi.html#addseries){.table-of-contents__link
    .toc-highlight}
