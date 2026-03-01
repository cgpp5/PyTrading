- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [CustomConflationContext]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: CustomConflationContext\<HorzScaleItem, TData\>

Context object provided to custom series conflation reducers. This wraps
the internal SeriesPlotRow data while providing a user-friendly
interface.

## Type parameters[​](CustomConflationContext.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem** = [`Time`](../type-aliases/Time.html)

• **TData** *extends* [`CustomData`](CustomData.html)\<`HorzScaleItem`\>
= [`CustomData`](CustomData.html)\<`HorzScaleItem`\>

## Properties[​](CustomConflationContext.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### data[​](CustomConflationContext.html#data "Direct link to data"){.hash-link aria-label="Direct link to data"} {#data .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **data**: `TData`

The original custom data item provided by the user.

------------------------------------------------------------------------

### index[​](CustomConflationContext.html#index "Direct link to index"){.hash-link aria-label="Direct link to index"} {#index .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **index**: `number`

The time index of the data point in the series.

------------------------------------------------------------------------

### originalTime[​](CustomConflationContext.html#originaltime "Direct link to originalTime"){.hash-link aria-label="Direct link to originalTime"} {#originaltime .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **originalTime**: `HorzScaleItem`

The original time value provided by the user.

------------------------------------------------------------------------

### time[​](CustomConflationContext.html#time "Direct link to time"){.hash-link aria-label="Direct link to time"} {#time .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **time**: `unknown`

The internal time point object.

------------------------------------------------------------------------

### priceValues[​](CustomConflationContext.html#pricevalues "Direct link to priceValues"){.hash-link aria-label="Direct link to priceValues"} {#pricevalues .anchor .anchorWithStickyNavbar_LWe7}

> `readonly` **priceValues**:
> [`CustomSeriesPricePlotValues`](../type-aliases/CustomSeriesPricePlotValues.html)

The computed price values for this data point (as returned by
priceValueBuilder). The last value in this array is used as the current
price.

- [Type
  parameters](CustomConflationContext.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](CustomConflationContext.html#properties){.table-of-contents__link
  .toc-highlight}
  - [data](CustomConflationContext.html#data){.table-of-contents__link
    .toc-highlight}
  - [index](CustomConflationContext.html#index){.table-of-contents__link
    .toc-highlight}
  - [originalTime](CustomConflationContext.html#originaltime){.table-of-contents__link
    .toc-highlight}
  - [time](CustomConflationContext.html#time){.table-of-contents__link
    .toc-highlight}
  - [priceValues](CustomConflationContext.html#pricevalues){.table-of-contents__link
    .toc-highlight}
