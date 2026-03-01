- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Functions]{.breadcrumbs__link}
- [createYieldCurveChart]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Function: createYieldCurveChart()

> **createYieldCurveChart**(`container`, `options`?):
> [`IYieldCurveChartApi`](../interfaces/IYieldCurveChartApi.html)

Creates a yield curve chart with the specified options.

A yield curve chart differs from the default chart type in the following
ways:

- Horizontal scale is linearly spaced, and defined in monthly time
  duration units
- Whitespace is ignored for the crosshair and grid lines

## Parameters[​](createYieldCurveChart.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **container**: `string` \| `HTMLElement`

ID of HTML element or element itself

• **options?**: [`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`YieldCurveChartOptions`](../interfaces/YieldCurveChartOptions.html)\>

The yield chart options.

## Returns[​](createYieldCurveChart.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

[`IYieldCurveChartApi`](../interfaces/IYieldCurveChartApi.html)

An interface to the created chart

- [Parameters](createYieldCurveChart.html#parameters){.table-of-contents__link
  .toc-highlight}
- [Returns](createYieldCurveChart.html#returns){.table-of-contents__link
  .toc-highlight}
