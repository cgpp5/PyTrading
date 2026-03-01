- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Plugins]{.breadcrumbs__link}
- [Canvas Rendering Target]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Canvas Rendering Target

The renderer functions used within the plugins (both Custom Series, and
Drawing Primitives) are provided with a `CanvasRenderingTarget2D`
interface on which the drawing logic (using the [Browser\'s 2D Canvas
API](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D){target="_blank"
rel="noopener noreferrer"}) should be executed.
`CanvasRenderingTarget2D` is provided by the [Fancy
Canvas](https://github.com/tradingview/fancy-canvas){target="_blank"
rel="noopener noreferrer"} library.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]{.admonitionIcon_Rf37}info

The typescript definitions can be viewed here:

- [fancy-canvas on
  npmjs.com](https://www.npmjs.com/package/fancy-canvas?activeTab=code){target="_blank"
  rel="noopener noreferrer"}

and specifically the definition for `CanvasRenderingTarget2D` can be
viewed here:

- [canvas-rendering-target.d.ts](https://unpkg.com/fancy-canvas/canvas-rendering-target.d.ts){target="_blank"
  rel="noopener noreferrer"}

## Using `CanvasRenderingTarget2D`[​](canvas-rendering-target.html#using-canvasrenderingtarget2d "Direct link to using-canvasrenderingtarget2d"){.hash-link aria-label="Direct link to using-canvasrenderingtarget2d"} {#using-canvasrenderingtarget2d .anchor .anchorWithStickyNavbar_LWe7}

`CanvasRenderingTarget2D` provides two rendering scope which you can
use:

- `useMediaCoordinateSpace`
- `useBitmapCoordinateSpace`

## Difference between Bitmap and Media[​](canvas-rendering-target.html#difference-between-bitmap-and-media "Direct link to Difference between Bitmap and Media"){.hash-link aria-label="Direct link to Difference between Bitmap and Media"} {#difference-between-bitmap-and-media .anchor .anchorWithStickyNavbar_LWe7}

Bitmap sizing represents the actual physical pixels on the device\'s
screen, while the media size represents the size of a pixel according to
the operating system (and browser) which is generally an integer
representing the ratio of actual physical pixels are used to render a
media pixel. This integer ratio is referred to as the device pixel
ratio.

Using the bitmap sizing allows for more control over the drawn image to
ensure that the graphics are crisp and pixel perfect, however this
generally means that the code will contain a lot multiplication of
coordinates by the pixel ratio. In cases where you don\'t need to draw
using the bitmap sizing then it is easier to use media sizing as you
don\'t need to worry about the devices pixel ratio.

### Bitmap Coordinate Space[​](canvas-rendering-target.html#bitmap-coordinate-space "Direct link to Bitmap Coordinate Space"){.hash-link aria-label="Direct link to Bitmap Coordinate Space"} {#bitmap-coordinate-space .anchor .anchorWithStickyNavbar_LWe7}

`useBitmapCoordinateSpace` can be used to if you would like draw using
the actual devices pixels as the coordinate sizing. The provided scope
(of type `BitmapCoordinatesRenderingScope`) contains readonly values for
the following:

- `context`
  ([CanvasRenderingContext2D](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D){target="_blank"
  rel="noopener noreferrer"}). Context which can be used for rendering.
- `horizontalPixelRatio` (number)
- `verticalPixelRatio` (number)
- `bitmapSize` (Size). Height and width of the canvas in bitmap
  dimensions.
- `mediaSize` (Size). Height and width of the canvas in media
  dimensions.

#### Bitmap Coordinate Space Usage[​](canvas-rendering-target.html#bitmap-coordinate-space-usage "Direct link to Bitmap Coordinate Space Usage"){.hash-link aria-label="Direct link to Bitmap Coordinate Space Usage"} {#bitmap-coordinate-space-usage .anchor .anchorWithStickyNavbar_LWe7}

javascript

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
// target is an instance of CanvasRenderingTarget2D
target.useBitmapCoordinateSpace(scope => {
    // scope is an instance of BitmapCoordinatesRenderingScope

    // example of drawing a filled rectangle which fills the canvas
    scope.context.beginPath();
    scope.context.rect(0, 0, scope.bitmapSize.width, scope.bitmapSize.height);
    scope.context.fillStyle = 'rgba(100, 200, 50, 0.5)';
    scope.context.fill();
});
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

### Media Coordinate Space[​](canvas-rendering-target.html#media-coordinate-space "Direct link to Media Coordinate Space"){.hash-link aria-label="Direct link to Media Coordinate Space"} {#media-coordinate-space .anchor .anchorWithStickyNavbar_LWe7}

`useMediaCoordinateSpace` can be used to if you would like draw using
the media dimensions as the coordinate sizing. The provided scope (of
type `MediaCoordinatesRenderingScope`) contains readonly values for the
following:

- `context`
  ([CanvasRenderingContext2D](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D){target="_blank"
  rel="noopener noreferrer"}). Context which can be used for rendering.
- `mediaSize` (Size). Height and width of the canvas in media
  dimensions.

#### Media Coordinate Space Usage[​](canvas-rendering-target.html#media-coordinate-space-usage "Direct link to Media Coordinate Space Usage"){.hash-link aria-label="Direct link to Media Coordinate Space Usage"} {#media-coordinate-space-usage .anchor .anchorWithStickyNavbar_LWe7}

javascript

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
// target is an instance of CanvasRenderingTarget2D
target.useMediaCoordinateSpace(scope => {
    // scope is an instance of BitmapCoordinatesRenderingScope

    // example of drawing a filled rectangle which fills the canvas
    scope.context.beginPath();
    scope.context.rect(0, 0, scope.mediaSize.width, scope.mediaSize.height);
    scope.context.fillStyle = 'rgba(100, 200, 50, 0.5)';
    scope.context.fill();
});
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

## General Tips[​](canvas-rendering-target.html#general-tips "Direct link to General Tips"){.hash-link aria-label="Direct link to General Tips"} {#general-tips .anchor .anchorWithStickyNavbar_LWe7}

It is recommended that rendering functions should save and restore the
canvas context before and after all the rendering logic to ensure that
the canvas state is the same as when the renderer function was evoked.
To handle the case when an error in the code might prevent the restore
function from being evoked, you should use the try - finally code block
to ensure that the context is correctly restored in all cases.

**Note** that `useBitmapCoordinateSpace` and `useMediaCoordinateSpace`
will automatically save and restore the canvas context for the logic
defined within them. This tip for your additional rendering functions
within the `use*CoordinateSpace`.

javascript

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
function myRenderingFunction(scope) {
    const ctx = scope.context;

    // save the current state of the context to the stack
    ctx.save();

    try {
        // example code
        scope.context.beginPath();
        scope.context.rect(0, 0, scope.mediaSize.width, scope.mediaSize.height);
        scope.context.fillStyle = 'rgba(100, 200, 50, 0.5)';
        scope.context.fill();
    } finally {
        // restore the saved context from the stack
        ctx.restore();
    }
}

target.useMediaCoordinateSpace(scope => {
    myRenderingFunction(scope);
    myOtherRenderingFunction(scope);
    /* ... */
});
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

[](custom_series.html){.pagination-nav__link
.pagination-nav__link--prev}

Previous

Custom Series Types

[](pixel-perfect-rendering.html){.pagination-nav__link
.pagination-nav__link--next}

Next

Pixel Perfect Rendering

- [Using
  `CanvasRenderingTarget2D`](canvas-rendering-target.html#using-canvasrenderingtarget2d){.table-of-contents__link
  .toc-highlight}
- [Difference between Bitmap and
  Media](canvas-rendering-target.html#difference-between-bitmap-and-media){.table-of-contents__link
  .toc-highlight}
  - [Bitmap Coordinate
    Space](canvas-rendering-target.html#bitmap-coordinate-space){.table-of-contents__link
    .toc-highlight}
  - [Media Coordinate
    Space](canvas-rendering-target.html#media-coordinate-space){.table-of-contents__link
    .toc-highlight}
- [General
  Tips](canvas-rendering-target.html#general-tips){.table-of-contents__link
  .toc-highlight}
