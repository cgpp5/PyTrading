- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [PaneRendererCustomData]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: PaneRendererCustomData\<HorzScaleItem, TData\>

Data provide to the custom series pane view which can be used within the
renderer for drawing the series data.

## Type parameters[​](PaneRendererCustomData.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem**

• **TData** *extends* [`CustomData`](CustomData.html)\<`HorzScaleItem`\>

## Properties[​](PaneRendererCustomData.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### bars[​](PaneRendererCustomData.html#bars "Direct link to bars"){.hash-link aria-label="Direct link to bars"} {#bars .anchor .anchorWithStickyNavbar_LWe7}

> **bars**: readonly
> [`CustomBarItemData`](CustomBarItemData.html)\<`HorzScaleItem`,
> `TData`\>\[\]

List of all the series\' items and their x coordinates.

------------------------------------------------------------------------

### barSpacing[​](PaneRendererCustomData.html#barspacing "Direct link to barSpacing"){.hash-link aria-label="Direct link to barSpacing"} {#barspacing .anchor .anchorWithStickyNavbar_LWe7}

> **barSpacing**: `number`

Spacing between consecutive bars.

------------------------------------------------------------------------

### visibleRange[​](PaneRendererCustomData.html#visiblerange "Direct link to visibleRange"){.hash-link aria-label="Direct link to visibleRange"} {#visiblerange .anchor .anchorWithStickyNavbar_LWe7}

> **visibleRange**: [`IRange`](IRange.html)\<`number`\>

The current visible range of items on the chart.

------------------------------------------------------------------------

### conflationFactor[​](PaneRendererCustomData.html#conflationfactor "Direct link to conflationFactor"){.hash-link aria-label="Direct link to conflationFactor"} {#conflationfactor .anchor .anchorWithStickyNavbar_LWe7}

> **conflationFactor**: `number`

Current conflation factor. The value represents how many data points
have been combined to form this conflated data point. This can be used
to calculate the effective bar spacing until the next data point.
`effectiveBarSpacing = conflationFactor * barSpacing`. If you are
rendering a non-continuous series (like a Candlestick instead of Line)
then you likely would want to use the effectiveBarSpacing value for your
width calculations.

- [Type
  parameters](PaneRendererCustomData.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](PaneRendererCustomData.html#properties){.table-of-contents__link
  .toc-highlight}
  - [bars](PaneRendererCustomData.html#bars){.table-of-contents__link
    .toc-highlight}
  - [barSpacing](PaneRendererCustomData.html#barspacing){.table-of-contents__link
    .toc-highlight}
  - [visibleRange](PaneRendererCustomData.html#visiblerange){.table-of-contents__link
    .toc-highlight}
  - [conflationFactor](PaneRendererCustomData.html#conflationfactor){.table-of-contents__link
    .toc-highlight}
