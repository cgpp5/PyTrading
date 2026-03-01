- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Type Aliases]{.breadcrumbs__link}
- [TickMarkFormatter]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Type alias: TickMarkFormatter()

> **TickMarkFormatter**: (`time`, `tickMarkType`, `locale`) =\> `string`
> \| `null`

The `TickMarkFormatter` is used to customize tick mark labels on the
time scale.

This function should return `time` as a string formatted according to
`tickMarkType` type (year, month, etc) and `locale`.

Note that the returned string should be the shortest possible value and
should have no more than 8 characters. Otherwise, the tick marks will
overlap each other.

If the formatter function returns `null` then the default tick mark
formatter will be used as a fallback.

## Example[​](TickMarkFormatter.html#example "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const customFormatter = (time, tickMarkType, locale) => {
    // your code here
};
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

## Parameters[​](TickMarkFormatter.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **time**: [`Time`](Time.html)

• **tickMarkType**: [`TickMarkType`](../enumerations/TickMarkType.html)

• **locale**: `string`

## Returns[​](TickMarkFormatter.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`string` \| `null`

- [Example](TickMarkFormatter.html#example){.table-of-contents__link
  .toc-highlight}
- [Parameters](TickMarkFormatter.html#parameters){.table-of-contents__link
  .toc-highlight}
- [Returns](TickMarkFormatter.html#returns){.table-of-contents__link
  .toc-highlight}
