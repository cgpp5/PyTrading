- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Functions]{.breadcrumbs__link}
- [createTextWatermark]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Function: createTextWatermark()

> **createTextWatermark**\<`T`\>(`pane`, `options`):
> [`ITextWatermarkPluginApi`](../type-aliases/ITextWatermarkPluginApi.html)\<`T`\>

Creates an image watermark.

## Type parameters[​](createTextWatermark.html#type-parameters "Direct link to Type parameters"){.hash-link aria-label="Direct link to Type parameters"} {#type-parameters .anchor .anchorWithStickyNavbar_LWe7}

• **T**

## Parameters[​](createTextWatermark.html#parameters "Direct link to Parameters"){.hash-link aria-label="Direct link to Parameters"} {#parameters .anchor .anchorWithStickyNavbar_LWe7}

• **pane**: [`IPaneApi`](../interfaces/IPaneApi.html)\<`T`\>

Target pane.

• **options**: [`DeepPartial`](../type-aliases/DeepPartial.html)
\<[`TextWatermarkOptions`](../interfaces/TextWatermarkOptions.html)\>

Watermark options.

## Returns[​](createTextWatermark.html#returns "Direct link to Returns"){.hash-link aria-label="Direct link to Returns"} {#returns .anchor .anchorWithStickyNavbar_LWe7}

[`ITextWatermarkPluginApi`](../type-aliases/ITextWatermarkPluginApi.html)\<`T`\>

Image watermark wrapper.

## Example[​](createTextWatermark.html#example "Direct link to Example"){.hash-link aria-label="Direct link to Example"} {#example .anchor .anchorWithStickyNavbar_LWe7}

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}

const firstPane = chart.panes()[0];
const textWatermark = createTextWatermark(firstPane, {
      horzAlign: 'center',
      vertAlign: 'center',
      lines: [
        {
          text: 'Hello',
          color: 'rgba(255,0,0,0.5)',
          fontSize: 100,
          fontStyle: 'bold',
        },
        {
          text: 'This is a text watermark',
          color: 'rgba(0,0,255,0.5)',
          fontSize: 50,
          fontStyle: 'italic',
          fontFamily: 'monospace',
        },
      ],
});
// to change options
textWatermark.applyOptions({ horzAlign: 'left' });
// to remove watermark from the pane
textWatermark.detach();
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

- [Type
  parameters](createTextWatermark.html#type-parameters){.table-of-contents__link
  .toc-highlight}
- [Parameters](createTextWatermark.html#parameters){.table-of-contents__link
  .toc-highlight}
- [Returns](createTextWatermark.html#returns){.table-of-contents__link
  .toc-highlight}
- [Example](createTextWatermark.html#example){.table-of-contents__link
  .toc-highlight}
