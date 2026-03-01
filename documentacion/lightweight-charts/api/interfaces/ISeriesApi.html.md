- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [ISeriesApi]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: ISeriesApi\<TSeriesType, HorzScaleItem, TData, TOptions, TPartialOptions\>

Represents the interface for interacting with series.

## Type parameters[​](ISeriesApi.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **TSeriesType** *extends*
[`SeriesType`](../type-aliases/SeriesType.html)

• **HorzScaleItem** = [`Time`](../type-aliases/Time.html)

• **TData** =
[`SeriesDataItemTypeMap`](SeriesDataItemTypeMap.html)\<`HorzScaleItem`\>\[`TSeriesType`\]

• **TOptions** =
[`SeriesOptionsMap`](SeriesOptionsMap.html)\[`TSeriesType`\]

• **TPartialOptions** =
[`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.html)\[`TSeriesType`\]

## Methods[​](ISeriesApi.html#methods "Direct link to Methods"){.hash-link aria-label="Direct link to Methods"} {#methods .anchor .anchorWithStickyNavbar_LWe7}

### priceFormatter()[​](ISeriesApi.html#priceformatter "Direct link to priceFormatter()"){.hash-link aria-label="Direct link to priceFormatter()"} {#priceformatter .anchor .anchorWithStickyNavbar_LWe7}

> **priceFormatter**(): [`IPriceFormatter`](IPriceFormatter.html)

Returns current price formatter

#### Returns[​](ISeriesApi.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

[`IPriceFormatter`](IPriceFormatter.html)

Interface to the price formatter object that can be used to format
prices in the same way as the chart does

------------------------------------------------------------------------

### priceToCoordinate()[​](ISeriesApi.html#pricetocoordinate "Direct link to priceToCoordinate()"){.hash-link aria-label="Direct link to priceToCoordinate()"} {#pricetocoordinate .anchor .anchorWithStickyNavbar_LWe7}

> **priceToCoordinate**(`price`):
> [`Coordinate`](../type-aliases/Coordinate.html)

Converts specified series price to pixel coordinate according to the
series price scale

#### Parameters[​](ISeriesApi.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **price**: `number`

Input price to be converted

#### Returns[​](ISeriesApi.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

[`Coordinate`](../type-aliases/Coordinate.html)

Pixel coordinate of the price level on the chart

------------------------------------------------------------------------

### coordinateToPrice()[​](ISeriesApi.html#coordinatetoprice "Direct link to coordinateToPrice()"){.hash-link aria-label="Direct link to coordinateToPrice()"} {#coordinatetoprice .anchor .anchorWithStickyNavbar_LWe7}

> **coordinateToPrice**(`coordinate`):
> [`BarPrice`](../type-aliases/BarPrice.html)

Converts specified coordinate to price value according to the series
price scale

#### Parameters[​](ISeriesApi.html#parameters-1 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **coordinate**: `number`

Input coordinate to be converted

#### Returns[​](ISeriesApi.html#returns-2 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-2 .anchor .anchorWithStickyNavbar_LWe7}

[`BarPrice`](../type-aliases/BarPrice.html)

Price value of the coordinate on the chart

------------------------------------------------------------------------

### barsInLogicalRange()[​](ISeriesApi.html#barsinlogicalrange "Direct link to barsInLogicalRange()"){.hash-link aria-label="Direct link to barsInLogicalRange()"} {#barsinlogicalrange .anchor .anchorWithStickyNavbar_LWe7}

> **barsInLogicalRange**(`range`):
> [`BarsInfo`](BarsInfo.html)\<`HorzScaleItem`\>

Returns bars information for the series in the provided [logical
range](../../time-scale.html#logical-range) or `null`, if no series data
has been found in the requested range. This method can be used, for
instance, to implement downloading historical data while scrolling to
prevent a user from seeing empty space.

#### Parameters[​](ISeriesApi.html#parameters-2 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-2 .anchor .anchorWithStickyNavbar_LWe7}

• **range**: [`IRange`](IRange.html)\<`number`\>

The [logical range](../../time-scale.html#logical-range) to retrieve
info for.

#### Returns[​](ISeriesApi.html#returns-3 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-3 .anchor .anchorWithStickyNavbar_LWe7}

[`BarsInfo`](BarsInfo.html)\<`HorzScaleItem`\>

The bars info for the given logical range.

#### Examples[​](ISeriesApi.html#examples "Direct link to Examples"){.hash-link aria-label="Direct link to Examples"} {#examples .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const barsInfo = series.barsInLogicalRange(chart.timeScale().getVisibleLogicalRange());
console.log(barsInfo);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
function onVisibleLogicalRangeChanged(newVisibleLogicalRange) {
    const barsInfo = series.barsInLogicalRange(newVisibleLogicalRange);
    // if there less than 50 bars to the left of the visible area
    if (barsInfo !== null && barsInfo.barsBefore < 50) {
        // try to load additional historical data and prepend it to the series data
    }
}

chart.timeScale().subscribeVisibleLogicalRangeChange(onVisibleLogicalRangeChanged);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### applyOptions()[​](ISeriesApi.html#applyoptions "Direct link to applyOptions()"){.hash-link aria-label="Direct link to applyOptions()"} {#applyoptions .anchor .anchorWithStickyNavbar_LWe7}

> **applyOptions**(`options`): `void`

Applies new options to the existing series You can set options initially
when you create series or use the `applyOptions` method of the series to
change the existing options. Note that you can only pass options you
want to change.

#### Parameters[​](ISeriesApi.html#parameters-3 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-3 .anchor .anchorWithStickyNavbar_LWe7}

• **options**: `TPartialOptions`

Any subset of options.

#### Returns[​](ISeriesApi.html#returns-4 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-4 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### options()[​](ISeriesApi.html#options "Direct link to options()"){.hash-link aria-label="Direct link to options()"} {#options .anchor .anchorWithStickyNavbar_LWe7}

> **options**(): `Readonly`\<`TOptions`\>

Returns currently applied options

#### Returns[​](ISeriesApi.html#returns-5 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-5 .anchor .anchorWithStickyNavbar_LWe7}

`Readonly`\<`TOptions`\>

Full set of currently applied options, including defaults

------------------------------------------------------------------------

### priceScale()[​](ISeriesApi.html#pricescale "Direct link to priceScale()"){.hash-link aria-label="Direct link to priceScale()"} {#pricescale .anchor .anchorWithStickyNavbar_LWe7}

> **priceScale**(): [`IPriceScaleApi`](IPriceScaleApi.html)

Returns the API interface for controlling the price scale that this
series is currently attached to.

#### Returns[​](ISeriesApi.html#returns-6 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-6 .anchor .anchorWithStickyNavbar_LWe7}

[`IPriceScaleApi`](IPriceScaleApi.html)

IPriceScaleApi An interface for controlling the price scale (axis
component) currently used by this series

#### Remarks[​](ISeriesApi.html#remarks "Direct link to Remarks"){.hash-link aria-label="Direct link to Remarks"} {#remarks .anchor .anchorWithStickyNavbar_LWe7}

scale (by ID and pane) that the series is using at the time this method
is called. If you later move the series to a different pane or attach it
to a different price scale (e.g., from \'right\' to \'left\'), the
previously returned PriceScaleApi will NOT follow the series. It will
continue to control the original price scale it was created for.

To control the new price scale after moving a series, you must call this
method again to get a fresh PriceScaleApi instance for the current price
scale.

------------------------------------------------------------------------

### setData()[​](ISeriesApi.html#setdata "Direct link to setData()"){.hash-link aria-label="Direct link to setData()"} {#setdata .anchor .anchorWithStickyNavbar_LWe7}

> **setData**(`data`): `void`

Sets or replaces series data.

#### Parameters[​](ISeriesApi.html#parameters-4 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-4 .anchor .anchorWithStickyNavbar_LWe7}

• **data**: `TData`\[\]

Ordered (earlier time point goes first) array of data items. Old data is
fully replaced with the new one.

#### Returns[​](ISeriesApi.html#returns-7 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-7 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Examples[​](ISeriesApi.html#examples-1 "Direct link to Examples"){.hash-link aria-label="Direct link to Examples"} {#examples-1 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
lineSeries.setData([
    { time: '2018-12-12', value: 24.11 },
    { time: '2018-12-13', value: 31.74 },
]);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
barSeries.setData([
    { time: '2018-12-19', open: 141.77, high: 170.39, low: 120.25, close: 145.72 },
    { time: '2018-12-20', open: 145.72, high: 147.99, low: 100.11, close: 108.19 },
]);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### update()[​](ISeriesApi.html#update "Direct link to update()"){.hash-link aria-label="Direct link to update()"} {#update .anchor .anchorWithStickyNavbar_LWe7}

> **update**(`bar`, `historicalUpdate`?): `void`

Adds new data item to the existing set (or updates the latest item if
times of the passed/latest items are equal).

#### Parameters[​](ISeriesApi.html#parameters-5 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-5 .anchor .anchorWithStickyNavbar_LWe7}

• **bar**: `TData`

A single data item to be added. Time of the new item must be greater or
equal to the latest existing time point. If the new item\'s time is
equal to the last existing item\'s time, then the existing item is
replaced with the new one.

• **historicalUpdate?**: `boolean`

If true, allows updating an existing data point that is not the latest
bar. Default is false. Updating older data using `historicalUpdate` will
be slower than updating the most recent data point.

#### Returns[​](ISeriesApi.html#returns-8 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-8 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Examples[​](ISeriesApi.html#examples-2 "Direct link to Examples"){.hash-link aria-label="Direct link to Examples"} {#examples-2 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
lineSeries.update({
    time: '2018-12-12',
    value: 24.11,
});
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
barSeries.update({
    time: '2018-12-19',
    open: 141.77,
    high: 170.39,
    low: 120.25,
    close: 145.72,
});
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### pop()[​](ISeriesApi.html#pop "Direct link to pop()"){.hash-link aria-label="Direct link to pop()"} {#pop .anchor .anchorWithStickyNavbar_LWe7}

> **pop**(`count`): `TData`\[\]

Removes one or more data items from the end of the series.

#### Parameters[​](ISeriesApi.html#parameters-6 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-6 .anchor .anchorWithStickyNavbar_LWe7}

• **count**: `number`

The number of data items to remove.

#### Returns[​](ISeriesApi.html#returns-9 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-9 .anchor .anchorWithStickyNavbar_LWe7}

`TData`\[\]

The removed data items.

#### Example[​](ISeriesApi.html#example "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const removedData = lineSeries.pop(1);
console.log(removedData);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### dataByIndex()[​](ISeriesApi.html#databyindex "Direct link to dataByIndex()"){.hash-link aria-label="Direct link to dataByIndex()"} {#databyindex .anchor .anchorWithStickyNavbar_LWe7}

> **dataByIndex**(`logicalIndex`, `mismatchDirection`?): `TData`

Returns a bar data by provided logical index.

#### Parameters[​](ISeriesApi.html#parameters-7 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-7 .anchor .anchorWithStickyNavbar_LWe7}

• **logicalIndex**: `number`

Logical index

• **mismatchDirection?**:
[`MismatchDirection`](../enumerations/MismatchDirection.html)

Search direction if no data found at provided logical index.

#### Returns[​](ISeriesApi.html#returns-10 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-10 .anchor .anchorWithStickyNavbar_LWe7}

`TData`

Original data item provided via setData or update methods.

#### Example[​](ISeriesApi.html#example-1 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-1 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const originalData = series.dataByIndex(10, LightweightCharts.MismatchDirection.NearestLeft);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### data()[​](ISeriesApi.html#data "Direct link to data()"){.hash-link aria-label="Direct link to data()"} {#data .anchor .anchorWithStickyNavbar_LWe7}

> **data**(): readonly `TData`\[\]

Returns all the bar data for the series.

#### Returns[​](ISeriesApi.html#returns-11 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-11 .anchor .anchorWithStickyNavbar_LWe7}

readonly `TData`\[\]

Original data items provided via setData or update methods.

#### Example[​](ISeriesApi.html#example-2 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-2 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const originalData = series.data();
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### subscribeDataChanged()[​](ISeriesApi.html#subscribedatachanged "Direct link to subscribeDataChanged()"){.hash-link aria-label="Direct link to subscribeDataChanged()"} {#subscribedatachanged .anchor .anchorWithStickyNavbar_LWe7}

> **subscribeDataChanged**(`handler`): `void`

Subscribe to the data changed event. This event is fired whenever the
`update` or `setData` method is evoked on the series.

#### Parameters[​](ISeriesApi.html#parameters-8 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-8 .anchor .anchorWithStickyNavbar_LWe7}

• **handler**:
[`DataChangedHandler`](../type-aliases/DataChangedHandler.html)

Handler to be called on a data changed event.

#### Returns[​](ISeriesApi.html#returns-12 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-12 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Example[​](ISeriesApi.html#example-3 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-3 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
function myHandler() {
    const data = series.data();
    console.log(`The data has changed. New Data length: ${data.length}`);
}

series.subscribeDataChanged(myHandler);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### unsubscribeDataChanged()[​](ISeriesApi.html#unsubscribedatachanged "Direct link to unsubscribeDataChanged()"){.hash-link aria-label="Direct link to unsubscribeDataChanged()"} {#unsubscribedatachanged .anchor .anchorWithStickyNavbar_LWe7}

> **unsubscribeDataChanged**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using
[subscribeDataChanged](ISeriesApi.html#subscribedatachanged).

#### Parameters[​](ISeriesApi.html#parameters-9 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-9 .anchor .anchorWithStickyNavbar_LWe7}

• **handler**:
[`DataChangedHandler`](../type-aliases/DataChangedHandler.html)

Previously subscribed handler

#### Returns[​](ISeriesApi.html#returns-13 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-13 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Example[​](ISeriesApi.html#example-4 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-4 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
chart.unsubscribeDataChanged(myHandler);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### createPriceLine()[​](ISeriesApi.html#createpriceline "Direct link to createPriceLine()"){.hash-link aria-label="Direct link to createPriceLine()"} {#createpriceline .anchor .anchorWithStickyNavbar_LWe7}

> **createPriceLine**(`options`): [`IPriceLine`](IPriceLine.html)

Creates a new price line

#### Parameters[​](ISeriesApi.html#parameters-10 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-10 .anchor .anchorWithStickyNavbar_LWe7}

• **options**:
[`CreatePriceLineOptions`](../type-aliases/CreatePriceLineOptions.html)

Any subset of options, however `price` is required.

#### Returns[​](ISeriesApi.html#returns-14 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-14 .anchor .anchorWithStickyNavbar_LWe7}

[`IPriceLine`](IPriceLine.html)

#### Example[​](ISeriesApi.html#example-5 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-5 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const priceLine = series.createPriceLine({
    price: 80.0,
    color: 'green',
    lineWidth: 2,
    lineStyle: LightweightCharts.LineStyle.Dotted,
    axisLabelVisible: true,
    title: 'P/L 500',
});
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### removePriceLine()[​](ISeriesApi.html#removepriceline "Direct link to removePriceLine()"){.hash-link aria-label="Direct link to removePriceLine()"} {#removepriceline .anchor .anchorWithStickyNavbar_LWe7}

> **removePriceLine**(`line`): `void`

Removes the price line that was created before.

#### Parameters[​](ISeriesApi.html#parameters-11 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-11 .anchor .anchorWithStickyNavbar_LWe7}

• **line**: [`IPriceLine`](IPriceLine.html)

A line to remove.

#### Returns[​](ISeriesApi.html#returns-15 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-15 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Example[​](ISeriesApi.html#example-6 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-6 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const priceLine = series.createPriceLine({ price: 80.0 });
series.removePriceLine(priceLine);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### priceLines()[​](ISeriesApi.html#pricelines "Direct link to priceLines()"){.hash-link aria-label="Direct link to priceLines()"} {#pricelines .anchor .anchorWithStickyNavbar_LWe7}

> **priceLines**(): [`IPriceLine`](IPriceLine.html)\[\]

Returns an array of price lines.

#### Returns[​](ISeriesApi.html#returns-16 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-16 .anchor .anchorWithStickyNavbar_LWe7}

[`IPriceLine`](IPriceLine.html)\[\]

------------------------------------------------------------------------

### seriesType()[​](ISeriesApi.html#seriestype "Direct link to seriesType()"){.hash-link aria-label="Direct link to seriesType()"} {#seriestype .anchor .anchorWithStickyNavbar_LWe7}

> **seriesType**(): `TSeriesType`

Return current series type.

#### Returns[​](ISeriesApi.html#returns-17 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-17 .anchor .anchorWithStickyNavbar_LWe7}

`TSeriesType`

Type of the series.

#### Example[​](ISeriesApi.html#example-7 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-7 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const lineSeries = chart.addSeries(LineSeries);
console.log(lineSeries.seriesType()); // "Line"

const candlestickSeries = chart.addCandlestickSeries();
console.log(candlestickSeries.seriesType()); // "Candlestick"
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### lastValueData()[​](ISeriesApi.html#lastvaluedata "Direct link to lastValueData()"){.hash-link aria-label="Direct link to lastValueData()"} {#lastvaluedata .anchor .anchorWithStickyNavbar_LWe7}

> **lastValueData**(`globalLast`):
> [`LastValueDataResult`](../type-aliases/LastValueDataResult.html)

Return the last value data of the series.

#### Parameters[​](ISeriesApi.html#parameters-12 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-12 .anchor .anchorWithStickyNavbar_LWe7}

• **globalLast**: `boolean`

If false, get the last value in the current visible range. Otherwise,
fetch the absolute last value

#### Returns[​](ISeriesApi.html#returns-18 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-18 .anchor .anchorWithStickyNavbar_LWe7}

[`LastValueDataResult`](../type-aliases/LastValueDataResult.html)

The last value data of the series.

#### Example[​](ISeriesApi.html#example-8 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-8 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const lineSeries = chart.addSeries(LineSeries);
console.log(lineSeries.lastValueData(true)); // { noData: false, price: 24.11, color: '#000000' }

const candlestickSeries = chart.addCandlestickSeries();
console.log(candlestickSeries.lastValueData(false)); // { noData: false, price: 145.72, color: '#000000' }
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### attachPrimitive()[​](ISeriesApi.html#attachprimitive "Direct link to attachPrimitive()"){.hash-link aria-label="Direct link to attachPrimitive()"} {#attachprimitive .anchor .anchorWithStickyNavbar_LWe7}

> **attachPrimitive**(`primitive`): `void`

Attaches additional drawing primitive to the series

#### Parameters[​](ISeriesApi.html#parameters-13 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-13 .anchor .anchorWithStickyNavbar_LWe7}

• **primitive**:
[`ISeriesPrimitive`](../type-aliases/ISeriesPrimitive.html)\<`HorzScaleItem`\>

any implementation of ISeriesPrimitive interface

#### Returns[​](ISeriesApi.html#returns-19 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-19 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### detachPrimitive()[​](ISeriesApi.html#detachprimitive "Direct link to detachPrimitive()"){.hash-link aria-label="Direct link to detachPrimitive()"} {#detachprimitive .anchor .anchorWithStickyNavbar_LWe7}

> **detachPrimitive**(`primitive`): `void`

Detaches additional drawing primitive from the series

#### Parameters[​](ISeriesApi.html#parameters-14 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-14 .anchor .anchorWithStickyNavbar_LWe7}

• **primitive**:
[`ISeriesPrimitive`](../type-aliases/ISeriesPrimitive.html)\<`HorzScaleItem`\>

implementation of ISeriesPrimitive interface attached before Does
nothing if specified primitive was not attached

#### Returns[​](ISeriesApi.html#returns-20 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-20 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### moveToPane()[​](ISeriesApi.html#movetopane "Direct link to moveToPane()"){.hash-link aria-label="Direct link to moveToPane()"} {#movetopane .anchor .anchorWithStickyNavbar_LWe7}

> **moveToPane**(`paneIndex`): `void`

Move the series to another pane.

If the pane with the specified index does not exist, the pane will be
created.

#### Parameters[​](ISeriesApi.html#parameters-15 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-15 .anchor .anchorWithStickyNavbar_LWe7}

• **paneIndex**: `number`

The index of the pane. Should be a number between 0 and the total number
of panes.

#### Returns[​](ISeriesApi.html#returns-21 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-21 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### seriesOrder()[​](ISeriesApi.html#seriesorder "Direct link to seriesOrder()"){.hash-link aria-label="Direct link to seriesOrder()"} {#seriesorder .anchor .anchorWithStickyNavbar_LWe7}

> **seriesOrder**(): `number`

Gets the zero-based index of this series within the list of all series
on the current pane.

#### Returns[​](ISeriesApi.html#returns-22 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-22 .anchor .anchorWithStickyNavbar_LWe7}

`number`

The current index of the series in the pane\'s series collection.

------------------------------------------------------------------------

### setSeriesOrder()[​](ISeriesApi.html#setseriesorder "Direct link to setSeriesOrder()"){.hash-link aria-label="Direct link to setSeriesOrder()"} {#setseriesorder .anchor .anchorWithStickyNavbar_LWe7}

> **setSeriesOrder**(`order`): `void`

Sets the zero-based index of this series within the pane\'s series
collection, thereby adjusting its rendering order.

Note:

- The chart may automatically recalculate this index after operations
  such as removing other series or moving this series to a different
  pane.
- If the provided index is less than 0, equal to, or greater than the
  number of series, it will be clamped to a valid range.
- Price scales derive their formatters from the series with the lowest
  index; changing the order may affect the price scale\'s formatting

#### Parameters[​](ISeriesApi.html#parameters-16 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-16 .anchor .anchorWithStickyNavbar_LWe7}

• **order**: `number`

The desired zero-based index to set for this series within the pane.

#### Returns[​](ISeriesApi.html#returns-23 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-23 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### getPane()[​](ISeriesApi.html#getpane "Direct link to getPane()"){.hash-link aria-label="Direct link to getPane()"} {#getpane .anchor .anchorWithStickyNavbar_LWe7}

> **getPane**(): [`IPaneApi`](IPaneApi.html)\<`HorzScaleItem`\>

Returns the pane to which the series is currently attached.

#### Returns[​](ISeriesApi.html#returns-24 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-24 .anchor .anchorWithStickyNavbar_LWe7}

[`IPaneApi`](IPaneApi.html)\<`HorzScaleItem`\>

Pane API object to control the pane

- [Type
  parameters](ISeriesApi.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Methods](ISeriesApi.html#methods){.table-of-contents__link
  .toc-highlight}
  - [priceFormatter()](ISeriesApi.html#priceformatter){.table-of-contents__link
    .toc-highlight}
  - [priceToCoordinate()](ISeriesApi.html#pricetocoordinate){.table-of-contents__link
    .toc-highlight}
  - [coordinateToPrice()](ISeriesApi.html#coordinatetoprice){.table-of-contents__link
    .toc-highlight}
  - [barsInLogicalRange()](ISeriesApi.html#barsinlogicalrange){.table-of-contents__link
    .toc-highlight}
  - [applyOptions()](ISeriesApi.html#applyoptions){.table-of-contents__link
    .toc-highlight}
  - [options()](ISeriesApi.html#options){.table-of-contents__link
    .toc-highlight}
  - [priceScale()](ISeriesApi.html#pricescale){.table-of-contents__link
    .toc-highlight}
  - [setData()](ISeriesApi.html#setdata){.table-of-contents__link
    .toc-highlight}
  - [update()](ISeriesApi.html#update){.table-of-contents__link
    .toc-highlight}
  - [pop()](ISeriesApi.html#pop){.table-of-contents__link
    .toc-highlight}
  - [dataByIndex()](ISeriesApi.html#databyindex){.table-of-contents__link
    .toc-highlight}
  - [data()](ISeriesApi.html#data){.table-of-contents__link
    .toc-highlight}
  - [subscribeDataChanged()](ISeriesApi.html#subscribedatachanged){.table-of-contents__link
    .toc-highlight}
  - [unsubscribeDataChanged()](ISeriesApi.html#unsubscribedatachanged){.table-of-contents__link
    .toc-highlight}
  - [createPriceLine()](ISeriesApi.html#createpriceline){.table-of-contents__link
    .toc-highlight}
  - [removePriceLine()](ISeriesApi.html#removepriceline){.table-of-contents__link
    .toc-highlight}
  - [priceLines()](ISeriesApi.html#pricelines){.table-of-contents__link
    .toc-highlight}
  - [seriesType()](ISeriesApi.html#seriestype){.table-of-contents__link
    .toc-highlight}
  - [lastValueData()](ISeriesApi.html#lastvaluedata){.table-of-contents__link
    .toc-highlight}
  - [attachPrimitive()](ISeriesApi.html#attachprimitive){.table-of-contents__link
    .toc-highlight}
  - [detachPrimitive()](ISeriesApi.html#detachprimitive){.table-of-contents__link
    .toc-highlight}
  - [moveToPane()](ISeriesApi.html#movetopane){.table-of-contents__link
    .toc-highlight}
  - [seriesOrder()](ISeriesApi.html#seriesorder){.table-of-contents__link
    .toc-highlight}
  - [setSeriesOrder()](ISeriesApi.html#setseriesorder){.table-of-contents__link
    .toc-highlight}
  - [getPane()](ISeriesApi.html#getpane){.table-of-contents__link
    .toc-highlight}
