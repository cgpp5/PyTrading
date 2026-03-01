- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Plugins]{.breadcrumbs__link}
- [Pixel Perfect Rendering]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Best Practices for Pixel Perfect Rendering in Canvas Drawings

To achieve crisp pixel perfect rendering for your plugins, it is
recommended that the canvas drawings are created using bitmap
coordinates. The difference between media and bitmap coordinate spaces
is discussed on the [Canvas Rendering
Target](canvas-rendering-target.html) page. **Essentially, all drawing
actions should use integer positions and dimensions when on the bitmap
coordinate space.**

To ensure consistency between your plugins and the library\'s built-in
logic for rendering points on the chart, use of the following
calculation functions.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]{.admonitionIcon_Rf37}info

Variable names containing `media` refer to positions / dimensions
specified using the media coordinate space (such as the x and y
coordinates provided by the library to the renderers), and names
containing `bitmap` refer to positions / dimensions on the bitmap
coordinate space (actual device screen pixels).

## Centered Shapes[​](pixel-perfect-rendering.html#centered-shapes "Direct link to Centered Shapes"){.hash-link aria-label="Direct link to Centered Shapes"} {#centered-shapes .anchor .anchorWithStickyNavbar_LWe7}

If you need to draw a shape which is centred on a position (for example
a price or x coordinate) and has a desired width then you could use the
`positionsLine` function presented below. This can be used for drawing a
horizontal line at a specific price, or a vertical line aligned with the
centre of series point.

``` {.prism-code .language-typescript .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
interface BitmapPositionLength {
    /** coordinate for use with a bitmap rendering scope */
    position: number;
    /** length for use with a bitmap rendering scope */
    length: number;
}

function centreOffset(lineBitmapWidth: number): number {
    return Math.floor(lineBitmapWidth * 0.5);
}

/**
 * Calculates the bitmap position for an item with a desired length (height or width), and centred according to
 * a position coordinate defined in media sizing.
 * @param positionMedia - position coordinate for the bar (in media coordinates)
 * @param pixelRatio - pixel ratio. Either horizontal for x positions, or vertical for y positions
 * @param desiredWidthMedia - desired width (in media coordinates)
 * @returns Position of the start point and length dimension.
 */
    positionMedia: number,
    pixelRatio: number,
    desiredWidthMedia: number = 1,
    widthIsBitmap?: boolean
): BitmapPositionLength {
    const scaledPosition = Math.round(pixelRatio * positionMedia);
    const lineBitmapWidth = widthIsBitmap
        ? desiredWidthMedia
        : Math.round(desiredWidthMedia * pixelRatio);
    const offset = centreOffset(lineBitmapWidth);
    const position = scaledPosition - offset;
    return { position, length: lineBitmapWidth };
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

## Dual Point Shapes[​](pixel-perfect-rendering.html#dual-point-shapes "Direct link to Dual Point Shapes"){.hash-link aria-label="Direct link to Dual Point Shapes"} {#dual-point-shapes .anchor .anchorWithStickyNavbar_LWe7}

If you need to draw a shape between two coordinates (for example, y
coordinates for a high and low price) then you can use the
`positionsBox` function as presented below.

``` {.prism-code .language-typescript .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
/**
 * Determines the bitmap position and length for a dimension of a shape to be drawn.
 * @param position1Media - media coordinate for the first point
 * @param position2Media - media coordinate for the second point
 * @param pixelRatio - pixel ratio for the corresponding axis (vertical or horizontal)
 * @returns Position of the start point and length dimension.
 */
    position1Media: number,
    position2Media: number,
    pixelRatio: number
): BitmapPositionLength {
    const scaledPosition1 = Math.round(pixelRatio * position1Media);
    const scaledPosition2 = Math.round(pixelRatio * position2Media);
    return {
        position: Math.min(scaledPosition1, scaledPosition2),
        length: Math.abs(scaledPosition2 - scaledPosition1) + 1,
    };
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

## Default Widths[​](pixel-perfect-rendering.html#default-widths "Direct link to Default Widths"){.hash-link aria-label="Direct link to Default Widths"} {#default-widths .anchor .anchorWithStickyNavbar_LWe7}

Please refer to the following pages for functions defining the default
widths of shapes drawn by the library:

- [Crosshair and Grid
  Lines](pixel-perfect-rendering/widths/crosshair.html)
- [Candlesticks](pixel-perfect-rendering/widths/candlestick.html)
- [Columns (Histogram)](pixel-perfect-rendering/widths/columns.html)
- [Full Bar Width](pixel-perfect-rendering/widths/full-bar-width.html)

[](pixel-perfect-rendering/widths/candlestick.html){.pagination-nav__link
.pagination-nav__link--next}

Next

Candlesticks

- [Centered
  Shapes](pixel-perfect-rendering.html#centered-shapes){.table-of-contents__link
  .toc-highlight}
- [Dual Point
  Shapes](pixel-perfect-rendering.html#dual-point-shapes){.table-of-contents__link
  .toc-highlight}
- [Default
  Widths](pixel-perfect-rendering.html#default-widths){.table-of-contents__link
  .toc-highlight}
