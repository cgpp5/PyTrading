- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Plugins]{.breadcrumbs__link}
- [[Pixel Perfect
  Rendering]{itemprop="name"}](../../pixel-perfect-rendering.html){.breadcrumbs__link
  itemprop="item"}
- [Default Widths]{.breadcrumbs__link}
- [Columns]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

# Histogram Column Width Calculations

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]{.admonitionIcon_Rf37}tip

It is recommend that you first read the [Pixel Perfect
Rendering](../../pixel-perfect-rendering.html) page.

The following functions can be used to get the calculated width that the
library would use for a histogram column at a specific bar spacing and
device pixel ratio.

You can use the `calculateColumnPositionsInPlace` function instead of
the `calculateColumnPositions` function to perform the calculation on an
existing array of items without needing to create additional arrays
(which is more efficient). It is recommended that you memoize the
majority of the calculations below to improve the rendering performance.

``` {.prism-code .language-typescript .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
const alignToMinimalWidthLimit = 4;
const showSpacingMinimalBarWidth = 1;

/**
 * Spacing gap between columns.
 * @param barSpacingMedia - spacing between bars (media coordinate)
 * @param horizontalPixelRatio - horizontal pixel ratio
 * @returns Spacing gap between columns (in Bitmap coordinates)
 */
function columnSpacing(barSpacingMedia: number, horizontalPixelRatio: number) {
    return Math.ceil(barSpacingMedia * horizontalPixelRatio) <=
        showSpacingMinimalBarWidth
        ? 0
        : Math.max(1, Math.floor(horizontalPixelRatio));
}

/**
 * Desired width for columns. This may not be the final width because
 * it may be adjusted later to ensure all columns on screen have a
 * consistent width and gap.
 * @param barSpacingMedia - spacing between bars (media coordinate)
 * @param horizontalPixelRatio - horizontal pixel ratio
 * @param spacing - Spacing gap between columns (in Bitmap coordinates). (optional, provide if you have already calculated it)
 * @returns Desired width for column bars (in Bitmap coordinates)
 */
function desiredColumnWidth(
    barSpacingMedia: number,
    horizontalPixelRatio: number,
    spacing?: number
) {
    return (
        Math.round(barSpacingMedia * horizontalPixelRatio) -
        (spacing ?? columnSpacing(barSpacingMedia, horizontalPixelRatio))
    );
}

interface ColumnCommon {
    /** Spacing gap between columns */
    spacing: number;
    /** Shift columns left by one pixel */
    shiftLeft: boolean;
    /** Half width of a column */
    columnHalfWidthBitmap: number;
    /** horizontal pixel ratio */
    horizontalPixelRatio: number;
}

/**
 * Calculated values which are common to all the columns on the screen, and
 * are required to calculate the individual positions.
 * @param barSpacingMedia - spacing between bars (media coordinate)
 * @param horizontalPixelRatio - horizontal pixel ratio
 * @returns calculated values for subsequent column calculations
 */
function columnCommon(
    barSpacingMedia: number,
    horizontalPixelRatio: number
): ColumnCommon {
    const spacing = columnSpacing(barSpacingMedia, horizontalPixelRatio);
    const columnWidthBitmap = desiredColumnWidth(
        barSpacingMedia,
        horizontalPixelRatio,
        spacing
    );
    const shiftLeft = columnWidthBitmap % 2 === 0;
    const columnHalfWidthBitmap = (columnWidthBitmap - (shiftLeft ? 0 : 1)) / 2;
    return {
        spacing,
        shiftLeft,
        columnHalfWidthBitmap,
        horizontalPixelRatio,
    };
}

interface ColumnPosition {
    left: number;
    right: number;
    shiftLeft: boolean;
}

/**
 * Calculate the position for a column. These values can be later adjusted
 * by a second pass which corrects widths, and shifts columns.
 * @param xMedia - column x position (center) in media coordinates
 * @param columnData - precalculated common values (returned by `columnCommon`)
 * @param previousPosition - result from this function for the previous bar.
 * @returns initial column position
 */
function calculateColumnPosition(
    xMedia: number,
    columnData: ColumnCommon,
    previousPosition: ColumnPosition | undefined
): ColumnPosition {
    const xBitmapUnRounded = xMedia * columnData.horizontalPixelRatio;
    const xBitmap = Math.round(xBitmapUnRounded);
    const xPositions: ColumnPosition = {
        left: xBitmap - columnData.columnHalfWidthBitmap,
        right:
            xBitmap +
            columnData.columnHalfWidthBitmap -
            (columnData.shiftLeft ? 1 : 0),
        shiftLeft: xBitmap > xBitmapUnRounded,
    };
    const expectedAlignmentShift = columnData.spacing + 1;
    if (previousPosition) {
        if (xPositions.left - previousPosition.right !== expectedAlignmentShift) {
            // need to adjust alignment
            if (previousPosition.shiftLeft) {
                previousPosition.right = xPositions.left - expectedAlignmentShift;
            } else {
                xPositions.left = previousPosition.right + expectedAlignmentShift;
            }
        }
    }
    return xPositions;
}

function fixPositionsAndReturnSmallestWidth(
    positions: ColumnPosition[],
    initialMinWidth: number
): number {
    return positions.reduce((smallest: number, position: ColumnPosition) => {
        if (position.right < position.left) {
            position.right = position.left;
        }
        const width = position.right - position.left + 1;
        return Math.min(smallest, width);
    }, initialMinWidth);
}

function fixAlignmentForNarrowColumns(
    positions: ColumnPosition[],
    minColumnWidth: number
) {
    return positions.map((position: ColumnPosition) => {
        const width = position.right - position.left + 1;
        if (width <= minColumnWidth) return position;
        if (position.shiftLeft) {
            position.right -= 1;
        } else {
            position.left += 1;
        }
        return position;
    });
}

/**
 * Calculates the column positions and widths for the x positions.
 * This function creates a new array. You may get faster performance using the
 * `calculateColumnPositionsInPlace` function instead
 * @param xMediaPositions - x positions for the bars in media coordinates
 * @param barSpacingMedia - spacing between bars in media coordinates
 * @param horizontalPixelRatio - horizontal pixel ratio
 * @returns Positions for the columns
 */
    xMediaPositions: number[],
    barSpacingMedia: number,
    horizontalPixelRatio: number
): ColumnPosition[] {
    const common = columnCommon(barSpacingMedia, horizontalPixelRatio);
    const positions = new Array<ColumnPosition>(xMediaPositions.length);
    let previous: ColumnPosition | undefined = undefined;
    for (let i = 0; i < xMediaPositions.length; i++) {
        positions[i] = calculateColumnPosition(
            xMediaPositions[i],
            common,
            previous
        );
        previous = positions[i];
    }
    const initialMinWidth = Math.ceil(barSpacingMedia * horizontalPixelRatio);
    const minColumnWidth = fixPositionsAndReturnSmallestWidth(
        positions,
        initialMinWidth
    );
    if (common.spacing > 0 && minColumnWidth < alignToMinimalWidthLimit) {
        return fixAlignmentForNarrowColumns(positions, minColumnWidth);
    }
    return positions;
}

    x: number;
    column?: ColumnPosition;
}

/**
 * Calculates the column positions and widths for bars using the existing
 * array of items.
 * @param items - bar items which include an `x` property, and will be mutated to contain a column property
 * @param barSpacingMedia - bar spacing in media coordinates
 * @param horizontalPixelRatio - horizontal pixel ratio
 * @param startIndex - start index for visible bars within the items array
 * @param endIndex - end index for visible bars within the items array
 */
    items: ColumnPositionItem[],
    barSpacingMedia: number,
    horizontalPixelRatio: number,
    startIndex: number,
    endIndex: number
): void {
    const common = columnCommon(barSpacingMedia, horizontalPixelRatio);
    let previous: ColumnPosition | undefined = undefined;
    for (let i = startIndex; i < Math.min(endIndex, items.length); i++) {
        items[i].column = calculateColumnPosition(items[i].x, common, previous);
        previous = items[i].column;
    }
    const minColumnWidth = (items as ColumnPositionItem[]).reduce(
        (smallest: number, item: ColumnPositionItem, index: number) => {
            if (!item.column || index < startIndex || index > endIndex)
                return smallest;
            if (item.column.right < item.column.left) {
                item.column.right = item.column.left;
            }
            const width = item.column.right - item.column.left + 1;
            return Math.min(smallest, width);
        },
        Math.ceil(barSpacingMedia * horizontalPixelRatio)
    );
    if (common.spacing > 0 && minColumnWidth < alignToMinimalWidthLimit) {
        (items as ColumnPositionItem[]).forEach(
            (item: ColumnPositionItem, index: number) => {
                if (!item.column || index < startIndex || index > endIndex) return;
                const width = item.column.right - item.column.left + 1;
                if (width <= minColumnWidth) return item;
                if (item.column.shiftLeft) {
                    item.column.right -= 1;
                } else {
                    item.column.left += 1;
                }
                return item.column;
            }
        );
    }
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

[](candlestick.html){.pagination-nav__link .pagination-nav__link--prev}

Previous

Candlesticks

[](crosshair.html){.pagination-nav__link .pagination-nav__link--next}

Next

Crosshair
