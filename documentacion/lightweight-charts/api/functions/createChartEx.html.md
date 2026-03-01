- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Functions]{.breadcrumbs__link}
- [createChartEx]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Function: createChartEx()

> **createChartEx**\<`HorzScaleItem`,
> `THorzScaleBehavior`\>(`container`, `horzScaleBehavior`, `options`?):
> [`IChartApiBase`](../interfaces/IChartApiBase.html)\<`HorzScaleItem`\>

This function is the main entry point of the Lightweight Charting
Library. If you are using time values for the horizontal scale then it
is recommended that you rather use the [createChart](createChart.html)
function.

## Type parameters[​](createChartEx.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem**

type of points on the horizontal scale

• **THorzScaleBehavior** *extends*
[`IHorzScaleBehavior`](../interfaces/IHorzScaleBehavior.html)\<`HorzScaleItem`\>

type of horizontal axis strategy that encapsulate all the specific
behaviors of the horizontal scale type

## Parameters[​](createChartEx.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **container**: `string` \| `HTMLElement`

ID of HTML element or element itself

• **horzScaleBehavior**: `THorzScaleBehavior`

Horizontal scale behavior

• **options?**:
[`DeepPartial`](../type-aliases/DeepPartial.html)\<`ReturnType`\<`THorzScaleBehavior`\[`"options"`\]\>\>

Any subset of options to be applied at start.

## Returns[​](createChartEx.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

[`IChartApiBase`](../interfaces/IChartApiBase.html)\<`HorzScaleItem`\>

An interface to the created chart

- [Type
  parameters](createChartEx.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Parameters](createChartEx.html#parameters){.table-of-contents__link
  .toc-highlight}
- [Returns](createChartEx.html#returns){.table-of-contents__link
  .toc-highlight}
