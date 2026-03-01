- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [LayoutOptions]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: LayoutOptions

Represents layout options

## Properties[​](LayoutOptions.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### background[​](LayoutOptions.html#background "Direct link to background"){.hash-link aria-label="Direct link to background"} {#background .anchor .anchorWithStickyNavbar_LWe7}

> **background**: [`Background`](../type-aliases/Background.html)

Chart and scales background color.

#### Default Value[​](LayoutOptions.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`{ type: ColorType.Solid, color: '#FFFFFF' }`

------------------------------------------------------------------------

### textColor[​](LayoutOptions.html#textcolor "Direct link to textColor"){.hash-link aria-label="Direct link to textColor"} {#textcolor .anchor .anchorWithStickyNavbar_LWe7}

> **textColor**: `string`

Color of text on the scales.

#### Default Value[​](LayoutOptions.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

`'#191919'`

------------------------------------------------------------------------

### fontSize[​](LayoutOptions.html#fontsize "Direct link to fontSize"){.hash-link aria-label="Direct link to fontSize"} {#fontsize .anchor .anchorWithStickyNavbar_LWe7}

> **fontSize**: `number`

Font size of text on scales in pixels.

#### Default Value[​](LayoutOptions.html#default-value-2 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-2 .anchor .anchorWithStickyNavbar_LWe7}

`12`

------------------------------------------------------------------------

### fontFamily[​](LayoutOptions.html#fontfamily "Direct link to fontFamily"){.hash-link aria-label="Direct link to fontFamily"} {#fontfamily .anchor .anchorWithStickyNavbar_LWe7}

> **fontFamily**: `string`

Font family of text on the scales.

#### Default Value[​](LayoutOptions.html#default-value-3 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-3 .anchor .anchorWithStickyNavbar_LWe7}

`-apple-system, BlinkMacSystemFont, 'Trebuchet MS', Roboto, Ubuntu, sans-serif`

------------------------------------------------------------------------

### panes[​](LayoutOptions.html#panes "Direct link to panes"){.hash-link aria-label="Direct link to panes"} {#panes .anchor .anchorWithStickyNavbar_LWe7}

> **panes**: [`LayoutPanesOptions`](LayoutPanesOptions.html)

Panes options.

#### Default Value[​](LayoutOptions.html#default-value-4 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-4 .anchor .anchorWithStickyNavbar_LWe7}

`{ enableResize: true, separatorColor: '#2B2B43', separatorHoverColor: 'rgba(178, 181, 189, 0.2)'}`

------------------------------------------------------------------------

### attributionLogo[​](LayoutOptions.html#attributionlogo "Direct link to attributionLogo"){.hash-link aria-label="Direct link to attributionLogo"} {#attributionlogo .anchor .anchorWithStickyNavbar_LWe7}

> **attributionLogo**: `boolean`

Display the TradingView attribution logo on the main chart pane.

The licence for library specifies that you add the \"attribution
notice\" from the NOTICE file to your code and a link to
[https://www.tradingview.com/](https://www.tradingview.com/){target="_blank"
rel="noopener noreferrer"} to the page of your website or mobile
application that is available to your users. Using this attribution logo
is sufficient for meeting this linking requirement. However, if you
already fulfill this requirement then you can disable this attribution
logo.

#### Default Value[​](LayoutOptions.html#default-value-5 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-5 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
true
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### colorSpace[​](LayoutOptions.html#colorspace "Direct link to colorSpace"){.hash-link aria-label="Direct link to colorSpace"} {#colorspace .anchor .anchorWithStickyNavbar_LWe7}

> **colorSpace**: [`ColorSpace`](../type-aliases/ColorSpace.html)

Specifies the color space of the rendering context for the internal
canvas elements.

Note: this option should only be specified during the chart creation and
not changed at a later stage by using `applyOptions`.

#### Default Value[​](LayoutOptions.html#default-value-6 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-6 .anchor .anchorWithStickyNavbar_LWe7}

`srgb`

See [HTMLCanvasElement: getContext() method - Web APIs \|
MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext#colorspace){target="_blank"
rel="noopener noreferrer"} for more info

------------------------------------------------------------------------

### colorParsers[​](LayoutOptions.html#colorparsers "Direct link to colorParsers"){.hash-link aria-label="Direct link to colorParsers"} {#colorparsers .anchor .anchorWithStickyNavbar_LWe7}

> **colorParsers**:
> [`CustomColorParser`](../type-aliases/CustomColorParser.html)\[\]

Array of custom color parser functions to handle color formats outside
of standard sRGB values. Each parser function takes a string input and
should return either:

- An [Rgba](../type-aliases/Rgba.html) array \[r,g,b,a\] for valid
  colors (with values 0-255 for rgb and 0-1 for a)
- null if the parser cannot handle that color string, allowing the next
  parser to attempt it

Parsers are tried in order until one returns a non-null result. This
allows chaining multiple parsers to handle different color space
formats.

Note: this option should only be specified during the chart creation and
not changed at a later stage by using `applyOptions`.

The library already supports these color formats by default:

- Hex colors (#RGB, #RGBA, #RRGGBB, #RRGGBBAA)
- RGB/RGBA functions (rgb(), rgba())
- HSL/HSLA functions (hsl(), hsla())
- HWB function (hwb())
- Named colors (red, blue, etc.)
- \'transparent\' keyword

Custom parsers are only needed for other color spaces like:

- Display P3: color(display-p3 r g b)
- CIE Lab: lab(l a b)
- LCH: lch(l c h)
- Oklab: oklab(l a b)
- Oklch: oklch(l c h)
- \...

- [Properties](LayoutOptions.html#properties){.table-of-contents__link
  .toc-highlight}
  - [background](LayoutOptions.html#background){.table-of-contents__link
    .toc-highlight}
  - [textColor](LayoutOptions.html#textcolor){.table-of-contents__link
    .toc-highlight}
  - [fontSize](LayoutOptions.html#fontsize){.table-of-contents__link
    .toc-highlight}
  - [fontFamily](LayoutOptions.html#fontfamily){.table-of-contents__link
    .toc-highlight}
  - [panes](LayoutOptions.html#panes){.table-of-contents__link
    .toc-highlight}
  - [attributionLogo](LayoutOptions.html#attributionlogo){.table-of-contents__link
    .toc-highlight}
  - [colorSpace](LayoutOptions.html#colorspace){.table-of-contents__link
    .toc-highlight}
  - [colorParsers](LayoutOptions.html#colorparsers){.table-of-contents__link
    .toc-highlight}
