- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [BarsInfo]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: BarsInfo\<HorzScaleItem\>

Represents a range of bars and the number of bars outside the range.

## Extends[​](BarsInfo.html#extends "Direct link to Extends"){.hash-link aria-label="Direct link to Extends"} {#extends .anchor .anchorWithStickyNavbar_LWe7}

- `Partial` \<[`IRange`](IRange.html)\<`HorzScaleItem`\>\>

## Type parameters[​](BarsInfo.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **HorzScaleItem**

## Properties[​](BarsInfo.html#properties "Direct link to Properties"){.hash-link aria-label="Direct link to Properties"} {#properties .anchor .anchorWithStickyNavbar_LWe7}

### barsBefore[​](BarsInfo.html#barsbefore "Direct link to barsBefore"){.hash-link aria-label="Direct link to barsBefore"} {#barsbefore .anchor .anchorWithStickyNavbar_LWe7}

> **barsBefore**: `number`

The number of bars before the start of the range. Positive value means
that there are some bars before (out of logical range from the left) the
[IRange.from](IRange.html#from) logical index in the series. Negative
value means that the first series\' bar is inside the passed logical
range, and between the first series\' bar and the
[IRange.from](IRange.html#from) logical index are some bars.

------------------------------------------------------------------------

### barsAfter[​](BarsInfo.html#barsafter "Direct link to barsAfter"){.hash-link aria-label="Direct link to barsAfter"} {#barsafter .anchor .anchorWithStickyNavbar_LWe7}

> **barsAfter**: `number`

The number of bars after the end of the range. Positive value in the
`barsAfter` field means that there are some bars after (out of logical
range from the right) the [IRange.to](IRange.html#to) logical index in
the series. Negative value means that the last series\' bar is inside
the passed logical range, and between the last series\' bar and the
[IRange.to](IRange.html#to) logical index are some bars.

------------------------------------------------------------------------

### from?[​](BarsInfo.html#from "Direct link to from?"){.hash-link aria-label="Direct link to from?"} {#from .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **from**: `HorzScaleItem`

The from value. The start of the range.

#### Inherited from[​](BarsInfo.html#inherited-from "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from .anchor .anchorWithStickyNavbar_LWe7}

`Partial.from`

------------------------------------------------------------------------

### to?[​](BarsInfo.html#to "Direct link to to?"){.hash-link aria-label="Direct link to to?"} {#to .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **to**: `HorzScaleItem`

The to value. The end of the range.

#### Inherited from[​](BarsInfo.html#inherited-from-1 "Direct link to Inherited from"){.hash-link aria-label="Direct link to Inherited from"} {#inherited-from-1 .anchor .anchorWithStickyNavbar_LWe7}

`Partial.to`

- [Extends](BarsInfo.html#extends){.table-of-contents__link
  .toc-highlight}
- [Type
  parameters](BarsInfo.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Properties](BarsInfo.html#properties){.table-of-contents__link
  .toc-highlight}
  - [barsBefore](BarsInfo.html#barsbefore){.table-of-contents__link
    .toc-highlight}
  - [barsAfter](BarsInfo.html#barsafter){.table-of-contents__link
    .toc-highlight}
  - [from?](BarsInfo.html#from){.table-of-contents__link .toc-highlight}
  - [to?](BarsInfo.html#to){.table-of-contents__link .toc-highlight}
