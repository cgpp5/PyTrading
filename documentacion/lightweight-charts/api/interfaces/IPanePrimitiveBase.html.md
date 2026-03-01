- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [IPanePrimitiveBase]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: IPanePrimitiveBase\<TPaneAttachedParameters\>

Base interface for series primitives. It must be implemented to add some
external graphics to series

## Type parameters[​](IPanePrimitiveBase.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **TPaneAttachedParameters** = `unknown`

## Methods[​](IPanePrimitiveBase.html#methods "Direct link to Methods"){.hash-link aria-label="Direct link to Methods"} {#methods .anchor .anchorWithStickyNavbar_LWe7}

### updateAllViews()?[​](IPanePrimitiveBase.html#updateallviews "Direct link to updateAllViews()?"){.hash-link aria-label="Direct link to updateAllViews()?"} {#updateallviews .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **updateAllViews**(): `void`

This method is called when viewport has been changed, so primitive have
to recalculate / invalidate its data

#### Returns[​](IPanePrimitiveBase.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### paneViews()?[​](IPanePrimitiveBase.html#paneviews "Direct link to paneViews()?"){.hash-link aria-label="Direct link to paneViews()?"} {#paneviews .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **paneViews**(): readonly
> [`IPanePrimitivePaneView`](IPanePrimitivePaneView.html)\[\]

Returns array of objects representing primitive in the main area of the
chart

#### Returns[​](IPanePrimitiveBase.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

readonly [`IPanePrimitivePaneView`](IPanePrimitivePaneView.html)\[\]

array of objects; each of then must implement IPrimitivePaneView
interface

For performance reasons, the lightweight library uses internal caches
based on references to arrays So, this method must return new array if
set of views has changed and should try to return the same array if
nothing changed

------------------------------------------------------------------------

### attached()?[​](IPanePrimitiveBase.html#attached "Direct link to attached()?"){.hash-link aria-label="Direct link to attached()?"} {#attached .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **attached**(`param`): `void`

Attached Lifecycle hook.

#### Parameters[​](IPanePrimitiveBase.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **param**: `TPaneAttachedParameters`

An object containing useful references for the attached primitive to
use.

#### Returns[​](IPanePrimitiveBase.html#returns-2 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-2 .anchor .anchorWithStickyNavbar_LWe7}

`void`

void

------------------------------------------------------------------------

### detached()?[​](IPanePrimitiveBase.html#detached "Direct link to detached()?"){.hash-link aria-label="Direct link to detached()?"} {#detached .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **detached**(): `void`

Detached Lifecycle hook.

#### Returns[​](IPanePrimitiveBase.html#returns-3 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-3 .anchor .anchorWithStickyNavbar_LWe7}

`void`

void

------------------------------------------------------------------------

### hitTest()?[​](IPanePrimitiveBase.html#hittest "Direct link to hitTest()?"){.hash-link aria-label="Direct link to hitTest()?"} {#hittest .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **hitTest**(`x`, `y`):
> [`PrimitiveHoveredItem`](PrimitiveHoveredItem.html)

Hit test method which will be called by the library when the cursor is
moved. Use this to register object ids being hovered for use within the
crosshairMoved and click events emitted by the chart. Additionally, the
hit test result can specify a preferred cursor type to display for the
main chart pane. This method should return the top most hit for this
primitive if more than one object is being intersected.

#### Parameters[​](IPanePrimitiveBase.html#parameters-1 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **x**: `number`

x Coordinate of mouse event

• **y**: `number`

y Coordinate of mouse event

#### Returns[​](IPanePrimitiveBase.html#returns-4 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-4 .anchor .anchorWithStickyNavbar_LWe7}

[`PrimitiveHoveredItem`](PrimitiveHoveredItem.html)

- [Type
  parameters](IPanePrimitiveBase.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Methods](IPanePrimitiveBase.html#methods){.table-of-contents__link
  .toc-highlight}
  - [updateAllViews()?](IPanePrimitiveBase.html#updateallviews){.table-of-contents__link
    .toc-highlight}
  - [paneViews()?](IPanePrimitiveBase.html#paneviews){.table-of-contents__link
    .toc-highlight}
  - [attached()?](IPanePrimitiveBase.html#attached){.table-of-contents__link
    .toc-highlight}
  - [detached()?](IPanePrimitiveBase.html#detached){.table-of-contents__link
    .toc-highlight}
  - [hitTest()?](IPanePrimitiveBase.html#hittest){.table-of-contents__link
    .toc-highlight}
