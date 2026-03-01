- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [ISeriesPrimitiveBase]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: ISeriesPrimitiveBase\<TSeriesAttachedParameters\>

Base interface for series primitives. It must be implemented to add some
external graphics to series

## Type parameters[​](ISeriesPrimitiveBase.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **TSeriesAttachedParameters** = `unknown`

## Methods[​](ISeriesPrimitiveBase.html#methods "Direct link to Methods"){.hash-link aria-label="Direct link to Methods"} {#methods .anchor .anchorWithStickyNavbar_LWe7}

### updateAllViews()?[​](ISeriesPrimitiveBase.html#updateallviews "Direct link to updateAllViews()?"){.hash-link aria-label="Direct link to updateAllViews()?"} {#updateallviews .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **updateAllViews**(): `void`

This method is called when viewport has been changed, so primitive have
to recalculate / invalidate its data

#### Returns[​](ISeriesPrimitiveBase.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### priceAxisViews()?[​](ISeriesPrimitiveBase.html#priceaxisviews "Direct link to priceAxisViews()?"){.hash-link aria-label="Direct link to priceAxisViews()?"} {#priceaxisviews .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **priceAxisViews**(): readonly
> [`ISeriesPrimitiveAxisView`](ISeriesPrimitiveAxisView.html)\[\]

Returns array of labels to be drawn on the price axis used by the series

#### Returns[​](ISeriesPrimitiveBase.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

readonly [`ISeriesPrimitiveAxisView`](ISeriesPrimitiveAxisView.html)\[\]

array of objects; each of then must implement ISeriesPrimitiveAxisView
interface

For performance reasons, the lightweight library uses internal caches
based on references to arrays So, this method must return new array if
set of views has changed and should try to return the same array if
nothing changed

------------------------------------------------------------------------

### timeAxisViews()?[​](ISeriesPrimitiveBase.html#timeaxisviews "Direct link to timeAxisViews()?"){.hash-link aria-label="Direct link to timeAxisViews()?"} {#timeaxisviews .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **timeAxisViews**(): readonly
> [`ISeriesPrimitiveAxisView`](ISeriesPrimitiveAxisView.html)\[\]

Returns array of labels to be drawn on the time axis

#### Returns[​](ISeriesPrimitiveBase.html#returns-2 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-2 .anchor .anchorWithStickyNavbar_LWe7}

readonly [`ISeriesPrimitiveAxisView`](ISeriesPrimitiveAxisView.html)\[\]

array of objects; each of then must implement ISeriesPrimitiveAxisView
interface

For performance reasons, the lightweight library uses internal caches
based on references to arrays So, this method must return new array if
set of views has changed and should try to return the same array if
nothing changed

------------------------------------------------------------------------

### paneViews()?[​](ISeriesPrimitiveBase.html#paneviews "Direct link to paneViews()?"){.hash-link aria-label="Direct link to paneViews()?"} {#paneviews .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **paneViews**(): readonly
> [`IPrimitivePaneView`](IPrimitivePaneView.html)\[\]

Returns array of objects representing primitive in the main area of the
chart

#### Returns[​](ISeriesPrimitiveBase.html#returns-3 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-3 .anchor .anchorWithStickyNavbar_LWe7}

readonly [`IPrimitivePaneView`](IPrimitivePaneView.html)\[\]

array of objects; each of then must implement ISeriesPrimitivePaneView
interface

For performance reasons, the lightweight library uses internal caches
based on references to arrays So, this method must return new array if
set of views has changed and should try to return the same array if
nothing changed

------------------------------------------------------------------------

### priceAxisPaneViews()?[​](ISeriesPrimitiveBase.html#priceaxispaneviews "Direct link to priceAxisPaneViews()?"){.hash-link aria-label="Direct link to priceAxisPaneViews()?"} {#priceaxispaneviews .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **priceAxisPaneViews**(): readonly
> [`IPrimitivePaneView`](IPrimitivePaneView.html)\[\]

Returns array of objects representing primitive in the price axis area
of the chart

#### Returns[​](ISeriesPrimitiveBase.html#returns-4 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-4 .anchor .anchorWithStickyNavbar_LWe7}

readonly [`IPrimitivePaneView`](IPrimitivePaneView.html)\[\]

array of objects; each of then must implement ISeriesPrimitivePaneView
interface

For performance reasons, the lightweight library uses internal caches
based on references to arrays So, this method must return new array if
set of views has changed and should try to return the same array if
nothing changed

------------------------------------------------------------------------

### timeAxisPaneViews()?[​](ISeriesPrimitiveBase.html#timeaxispaneviews "Direct link to timeAxisPaneViews()?"){.hash-link aria-label="Direct link to timeAxisPaneViews()?"} {#timeaxispaneviews .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **timeAxisPaneViews**(): readonly
> [`IPrimitivePaneView`](IPrimitivePaneView.html)\[\]

Returns array of objects representing primitive in the time axis area of
the chart

#### Returns[​](ISeriesPrimitiveBase.html#returns-5 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-5 .anchor .anchorWithStickyNavbar_LWe7}

readonly [`IPrimitivePaneView`](IPrimitivePaneView.html)\[\]

array of objects; each of then must implement ISeriesPrimitivePaneView
interface

For performance reasons, the lightweight library uses internal caches
based on references to arrays So, this method must return new array if
set of views has changed and should try to return the same array if
nothing changed

------------------------------------------------------------------------

### autoscaleInfo()?[​](ISeriesPrimitiveBase.html#autoscaleinfo "Direct link to autoscaleInfo()?"){.hash-link aria-label="Direct link to autoscaleInfo()?"} {#autoscaleinfo .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **autoscaleInfo**(`startTimePoint`, `endTimePoint`):
> [`AutoscaleInfo`](AutoscaleInfo.html)

Return autoscaleInfo which will be merged with the series base
autoscaleInfo. You can use this to expand the autoscale range to include
visual elements drawn outside of the series\' current visible price
range.

**Important**: Please note that this method will be evoked very often
during scrolling and zooming of the chart, thus it is recommended that
this method is either simple to execute, or makes use of optimisations
such as caching to ensure that the chart remains responsive.

#### Parameters[​](ISeriesPrimitiveBase.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **startTimePoint**: [`Logical`](../type-aliases/Logical.html)

start time point for the current visible range

• **endTimePoint**: [`Logical`](../type-aliases/Logical.html)

end time point for the current visible range

#### Returns[​](ISeriesPrimitiveBase.html#returns-6 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-6 .anchor .anchorWithStickyNavbar_LWe7}

[`AutoscaleInfo`](AutoscaleInfo.html)

AutoscaleInfo

------------------------------------------------------------------------

### attached()?[​](ISeriesPrimitiveBase.html#attached "Direct link to attached()?"){.hash-link aria-label="Direct link to attached()?"} {#attached .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **attached**(`param`): `void`

Attached Lifecycle hook.

#### Parameters[​](ISeriesPrimitiveBase.html#parameters-1 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **param**: `TSeriesAttachedParameters`

An object containing useful references for the attached primitive to
use.

#### Returns[​](ISeriesPrimitiveBase.html#returns-7 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-7 .anchor .anchorWithStickyNavbar_LWe7}

`void`

void

------------------------------------------------------------------------

### detached()?[​](ISeriesPrimitiveBase.html#detached "Direct link to detached()?"){.hash-link aria-label="Direct link to detached()?"} {#detached .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **detached**(): `void`

Detached Lifecycle hook.

#### Returns[​](ISeriesPrimitiveBase.html#returns-8 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-8 .anchor .anchorWithStickyNavbar_LWe7}

`void`

void

------------------------------------------------------------------------

### hitTest()?[​](ISeriesPrimitiveBase.html#hittest "Direct link to hitTest()?"){.hash-link aria-label="Direct link to hitTest()?"} {#hittest .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **hitTest**(`x`, `y`):
> [`PrimitiveHoveredItem`](PrimitiveHoveredItem.html)

Hit test method which will be called by the library when the cursor is
moved. Use this to register object ids being hovered for use within the
crosshairMoved and click events emitted by the chart. Additionally, the
hit test result can specify a preferred cursor type to display for the
main chart pane. This method should return the top most hit for this
primitive if more than one object is being intersected.

#### Parameters[​](ISeriesPrimitiveBase.html#parameters-2 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-2 .anchor .anchorWithStickyNavbar_LWe7}

• **x**: `number`

x Coordinate of mouse event

• **y**: `number`

y Coordinate of mouse event

#### Returns[​](ISeriesPrimitiveBase.html#returns-9 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-9 .anchor .anchorWithStickyNavbar_LWe7}

[`PrimitiveHoveredItem`](PrimitiveHoveredItem.html)

- [Type
  parameters](ISeriesPrimitiveBase.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Methods](ISeriesPrimitiveBase.html#methods){.table-of-contents__link
  .toc-highlight}
  - [updateAllViews()?](ISeriesPrimitiveBase.html#updateallviews){.table-of-contents__link
    .toc-highlight}
  - [priceAxisViews()?](ISeriesPrimitiveBase.html#priceaxisviews){.table-of-contents__link
    .toc-highlight}
  - [timeAxisViews()?](ISeriesPrimitiveBase.html#timeaxisviews){.table-of-contents__link
    .toc-highlight}
  - [paneViews()?](ISeriesPrimitiveBase.html#paneviews){.table-of-contents__link
    .toc-highlight}
  - [priceAxisPaneViews()?](ISeriesPrimitiveBase.html#priceaxispaneviews){.table-of-contents__link
    .toc-highlight}
  - [timeAxisPaneViews()?](ISeriesPrimitiveBase.html#timeaxispaneviews){.table-of-contents__link
    .toc-highlight}
  - [autoscaleInfo()?](ISeriesPrimitiveBase.html#autoscaleinfo){.table-of-contents__link
    .toc-highlight}
  - [attached()?](ISeriesPrimitiveBase.html#attached){.table-of-contents__link
    .toc-highlight}
  - [detached()?](ISeriesPrimitiveBase.html#detached){.table-of-contents__link
    .toc-highlight}
  - [hitTest()?](ISeriesPrimitiveBase.html#hittest){.table-of-contents__link
    .toc-highlight}
