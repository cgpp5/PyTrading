- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [IPrimitivePaneRenderer]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: IPrimitivePaneRenderer

This interface represents rendering some element on the canvas

## Methods[​](IPrimitivePaneRenderer.html#methods "Direct link to Methods"){.hash-link aria-label="Direct link to Methods"} {#methods .anchor .anchorWithStickyNavbar_LWe7}

### draw()[​](IPrimitivePaneRenderer.html#draw "Direct link to draw()"){.hash-link aria-label="Direct link to draw()"} {#draw .anchor .anchorWithStickyNavbar_LWe7}

> **draw**(`target`, `utils`?): `void`

Method to draw main content of the element

#### Parameters[​](IPrimitivePaneRenderer.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **target**: `CanvasRenderingTarget2D`

canvas context to draw on, refer to FancyCanvas library for more details
about this class

• **utils?**: [`DrawingUtils`](DrawingUtils.html)

exposes drawing utilities (such as setLineStyle) from the library to
plugins

#### Returns[​](IPrimitivePaneRenderer.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### drawBackground()?[​](IPrimitivePaneRenderer.html#drawbackground "Direct link to drawBackground()?"){.hash-link aria-label="Direct link to drawBackground()?"} {#drawbackground .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **drawBackground**(`target`, `utils`?): `void`

Optional method to draw the background. Some elements could implement
this method to draw on the background of the chart. Usually this is some
kind of watermarks or time areas highlighting.

#### Parameters[​](IPrimitivePaneRenderer.html#parameters-1 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **target**: `CanvasRenderingTarget2D`

canvas context to draw on, refer FancyCanvas library for more details
about this class

• **utils?**: [`DrawingUtils`](DrawingUtils.html)

exposes drawing utilities (such as setLineStyle) from the library to
plugins

#### Returns[​](IPrimitivePaneRenderer.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

`void`

- [Methods](IPrimitivePaneRenderer.html#methods){.table-of-contents__link
  .toc-highlight}
  - [draw()](IPrimitivePaneRenderer.html#draw){.table-of-contents__link
    .toc-highlight}
  - [drawBackground()?](IPrimitivePaneRenderer.html#drawbackground){.table-of-contents__link
    .toc-highlight}
