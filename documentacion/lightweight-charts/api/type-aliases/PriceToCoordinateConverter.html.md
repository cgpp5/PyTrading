- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Type Aliases]{.breadcrumbs__link}
- [PriceToCoordinateConverter]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Type alias: PriceToCoordinateConverter()

> **PriceToCoordinateConverter**: (`price`) =\>
> [`Coordinate`](Coordinate.html) \| `null`

Converter function for changing prices into vertical coordinate values.

This is provided as a convenience function since the series original
data will most likely be defined in price values, and the renderer needs
to draw with coordinates. This returns the same values as directly using
the series\' priceToCoordinate method.

## Parameters[​](PriceToCoordinateConverter.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **price**: `number`

## Returns[​](PriceToCoordinateConverter.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

[`Coordinate`](Coordinate.html) \| `null`

- [Parameters](PriceToCoordinateConverter.html#parameters){.table-of-contents__link
  .toc-highlight}
- [Returns](PriceToCoordinateConverter.html#returns){.table-of-contents__link
  .toc-highlight}
