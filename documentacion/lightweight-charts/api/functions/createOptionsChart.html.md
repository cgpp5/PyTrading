- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Functions]{.breadcrumbs__link}
- [createOptionsChart]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Function: createOptionsChart()

> **createOptionsChart**(`container`, `options`?):
> [`IChartApiBase`](../interfaces/IChartApiBase.html)\<`number`\>

Creates an \'options\' chart with price values on the horizontal scale.

This function is used to create a specialized chart type where the
horizontal scale represents price values instead of time. It\'s
particularly useful for visualizing option chains, price distributions,
or any data where price is the primary x-axis metric.

## Parameters[​](createOptionsChart.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **container**: `string` \| `HTMLElement`

The DOM element or its id where the chart will be rendered.

• **options?**: [`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`PriceChartOptions`](../interfaces/PriceChartOptions.html)\>

Optional configuration options for the price chart.

## Returns[​](createOptionsChart.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

[`IChartApiBase`](../interfaces/IChartApiBase.html)\<`number`\>

An instance of IChartApiBase configured for price-based horizontal
scaling.

- [Parameters](createOptionsChart.html#parameters){.table-of-contents__link
  .toc-highlight}
- [Returns](createOptionsChart.html#returns){.table-of-contents__link
  .toc-highlight}
