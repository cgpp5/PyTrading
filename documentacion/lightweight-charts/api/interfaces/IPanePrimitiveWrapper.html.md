- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [IPanePrimitiveWrapper]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: IPanePrimitiveWrapper\<T, Options\>

Interface for a pane primitive.

## Type parameters[​](IPanePrimitiveWrapper.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **T**

• **Options**

## Properties[​](IPanePrimitiveWrapper.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### detach()[​](IPanePrimitiveWrapper.html#detach "Direct link to detach()"){.hash-link aria-label="Direct link to detach()"} {#detach .anchor .anchorWithStickyNavbar_LWe7}

> **detach**: () =\> `void`

Detaches the plugin from the pane.

#### Returns[​](IPanePrimitiveWrapper.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### getPane()[​](IPanePrimitiveWrapper.html#getpane "Direct link to getPane()"){.hash-link aria-label="Direct link to getPane()"} {#getpane .anchor .anchorWithStickyNavbar_LWe7}

> **getPane**: () =\> [`IPaneApi`](IPaneApi.html)\<`T`\>

Returns the current pane.

#### Returns[​](IPanePrimitiveWrapper.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

[`IPaneApi`](IPaneApi.html)\<`T`\>

------------------------------------------------------------------------

### applyOptions()?[​](IPanePrimitiveWrapper.html#applyoptions "Direct link to applyOptions()?"){.hash-link aria-label="Direct link to applyOptions()?"} {#applyoptions .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **applyOptions**: (`options`) =\> `void`

Applies options to the primitive.

#### Parameters[​](IPanePrimitiveWrapper.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **options**:
[`DeepPartial`](../type-aliases/DeepPartial.html)\<`Options`\>

Options to apply. The options are deeply merged with the current
options.

#### Returns[​](IPanePrimitiveWrapper.html#returns-2 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-2 .anchor .anchorWithStickyNavbar_LWe7}

`void`

- [Type
  parameters](IPanePrimitiveWrapper.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](IPanePrimitiveWrapper.html#properties){.table-of-contents__link
  .toc-highlight}
  - [detach()](IPanePrimitiveWrapper.html#detach){.table-of-contents__link
    .toc-highlight}
  - [getPane()](IPanePrimitiveWrapper.html#getpane){.table-of-contents__link
    .toc-highlight}
  - [applyOptions()?](IPanePrimitiveWrapper.html#applyoptions){.table-of-contents__link
    .toc-highlight}
