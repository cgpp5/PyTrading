- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [ICustomSeriesPaneView]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: ICustomSeriesPaneView\<HorzScaleItem, TData, TSeriesOptions\>

This interface represents the view for the custom series

## Type parameters[​](ICustomSeriesPaneView.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem** = [`Time`](../type-aliases/Time.html)

• **TData** *extends* [`CustomData`](CustomData.html)\<`HorzScaleItem`\>
= [`CustomData`](CustomData.html)\<`HorzScaleItem`\>

• **TSeriesOptions** *extends*
[`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.html) =
[`CustomSeriesOptions`](../type-aliases/CustomSeriesOptions.html)

## Methods[​](ICustomSeriesPaneView.html#methods "Direct link to Methods"){.hash-link aria-label="Direct link to Methods"} {#methods .anchor .anchorWithStickyNavbar_LWe7}

### renderer()[​](ICustomSeriesPaneView.html#renderer "Direct link to renderer()"){.hash-link aria-label="Direct link to renderer()"} {#renderer .anchor .anchorWithStickyNavbar_LWe7}

> **renderer**():
> [`ICustomSeriesPaneRenderer`](ICustomSeriesPaneRenderer.html)

This method returns a renderer - special object to draw data for the
series on the main chart pane.

#### Returns[​](ICustomSeriesPaneView.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

[`ICustomSeriesPaneRenderer`](ICustomSeriesPaneRenderer.html)

an renderer object to be used for drawing.

------------------------------------------------------------------------

### update()[​](ICustomSeriesPaneView.html#update "Direct link to update()"){.hash-link aria-label="Direct link to update()"} {#update .anchor .anchorWithStickyNavbar_LWe7}

> **update**(`data`, `seriesOptions`): `void`

This method will be called with the latest data for the renderer to use
during the next paint.

#### Parameters[​](ICustomSeriesPaneView.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **data**:
[`PaneRendererCustomData`](PaneRendererCustomData.html)\<`HorzScaleItem`,
`TData`\>

• **seriesOptions**: `TSeriesOptions`

#### Returns[​](ICustomSeriesPaneView.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### priceValueBuilder()[​](ICustomSeriesPaneView.html#pricevaluebuilder "Direct link to priceValueBuilder()"){.hash-link aria-label="Direct link to priceValueBuilder()"} {#pricevaluebuilder .anchor .anchorWithStickyNavbar_LWe7}

> **priceValueBuilder**(`plotRow`):
> [`CustomSeriesPricePlotValues`](../type-aliases/CustomSeriesPricePlotValues.html)

A function for interpreting the custom series data and returning an
array of numbers representing the price values for the item. These price
values are used by the chart to determine the auto-scaling (to ensure
the items are in view) and the crosshair and price line positions. The
last value in the array will be used as the current value. You
shouldn\'t need to have more than 3 values in this array since the
library only needs a largest, smallest, and current value.

#### Parameters[​](ICustomSeriesPaneView.html#parameters-1 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **plotRow**: `TData`

#### Returns[​](ICustomSeriesPaneView.html#returns-2 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-2 .anchor .anchorWithStickyNavbar_LWe7}

[`CustomSeriesPricePlotValues`](../type-aliases/CustomSeriesPricePlotValues.html)

------------------------------------------------------------------------

### isWhitespace()[​](ICustomSeriesPaneView.html#iswhitespace "Direct link to isWhitespace()"){.hash-link aria-label="Direct link to isWhitespace()"} {#iswhitespace .anchor .anchorWithStickyNavbar_LWe7}

> **isWhitespace**(`data`):
> `data is CustomSeriesWhitespaceData<HorzScaleItem>`

A function for testing whether a data point should be considered fully
specified, or if it should be considered as whitespace. Should return
`true` if is whitespace.

#### Parameters[​](ICustomSeriesPaneView.html#parameters-2 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-2 .anchor .anchorWithStickyNavbar_LWe7}

• **data**: `TData` \|
[`CustomSeriesWhitespaceData`](CustomSeriesWhitespaceData.html)\<`HorzScaleItem`\>

data point to be tested

#### Returns[​](ICustomSeriesPaneView.html#returns-3 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-3 .anchor .anchorWithStickyNavbar_LWe7}

`data is CustomSeriesWhitespaceData<HorzScaleItem>`

------------------------------------------------------------------------

### defaultOptions()[​](ICustomSeriesPaneView.html#defaultoptions "Direct link to defaultOptions()"){.hash-link aria-label="Direct link to defaultOptions()"} {#defaultoptions .anchor .anchorWithStickyNavbar_LWe7}

> **defaultOptions**(): `TSeriesOptions`

Default options

#### Returns[​](ICustomSeriesPaneView.html#returns-4 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-4 .anchor .anchorWithStickyNavbar_LWe7}

`TSeriesOptions`

------------------------------------------------------------------------

### destroy()?[​](ICustomSeriesPaneView.html#destroy "Direct link to destroy()?"){.hash-link aria-label="Direct link to destroy()?"} {#destroy .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **destroy**(): `void`

This method will be evoked when the series has been removed from the
chart. This method should be used to clean up any objects, references,
and other items that could potentially cause memory leaks.

This method should contain all the necessary code to clean up the object
before it is removed from memory. This includes removing any event
listeners or timers that are attached to the object, removing any
references to other objects, and resetting any values or properties that
were modified during the lifetime of the object.

#### Returns[​](ICustomSeriesPaneView.html#returns-5 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-5 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### conflationReducer()?[​](ICustomSeriesPaneView.html#conflationreducer "Direct link to conflationReducer()?"){.hash-link aria-label="Direct link to conflationReducer()?"} {#conflationreducer .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **conflationReducer**(`item1`, `item2`): `TData`

Optional reducer used for conflation of custom data points. Given
exactly 2 custom data contexts, should return a single aggregated item.
Each context provides access to the original data plus metadata needed
for conflation.

#### Parameters[​](ICustomSeriesPaneView.html#parameters-3 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-3 .anchor .anchorWithStickyNavbar_LWe7}

• **item1**:
[`CustomConflationContext`](CustomConflationContext.html)\<`HorzScaleItem`,
`TData`\>

• **item2**:
[`CustomConflationContext`](CustomConflationContext.html)\<`HorzScaleItem`,
`TData`\>

#### Returns[​](ICustomSeriesPaneView.html#returns-6 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-6 .anchor .anchorWithStickyNavbar_LWe7}

`TData`

- [Type
  parameters](ICustomSeriesPaneView.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Methods](ICustomSeriesPaneView.html#methods){.table-of-contents__link
  .toc-highlight}
  - [renderer()](ICustomSeriesPaneView.html#renderer){.table-of-contents__link
    .toc-highlight}
  - [update()](ICustomSeriesPaneView.html#update){.table-of-contents__link
    .toc-highlight}
  - [priceValueBuilder()](ICustomSeriesPaneView.html#pricevaluebuilder){.table-of-contents__link
    .toc-highlight}
  - [isWhitespace()](ICustomSeriesPaneView.html#iswhitespace){.table-of-contents__link
    .toc-highlight}
  - [defaultOptions()](ICustomSeriesPaneView.html#defaultoptions){.table-of-contents__link
    .toc-highlight}
  - [destroy()?](ICustomSeriesPaneView.html#destroy){.table-of-contents__link
    .toc-highlight}
  - [conflationReducer()?](ICustomSeriesPaneView.html#conflationreducer){.table-of-contents__link
    .toc-highlight}
