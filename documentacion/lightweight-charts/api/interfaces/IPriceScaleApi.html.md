- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Interfaces]{.breadcrumbs__link}
- [IPriceScaleApi]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Interface: IPriceScaleApi

Interface to control chart\'s price scale

## Methods[​](IPriceScaleApi.html#methods "Direct link to Methods"){.hash-link aria-label="Direct link to Methods"} {#methods .anchor .anchorWithStickyNavbar_LWe7}

### applyOptions()[​](IPriceScaleApi.html#applyoptions "Direct link to applyOptions()"){.hash-link aria-label="Direct link to applyOptions()"} {#applyoptions .anchor .anchorWithStickyNavbar_LWe7}

> **applyOptions**(`options`): `void`

Applies new options to the price scale

#### Parameters[​](IPriceScaleApi.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **options**: [`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`PriceScaleOptions`](PriceScaleOptions.html)\>

Any subset of options.

#### Returns[​](IPriceScaleApi.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### options()[​](IPriceScaleApi.html#options "Direct link to options()"){.hash-link aria-label="Direct link to options()"} {#options .anchor .anchorWithStickyNavbar_LWe7}

> **options**(): `Readonly`
> \<[`PriceScaleOptions`](PriceScaleOptions.html)\>

Returns currently applied options of the price scale

#### Returns[​](IPriceScaleApi.html#returns-1 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-1 .anchor .anchorWithStickyNavbar_LWe7}

`Readonly` \<[`PriceScaleOptions`](PriceScaleOptions.html)\>

Full set of currently applied options, including defaults

------------------------------------------------------------------------

### width()[​](IPriceScaleApi.html#width "Direct link to width()"){.hash-link aria-label="Direct link to width()"} {#width .anchor .anchorWithStickyNavbar_LWe7}

> **width**(): `number`

Returns a width of the price scale if it\'s visible or 0 if invisible.

#### Returns[​](IPriceScaleApi.html#returns-2 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-2 .anchor .anchorWithStickyNavbar_LWe7}

`number`

------------------------------------------------------------------------

### setVisibleRange()[​](IPriceScaleApi.html#setvisiblerange "Direct link to setVisibleRange()"){.hash-link aria-label="Direct link to setVisibleRange()"} {#setvisiblerange .anchor .anchorWithStickyNavbar_LWe7}

> **setVisibleRange**(`range`): `void`

Sets the visible range of the price scale.

#### Parameters[​](IPriceScaleApi.html#parameters-1 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-1 .anchor .anchorWithStickyNavbar_LWe7}

• **range**: [`IRange`](IRange.html)\<`number`\>

The visible range to set, with `from` and `to` properties.

#### Returns[​](IPriceScaleApi.html#returns-3 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-3 .anchor .anchorWithStickyNavbar_LWe7}

`void`

------------------------------------------------------------------------

### getVisibleRange()[​](IPriceScaleApi.html#getvisiblerange "Direct link to getVisibleRange()"){.hash-link aria-label="Direct link to getVisibleRange()"} {#getvisiblerange .anchor .anchorWithStickyNavbar_LWe7}

> **getVisibleRange**(): [`IRange`](IRange.html)\<`number`\>

Returns the visible range of the price scale.

#### Returns[​](IPriceScaleApi.html#returns-4 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-4 .anchor .anchorWithStickyNavbar_LWe7}

[`IRange`](IRange.html)\<`number`\>

The visible range of the price scale, or null if the range is not set.

------------------------------------------------------------------------

### setAutoScale()[​](IPriceScaleApi.html#setautoscale "Direct link to setAutoScale()"){.hash-link aria-label="Direct link to setAutoScale()"} {#setautoscale .anchor .anchorWithStickyNavbar_LWe7}

> **setAutoScale**(`on`): `void`

Sets the auto scale mode of the price scale.

#### Parameters[​](IPriceScaleApi.html#parameters-2 "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters-2 .anchor .anchorWithStickyNavbar_LWe7}

• **on**: `boolean`

If true, enables auto scaling; if false, disables it.

#### Returns[​](IPriceScaleApi.html#returns-5 "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns-5 .anchor .anchorWithStickyNavbar_LWe7}

`void`

- [Methods](IPriceScaleApi.html#methods){.table-of-contents__link
  .toc-highlight}
  - [applyOptions()](IPriceScaleApi.html#applyoptions){.table-of-contents__link
    .toc-highlight}
  - [options()](IPriceScaleApi.html#options){.table-of-contents__link
    .toc-highlight}
  - [width()](IPriceScaleApi.html#width){.table-of-contents__link
    .toc-highlight}
  - [setVisibleRange()](IPriceScaleApi.html#setvisiblerange){.table-of-contents__link
    .toc-highlight}
  - [getVisibleRange()](IPriceScaleApi.html#getvisiblerange){.table-of-contents__link
    .toc-highlight}
  - [setAutoScale()](IPriceScaleApi.html#setautoscale){.table-of-contents__link
    .toc-highlight}
