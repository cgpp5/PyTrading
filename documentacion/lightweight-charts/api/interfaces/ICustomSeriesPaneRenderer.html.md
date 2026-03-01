- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [ICustomSeriesPaneRenderer]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: ICustomSeriesPaneRenderer

Renderer for the custom series. This paints on the main chart pane.

## Methods[​](ICustomSeriesPaneRenderer.html#methods "Direct link to Methods"){.hash-link aria-label="Direct link to Methods"} {#methods .anchor .anchorWithStickyNavbar_LWe7}

### draw()[​](ICustomSeriesPaneRenderer.html#draw "Direct link to draw()"){.hash-link aria-label="Direct link to draw()"} {#draw .anchor .anchorWithStickyNavbar_LWe7}

> **draw**(`target`, `priceConverter`, `isHovered`, `hitTestData`?):
> `void`

Draw function for the renderer.

#### Parameters[​](ICustomSeriesPaneRenderer.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **target**: `CanvasRenderingTarget2D`

canvas context to draw on, refer to FancyCanvas library for more details
about this class.

• **priceConverter**:
[`PriceToCoordinateConverter`](../type-aliases/PriceToCoordinateConverter.html)

converter function for changing prices into vertical coordinate values.

• **isHovered**: `boolean`

Whether the series is hovered.

• **hitTestData?**: `unknown`

Optional hit test data for the series.

#### Returns[​](ICustomSeriesPaneRenderer.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`void`

- [Methods](ICustomSeriesPaneRenderer.html#methods){.table-of-contents__link
  .toc-highlight}
  - [draw()](ICustomSeriesPaneRenderer.html#draw){.table-of-contents__link
    .toc-highlight}
