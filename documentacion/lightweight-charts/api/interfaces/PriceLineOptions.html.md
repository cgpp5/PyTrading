- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [PriceLineOptions]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: PriceLineOptions

Represents a price line options.

## Properties[​](PriceLineOptions.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### id?[​](PriceLineOptions.html#id "Direct link to id?"){.hash-link aria-label="Direct link to id?"} {#id .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **id**: `string`

The optional ID of this price line.

------------------------------------------------------------------------

### price[​](PriceLineOptions.html#price "Direct link to price"){.hash-link aria-label="Direct link to price"} {#price .anchor .anchorWithStickyNavbar_LWe7}

> **price**: `number`

Price line\'s value.

#### Default Value[​](PriceLineOptions.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`0`

------------------------------------------------------------------------

### color[​](PriceLineOptions.html#color "Direct link to color"){.hash-link aria-label="Direct link to color"} {#color .anchor .anchorWithStickyNavbar_LWe7}

> **color**: `string`

Price line\'s color.

#### Default Value[​](PriceLineOptions.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

`''`

------------------------------------------------------------------------

### lineWidth[​](PriceLineOptions.html#linewidth "Direct link to lineWidth"){.hash-link aria-label="Direct link to lineWidth"} {#linewidth .anchor .anchorWithStickyNavbar_LWe7}

> **lineWidth**: [`LineWidth`](../type-aliases/LineWidth.html)

Price line\'s width in pixels.

#### Default Value[​](PriceLineOptions.html#default-value-2 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-2 .anchor .anchorWithStickyNavbar_LWe7}

`1`

------------------------------------------------------------------------

### lineStyle[​](PriceLineOptions.html#linestyle "Direct link to lineStyle"){.hash-link aria-label="Direct link to lineStyle"} {#linestyle .anchor .anchorWithStickyNavbar_LWe7}

> **lineStyle**: [`LineStyle`](../enumerations/LineStyle.html)

Price line\'s style.

#### Default Value[​](PriceLineOptions.html#default-value-3 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-3 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
{@link LineStyle.Solid}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### lineVisible[​](PriceLineOptions.html#linevisible "Direct link to lineVisible"){.hash-link aria-label="Direct link to lineVisible"} {#linevisible .anchor .anchorWithStickyNavbar_LWe7}

> **lineVisible**: `boolean`

Display line.

#### Default Value[​](PriceLineOptions.html#default-value-4 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-4 .anchor .anchorWithStickyNavbar_LWe7}

`true`

------------------------------------------------------------------------

### axisLabelVisible[​](PriceLineOptions.html#axislabelvisible "Direct link to axisLabelVisible"){.hash-link aria-label="Direct link to axisLabelVisible"} {#axislabelvisible .anchor .anchorWithStickyNavbar_LWe7}

> **axisLabelVisible**: `boolean`

Display the current price value in on the price scale.

#### Default Value[​](PriceLineOptions.html#default-value-5 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-5 .anchor .anchorWithStickyNavbar_LWe7}

`true`

------------------------------------------------------------------------

### title[​](PriceLineOptions.html#title "Direct link to title"){.hash-link aria-label="Direct link to title"} {#title .anchor .anchorWithStickyNavbar_LWe7}

> **title**: `string`

Price line\'s on the chart pane.

#### Default Value[​](PriceLineOptions.html#default-value-6 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-6 .anchor .anchorWithStickyNavbar_LWe7}

`''`

------------------------------------------------------------------------

### axisLabelColor[​](PriceLineOptions.html#axislabelcolor "Direct link to axisLabelColor"){.hash-link aria-label="Direct link to axisLabelColor"} {#axislabelcolor .anchor .anchorWithStickyNavbar_LWe7}

> **axisLabelColor**: `string`

Background color for the axis label. Will default to the price line
color if unspecified.

#### Default Value[​](PriceLineOptions.html#default-value-7 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-7 .anchor .anchorWithStickyNavbar_LWe7}

`''`

------------------------------------------------------------------------

### axisLabelTextColor[​](PriceLineOptions.html#axislabeltextcolor "Direct link to axisLabelTextColor"){.hash-link aria-label="Direct link to axisLabelTextColor"} {#axislabeltextcolor .anchor .anchorWithStickyNavbar_LWe7}

> **axisLabelTextColor**: `string`

Text color for the axis label.

#### Default Value[​](PriceLineOptions.html#default-value-8 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-8 .anchor .anchorWithStickyNavbar_LWe7}

`''`

- [Properties](PriceLineOptions.html#properties){.table-of-contents__link
  .toc-highlight}
  - [id?](PriceLineOptions.html#id){.table-of-contents__link
    .toc-highlight}
  - [price](PriceLineOptions.html#price){.table-of-contents__link
    .toc-highlight}
  - [color](PriceLineOptions.html#color){.table-of-contents__link
    .toc-highlight}
  - [lineWidth](PriceLineOptions.html#linewidth){.table-of-contents__link
    .toc-highlight}
  - [lineStyle](PriceLineOptions.html#linestyle){.table-of-contents__link
    .toc-highlight}
  - [lineVisible](PriceLineOptions.html#linevisible){.table-of-contents__link
    .toc-highlight}
  - [axisLabelVisible](PriceLineOptions.html#axislabelvisible){.table-of-contents__link
    .toc-highlight}
  - [title](PriceLineOptions.html#title){.table-of-contents__link
    .toc-highlight}
  - [axisLabelColor](PriceLineOptions.html#axislabelcolor){.table-of-contents__link
    .toc-highlight}
  - [axisLabelTextColor](PriceLineOptions.html#axislabeltextcolor){.table-of-contents__link
    .toc-highlight}
