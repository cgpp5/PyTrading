- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Plugins]{.breadcrumbs__link}
- [Series Primitives]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Series Primitives

Primitives are extensions to the series which can define views and
renderers to draw on the chart using
[CanvasRenderingContext2D](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D){target="_blank"
rel="noopener noreferrer"}.

Primitives are defined by implementing the
[`ISeriesPrimitive`](../api/type-aliases/ISeriesPrimitive.html)
interface. The interface defines the basic functionality and structure
required for creating custom primitives.

## Views[​](series-primitives.html#views "Direct link to Views"){.hash-link aria-label="Direct link to Views"} {#views .anchor .anchorWithStickyNavbar_LWe7}

The primary purpose of a series primitive is to provide one, or more,
views to the library which contain the state and logic required to draw
on the chart panes.

There are two types of views which are supported within
`ISeriesPrimitive` which are:

- [`IPrimitivePaneView`](../api/interfaces/IPrimitivePaneView.html)
- [`ISeriesPrimitiveAxisView`](../api/interfaces/ISeriesPrimitiveAxisView.html)

The library will evoke the following getter functions (if defined) to
get references to the primitive\'s defined views for the corresponding
section of the chart:

- [`paneViews`](../api/interfaces/ISeriesPrimitiveBase.html#paneviews)
- [`priceAxisPaneViews`](../api/interfaces/ISeriesPrimitiveBase.html#priceaxispaneviews)
- [`timeAxisPaneViews`](../api/interfaces/ISeriesPrimitiveBase.html#timeaxispaneviews)
- [`priceAxisViews`](../api/interfaces/ISeriesPrimitiveBase.html#priceaxisviews)
- [`timeAxisViews`](../api/interfaces/ISeriesPrimitiveBase.html#timeaxisviews)

The first three views allow drawing on the corresponding panes (main
chart pane, price scale pane, and horizontal time scale pane) using the
[CanvasRenderingContext2D](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D){target="_blank"
rel="noopener noreferrer"} and should implement the
`ISeriesPrimitivePaneView` interface.

The views returned by the `priceAxisViews` and `timeAxisViews` getter
methods should implement the `ISeriesPrimitiveAxisView` interface and
are used to define labels to be drawn on the corresponding scales.

Below is a visual example showing the various sections of the chart
where a Primitive can draw.

 

### IPrimitivePaneView[​](series-primitives.html#iprimitivepaneview "Direct link to IPrimitivePaneView"){.hash-link aria-label="Direct link to IPrimitivePaneView"} {#iprimitivepaneview .anchor .anchorWithStickyNavbar_LWe7}

The [`IPrimitivePaneView`](../api/interfaces/IPrimitivePaneView.html)
interface can be used to define a view which provides a renderer
(implementing the
[`IPrimitivePaneRenderer`](../api/interfaces/IPrimitivePaneRenderer.html)
interface) for drawing on the corresponding area of the chart using the
[CanvasRenderingContext2D](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D){target="_blank"
rel="noopener noreferrer"} API. The view can define a
[`zOrder`](../api/interfaces/IPrimitivePaneView.html#zorder) to control
where in the visual stack the drawing will occur (See
[`PrimitivePaneViewZOrder`](../api/type-aliases/PrimitivePaneViewZOrder.html)
for more information).

Renderers should provide a
[`draw`](../api/interfaces/IPrimitivePaneRenderer.html#draw) method
which will be given a `CanvasRenderingTarget2D` target on which it can
draw. Additionally, a renderer can optionally provide a
[`drawBackground`](../api/interfaces/IPrimitivePaneRenderer.html#drawbackground)
method for drawing beneath other elements on the same zOrder.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]{.admonitionIcon_Rf37}tip

`CanvasRenderingTarget2D` is explained in more detail on the [Canvas
Rendering Target](canvas-rendering-target.html) page.

#### Interactive Demo of zOrder layers[​](series-primitives.html#interactive-demo-of-zorder-layers "Direct link to Interactive Demo of zOrder layers"){.hash-link aria-label="Direct link to Interactive Demo of zOrder layers"} {#interactive-demo-of-zorder-layers .anchor .anchorWithStickyNavbar_LWe7}

Below is an interactive demo chart illustrating where each zOrder is
drawn relative to the existing chart elements such as the grid, series,
and crosshair.

 

### ISeriesPrimitiveAxisView[​](series-primitives.html#iseriesprimitiveaxisview "Direct link to ISeriesPrimitiveAxisView"){.hash-link aria-label="Direct link to ISeriesPrimitiveAxisView"} {#iseriesprimitiveaxisview .anchor .anchorWithStickyNavbar_LWe7}

The
[`ISeriesPrimitiveAxisView`](../api/interfaces/ISeriesPrimitiveAxisView.html)
interface can be used to define a label on the price or time axis.

This interface provides several methods to define the appearance and
position of the label, such as the
[`coordinate`](../api/interfaces/ISeriesPrimitiveAxisView.html#coordinate)
method, which should return the desired coordinate for the label on the
axis. It also defines optional methods to set the fixed coordinate,
text, text color, background color, and visibility of the label.

Please see the
[`ISeriesPrimitiveAxisView`](../api/interfaces/ISeriesPrimitiveAxisView.html)
interface for more details.

## Lifecycle Methods[​](series-primitives.html#lifecycle-methods "Direct link to Lifecycle Methods"){.hash-link aria-label="Direct link to Lifecycle Methods"} {#lifecycle-methods .anchor .anchorWithStickyNavbar_LWe7}

Your primitive can use the
[`attached`](../api/interfaces/ISeriesPrimitiveBase.html#attached) and
[`detached`](../api/interfaces/ISeriesPrimitiveBase.html#detached)
lifecycle methods to manage the lifecycle of the primitive, such as
creating or removing external objects and event handlers.

### attached[​](series-primitives.html#attached "Direct link to attached"){.hash-link aria-label="Direct link to attached"} {#attached .anchor .anchorWithStickyNavbar_LWe7}

This method is called when the primitive is attached to a chart. The
attached method is evoked with a [single
argument](../api/interfaces/SeriesAttachedParameter.html) containing
properties for the chart, series, and a callback to request an update.
The `chart` and `series` properties are references to the chart API and
the series API instances for convenience purposes so that they don\'t
need to be manually provided within the primitive\'s constructor (if
needed by the primitive).

The `requestUpdate` callback allows the primitive to notify the chart
that it should be updated and redrawn.

### detached[​](series-primitives.html#detached "Direct link to detached"){.hash-link aria-label="Direct link to detached"} {#detached .anchor .anchorWithStickyNavbar_LWe7}

This method is called when the primitive is detached from a chart. This
can be used to remove any external objects or event handlers that were
created during the attached lifecycle method.

## Updating Views[​](series-primitives.html#updating-views "Direct link to Updating Views"){.hash-link aria-label="Direct link to Updating Views"} {#updating-views .anchor .anchorWithStickyNavbar_LWe7}

Your primitive should update the views in the
[`updateAllViews()`](../api/interfaces/ISeriesPrimitiveBase.html#updateallviews)
method such that when the renderers are evoked, they can draw with the
latest information. The library invokes this method when it wants to
update and redraw the chart. If you would like to notify the library
that it should trigger an update then you can use the `requestUpdate`
callback provided by the attached lifecycle method.

## Extending the Autoscale Info[​](series-primitives.html#extending-the-autoscale-info "Direct link to Extending the Autoscale Info"){.hash-link aria-label="Direct link to Extending the Autoscale Info"} {#extending-the-autoscale-info .anchor .anchorWithStickyNavbar_LWe7}

The
[`autoscaleInfo()`](../api/interfaces/ISeriesPrimitiveBase.html#autoscaleinfo)
method can be provided to extend the base autoScale information of the
series. This can be used to ensure that the chart is automatically
scaled correctly to include all the graphics drawn by the primitive.

Whenever the chart needs to calculate the vertical visible range of the
series within the current time range then it will evoke this method.
This method can be omitted and the library will use the normal autoscale
information for the series. If the method is implemented then the
returned values will be merged with the base autoscale information to
define the vertical visible range.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]{.admonitionIcon_Rf37}warning

Please note that this method will be evoked very often during scrolling
and zooming of the chart, thus it is recommended that this method is
either simple to execute, or makes use of optimisations such as caching
to ensure that the chart remains responsive.

[](intro.html){.pagination-nav__link .pagination-nav__link--prev}

Previous

Overview

[](pane-primitives.html){.pagination-nav__link
.pagination-nav__link--next}

Next

Pane Primitives

- [Views](series-primitives.html#views){.table-of-contents__link
  .toc-highlight}
  - [IPrimitivePaneView](series-primitives.html#iprimitivepaneview){.table-of-contents__link
    .toc-highlight}
  - [ISeriesPrimitiveAxisView](series-primitives.html#iseriesprimitiveaxisview){.table-of-contents__link
    .toc-highlight}
- [Lifecycle
  Methods](series-primitives.html#lifecycle-methods){.table-of-contents__link
  .toc-highlight}
  - [attached](series-primitives.html#attached){.table-of-contents__link
    .toc-highlight}
  - [detached](series-primitives.html#detached){.table-of-contents__link
    .toc-highlight}
- [Updating
  Views](series-primitives.html#updating-views){.table-of-contents__link
  .toc-highlight}
- [Extending the Autoscale
  Info](series-primitives.html#extending-the-autoscale-info){.table-of-contents__link
  .toc-highlight}
