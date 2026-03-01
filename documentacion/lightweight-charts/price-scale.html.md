- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Price scale]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Price scale

The **price scale** (or price axis) is a vertical scale that maps prices
to coordinates and vice versa. The conversion rules depend on the price
scale mode, the chart\'s height, and the visible part of the data.

![Price
scales](../assets/images/price-scales-5ff372fd08578f74710940c724ad5df4.png "Price scales"){.img_ev3q
decoding="async" loading="lazy" width="687" height="387"}

## Create price scale[​](price-scale.html#create-price-scale "Direct link to Create price scale"){.hash-link aria-label="Direct link to Create price scale"} {#create-price-scale .anchor .anchorWithStickyNavbar_LWe7}

By default, a chart has two visible price scales: left and right.
Additionally, you can create an unlimited number of overlay price
scales, which remain hidden in the UI. Overlay price scales allow series
to be plotted without affecting the existing visible scales. This is
particularly useful for indicators like Volume, where values can differ
significantly from price data.

To create an overlay price scale, assign
[`priceScaleId`](api/interfaces/SeriesOptionsCommon.html#pricescaleid)
to a series. Note that the `priceScaleId` value should differ from price
scale IDs on the left and right. The chart will create an overlay price
scale with the provided ID.

If a price scale with such ID already exists, a series will be attached
to the existing price scale. Further, you can use the provided price
scale ID to retrieve its API object using the
[`IChartApi.priceScale`](api/interfaces/IChartApi.html#pricescale)
method.

See the [Price and
Volume](https://tradingview.github.io/lightweight-charts/tutorials/how_to/price-and-volume)
article for an example of adding a Volume indicator using an overlay
price scale.

## Modify price scale[​](price-scale.html#modify-price-scale "Direct link to Modify price scale"){.hash-link aria-label="Direct link to Modify price scale"} {#modify-price-scale .anchor .anchorWithStickyNavbar_LWe7}

To modify the left price scale, use the
[`leftPriceScale`](api/interfaces/ChartOptionsBase.html#leftpricescale)
option. For the right price scale, use
[`rightPriceScale`](api/interfaces/ChartOptionsBase.html#rightpricescale).
To change the default settings for an overlay price scale, use the
[`overlayPriceScales`](api/interfaces/ChartOptionsBase.html#overlaypricescales)
option.

You can use the
[`IChartApi.priceScale`](api/interfaces/IChartApi.html#pricescale)
method to retrieve the API object for any price scale. Similarly, to
access the API object for the price scale that a series is attached to,
use the
[`ISeriesApi.priceScale`](api/interfaces/ISeriesApi.html#pricescale)
method.

## Remove price scale[​](price-scale.html#remove-price-scale "Direct link to Remove price scale"){.hash-link aria-label="Direct link to Remove price scale"} {#remove-price-scale .anchor .anchorWithStickyNavbar_LWe7}

The default left and right price scales cannot be removed, you can only
hide them by setting the
[`visible`](api/interfaces/PriceScaleOptions.html#visible) option to
`false`.

An overlay price scale exists as long as at least one series is attached
to it. To remove an overlay price scale, remove all series attached to
this price scale.

[](chart-types.html){.pagination-nav__link .pagination-nav__link--prev}

Previous

Chart types

[](time-scale.html){.pagination-nav__link .pagination-nav__link--next}

Next

Time scale

- [Create price
  scale](price-scale.html#create-price-scale){.table-of-contents__link
  .toc-highlight}
- [Modify price
  scale](price-scale.html#modify-price-scale){.table-of-contents__link
  .toc-highlight}
- [Remove price
  scale](price-scale.html#remove-price-scale){.table-of-contents__link
  .toc-highlight}
