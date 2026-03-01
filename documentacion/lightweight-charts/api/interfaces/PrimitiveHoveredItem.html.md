- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [PrimitiveHoveredItem]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: PrimitiveHoveredItem

Data representing the currently hovered object from the Hit test.

## Properties[​](PrimitiveHoveredItem.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### cursorStyle?[​](PrimitiveHoveredItem.html#cursorstyle "Direct link to cursorStyle?"){.hash-link aria-label="Direct link to cursorStyle?"} {#cursorstyle .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **cursorStyle**: `string`

CSS cursor style as defined here: [MDN: CSS
Cursor](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor){target="_blank"
rel="noopener noreferrer"} or `undefined` if you want the library to use
the default cursor style instead.

------------------------------------------------------------------------

### externalId[​](PrimitiveHoveredItem.html#externalid "Direct link to externalId"){.hash-link aria-label="Direct link to externalId"} {#externalid .anchor .anchorWithStickyNavbar_LWe7}

> **externalId**: `string`

Hovered objects external ID. Can be used to identify the source item
within a mouse subscriber event.

------------------------------------------------------------------------

### zOrder[​](PrimitiveHoveredItem.html#zorder "Direct link to zOrder"){.hash-link aria-label="Direct link to zOrder"} {#zorder .anchor .anchorWithStickyNavbar_LWe7}

> **zOrder**:
> [`PrimitivePaneViewZOrder`](../type-aliases/PrimitivePaneViewZOrder.html)

The zOrder of the hovered item.

------------------------------------------------------------------------

### isBackground?[​](PrimitiveHoveredItem.html#isbackground "Direct link to isBackground?"){.hash-link aria-label="Direct link to isBackground?"} {#isbackground .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **isBackground**: `boolean`

Set to true if the object is rendered using `drawBackground` instead of
`draw`.

- [Properties](PrimitiveHoveredItem.html#properties){.table-of-contents__link
  .toc-highlight}
  - [cursorStyle?](PrimitiveHoveredItem.html#cursorstyle){.table-of-contents__link
    .toc-highlight}
  - [externalId](PrimitiveHoveredItem.html#externalid){.table-of-contents__link
    .toc-highlight}
  - [zOrder](PrimitiveHoveredItem.html#zorder){.table-of-contents__link
    .toc-highlight}
  - [isBackground?](PrimitiveHoveredItem.html#isbackground){.table-of-contents__link
    .toc-highlight}
