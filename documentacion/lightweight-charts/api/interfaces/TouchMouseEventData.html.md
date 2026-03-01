- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [TouchMouseEventData]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: TouchMouseEventData

The TouchMouseEventData interface represents events that occur due to
the user interacting with a pointing device (such as a mouse). See
[MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent){target="_blank"
rel="noopener noreferrer"}

## Properties[​](TouchMouseEventData.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### clientX[​](TouchMouseEventData.html#clientx "Direct link to clientX"){.hash-link aria-label="Direct link to clientX"} {#clientx .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **clientX**:
> [`Coordinate`](../type-aliases/Coordinate.html)

The X coordinate of the mouse pointer in local (DOM content)
coordinates.

------------------------------------------------------------------------

### clientY[​](TouchMouseEventData.html#clienty "Direct link to clientY"){.hash-link aria-label="Direct link to clientY"} {#clienty .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **clientY**:
> [`Coordinate`](../type-aliases/Coordinate.html)

The Y coordinate of the mouse pointer in local (DOM content)
coordinates.

------------------------------------------------------------------------

### pageX[​](TouchMouseEventData.html#pagex "Direct link to pageX"){.hash-link aria-label="Direct link to pageX"} {#pagex .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **pageX**: [`Coordinate`](../type-aliases/Coordinate.html)

The X coordinate of the mouse pointer relative to the whole document.

------------------------------------------------------------------------

### pageY[​](TouchMouseEventData.html#pagey "Direct link to pageY"){.hash-link aria-label="Direct link to pageY"} {#pagey .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **pageY**: [`Coordinate`](../type-aliases/Coordinate.html)

The Y coordinate of the mouse pointer relative to the whole document.

------------------------------------------------------------------------

### screenX[​](TouchMouseEventData.html#screenx "Direct link to screenX"){.hash-link aria-label="Direct link to screenX"} {#screenx .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **screenX**:
> [`Coordinate`](../type-aliases/Coordinate.html)

The X coordinate of the mouse pointer in global (screen) coordinates.

------------------------------------------------------------------------

### screenY[​](TouchMouseEventData.html#screeny "Direct link to screenY"){.hash-link aria-label="Direct link to screenY"} {#screeny .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **screenY**:
> [`Coordinate`](../type-aliases/Coordinate.html)

The Y coordinate of the mouse pointer in global (screen) coordinates.

------------------------------------------------------------------------

### localX[​](TouchMouseEventData.html#localx "Direct link to localX"){.hash-link aria-label="Direct link to localX"} {#localx .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **localX**: [`Coordinate`](../type-aliases/Coordinate.html)

The X coordinate of the mouse pointer relative to the chart / price axis
/ time axis canvas element.

------------------------------------------------------------------------

### localY[​](TouchMouseEventData.html#localy "Direct link to localY"){.hash-link aria-label="Direct link to localY"} {#localy .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **localY**: [`Coordinate`](../type-aliases/Coordinate.html)

The Y coordinate of the mouse pointer relative to the chart / price axis
/ time axis canvas element.

------------------------------------------------------------------------

### ctrlKey[​](TouchMouseEventData.html#ctrlkey "Direct link to ctrlKey"){.hash-link aria-label="Direct link to ctrlKey"} {#ctrlkey .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **ctrlKey**: `boolean`

Returns a boolean value that is true if the Ctrl key was active when the
key event was generated.

------------------------------------------------------------------------

### altKey[​](TouchMouseEventData.html#altkey "Direct link to altKey"){.hash-link aria-label="Direct link to altKey"} {#altkey .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **altKey**: `boolean`

Returns a boolean value that is true if the Alt (Option or ⌥ on macOS)
key was active when the key event was generated.

------------------------------------------------------------------------

### shiftKey[​](TouchMouseEventData.html#shiftkey "Direct link to shiftKey"){.hash-link aria-label="Direct link to shiftKey"} {#shiftkey .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **shiftKey**: `boolean`

Returns a boolean value that is true if the Shift key was active when
the key event was generated.

------------------------------------------------------------------------

### metaKey[​](TouchMouseEventData.html#metakey "Direct link to metaKey"){.hash-link aria-label="Direct link to metaKey"} {#metakey .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **metaKey**: `boolean`

Returns a boolean value that is true if the Meta key (on Mac keyboards,
the ⌘ Command key; on Windows keyboards, the Windows key (⊞)) was active
when the key event was generated.

- [Properties](TouchMouseEventData.html#properties){.table-of-contents__link
  .toc-highlight}
  - [clientX](TouchMouseEventData.html#clientx){.table-of-contents__link
    .toc-highlight}
  - [clientY](TouchMouseEventData.html#clienty){.table-of-contents__link
    .toc-highlight}
  - [pageX](TouchMouseEventData.html#pagex){.table-of-contents__link
    .toc-highlight}
  - [pageY](TouchMouseEventData.html#pagey){.table-of-contents__link
    .toc-highlight}
  - [screenX](TouchMouseEventData.html#screenx){.table-of-contents__link
    .toc-highlight}
  - [screenY](TouchMouseEventData.html#screeny){.table-of-contents__link
    .toc-highlight}
  - [localX](TouchMouseEventData.html#localx){.table-of-contents__link
    .toc-highlight}
  - [localY](TouchMouseEventData.html#localy){.table-of-contents__link
    .toc-highlight}
  - [ctrlKey](TouchMouseEventData.html#ctrlkey){.table-of-contents__link
    .toc-highlight}
  - [altKey](TouchMouseEventData.html#altkey){.table-of-contents__link
    .toc-highlight}
  - [shiftKey](TouchMouseEventData.html#shiftkey){.table-of-contents__link
    .toc-highlight}
  - [metaKey](TouchMouseEventData.html#metakey){.table-of-contents__link
    .toc-highlight}
