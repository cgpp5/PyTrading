- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [ITimeScaleApi]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: ITimeScaleApi\<HorzScaleItem\>

Interface to chart time scale

## Type parameters[​](ITimeScaleApi.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem**

## Methods[​](ITimeScaleApi.html#methods "Direct link to Methods"){.hash-link aria-label="Direct link to Methods"} {#methods .anchor .anchorWithStickyNavbar_LWe7}

### scrollPosition()[​](ITimeScaleApi.html#scrollposition "Direct link to scrollPosition()"){.hash-link aria-label="Direct link to scrollPosition()"} {#scrollposition .anchor .anchorWithStickyNavbar_LWe7}

> **scrollPosition**(): `number`

Return the distance from the right edge of the time scale to the lastest
bar of the series measured in bars.

#### Returns[​](ITimeScaleApi.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`number`

------------------------------------------------------------------------

### scrollToPosition()[​](ITimeScaleApi.html#scrolltoposition "Direct link to scrollToPosition()"){.hash-link aria-label="Direct link to scrollToPosition()"} {#scrolltoposition .anchor .anchorWithStickyNavbar_LWe7}

> **scrollToPosition**(`position`, `animated`): `void`

Scrolls the chart to the specified position.

#### Parameters[​](ITimeScaleApi.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **position**: `number`

Target data position

• **animated**: `boolean`

Setting this to true makes the chart scrolling smooth and adds animation

#### Returns[​](ITimeScaleApi.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### scrollToRealTime()[​](ITimeScaleApi.html#scrolltorealtime "Direct link to scrollToRealTime()"){.hash-link aria-label="Direct link to scrollToRealTime()"} {#scrolltorealtime .anchor .anchorWithStickyNavbar_LWe7}

> **scrollToRealTime**(): `void`

Restores default scroll position of the chart. This process is always
animated.

#### Returns[​](ITimeScaleApi.html#returns-2 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-2 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### getVisibleRange()[​](ITimeScaleApi.html#getvisiblerange "Direct link to getVisibleRange()"){.hash-link aria-label="Direct link to getVisibleRange()"} {#getvisiblerange .anchor .anchorWithStickyNavbar_LWe7}

> **getVisibleRange**(): [`IRange`](IRange.html)\<`HorzScaleItem`\>

Returns current visible time range of the chart.

Note that this method cannot extrapolate time and will use the only
currently existent data. To get complete information about current
visible range, please use
[getVisibleLogicalRange](ITimeScaleApi.html#getvisiblelogicalrange) and
[ISeriesApi.barsInLogicalRange](ISeriesApi.html#barsinlogicalrange).

#### Returns[​](ITimeScaleApi.html#returns-3 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-3 .anchor .anchorWithStickyNavbar_LWe7}

[`IRange`](IRange.html)\<`HorzScaleItem`\>

Visible range or null if the chart has no data at all.

------------------------------------------------------------------------

### setVisibleRange()[​](ITimeScaleApi.html#setvisiblerange "Direct link to setVisibleRange()"){.hash-link aria-label="Direct link to setVisibleRange()"} {#setvisiblerange .anchor .anchorWithStickyNavbar_LWe7}

> **setVisibleRange**(`range`): `void`

Sets visible range of data.

Note that this method cannot extrapolate time and will use the only
currently existent data. Thus, for example, if currently a chart
doesn\'t have data prior `2018-01-01` date and you set visible range
with `from` date `2016-01-01`, it will be automatically adjusted to
`2018-01-01` (and the same for `to` date).

But if you can approximate indexes on your own - you could use
[setVisibleLogicalRange](ITimeScaleApi.html#setvisiblelogicalrange)
instead.

#### Parameters[​](ITimeScaleApi.html#parameters-1 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **range**: [`IRange`](IRange.html)\<`HorzScaleItem`\>

Target visible range of data.

#### Returns[​](ITimeScaleApi.html#returns-4 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-4 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Example[​](ITimeScaleApi.html#example "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
chart.timeScale().setVisibleRange({
    from: (new Date(Date.UTC(2018, 0, 1, 0, 0, 0, 0))).getTime() / 1000,
    to: (new Date(Date.UTC(2018, 1, 1, 0, 0, 0, 0))).getTime() / 1000,
});
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### getVisibleLogicalRange()[​](ITimeScaleApi.html#getvisiblelogicalrange "Direct link to getVisibleLogicalRange()"){.hash-link aria-label="Direct link to getVisibleLogicalRange()"} {#getvisiblelogicalrange .anchor .anchorWithStickyNavbar_LWe7}

> **getVisibleLogicalRange**():
> [`LogicalRange`](../type-aliases/LogicalRange.html)

Returns the current visible [logical
range](../../time-scale.html#logical-range) of the chart as an object
with the first and last time points of the logical range, or returns
`null` if the chart has no data.

#### Returns[​](ITimeScaleApi.html#returns-5 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-5 .anchor .anchorWithStickyNavbar_LWe7}

[`LogicalRange`](../type-aliases/LogicalRange.html)

Visible range or null if the chart has no data at all.

------------------------------------------------------------------------

### setVisibleLogicalRange()[​](ITimeScaleApi.html#setvisiblelogicalrange "Direct link to setVisibleLogicalRange()"){.hash-link aria-label="Direct link to setVisibleLogicalRange()"} {#setvisiblelogicalrange .anchor .anchorWithStickyNavbar_LWe7}

> **setVisibleLogicalRange**(`range`): `void`

Sets visible [logical range](../../time-scale.html#logical-range) of
data.

#### Parameters[​](ITimeScaleApi.html#parameters-2 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-2 .anchor .anchorWithStickyNavbar_LWe7}

• **range**: [`IRange`](IRange.html)\<`number`\>

Target visible logical range of data.

#### Returns[​](ITimeScaleApi.html#returns-6 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-6 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Example[​](ITimeScaleApi.html#example-1 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-1 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
chart.timeScale().setVisibleLogicalRange({ from: 0, to: 10 });
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### resetTimeScale()[​](ITimeScaleApi.html#resettimescale "Direct link to resetTimeScale()"){.hash-link aria-label="Direct link to resetTimeScale()"} {#resettimescale .anchor .anchorWithStickyNavbar_LWe7}

> **resetTimeScale**(): `void`

Restores default zoom level and scroll position of the time scale.

#### Returns[​](ITimeScaleApi.html#returns-7 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-7 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### fitContent()[​](ITimeScaleApi.html#fitcontent "Direct link to fitContent()"){.hash-link aria-label="Direct link to fitContent()"} {#fitcontent .anchor .anchorWithStickyNavbar_LWe7}

> **fitContent**(): `void`

Automatically calculates the visible range to fit all data from all
series.

#### Returns[​](ITimeScaleApi.html#returns-8 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-8 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### logicalToCoordinate()[​](ITimeScaleApi.html#logicaltocoordinate "Direct link to logicalToCoordinate()"){.hash-link aria-label="Direct link to logicalToCoordinate()"} {#logicaltocoordinate .anchor .anchorWithStickyNavbar_LWe7}

> **logicalToCoordinate**(`logical`):
> [`Coordinate`](../type-aliases/Coordinate.html)

Converts a logical index to local x coordinate.

#### Parameters[​](ITimeScaleApi.html#parameters-3 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-3 .anchor .anchorWithStickyNavbar_LWe7}

• **logical**: [`Logical`](../type-aliases/Logical.html)

Logical index needs to be converted

#### Returns[​](ITimeScaleApi.html#returns-9 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-9 .anchor .anchorWithStickyNavbar_LWe7}

[`Coordinate`](../type-aliases/Coordinate.html)

x coordinate of that time or `null` if the chart doesn\'t have data

------------------------------------------------------------------------

### coordinateToLogical()[​](ITimeScaleApi.html#coordinatetological "Direct link to coordinateToLogical()"){.hash-link aria-label="Direct link to coordinateToLogical()"} {#coordinatetological .anchor .anchorWithStickyNavbar_LWe7}

> **coordinateToLogical**(`x`):
> [`Logical`](../type-aliases/Logical.html)

Converts a coordinate to logical index.

#### Parameters[​](ITimeScaleApi.html#parameters-4 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-4 .anchor .anchorWithStickyNavbar_LWe7}

• **x**: `number`

Coordinate needs to be converted

#### Returns[​](ITimeScaleApi.html#returns-10 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-10 .anchor .anchorWithStickyNavbar_LWe7}

[`Logical`](../type-aliases/Logical.html)

Logical index that is located on that coordinate or `null` if the chart
doesn\'t have data

------------------------------------------------------------------------

### timeToIndex()[​](ITimeScaleApi.html#timetoindex "Direct link to timeToIndex()"){.hash-link aria-label="Direct link to timeToIndex()"} {#timetoindex .anchor .anchorWithStickyNavbar_LWe7}

> **timeToIndex**(`time`, `findNearest`?):
> [`TimePointIndex`](../type-aliases/TimePointIndex.html)

Converts a time to local x coordinate.

#### Parameters[​](ITimeScaleApi.html#parameters-5 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-5 .anchor .anchorWithStickyNavbar_LWe7}

• **time**: `HorzScaleItem`

Time needs to be converted

• **findNearest?**: `boolean`

#### Returns[​](ITimeScaleApi.html#returns-11 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-11 .anchor .anchorWithStickyNavbar_LWe7}

[`TimePointIndex`](../type-aliases/TimePointIndex.html)

X coordinate of that time or `null` if no time found on time scale

------------------------------------------------------------------------

### timeToCoordinate()[​](ITimeScaleApi.html#timetocoordinate "Direct link to timeToCoordinate()"){.hash-link aria-label="Direct link to timeToCoordinate()"} {#timetocoordinate .anchor .anchorWithStickyNavbar_LWe7}

> **timeToCoordinate**(`time`):
> [`Coordinate`](../type-aliases/Coordinate.html)

Converts a time to local x coordinate.

#### Parameters[​](ITimeScaleApi.html#parameters-6 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-6 .anchor .anchorWithStickyNavbar_LWe7}

• **time**: `HorzScaleItem`

Time needs to be converted

#### Returns[​](ITimeScaleApi.html#returns-12 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-12 .anchor .anchorWithStickyNavbar_LWe7}

[`Coordinate`](../type-aliases/Coordinate.html)

X coordinate of that time or `null` if no time found on time scale

------------------------------------------------------------------------

### coordinateToTime()[​](ITimeScaleApi.html#coordinatetotime "Direct link to coordinateToTime()"){.hash-link aria-label="Direct link to coordinateToTime()"} {#coordinatetotime .anchor .anchorWithStickyNavbar_LWe7}

> **coordinateToTime**(`x`): `HorzScaleItem`

Converts a coordinate to time.

#### Parameters[​](ITimeScaleApi.html#parameters-7 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-7 .anchor .anchorWithStickyNavbar_LWe7}

• **x**: `number`

Coordinate needs to be converted.

#### Returns[​](ITimeScaleApi.html#returns-13 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-13 .anchor .anchorWithStickyNavbar_LWe7}

`HorzScaleItem`

Time of a bar that is located on that coordinate or `null` if there are
no bars found on that coordinate.

------------------------------------------------------------------------

### width()[​](ITimeScaleApi.html#width "Direct link to width()"){.hash-link aria-label="Direct link to width()"} {#width .anchor .anchorWithStickyNavbar_LWe7}

> **width**(): `number`

Returns a width of the time scale.

#### Returns[​](ITimeScaleApi.html#returns-14 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-14 .anchor .anchorWithStickyNavbar_LWe7}

`number`

------------------------------------------------------------------------

### height()[​](ITimeScaleApi.html#height "Direct link to height()"){.hash-link aria-label="Direct link to height()"} {#height .anchor .anchorWithStickyNavbar_LWe7}

> **height**(): `number`

Returns a height of the time scale.

#### Returns[​](ITimeScaleApi.html#returns-15 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-15 .anchor .anchorWithStickyNavbar_LWe7}

`number`

------------------------------------------------------------------------

### subscribeVisibleTimeRangeChange()[​](ITimeScaleApi.html#subscribevisibletimerangechange "Direct link to subscribeVisibleTimeRangeChange()"){.hash-link aria-label="Direct link to subscribeVisibleTimeRangeChange()"} {#subscribevisibletimerangechange .anchor .anchorWithStickyNavbar_LWe7}

> **subscribeVisibleTimeRangeChange**(`handler`): `void`

Subscribe to the visible time range change events.

The argument passed to the handler function is an object with `from` and
`to` properties of type [Time](../type-aliases/Time.html), or `null` if
there is no visible data.

#### Parameters[​](ITimeScaleApi.html#parameters-8 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-8 .anchor .anchorWithStickyNavbar_LWe7}

• **handler**:
[`TimeRangeChangeEventHandler`](../type-aliases/TimeRangeChangeEventHandler.html)\<`HorzScaleItem`\>

Handler (function) to be called when the visible indexes change.

#### Returns[​](ITimeScaleApi.html#returns-16 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-16 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Example[​](ITimeScaleApi.html#example-2 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-2 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
function myVisibleTimeRangeChangeHandler(newVisibleTimeRange) {
    if (newVisibleTimeRange === null) {
        // handle null
    }

    // handle new logical range
}

chart.timeScale().subscribeVisibleTimeRangeChange(myVisibleTimeRangeChangeHandler);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### unsubscribeVisibleTimeRangeChange()[​](ITimeScaleApi.html#unsubscribevisibletimerangechange "Direct link to unsubscribeVisibleTimeRangeChange()"){.hash-link aria-label="Direct link to unsubscribeVisibleTimeRangeChange()"} {#unsubscribevisibletimerangechange .anchor .anchorWithStickyNavbar_LWe7}

> **unsubscribeVisibleTimeRangeChange**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using
[subscribeVisibleTimeRangeChange](ITimeScaleApi.html#subscribevisibletimerangechange).

#### Parameters[​](ITimeScaleApi.html#parameters-9 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-9 .anchor .anchorWithStickyNavbar_LWe7}

• **handler**:
[`TimeRangeChangeEventHandler`](../type-aliases/TimeRangeChangeEventHandler.html)\<`HorzScaleItem`\>

Previously subscribed handler

#### Returns[​](ITimeScaleApi.html#returns-17 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-17 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Example[​](ITimeScaleApi.html#example-3 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-3 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
chart.timeScale().unsubscribeVisibleTimeRangeChange(myVisibleTimeRangeChangeHandler);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### subscribeVisibleLogicalRangeChange()[​](ITimeScaleApi.html#subscribevisiblelogicalrangechange "Direct link to subscribeVisibleLogicalRangeChange()"){.hash-link aria-label="Direct link to subscribeVisibleLogicalRangeChange()"} {#subscribevisiblelogicalrangechange .anchor .anchorWithStickyNavbar_LWe7}

> **subscribeVisibleLogicalRangeChange**(`handler`): `void`

Subscribe to the visible logical range change events.

The argument passed to the handler function is an object with `from` and
`to` properties of type `number`, or `null` if there is no visible data.

#### Parameters[​](ITimeScaleApi.html#parameters-10 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-10 .anchor .anchorWithStickyNavbar_LWe7}

• **handler**:
[`LogicalRangeChangeEventHandler`](../type-aliases/LogicalRangeChangeEventHandler.html)

Handler (function) to be called when the visible indexes change.

#### Returns[​](ITimeScaleApi.html#returns-18 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-18 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Example[​](ITimeScaleApi.html#example-4 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-4 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
function myVisibleLogicalRangeChangeHandler(newVisibleLogicalRange) {
    if (newVisibleLogicalRange === null) {
        // handle null
    }

    // handle new logical range
}

chart.timeScale().subscribeVisibleLogicalRangeChange(myVisibleLogicalRangeChangeHandler);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### unsubscribeVisibleLogicalRangeChange()[​](ITimeScaleApi.html#unsubscribevisiblelogicalrangechange "Direct link to unsubscribeVisibleLogicalRangeChange()"){.hash-link aria-label="Direct link to unsubscribeVisibleLogicalRangeChange()"} {#unsubscribevisiblelogicalrangechange .anchor .anchorWithStickyNavbar_LWe7}

> **unsubscribeVisibleLogicalRangeChange**(`handler`): `void`

Unsubscribe a handler that was previously subscribed using
[subscribeVisibleLogicalRangeChange](ITimeScaleApi.html#subscribevisiblelogicalrangechange).

#### Parameters[​](ITimeScaleApi.html#parameters-11 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-11 .anchor .anchorWithStickyNavbar_LWe7}

• **handler**:
[`LogicalRangeChangeEventHandler`](../type-aliases/LogicalRangeChangeEventHandler.html)

Previously subscribed handler

#### Returns[​](ITimeScaleApi.html#returns-19 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-19 .anchor .anchorWithStickyNavbar_LWe7}

`void`

#### Example[​](ITimeScaleApi.html#example-5 "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example-5 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
chart.timeScale().unsubscribeVisibleLogicalRangeChange(myVisibleLogicalRangeChangeHandler);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### subscribeSizeChange()[​](ITimeScaleApi.html#subscribesizechange "Direct link to subscribeSizeChange()"){.hash-link aria-label="Direct link to subscribeSizeChange()"} {#subscribesizechange .anchor .anchorWithStickyNavbar_LWe7}

> **subscribeSizeChange**(`handler`): `void`

Adds a subscription to time scale size changes

#### Parameters[​](ITimeScaleApi.html#parameters-12 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-12 .anchor .anchorWithStickyNavbar_LWe7}

• **handler**:
[`SizeChangeEventHandler`](../type-aliases/SizeChangeEventHandler.html)

Handler (function) to be called when the time scale size changes

#### Returns[​](ITimeScaleApi.html#returns-20 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-20 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### unsubscribeSizeChange()[​](ITimeScaleApi.html#unsubscribesizechange "Direct link to unsubscribeSizeChange()"){.hash-link aria-label="Direct link to unsubscribeSizeChange()"} {#unsubscribesizechange .anchor .anchorWithStickyNavbar_LWe7}

> **unsubscribeSizeChange**(`handler`): `void`

Removes a subscription to time scale size changes

#### Parameters[​](ITimeScaleApi.html#parameters-13 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-13 .anchor .anchorWithStickyNavbar_LWe7}

• **handler**:
[`SizeChangeEventHandler`](../type-aliases/SizeChangeEventHandler.html)

Previously subscribed handler

#### Returns[​](ITimeScaleApi.html#returns-21 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-21 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### applyOptions()[​](ITimeScaleApi.html#applyoptions "Direct link to applyOptions()"){.hash-link aria-label="Direct link to applyOptions()"} {#applyoptions .anchor .anchorWithStickyNavbar_LWe7}

> **applyOptions**(`options`): `void`

Applies new options to the time scale.

#### Parameters[​](ITimeScaleApi.html#parameters-14 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-14 .anchor .anchorWithStickyNavbar_LWe7}

• **options**: [`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`HorzScaleOptions`](HorzScaleOptions.html)\>

Any subset of options.

#### Returns[​](ITimeScaleApi.html#returns-22 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-22 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### options()[​](ITimeScaleApi.html#options "Direct link to options()"){.hash-link aria-label="Direct link to options()"} {#options .anchor .anchorWithStickyNavbar_LWe7}

> **options**(): `Readonly`
> \<[`HorzScaleOptions`](HorzScaleOptions.html)\>

Returns current options

#### Returns[​](ITimeScaleApi.html#returns-23 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-23 .anchor .anchorWithStickyNavbar_LWe7}

`Readonly` \<[`HorzScaleOptions`](HorzScaleOptions.html)\>

Currently applied options

- [Type
  parameters](ITimeScaleApi.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Methods](ITimeScaleApi.html#methods){.table-of-contents__link
  .toc-highlight}
  - [scrollPosition()](ITimeScaleApi.html#scrollposition){.table-of-contents__link
    .toc-highlight}
  - [scrollToPosition()](ITimeScaleApi.html#scrolltoposition){.table-of-contents__link
    .toc-highlight}
  - [scrollToRealTime()](ITimeScaleApi.html#scrolltorealtime){.table-of-contents__link
    .toc-highlight}
  - [getVisibleRange()](ITimeScaleApi.html#getvisiblerange){.table-of-contents__link
    .toc-highlight}
  - [setVisibleRange()](ITimeScaleApi.html#setvisiblerange){.table-of-contents__link
    .toc-highlight}
  - [getVisibleLogicalRange()](ITimeScaleApi.html#getvisiblelogicalrange){.table-of-contents__link
    .toc-highlight}
  - [setVisibleLogicalRange()](ITimeScaleApi.html#setvisiblelogicalrange){.table-of-contents__link
    .toc-highlight}
  - [resetTimeScale()](ITimeScaleApi.html#resettimescale){.table-of-contents__link
    .toc-highlight}
  - [fitContent()](ITimeScaleApi.html#fitcontent){.table-of-contents__link
    .toc-highlight}
  - [logicalToCoordinate()](ITimeScaleApi.html#logicaltocoordinate){.table-of-contents__link
    .toc-highlight}
  - [coordinateToLogical()](ITimeScaleApi.html#coordinatetological){.table-of-contents__link
    .toc-highlight}
  - [timeToIndex()](ITimeScaleApi.html#timetoindex){.table-of-contents__link
    .toc-highlight}
  - [timeToCoordinate()](ITimeScaleApi.html#timetocoordinate){.table-of-contents__link
    .toc-highlight}
  - [coordinateToTime()](ITimeScaleApi.html#coordinatetotime){.table-of-contents__link
    .toc-highlight}
  - [width()](ITimeScaleApi.html#width){.table-of-contents__link
    .toc-highlight}
  - [height()](ITimeScaleApi.html#height){.table-of-contents__link
    .toc-highlight}
  - [subscribeVisibleTimeRangeChange()](ITimeScaleApi.html#subscribevisibletimerangechange){.table-of-contents__link
    .toc-highlight}
  - [unsubscribeVisibleTimeRangeChange()](ITimeScaleApi.html#unsubscribevisibletimerangechange){.table-of-contents__link
    .toc-highlight}
  - [subscribeVisibleLogicalRangeChange()](ITimeScaleApi.html#subscribevisiblelogicalrangechange){.table-of-contents__link
    .toc-highlight}
  - [unsubscribeVisibleLogicalRangeChange()](ITimeScaleApi.html#unsubscribevisiblelogicalrangechange){.table-of-contents__link
    .toc-highlight}
  - [subscribeSizeChange()](ITimeScaleApi.html#subscribesizechange){.table-of-contents__link
    .toc-highlight}
  - [unsubscribeSizeChange()](ITimeScaleApi.html#unsubscribesizechange){.table-of-contents__link
    .toc-highlight}
  - [applyOptions()](ITimeScaleApi.html#applyoptions){.table-of-contents__link
    .toc-highlight}
  - [options()](ITimeScaleApi.html#options){.table-of-contents__link
    .toc-highlight}
