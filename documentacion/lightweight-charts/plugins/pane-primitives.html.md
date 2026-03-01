- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Plugins]{.breadcrumbs__link}
- [Pane Primitives]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Pane Primitives

In addition to Series Primitives, the library now supports Pane
Primitives. These are essentially the same as Series Primitives but are
designed to draw on the pane of a chart rather than being associated
with a specific series. Pane Primitives can be used for features like
watermarks or other chart-wide annotations.

## Key Differences from Series Primitives[​](pane-primitives.html#key-differences-from-series-primitives "Direct link to Key Differences from Series Primitives"){.hash-link aria-label="Direct link to Key Differences from Series Primitives"} {#key-differences-from-series-primitives .anchor .anchorWithStickyNavbar_LWe7}

1.  Pane Primitives are attached to the chart pane rather than a
    specific series.
2.  They cannot draw on the price and time scales.
3.  They are ideal for chart-wide features that are not tied to a
    particular series.

## Adding a Pane Primitive[​](pane-primitives.html#adding-a-pane-primitive "Direct link to Adding a Pane Primitive"){.hash-link aria-label="Direct link to Adding a Pane Primitive"} {#adding-a-pane-primitive .anchor .anchorWithStickyNavbar_LWe7}

Pane Primitives can be added to a chart using the `attachPrimitive`
method on the [`IPaneApi`](../api/interfaces/IPaneApi.html) interface.
Here\'s an example:

``` {.prism-code .language-javascript .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const chart = createChart(document.getElementById('container'));
const pane = chart.panes()[0]; // Get the first (main) pane

const myPanePrimitive = new MyCustomPanePrimitive();
pane.attachPrimitive(myPanePrimitive);
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

## Implementing a Pane Primitive[​](pane-primitives.html#implementing-a-pane-primitive "Direct link to Implementing a Pane Primitive"){.hash-link aria-label="Direct link to Implementing a Pane Primitive"} {#implementing-a-pane-primitive .anchor .anchorWithStickyNavbar_LWe7}

To create a Pane Primitive, you should implement the
[`IPanePrimitive`](../api/type-aliases/IPanePrimitive.html) interface.
This interface is similar to
[`ISeriesPrimitive`](../api/type-aliases/ISeriesPrimitive.html), but
with some key differences:

- It doesn\'t include methods for drawing on price and time scales.
- The `paneViews` method is used to define what will be drawn on the
  chart pane.

Here\'s a basic example of a Pane Primitive implementation:

``` {.prism-code .language-javascript .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
class MyCustomPanePrimitive {
    paneViews() {
        return [
            {
                renderer: {
                    draw: target => {
                        // Custom drawing logic here
                    },
                },
            },
        ];
    }

    // Other methods as needed...
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

For more details on implementing Pane Primitives, refer to the
[`IPanePrimitive`](../api/type-aliases/IPanePrimitive.html) interface
documentation.

[](series-primitives.html){.pagination-nav__link
.pagination-nav__link--prev}

Previous

Series Primitives

[](custom_series.html){.pagination-nav__link
.pagination-nav__link--next}

Next

Custom Series Types

- [Key Differences from Series
  Primitives](pane-primitives.html#key-differences-from-series-primitives){.table-of-contents__link
  .toc-highlight}
- [Adding a Pane
  Primitive](pane-primitives.html#adding-a-pane-primitive){.table-of-contents__link
  .toc-highlight}
- [Implementing a Pane
  Primitive](pane-primitives.html#implementing-a-pane-primitive){.table-of-contents__link
  .toc-highlight}
