- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [CustomBarItemData]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: CustomBarItemData\<HorzScaleItem, TData\>

Renderer data for an item within the custom series.

## Type parameters[​](CustomBarItemData.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem**

• **TData** *extends* [`CustomData`](CustomData.html)\<`HorzScaleItem`\>
= [`CustomData`](CustomData.html)\<`HorzScaleItem`\>

## Properties[​](CustomBarItemData.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### x[​](CustomBarItemData.html#x "Direct link to x"){.hash-link aria-label="Direct link to x"} {#x .anchor .anchorWithStickyNavbar_LWe7}

> **x**: `number`

Horizontal coordinate for the item. Measured from the left edge of the
pane in pixels.

------------------------------------------------------------------------

### time[​](CustomBarItemData.html#time "Direct link to time"){.hash-link aria-label="Direct link to time"} {#time .anchor .anchorWithStickyNavbar_LWe7}

> **time**: `number`

Time scale index for the item. This isn\'t the timestamp but rather the
logical index.

------------------------------------------------------------------------

### originalData[​](CustomBarItemData.html#originaldata "Direct link to originalData"){.hash-link aria-label="Direct link to originalData"} {#originaldata .anchor .anchorWithStickyNavbar_LWe7}

> **originalData**: `TData`

Original data for the item.

------------------------------------------------------------------------

### barColor[​](CustomBarItemData.html#barcolor "Direct link to barColor"){.hash-link aria-label="Direct link to barColor"} {#barcolor .anchor .anchorWithStickyNavbar_LWe7}

> **barColor**: `string`

Color assigned for the item, typically used for price line and price
scale label.

- [Type
  parameters](CustomBarItemData.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](CustomBarItemData.html#properties){.table-of-contents__link
  .toc-highlight}
  - [x](CustomBarItemData.html#x){.table-of-contents__link
    .toc-highlight}
  - [time](CustomBarItemData.html#time){.table-of-contents__link
    .toc-highlight}
  - [originalData](CustomBarItemData.html#originaldata){.table-of-contents__link
    .toc-highlight}
  - [barColor](CustomBarItemData.html#barcolor){.table-of-contents__link
    .toc-highlight}
