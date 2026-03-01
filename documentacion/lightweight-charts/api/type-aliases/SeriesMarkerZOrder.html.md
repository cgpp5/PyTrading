- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Type Aliases]{.breadcrumbs__link}
- [SeriesMarkerZOrder]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

# Type alias: SeriesMarkerZOrder

> **SeriesMarkerZOrder**: `"top"` \| `"aboveSeries"` \| `"normal"`

The visual stacking order for the markers within the chart.

- `normal`: Markers are drawn together with the series they belong to.
  They can appear below other series depending on the series stacking
  order.
- `aboveSeries`: Markers are drawn above all series but below primitives
  that use the \'top\' zOrder layer.
- `top`: Markers are drawn on the topmost primitive layer, above all
  series and (most) other primitives.
