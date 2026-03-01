- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [YieldCurveOptions]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: YieldCurveOptions

Options specific to yield curve charts.

## Properties[​](YieldCurveOptions.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### baseResolution[​](YieldCurveOptions.html#baseresolution "Direct link to baseResolution"){.hash-link aria-label="Direct link to baseResolution"} {#baseresolution .anchor .anchorWithStickyNavbar_LWe7}

> **baseResolution**: `number`

The smallest time unit for the yield curve, typically representing one
month. This value determines the granularity of the time scale.

#### Default Value[​](YieldCurveOptions.html#default-value "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
1
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### minimumTimeRange[​](YieldCurveOptions.html#minimumtimerange "Direct link to minimumTimeRange"){.hash-link aria-label="Direct link to minimumTimeRange"} {#minimumtimerange .anchor .anchorWithStickyNavbar_LWe7}

> **minimumTimeRange**: `number`

The minimum time range to be displayed on the chart, in units of
baseResolution. This ensures that the chart always shows at least this
much time range, even if there\'s less data.

#### Default Value[​](YieldCurveOptions.html#default-value-1 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-1 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
120 (10 years)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### startTimeRange[​](YieldCurveOptions.html#starttimerange "Direct link to startTimeRange"){.hash-link aria-label="Direct link to startTimeRange"} {#starttimerange .anchor .anchorWithStickyNavbar_LWe7}

> **startTimeRange**: `number`

The starting time value for the chart, in units of baseResolution. This
determines where the time scale begins.

#### Default Value[​](YieldCurveOptions.html#default-value-2 "Direct link to Default Value"){.hash-link aria-label="Direct link to Default Value"} {#default-value-2 .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-ts .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
0
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

------------------------------------------------------------------------

### formatTime()?[​](YieldCurveOptions.html#formattime "Direct link to formatTime()?"){.hash-link aria-label="Direct link to formatTime()?"} {#formattime .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **formatTime**: (`months`) =\> `string`

Optional custom formatter for time values on the horizontal axis. If not
provided, a default formatter will be used.

#### Parameters[​](YieldCurveOptions.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **months**: `number`

The number of months (or baseResolution units) to format

#### Returns[​](YieldCurveOptions.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`string`

- [Properties](YieldCurveOptions.html#properties){.table-of-contents__link
  .toc-highlight}
  - [baseResolution](YieldCurveOptions.html#baseresolution){.table-of-contents__link
    .toc-highlight}
  - [minimumTimeRange](YieldCurveOptions.html#minimumtimerange){.table-of-contents__link
    .toc-highlight}
  - [startTimeRange](YieldCurveOptions.html#starttimerange){.table-of-contents__link
    .toc-highlight}
  - [formatTime()?](YieldCurveOptions.html#formattime){.table-of-contents__link
    .toc-highlight}
