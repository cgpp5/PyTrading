- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [IPrimitivePaneView]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: IPrimitivePaneView

This interface represents the primitive for one of the pane of the chart
(main chart area, time scale, price scale).

## Methods[​](IPrimitivePaneView.html#methods "Direct link to Methods"){.hash-link aria-label="Direct link to Methods"} {#methods .anchor .anchorWithStickyNavbar_LWe7}

### zOrder()?[​](IPrimitivePaneView.html#zorder "Direct link to zOrder()?"){.hash-link aria-label="Direct link to zOrder()?"} {#zorder .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **zOrder**():
> [`PrimitivePaneViewZOrder`](../type-aliases/PrimitivePaneViewZOrder.html)

Defines where in the visual layer stack the renderer should be executed.
Default is `'normal'`.

#### Returns[​](IPrimitivePaneView.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

[`PrimitivePaneViewZOrder`](../type-aliases/PrimitivePaneViewZOrder.html)

the desired position in the visual layer stack.

#### See[​](IPrimitivePaneView.html#see "Direct link to See"){.hash-link aria-label="Direct link to See"} {#see .anchor .anchorWithStickyNavbar_LWe7}

[PrimitivePaneViewZOrder](../type-aliases/PrimitivePaneViewZOrder.html)

------------------------------------------------------------------------

### renderer()[​](IPrimitivePaneView.html#renderer "Direct link to renderer()"){.hash-link aria-label="Direct link to renderer()"} {#renderer .anchor .anchorWithStickyNavbar_LWe7}

> **renderer**():
> [`IPrimitivePaneRenderer`](IPrimitivePaneRenderer.html)

This method returns a renderer - special object to draw data

#### Returns[​](IPrimitivePaneView.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

[`IPrimitivePaneRenderer`](IPrimitivePaneRenderer.html)

an renderer object to be used for drawing, or `null` if we have nothing
to draw.

- [Methods](IPrimitivePaneView.html#methods){.table-of-contents__link
  .toc-highlight}
  - [zOrder()?](IPrimitivePaneView.html#zorder){.table-of-contents__link
    .toc-highlight}
  - [renderer()](IPrimitivePaneView.html#renderer){.table-of-contents__link
    .toc-highlight}
