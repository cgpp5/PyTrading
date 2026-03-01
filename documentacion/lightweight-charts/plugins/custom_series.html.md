- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Plugins]{.breadcrumbs__link}
- [Custom Series Types]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Custom Series Types

Custom series allow developers to create new types of series with their
own data structures, and rendering logic (implemented using
[CanvasRenderingContext2D](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D){target="_blank"
rel="noopener noreferrer"} methods). These custom series extend the
current capabilities of our built-in series, providing a consistent API
which mirrors the built-in chart types.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]{.admonitionIcon_Rf37}note

These series are expected to have a uniform width for each data point,
which ensures that the chart maintains a consistent look and feel across
all series types. The only restriction on the data structure is that it
should extend the [`CustomData`](../api/interfaces/CustomData.html)
interface (have a valid time property for each data point).

## Defining a Custom Series[​](custom_series.html#defining-a-custom-series "Direct link to Defining a Custom Series"){.hash-link aria-label="Direct link to Defining a Custom Series"} {#defining-a-custom-series .anchor .anchorWithStickyNavbar_LWe7}

A custom series should implement the
[`ICustomSeriesPaneView`](../api/interfaces/ICustomSeriesPaneView.html)
interface. The interface defines the basic functionality and structure
required for creating a custom series view.

It includes the following methods and properties:

### Renderer[​](custom_series.html#renderer "Direct link to Renderer"){.hash-link aria-label="Direct link to Renderer"} {#renderer .anchor .anchorWithStickyNavbar_LWe7}

- ICustomSeriesPaneView property:
  [`renderer`](../api/interfaces/ICustomSeriesPaneView.html#renderer)

This method should return a renderer which implements the
[`ICustomSeriesPaneRenderer`](../api/interfaces/ICustomSeriesPaneRenderer.html)
interface and is used to draw the series data on the main chart pane.

The [`draw`](../api/interfaces/ICustomSeriesPaneRenderer.html#draw)
method of the renderer is evoked whenever the chart needs to draw the
series.

The
[`PriceToCoordinateConverter`](../api/type-aliases/PriceToCoordinateConverter.html)
provided as the 2nd argument to the draw method is a convenience
function for changing prices into vertical coordinate values. It is
provided since the series\' original data will most likely be defined in
price values, and the renderer needs to draw with coordinates. The
values returned by the converter will be defined in mediaSize (unscaled
by `devicePixelRatio`).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]{.admonitionIcon_Rf37}tip

`CanvasRenderingTarget2D` provided within the `draw` function is
explained in more detail on the [Canvas Rendering
Target](canvas-rendering-target.html) page.

### Update[​](custom_series.html#update "Direct link to Update"){.hash-link aria-label="Direct link to Update"} {#update .anchor .anchorWithStickyNavbar_LWe7}

- ICustomSeriesPaneView property:
  [`update`](../api/interfaces/ICustomSeriesPaneView.html#update)

This method will be called with the latest data for the renderer to use
during the next paint.

The update method is evoked with two parameters: `data` (discussed
below), and `seriesOptions`. seriesOptions is a reference to the
currently applied options for the series

The
[`PaneRendererCustomData`](../api/interfaces/PaneRendererCustomData.html)
interface provides the data that can be used within the renderer for
drawing the series data. It includes the following properties:

- `bars`: List of all the series\' items and their x coordinates. See
  [`CustomBarItemData`](../api/interfaces/CustomBarItemData.html) for
  more details
- `barSpacing`: Spacing between consecutive bars.
- `visibleRange`: The current visible range of items on the chart.

### Price Value Builder[​](custom_series.html#price-value-builder "Direct link to Price Value Builder"){.hash-link aria-label="Direct link to Price Value Builder"} {#price-value-builder .anchor .anchorWithStickyNavbar_LWe7}

- ICustomSeriesPaneView property:
  [`priceValueBuilder`](../api/interfaces/ICustomSeriesPaneView.html#pricevaluebuilder)

A function for interpreting the custom series data and returning an
array of numbers representing the prices values for the item,
specifically the equivalent highest, lowest, and current price values
for the data item.

These price values are used by the chart to determine the auto-scaling
(to ensure the items are in view) and the crosshair and price line
positions. The largest and smallest values in the array will be used to
specify the visible range of the painted item, and the last value will
be used for the crosshair and price line position.

### Whitespace[​](custom_series.html#whitespace "Direct link to Whitespace"){.hash-link aria-label="Direct link to Whitespace"} {#whitespace .anchor .anchorWithStickyNavbar_LWe7}

- ICustomSeriesPaneView property:
  [`isWhitespace`](../api/interfaces/ICustomSeriesPaneView.html#iswhitespace)

A function used by the library to determine which data points provided
by the user should be considered Whitespace. The method should return
`true` when the data point is Whitespace. Data points which are
whitespace data won\'t be provided to the renderer, or the
`priceValueBuilder`.

### Default Options[​](custom_series.html#default-options "Direct link to Default Options"){.hash-link aria-label="Direct link to Default Options"} {#default-options .anchor .anchorWithStickyNavbar_LWe7}

- ICustomSeriesPaneView property:
  [`defaultOptions`](../api/interfaces/ICustomSeriesPaneView.html#defaultoptions)

The default options to be used for the series. The user can override
these values using the options argument in
[`addCustomSeries`](../api/interfaces/IChartApi.html#addcustomseries),
or via the
[`applyOptions`](../api/interfaces/ISeriesApi.html#applyoptions) method
on the `ISeriesAPI`.

### Destroy[​](custom_series.html#destroy "Direct link to Destroy"){.hash-link aria-label="Direct link to Destroy"} {#destroy .anchor .anchorWithStickyNavbar_LWe7}

- ICustomSeriesPaneView property:
  [`destroy`](../api/interfaces/ICustomSeriesPaneView.html#destroy)

This method will be evoked when the series has been removed from the
chart. This method should be used to clean up any objects, references,
and other items that could potentially cause memory leaks.

This method should contain all the necessary code to clean up the object
before it is removed from memory. This includes removing any event
listeners or timers that are attached to the object, removing any
references to other objects, and resetting any values or properties that
were modified during the lifetime of the object.

[](pane-primitives.html){.pagination-nav__link
.pagination-nav__link--prev}

Previous

Pane Primitives

[](canvas-rendering-target.html){.pagination-nav__link
.pagination-nav__link--next}

Next

Canvas Rendering Target

- [Defining a Custom
  Series](custom_series.html#defining-a-custom-series){.table-of-contents__link
  .toc-highlight}
  - [Renderer](custom_series.html#renderer){.table-of-contents__link
    .toc-highlight}
  - [Update](custom_series.html#update){.table-of-contents__link
    .toc-highlight}
  - [Price Value
    Builder](custom_series.html#price-value-builder){.table-of-contents__link
    .toc-highlight}
  - [Whitespace](custom_series.html#whitespace){.table-of-contents__link
    .toc-highlight}
  - [Default
    Options](custom_series.html#default-options){.table-of-contents__link
    .toc-highlight}
  - [Destroy](custom_series.html#destroy){.table-of-contents__link
    .toc-highlight}
