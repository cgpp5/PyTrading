- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [ISeriesPrimitiveAxisView]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: ISeriesPrimitiveAxisView

This interface represents a label on the price or time axis

## Methods[​](ISeriesPrimitiveAxisView.html#methods "Direct link to Methods"){.hash-link aria-label="Direct link to Methods"} {#methods .anchor .anchorWithStickyNavbar_LWe7}

### coordinate()[​](ISeriesPrimitiveAxisView.html#coordinate "Direct link to coordinate()"){.hash-link aria-label="Direct link to coordinate()"} {#coordinate .anchor .anchorWithStickyNavbar_LWe7}

> **coordinate**(): `number`

The desired coordinate for the label. Note that the label will be
automatically moved to prevent overlapping with other labels. If you
would like the label to be drawn at the exact coordinate under all
circumstances then rather use `fixedCoordinate`. For a price axis the
value returned will represent the vertical distance (pixels) from the
top. For a time axis the value will represent the horizontal distance
from the left.

#### Returns[​](ISeriesPrimitiveAxisView.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`number`

coordinate. distance from top for price axis, or distance from left for
time axis.

------------------------------------------------------------------------

### fixedCoordinate()?[​](ISeriesPrimitiveAxisView.html#fixedcoordinate "Direct link to fixedCoordinate()?"){.hash-link aria-label="Direct link to fixedCoordinate()?"} {#fixedcoordinate .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **fixedCoordinate**(): `number`

fixed coordinate of the label. A label with a fixed coordinate value
will always be drawn at the specified coordinate and will appear above
any \'unfixed\' labels. If you supply a fixed coordinate then you should
return a large negative number for `coordinate` so that the automatic
placement of unfixed labels doesn\'t leave a blank space for this label.
For a price axis the value returned will represent the vertical distance
(pixels) from the top. For a time axis the value will represent the
horizontal distance from the left.

#### Returns[​](ISeriesPrimitiveAxisView.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

`number`

coordinate. distance from top for price axis, or distance from left for
time axis.

------------------------------------------------------------------------

### text()[​](ISeriesPrimitiveAxisView.html#text "Direct link to text()"){.hash-link aria-label="Direct link to text()"} {#text .anchor .anchorWithStickyNavbar_LWe7}

> **text**(): `string`

#### Returns[​](ISeriesPrimitiveAxisView.html#returns-2 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-2 .anchor .anchorWithStickyNavbar_LWe7}

`string`

text of the label

------------------------------------------------------------------------

### textColor()[​](ISeriesPrimitiveAxisView.html#textcolor "Direct link to textColor()"){.hash-link aria-label="Direct link to textColor()"} {#textcolor .anchor .anchorWithStickyNavbar_LWe7}

> **textColor**(): `string`

#### Returns[​](ISeriesPrimitiveAxisView.html#returns-3 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-3 .anchor .anchorWithStickyNavbar_LWe7}

`string`

text color of the label

------------------------------------------------------------------------

### backColor()[​](ISeriesPrimitiveAxisView.html#backcolor "Direct link to backColor()"){.hash-link aria-label="Direct link to backColor()"} {#backcolor .anchor .anchorWithStickyNavbar_LWe7}

> **backColor**(): `string`

#### Returns[​](ISeriesPrimitiveAxisView.html#returns-4 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-4 .anchor .anchorWithStickyNavbar_LWe7}

`string`

background color of the label

------------------------------------------------------------------------

### visible()?[​](ISeriesPrimitiveAxisView.html#visible "Direct link to visible()?"){.hash-link aria-label="Direct link to visible()?"} {#visible .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **visible**(): `boolean`

#### Returns[​](ISeriesPrimitiveAxisView.html#returns-5 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-5 .anchor .anchorWithStickyNavbar_LWe7}

`boolean`

whether the label should be visible (default: `true`)

------------------------------------------------------------------------

### tickVisible()?[​](ISeriesPrimitiveAxisView.html#tickvisible "Direct link to tickVisible()?"){.hash-link aria-label="Direct link to tickVisible()?"} {#tickvisible .anchor .anchorWithStickyNavbar_LWe7}

> `optional` **tickVisible**(): `boolean`

#### Returns[​](ISeriesPrimitiveAxisView.html#returns-6 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-6 .anchor .anchorWithStickyNavbar_LWe7}

`boolean`

whether the tick mark line should be visible (default: `true`)

- [Methods](ISeriesPrimitiveAxisView.html#methods){.table-of-contents__link
  .toc-highlight}
  - [coordinate()](ISeriesPrimitiveAxisView.html#coordinate){.table-of-contents__link
    .toc-highlight}
  - [fixedCoordinate()?](ISeriesPrimitiveAxisView.html#fixedcoordinate){.table-of-contents__link
    .toc-highlight}
  - [text()](ISeriesPrimitiveAxisView.html#text){.table-of-contents__link
    .toc-highlight}
  - [textColor()](ISeriesPrimitiveAxisView.html#textcolor){.table-of-contents__link
    .toc-highlight}
  - [backColor()](ISeriesPrimitiveAxisView.html#backcolor){.table-of-contents__link
    .toc-highlight}
  - [visible()?](ISeriesPrimitiveAxisView.html#visible){.table-of-contents__link
    .toc-highlight}
  - [tickVisible()?](ISeriesPrimitiveAxisView.html#tickvisible){.table-of-contents__link
    .toc-highlight}
