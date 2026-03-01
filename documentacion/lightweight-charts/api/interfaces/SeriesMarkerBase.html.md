- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [SeriesMarkerBase]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: SeriesMarkerBase\<TimeType\>

Represents a series marker.

## Extended by[​](SeriesMarkerBase.html#extended-by "Direct link to Extended by"){.hash-link aria-label="Direct link to Extended by"} {#extended-by .anchor .anchorWithStickyNavbar_LWe7}

- [`SeriesMarkerBar`](SeriesMarkerBar.html)
- [`SeriesMarkerPrice`](SeriesMarkerPrice.html)

## Type parameters[​](SeriesMarkerBase.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **TimeType**

## Properties[​](SeriesMarkerBase.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### time[​](SeriesMarkerBase.html#time "Direct link to time"){.hash-link aria-label="Direct link to time"} {#time .anchor .anchorWithStickyNavbar_LWe7}

> **time**: `TimeType`

The time of the marker.

------------------------------------------------------------------------

### position[​](SeriesMarkerBase.html#position "Direct link to position"){.hash-link aria-label="Direct link to position"} {#position .anchor .anchorWithStickyNavbar_LWe7}

> **position**:
> [`SeriesMarkerPosition`](../type-aliases/SeriesMarkerPosition.html)

The position of the marker.

------------------------------------------------------------------------

### shape[​](SeriesMarkerBase.html#shape "Direct link to shape"){.hash-link aria-label="Direct link to shape"} {#shape .anchor .anchorWithStickyNavbar_LWe7}

> **shape**:
> [`SeriesMarkerShape`](../type-aliases/SeriesMarkerShape.html)

The shape of the marker.

------------------------------------------------------------------------

### color[​](SeriesMarkerBase.html#color "Direct link to color"){.hash-link aria-label="Direct link to color"} {#color .anchor .anchorWithStickyNavbar_LWe7}

> **color**: `string`

The color of the marker.

------------------------------------------------------------------------

### id?[​](SeriesMarkerBase.html#id "Direct link to id?"){.hash-link aria-label="Direct link to id?"} {#id .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **id**: `string`

The ID of the marker.

------------------------------------------------------------------------

### text?[​](SeriesMarkerBase.html#text "Direct link to text?"){.hash-link aria-label="Direct link to text?"} {#text .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **text**: `string`

The optional text of the marker.

------------------------------------------------------------------------

### size?[​](SeriesMarkerBase.html#size "Direct link to size?"){.hash-link aria-label="Direct link to size?"} {#size .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **size**: `number`

The optional size of the marker.

#### Default Value[​](SeriesMarkerBase.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`1`

------------------------------------------------------------------------

### price?[​](SeriesMarkerBase.html#price "Direct link to price?"){.hash-link aria-label="Direct link to price?"} {#price .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **price**: `number`

The price value for exact Y-axis positioning.

Required when using
[SeriesMarkerPricePosition](../type-aliases/SeriesMarkerPricePosition.html)
position type.

- [Extended
  by](SeriesMarkerBase.html#extended-by){.table-of-contents__link
  .toc-highlight}
- [Type
  parameters](SeriesMarkerBase.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](SeriesMarkerBase.html#properties){.table-of-contents__link
  .toc-highlight}
  - [time](SeriesMarkerBase.html#time){.table-of-contents__link
    .toc-highlight}
  - [position](SeriesMarkerBase.html#position){.table-of-contents__link
    .toc-highlight}
  - [shape](SeriesMarkerBase.html#shape){.table-of-contents__link
    .toc-highlight}
  - [color](SeriesMarkerBase.html#color){.table-of-contents__link
    .toc-highlight}
  - [id?](SeriesMarkerBase.html#id){.table-of-contents__link
    .toc-highlight}
  - [text?](SeriesMarkerBase.html#text){.table-of-contents__link
    .toc-highlight}
  - [size?](SeriesMarkerBase.html#size){.table-of-contents__link
    .toc-highlight}
  - [price?](SeriesMarkerBase.html#price){.table-of-contents__link
    .toc-highlight}
