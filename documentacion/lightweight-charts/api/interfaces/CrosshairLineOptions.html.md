- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [CrosshairLineOptions]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: CrosshairLineOptions

Structure describing a crosshair line (vertical or horizontal)

## Properties[​](CrosshairLineOptions.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### color[​](CrosshairLineOptions.html#color "Direct link to color"){.hash-link aria-label="Direct link to color"} {#color .anchor .anchorWithStickyNavbar_LWe7}

> **color**: `string`

Crosshair line color.

#### Default Value[​](CrosshairLineOptions.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`'#758696'`

------------------------------------------------------------------------

### width[​](CrosshairLineOptions.html#width "Direct link to width"){.hash-link aria-label="Direct link to width"} {#width .anchor .anchorWithStickyNavbar_LWe7}

> **width**: [`LineWidth`](../type-aliases/LineWidth.html)

Crosshair line width.

#### Default Value[​](CrosshairLineOptions.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

`1`

------------------------------------------------------------------------

### style[​](CrosshairLineOptions.html#style "Direct link to style"){.hash-link aria-label="Direct link to style"} {#style .anchor .anchorWithStickyNavbar_LWe7}

> **style**: [`LineStyle`](../enumerations/LineStyle.html)

Crosshair line style.

#### Default Value[​](CrosshairLineOptions.html#default-value-2 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-2 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
{@link LineStyle.LargeDashed}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### visible[​](CrosshairLineOptions.html#visible "Direct link to visible"){.hash-link aria-label="Direct link to visible"} {#visible .anchor .anchorWithStickyNavbar_LWe7}

> **visible**: `boolean`

Display the crosshair line.

Note that disabling crosshair lines does not disable crosshair marker on
Line and Area series. It can be disabled by using
`crosshairMarkerVisible` option of a relevant series.

#### See[​](CrosshairLineOptions.html#see "Direct link to See"){.hash-link aria-label="Direct link to See"} {#see .anchor .anchorWithStickyNavbar_LWe7}

- [LineStyleOptions.crosshairMarkerVisible](LineStyleOptions.html#crosshairmarkervisible)
- [AreaStyleOptions.crosshairMarkerVisible](AreaStyleOptions.html#crosshairmarkervisible)
- [BaselineStyleOptions.crosshairMarkerVisible](BaselineStyleOptions.html#crosshairmarkervisible)

#### Default Value[​](CrosshairLineOptions.html#default-value-3 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-3 .anchor .anchorWithStickyNavbar_LWe7}

`true`

------------------------------------------------------------------------

### labelVisible[​](CrosshairLineOptions.html#labelvisible "Direct link to labelVisible"){.hash-link aria-label="Direct link to labelVisible"} {#labelvisible .anchor .anchorWithStickyNavbar_LWe7}

> **labelVisible**: `boolean`

Display the crosshair label on the relevant scale.

#### Default Value[​](CrosshairLineOptions.html#default-value-4 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-4 .anchor .anchorWithStickyNavbar_LWe7}

`true`

------------------------------------------------------------------------

### labelBackgroundColor[​](CrosshairLineOptions.html#labelbackgroundcolor "Direct link to labelBackgroundColor"){.hash-link aria-label="Direct link to labelBackgroundColor"} {#labelbackgroundcolor .anchor .anchorWithStickyNavbar_LWe7}

> **labelBackgroundColor**: `string`

Crosshair label background color.

#### Default Value[​](CrosshairLineOptions.html#default-value-5 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-5 .anchor .anchorWithStickyNavbar_LWe7}

`'#4c525e'`

- [Properties](CrosshairLineOptions.html#properties){.table-of-contents__link
  .toc-highlight}
  - [color](CrosshairLineOptions.html#color){.table-of-contents__link
    .toc-highlight}
  - [width](CrosshairLineOptions.html#width){.table-of-contents__link
    .toc-highlight}
  - [style](CrosshairLineOptions.html#style){.table-of-contents__link
    .toc-highlight}
  - [visible](CrosshairLineOptions.html#visible){.table-of-contents__link
    .toc-highlight}
  - [labelVisible](CrosshairLineOptions.html#labelvisible){.table-of-contents__link
    .toc-highlight}
  - [labelBackgroundColor](CrosshairLineOptions.html#labelbackgroundcolor){.table-of-contents__link
    .toc-highlight}
