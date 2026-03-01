- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [PriceFormatBuiltIn]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: PriceFormatBuiltIn

Represents series value formatting options. The precision and minMove
properties allow wide customization of formatting.

## Examples[​](PriceFormatBuiltIn.html#examples "Direct link to Examples"){.hash-link aria-label="Direct link to Examples"} {#examples .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
`minMove=0.01`, `precision` is not specified - prices will change like 1.13, 1.14, 1.15 etc.
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
`minMove=0.01`, `precision=3` - prices will change like 1.130, 1.140, 1.150 etc.
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
`minMove=0.05`, `precision` is not specified - prices will change like 1.10, 1.15, 1.20 etc.
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

## Properties[​](PriceFormatBuiltIn.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### type[​](PriceFormatBuiltIn.html#type "Direct link to type"){.hash-link aria-label="Direct link to type"} {#type .anchor .anchorWithStickyNavbar_LWe7}

> **type**: `"percent"` \| `"price"` \| `"volume"`

Built-in price formats:

- `'price'` is the most common choice; it allows customization of
  precision and rounding of prices.
- `'volume'` uses abbreviation for formatting prices like `1.2K` or
  `12.67M`.
- `'percent'` uses `%` sign at the end of prices.

------------------------------------------------------------------------

### precision[​](PriceFormatBuiltIn.html#precision "Direct link to precision"){.hash-link aria-label="Direct link to precision"} {#precision .anchor .anchorWithStickyNavbar_LWe7}

> **precision**: `number`

Number of digits after the decimal point. If it is not set, then its
value is calculated automatically based on minMove.

#### Default Value[​](PriceFormatBuiltIn.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

`2` if both [minMove](PriceFormatBuiltIn.html#minmove) and
[precision](PriceFormatBuiltIn.html#precision) are not provided,
calculated automatically based on
[minMove](PriceFormatBuiltIn.html#minmove) otherwise.

------------------------------------------------------------------------

### minMove[​](PriceFormatBuiltIn.html#minmove "Direct link to minMove"){.hash-link aria-label="Direct link to minMove"} {#minmove .anchor .anchorWithStickyNavbar_LWe7}

> **minMove**: `number`

The minimum possible step size for price value movement. This value
shouldn\'t have more decimal digits than the precision.

#### Default Value[​](PriceFormatBuiltIn.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

`0.01`

------------------------------------------------------------------------

### base?[​](PriceFormatBuiltIn.html#base "Direct link to base?"){.hash-link aria-label="Direct link to base?"} {#base .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **base**: `number`

The base value for the price format. It should equal to 1 /
[minMove](PriceFormatBuiltIn.html#minmove). If this option is specified,
we ignore the [minMove](PriceFormatBuiltIn.html#minmove) option. It can
be useful for cases with very small price movements like `1e-18` where
we can reach limitations of floating point precision.

- [Examples](PriceFormatBuiltIn.html#examples){.table-of-contents__link
  .toc-highlight}
- [Properties](PriceFormatBuiltIn.html#properties){.table-of-contents__link
  .toc-highlight}
  - [type](PriceFormatBuiltIn.html#type){.table-of-contents__link
    .toc-highlight}
  - [precision](PriceFormatBuiltIn.html#precision){.table-of-contents__link
    .toc-highlight}
  - [minMove](PriceFormatBuiltIn.html#minmove){.table-of-contents__link
    .toc-highlight}
  - [base?](PriceFormatBuiltIn.html#base){.table-of-contents__link
    .toc-highlight}
