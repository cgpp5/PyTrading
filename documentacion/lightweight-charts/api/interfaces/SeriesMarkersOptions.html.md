- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [SeriesMarkersOptions]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: SeriesMarkersOptions

Configuration options for the series markers plugin. These options
affect all markers managed by the plugin.

## Properties[​](SeriesMarkersOptions.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### autoScale[​](SeriesMarkersOptions.html#autoscale "Direct link to autoScale"){.hash-link aria-label="Direct link to autoScale"} {#autoscale .anchor .anchorWithStickyNavbar_LWe7}

> **autoScale**: `boolean`

Specifies whether the auto-scaling calculation should expand to include
the size of markers.

When `true`, the auto-scale feature will adjust the price scale\'s range
to ensure series markers are fully visible and not cropped by the
chart\'s edges.

When `false`, the scale will only fit the series data points, which may
cause markers to be partially hidden.

Note: This option only has an effect when auto-scaling is enabled for
the price scale.

#### Default Value[​](SeriesMarkersOptions.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`true`

------------------------------------------------------------------------

### zOrder[​](SeriesMarkersOptions.html#zorder "Direct link to zOrder"){.hash-link aria-label="Direct link to zOrder"} {#zorder .anchor .anchorWithStickyNavbar_LWe7}

> **zOrder**:
> [`SeriesMarkerZOrder`](../type-aliases/SeriesMarkerZOrder.html)

Defines the stacking order of the markers relative to the series and
other primitives.

#### Default Value[​](SeriesMarkersOptions.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

`normal`

- [Properties](SeriesMarkersOptions.html#properties){.table-of-contents__link
  .toc-highlight}
  - [autoScale](SeriesMarkersOptions.html#autoscale){.table-of-contents__link
    .toc-highlight}
  - [zOrder](SeriesMarkersOptions.html#zorder){.table-of-contents__link
    .toc-highlight}
