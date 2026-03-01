- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [SeriesAttachedParameter]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: SeriesAttachedParameter\<HorzScaleItem, TSeriesType\>

Object containing references to the chart and series instances, and a
requestUpdate method for triggering a refresh of the chart.

## Type parameters[​](SeriesAttachedParameter.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem** = [`Time`](../type-aliases/Time.html)

• **TSeriesType** *extends*
[`SeriesType`](../type-aliases/SeriesType.html) = keyof
[`SeriesOptionsMap`](SeriesOptionsMap.html)

## Properties[​](SeriesAttachedParameter.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### chart[​](SeriesAttachedParameter.html#chart "Direct link to chart"){.hash-link aria-label="Direct link to chart"} {#chart .anchor .anchorWithStickyNavbar_LWe7}

> **chart**: [`IChartApiBase`](IChartApiBase.html)\<`HorzScaleItem`\>

Chart instance.

------------------------------------------------------------------------

### series[​](SeriesAttachedParameter.html#series "Direct link to series"){.hash-link aria-label="Direct link to series"} {#series .anchor .anchorWithStickyNavbar_LWe7}

> **series**: [`ISeriesApi`](ISeriesApi.html)\<`TSeriesType`,
> `HorzScaleItem`,
> [`SeriesDataItemTypeMap`](SeriesDataItemTypeMap.html)\<`HorzScaleItem`\>\[`TSeriesType`\],
> [`SeriesOptionsMap`](SeriesOptionsMap.html)\[`TSeriesType`\],
> [`SeriesPartialOptionsMap`](SeriesPartialOptionsMap.html)\[`TSeriesType`\]\>

Series to which the Primitive is attached.

------------------------------------------------------------------------

### requestUpdate()[​](SeriesAttachedParameter.html#requestupdate "Direct link to requestUpdate()"){.hash-link aria-label="Direct link to requestUpdate()"} {#requestupdate .anchor .anchorWithStickyNavbar_LWe7}

> **requestUpdate**: () =\> `void`

Request an update (redraw the chart)

#### Returns[​](SeriesAttachedParameter.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### horzScaleBehavior[​](SeriesAttachedParameter.html#horzscalebehavior "Direct link to horzScaleBehavior"){.hash-link aria-label="Direct link to horzScaleBehavior"} {#horzscalebehavior .anchor .anchorWithStickyNavbar_LWe7}

> **horzScaleBehavior**:
> [`IHorzScaleBehavior`](IHorzScaleBehavior.html)\<`HorzScaleItem`\>

Horizontal Scale Behaviour for the chart.

- [Type
  parameters](SeriesAttachedParameter.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](SeriesAttachedParameter.html#properties){.table-of-contents__link
  .toc-highlight}
  - [chart](SeriesAttachedParameter.html#chart){.table-of-contents__link
    .toc-highlight}
  - [series](SeriesAttachedParameter.html#series){.table-of-contents__link
    .toc-highlight}
  - [requestUpdate()](SeriesAttachedParameter.html#requestupdate){.table-of-contents__link
    .toc-highlight}
  - [horzScaleBehavior](SeriesAttachedParameter.html#horzscalebehavior){.table-of-contents__link
    .toc-highlight}
