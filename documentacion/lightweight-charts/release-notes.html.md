- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Release Notes]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Release Notes

## 5.1.0[​](release-notes.html#510 "Direct link to 5.1.0"){.hash-link aria-label="Direct link to 5.1.0"} {#510 .anchor .anchorWithStickyNavbar_LWe7}

Version 5.1.0 introduces **data conflation**, a powerful performance
optimization feature designed for charts with very large datasets. For
most use cases with typical dataset sizes, this feature will operate
transparently in the background. However, if you\'re working with
datasets containing tens of thousands of data points or more, conflation
can dramatically improve rendering performance when users zoom out.

### Major Updates in 5.1[​](release-notes.html#major-updates-in-51 "Direct link to Major Updates in 5.1"){.hash-link aria-label="Direct link to Major Updates in 5.1"} {#major-updates-in-51 .anchor .anchorWithStickyNavbar_LWe7}

#### Data Conflation[​](release-notes.html#data-conflation "Direct link to Data Conflation"){.hash-link aria-label="Direct link to Data Conflation"} {#data-conflation .anchor .anchorWithStickyNavbar_LWe7}

Data conflation is an automatic performance optimization that merges
data points when zoomed out, significantly improving rendering
performance for large datasets. When bar spacing falls below a threshold
where multiple data points would be rendered in less than 0.5 pixels of
screen space, the library intelligently combines them into single
points.

**Key features:**

- **Opt-in activation**: Conflation is disabled by default and can be
  enabled via the `enableConflation` option.
- **Configurable options**: Control conflation behavior through new time
  scale and series options:
  - `enableConflation` - Enable or disable the feature (default: false).
  - `conflationThresholdFactor` - Adjust the zoom level threshold for
    activation and create smoothing effects. Higher values (2.0, 4.0,
    8.0+) result in smoother-looking charts, particularly useful for
    sparklines and small charts where smooth appearance is prioritized
    over showing every data point.
  - `precomputeConflationOnInit` - Pre-calculate conflated data on
    initialization for improved zoom performance at the cost of initial
    load time and memory usage (default: false).
  - `precomputeConflationPriority` - Control background computation
    priority when using the Prioritized Task Scheduling API (default:
    \'background\').
- **Custom series support**: Plugin developers can implement custom
  aggregation logic through the new `CustomConflationReducer` interface.

This feature is particularly beneficial for applications displaying
historical data spanning years or real-time feeds that accumulate large
amounts of data over time. For typical use cases with moderate dataset
sizes, conflation can remain disabled without any impact.

(PR
[#1945](https://github.com/tradingview/lightweight-charts/pull/1945){target="_blank"
rel="noopener noreferrer"})

**Enhancements**

- Added `doNotSnapToHiddenSeriesIndices` option to `CrosshairOptions`.
  When enabled, the crosshair will snap to the nearest visible series
  data point instead of snapping to hidden series indices. (PR
  [#1995](https://github.com/tradingview/lightweight-charts/pull/1995){target="_blank"
  rel="noopener noreferrer"})

**Bug Fixes**

- Fixed price axis label positioning when using plugin views that don\'t
  implement the optional `fixedCoordinate()` method. Previously, labels
  were incorrectly treated as positioned at coordinate 0, causing false
  overlap detection. (PR
  [#1993](https://github.com/tradingview/lightweight-charts/pull/1993){target="_blank"
  rel="noopener noreferrer"}, fixes
  [#1986](https://github.com/tradingview/lightweight-charts/issues/1986){target="_blank"
  rel="noopener noreferrer"}, contributed by
  [\@tpunt](https://github.com/tpunt){target="_blank"
  rel="noopener noreferrer"})

- Fixed time scale `fitContent` method to properly respect the
  `rightOffset` option when `rightOffsetPixels` is not set. This
  addresses a regression introduced in version 5.0.9. (PR
  [#1989](https://github.com/tradingview/lightweight-charts/pull/1989){target="_blank"
  rel="noopener noreferrer"}, fixes
  [#1988](https://github.com/tradingview/lightweight-charts/issues/1988){target="_blank"
  rel="noopener noreferrer"})

**Contributors**

We\'d like to thank our external contributors for their valuable
contributions to this release:

- [\@tpunt](https://github.com/tpunt){target="_blank"
  rel="noopener noreferrer"} (Thomas Punt)

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v5.0.9..v5.1.0){target="_blank"
rel="noopener noreferrer"}.

## 5.0.9[​](release-notes.html#509 "Direct link to 5.0.9"){.hash-link aria-label="Direct link to 5.0.9"} {#509 .anchor .anchorWithStickyNavbar_LWe7}

**Enhancements**

- Added `rightOffsetPixels` option to `HorzScaleOptions`, allowing
  margin space from the right side of the chart to be set in pixels.
  This option takes precedence over `rightOffset` and ensures consistent
  pixel offset when using `fitContent` on charts with different amounts
  of data. The pixel-based offset remains consistent during zoom
  operations. (PR
  [#1957](https://github.com/tradingview/lightweight-charts/pull/1957){target="_blank"
  rel="noopener noreferrer"})
- Added `pop` method to series API that removes a specified number of
  data points from the end of the series and returns the removed data.
  (PR
  [#1949](https://github.com/tradingview/lightweight-charts/pull/1949){target="_blank"
  rel="noopener noreferrer"}, fixes
  [#1518](https://github.com/tradingview/lightweight-charts/issues/1518){target="_blank"
  rel="noopener noreferrer"}, contributed by
  [\@tpunt](https://github.com/tpunt){target="_blank"
  rel="noopener noreferrer"})
- Enhanced `takeScreenshot` method with two new optional parameters:
  - `addTopLayer` - includes top layer primitives in the screenshot
    (default: false)
  - `includeCrosshair` - includes the crosshair when `addTopLayer` is
    enabled (default: false) (PR
    [#1977](https://github.com/tradingview/lightweight-charts/pull/1977){target="_blank"
    rel="noopener noreferrer"})
- Added `autoScale` option to `SeriesMarkersOptions`, allowing control
  over whether markers are included in the auto-scaling calculation of
  the price scale. When enabled (default: true), the chart will adjust
  its scale to ensure markers are fully visible. (PR
  [#1940](https://github.com/tradingview/lightweight-charts/pull/1940){target="_blank"
  rel="noopener noreferrer"}, contributed by
  [\@zbinlin](https://github.com/zbinlin){target="_blank"
  rel="noopener noreferrer"})
- Added `base` option to price format configuration as an alternative to
  `minMove`. This helps avoid floating-point precision limitations when
  dealing with extremely small price movements. (PR
  [#1952](https://github.com/tradingview/lightweight-charts/pull/1952){target="_blank"
  rel="noopener noreferrer"})
- Enhanced plugin API with additional functionality:
  - Added `lastValueData()` method to the public series API
  - Exposed `setLineStyle` drawing utility through a new `DrawingUtils`
    interface (PR
    [#1956](https://github.com/tradingview/lightweight-charts/pull/1956){target="_blank"
    rel="noopener noreferrer"}, contributed by
    [\@tpunt](https://github.com/tpunt){target="_blank"
    rel="noopener noreferrer"})

**Bug Fixes**

- Fixed price scale visible range calculation when in logarithmic scale
  mode by properly converting the range from log space and handling
  precision issues with rounding. (PR
  [#1965](https://github.com/tradingview/lightweight-charts/pull/1965){target="_blank"
  rel="noopener noreferrer"}, contributed by
  [\@tpunt](https://github.com/tpunt){target="_blank"
  rel="noopener noreferrer"})

**Plugin & Indicator Examples**

- Added *Dual Range Histogram Series* custom plugin example that
  visualizes paired positive and negative value ranges for each time
  point using a column-based display. (PR
  [#1934](https://github.com/tradingview/lightweight-charts/pull/1934){target="_blank"
  rel="noopener noreferrer"})
- Added *Pretty Histogram* plugin example demonstrating non-standard
  histogram rendering. (PR
  [#1930](https://github.com/tradingview/lightweight-charts/pull/1930){target="_blank"
  rel="noopener noreferrer"})
- Added examples demonstrating how to implement indicators (studies)
  within Lightweight Charts. See the [Analysis Indicators
  tutorial](https://tradingview.github.io/lightweight-charts/tutorials#analysis-indicators){target="_blank"
  rel="noopener noreferrer"} for more information. (PR
  [#1915](https://github.com/tradingview/lightweight-charts/pull/1915){target="_blank"
  rel="noopener noreferrer"})

**Contributors**

We\'d like to thank our external contributors for their valuable
contributions to this release:

- [\@tpunt](https://github.com/tpunt){target="_blank"
  rel="noopener noreferrer"} (Thomas Punt)
- [\@zbinlin](https://github.com/zbinlin){target="_blank"
  rel="noopener noreferrer"} (Colin Cheng)

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v5.0.8..v5.0.9){target="_blank"
rel="noopener noreferrer"}.

## 5.0.8[​](release-notes.html#508 "Direct link to 5.0.8"){.hash-link aria-label="Direct link to 5.0.8"} {#508 .anchor .anchorWithStickyNavbar_LWe7}

**Enhancements**

- Improved pane API with several new methods and options:
  - Added `addDefaultPane` option to chart options, allowing creation of
    charts with no initial panes
  - Added `addPane` method to `IChartApi` for programmatically adding
    panes
  - Added `setPreserveEmptyPane` and `preserveEmptyPane` methods to
    control empty pane behavior
  - Added `getStretchFactor` and `setStretchFactor` methods to control
    relative pane sizes
  - Added `addCustomSeries` and `addSeries` methods to `IPaneApi` for
    creating series directly on a specific pane
  - Updated `getHTMLElement` to return `null` when a pane hasn\'t been
    created yet
  - These improvements provide greater flexibility when working with
    multi-pane charts (PR
    [#1894](https://github.com/tradingview/lightweight-charts/pull/1894){target="_blank"
    rel="noopener noreferrer"}, fixes
    [#1898](https://github.com/tradingview/lightweight-charts/issues/1898){target="_blank"
    rel="noopener noreferrer"},
    [#1896](https://github.com/tradingview/lightweight-charts/issues/1896){target="_blank"
    rel="noopener noreferrer"},
    [#1872](https://github.com/tradingview/lightweight-charts/issues/1872){target="_blank"
    rel="noopener noreferrer"},
    [#1907](https://github.com/tradingview/lightweight-charts/issues/1907){target="_blank"
    rel="noopener noreferrer"})
- Added additional price scale tick mark formatting capabilities:
  - Added `formatTickmarks` method to `IPriceFormatter` interface
  - Added `tickmarksPriceFormatter` and `tickmarksPercentageFormatter`
    options to `LocalizationOptionsBase`
  - Added `tickmarksFormatter` option to `PriceFormatCustom`
  - These new formatters provide all tick mark values at once, allowing
    for context-aware formatting decisions such as determining the
    optimal precision level needed (PR
    [#1903](https://github.com/tradingview/lightweight-charts/pull/1903){target="_blank"
    rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v5.0.7..v5.0.8){target="_blank"
rel="noopener noreferrer"}.

## 5.0.7[​](release-notes.html#507 "Direct link to 5.0.7"){.hash-link aria-label="Direct link to 5.0.7"} {#507 .anchor .anchorWithStickyNavbar_LWe7}

**Enhancements**

- Added price scale visible range control with new methods in
  `IPriceScaleApi`: `setVisibleRange(range)`, `getVisibleRange()`, and
  `setAutoScale(on)`. These methods allow for programmatic control of
  the visible price range on a price scale. Also added
  `ensureEdgeTickMarksVisible` option to `PriceScaleOptions`, which
  ensures tick marks are always visible at the very top and bottom of
  the price scale, providing clear boundary indicators. These features
  are particularly useful for charts with zooming and panning disabled
  that are primarily for display purposes. (PR
  [#1856](https://github.com/tradingview/lightweight-charts/pull/1856){target="_blank"
  rel="noopener noreferrer"})
- Added control over the rendering stacking order of series markers
  through a new `zOrder` option in the series markers plugin. This
  enhancement provides greater flexibility in controlling marker
  visibility and layering in complex charts. (PR
  [#1876](https://github.com/tradingview/lightweight-charts/pull/1876){target="_blank"
  rel="noopener noreferrer"}).

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v5.0.6..v5.0.7){target="_blank"
rel="noopener noreferrer"}.

## 5.0.6[​](release-notes.html#506 "Direct link to 5.0.6"){.hash-link aria-label="Direct link to 5.0.6"} {#506 .anchor .anchorWithStickyNavbar_LWe7}

**Enhancements**

- Implemented series order functionality, allowing control over the
  rendering order of series within a pane. Series with higher order
  values are rendered on top of those with lower values. Added two new
  methods to `ISeriesApi`: `seriesOrder()` to get the current order
  index and `setSeriesOrder(order)` to set a specific order. (PR
  [#1868](https://github.com/tradingview/lightweight-charts/pull/1868){target="_blank"
  rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v5.0.5..v5.0.6){target="_blank"
rel="noopener noreferrer"}.

## 5.0.5[​](release-notes.html#505 "Direct link to 5.0.5"){.hash-link aria-label="Direct link to 5.0.5"} {#505 .anchor .anchorWithStickyNavbar_LWe7}

**Bug Fixes**

- Fixed an issue where the series marker plugin could throw an exception
  if the series data required for individual markers could not be found
  (such as when the data is cleared or changed via ⁠setData on the
  series). (PR
  [#1845](https://github.com/tradingview/lightweight-charts/pull/1845){target="_blank"
  rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v5.0.4..v5.0.5){target="_blank"
rel="noopener noreferrer"}.

## 5.0.4[​](release-notes.html#504 "Direct link to 5.0.4"){.hash-link aria-label="Direct link to 5.0.4"} {#504 .anchor .anchorWithStickyNavbar_LWe7}

**Improvements**

- Fixed performance degradation when adding series markers to charts
  with large datasets (15,000+ data points) by optimizing marker
  calculations to only run when necessary. (PR
  [#1835](https://github.com/tradingview/lightweight-charts/pull/1835){target="_blank"
  rel="noopener noreferrer"}, fixes
  [#1808](https://github.com/tradingview/lightweight-charts/issues/1808){target="_blank"
  rel="noopener noreferrer"})
- Added price-based positioning for series markers, allowing more
  precise control over marker placement. New position types include
  `atPriceTop`, `atPriceBottom`, and `atPriceMiddle`, which require a
  `price` value to be specified. (PR
  [#1826](https://github.com/tradingview/lightweight-charts/pull/1826){target="_blank"
  rel="noopener noreferrer"}, thanks to
  [\@EranGrin](https://github.com/EranGrin){target="_blank"
  rel="noopener noreferrer"})
- Added `MagnetOHLC` to `CrosshairMode`. This mode sticks the
  crosshair\'s horizontal line to the price value of a single-value
  series or to the open/high/low/close price of OHLC-based series. (PR
  [#1831](https://github.com/tradingview/lightweight-charts/pull/1831){target="_blank"
  rel="noopener noreferrer"}, thanks to
  [\@Jonney](https://github.com/Jonney){target="_blank"
  rel="noopener noreferrer"})

**Bug Fixes**

- Fixed an issue where the crosshair marker would be visible on the
  first data point when the chart is initially loaded, before any user
  interaction. This behavior has been reverted to match version 4, where
  the crosshair remains hidden until user interaction. (PR
  [#1840](https://github.com/tradingview/lightweight-charts/pull/1840){target="_blank"
  rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v5.0.3..v5.0.4){target="_blank"
rel="noopener noreferrer"}.

## 5.0.3[​](release-notes.html#503 "Direct link to 5.0.3"){.hash-link aria-label="Direct link to 5.0.3"} {#503 .anchor .anchorWithStickyNavbar_LWe7}

**Bug Fixes**

- Fixed an issue where changing the price scale for one pane would
  impact all panes in multi-pane setups. Added pane index parameter to
  the price scale API to ensure changes only affect the intended pane.
  (PR
  [#1821](https://github.com/tradingview/lightweight-charts/pull/1821){target="_blank"
  rel="noopener noreferrer"}, fixes
  [#1817](https://github.com/tradingview/lightweight-charts/issues/1817){target="_blank"
  rel="noopener noreferrer"})
- Fixed an issue where a cursorStyle defined in a primitive hit-test
  wouldn\'t be applied. Additionally improved cursor style handling to
  maintain the correct cursor when the mouse remains in the same
  position while price/time scales are adjusted. (PR
  [#1823](https://github.com/tradingview/lightweight-charts/pull/1823){target="_blank"
  rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v5.0.2..v5.0.3){target="_blank"
rel="noopener noreferrer"}.

## 5.0.2[​](release-notes.html#502 "Direct link to 5.0.2"){.hash-link aria-label="Direct link to 5.0.2"} {#502 .anchor .anchorWithStickyNavbar_LWe7}

**Bug Fixes**

- Fixed an issue where the crosshair marker would remain visible after
  the mouse pointer has left the chart. (PR
  [#1807](https://github.com/tradingview/lightweight-charts/issues/1807){target="_blank"
  rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v5.0.1..v5.0.2){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 5.0.0[​](release-notes.html#500 "Direct link to 5.0.0"){.hash-link aria-label="Direct link to 5.0.0"} {#500 .anchor .anchorWithStickyNavbar_LWe7}

Version 5.0.0 represents a significant milestone in the evolution of
Lightweight Charts™, delivering on our commitment to keep the library
truly \"lightweight\". Despite adding numerous new features,
improvements, and fixes, we\'ve managed to reduce the bundle size by up
to 16%, bringing the base bundle size down to just 35kB. This remarkable
reduction was achieved through enhanced tree-shaking capabilities,
modernized architecture, and careful optimization of core features.

This release introduces highly requested features like multi-pane
support and new chart types. It also modernizes the codebase and
improves its architecture to set a foundation for future enhancements
without compromising on size.

### Major Updates in 5.0[​](release-notes.html#major-updates-in-50 "Direct link to Major Updates in 5.0"){.hash-link aria-label="Direct link to Major Updates in 5.0"} {#major-updates-in-50 .anchor .anchorWithStickyNavbar_LWe7}

#### Multi-Pane Support[​](release-notes.html#multi-pane-support "Direct link to Multi-Pane Support"){.hash-link aria-label="Direct link to Multi-Pane Support"} {#multi-pane-support .anchor .anchorWithStickyNavbar_LWe7}

One of our most requested features, multi-pane support is now available.
It allows you to create complex chart layouts with multiple independent
viewing areas. This enhancement enables sophisticated technical analysis
setups and better visualization of related data series. Additional key
benefits include:

- Full support for multiple panes within a single chart
- Independent scale and series management per pane
- Flexible pane sizing and arrangement options

See [Panes](panes.html) for more information.

#### New Chart Types[​](release-notes.html#new-chart-types "Direct link to New Chart Types"){.hash-link aria-label="Direct link to New Chart Types"} {#new-chart-types .anchor .anchorWithStickyNavbar_LWe7}

**Yield Curve Charts**

- New specialized chart type for displaying yield curves
- Custom horizontal scale behavior with linear spacing
- Optimized whitespace handling

**Options Charts**

- Price-based horizontal scale support
- Specialized formatting and interaction handling
- Ideal for options chain visualization

See [Chart types](chart-types.html) for more information about the
[Yield Curve Chart](chart-types.html#yield-curve-chart) and [Options
Chart](chart-types.html#options-chart-price-based) types.

#### Enhanced Color Support[​](release-notes.html#enhanced-color-support "Direct link to Enhanced Color Support"){.hash-link aria-label="Direct link to Enhanced Color Support"} {#enhanced-color-support .anchor .anchorWithStickyNavbar_LWe7}

- Expanded native support for sRGB-based colors (RGB, RGBA, hex, named
  colors, HSL)
- Support for expanded color gamuts like Display P3
- Ability to specify a custom color parser to add support for non-sRGB
  formats
- Reduced bundle size through browser-native color parsing

#### Architectural Improvements[​](release-notes.html#architectural-improvements "Direct link to Architectural Improvements"){.hash-link aria-label="Direct link to Architectural Improvements"} {#architectural-improvements .anchor .anchorWithStickyNavbar_LWe7}

- Watermark feature reimplemented as plugins (`TextWatermark` and
  `ImageWatermark`)
- Series Markers extracted as a plugin for better tree-shaking
- New Up/Down Markers Plugin for price change visualization
- Introduction of Pane Primitives for plugin attachment

### Breaking Changes[​](release-notes.html#breaking-changes "Direct link to Breaking Changes"){.hash-link aria-label="Direct link to Breaking Changes"} {#breaking-changes .anchor .anchorWithStickyNavbar_LWe7}

- New unified series creation API (see [migration
  guide](migrations/from-v4-to-v5.html))
- Dropped CommonJS support and updated JS syntax version to ES2020
- Watermark functionality moved to plugins
- Series markers implementation changed to plugin system

### Enhancements[​](release-notes.html#enhancements "Direct link to Enhancements"){.hash-link aria-label="Direct link to Enhancements"} {#enhancements .anchor .anchorWithStickyNavbar_LWe7}

- Added relative gradient option for baseline and area series
  (`relativeGradient`)
- New time scale option for maximum bar spacing (`maxBarSpacing`)
- Added `priceLines()` method to `ISeriesApi` interface
- Enhanced watermark capabilities with multi-line text support
- Improved plugin system with Pane Primitives support
- Better tree-shaking capabilities for smaller bundle sizes

### Bug Fixes[​](release-notes.html#bug-fixes "Direct link to Bug Fixes"){.hash-link aria-label="Direct link to Bug Fixes"} {#bug-fixes .anchor .anchorWithStickyNavbar_LWe7}

- Fixed primitive detachment update issues
  ([#1594](https://github.com/tradingview/lightweight-charts/issues/1594){target="_blank"
  rel="noopener noreferrer"})
- Various performance and rendering improvements

### Migration Guide[​](release-notes.html#migration-guide "Direct link to Migration Guide"){.hash-link aria-label="Direct link to Migration Guide"} {#migration-guide .anchor .anchorWithStickyNavbar_LWe7}

We\'ve prepared a comprehensive migration guide to help you upgrade from
v4 to v5. Key areas to note:

1.  Series Creation API changes
2.  Watermarks and Series Markers moving to separate plugins
3.  Plugin system updates

See the full migration guide: [Migrating from v4 to
v5](migrations/from-v4-to-v5.html)

### Technical Notes[​](release-notes.html#technical-notes "Direct link to Technical Notes"){.hash-link aria-label="Direct link to Technical Notes"} {#technical-notes .anchor .anchorWithStickyNavbar_LWe7}

This release uses ES2020 syntax and no longer supports CommonJS. If you
need to support older environments, you\'ll need to set up transpilation
for the `lightweight-charts` package in your build system using tools
like Babel.

As always, we thank you for your support and help in making Lightweight
Charts™ the best product on the financial web. We look forward to seeing
what you build with these new capabilities!

You can always send us your feedback via GitHub. Happy trading!

Team TradingView

See [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v4.2.3..v5.0.1){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 4.2.3[​](release-notes.html#423 "Direct link to 4.2.3"){.hash-link aria-label="Direct link to 4.2.3"} {#423 .anchor .anchorWithStickyNavbar_LWe7}

**Minor Improvements**

- Improve check for crosshair label visibility on the price scale. This
  improves upon previous work (#1743 in v4.2.2) by reducing the
  allocated space for the crosshair when it is enabled, but the label is
  disabled. (PR
  [#1757](https://github.com/tradingview/lightweight-charts/issues/1757){target="_blank"
  rel="noopener noreferrer"})

**Bug Fixes**

- Added additional prototype pollution protection for internal merge
  helper function. (PR
  [#1758](https://github.com/tradingview/lightweight-charts/issues/1758){target="_blank"
  rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v4.2.2..v4.2.3){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 4.2.2[​](release-notes.html#422 "Direct link to 4.2.2"){.hash-link aria-label="Direct link to 4.2.2"} {#422 .anchor .anchorWithStickyNavbar_LWe7}

**Minor Improvements**

- Improved price scale width calculation by not allocating space for
  crosshair labels when the crosshair is disabled. (PR
  [#1743](https://github.com/tradingview/lightweight-charts/issues/1743){target="_blank"
  rel="noopener noreferrer"})

**Bug Fixes**

- Fixed calculations for `fixLeftEdge` and `fixRightEdge` on the first
  render when both are true and data is added to an initially empty
  chart. Fixes issue
  [#1356](https://github.com/tradingview/lightweight-charts/issues/1356){target="_blank"
  rel="noopener noreferrer"}. (PR
  [#1741](https://github.com/tradingview/lightweight-charts/issues/1741){target="_blank"
  rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v4.2.1..v4.2.2){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 4.2.1[​](release-notes.html#421 "Direct link to 4.2.1"){.hash-link aria-label="Direct link to 4.2.1"} {#421 .anchor .anchorWithStickyNavbar_LWe7}

**Bug Fixes**

- Fixed an issue where the series title part of a price scale label
  appeared blurry when using Firefox.

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v4.2.0..v4.2.1){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 4.2.0[​](release-notes.html#420 "Direct link to 4.2.0"){.hash-link aria-label="Direct link to 4.2.0"} {#420 .anchor .anchorWithStickyNavbar_LWe7}

**Enhancements**

- Added new
  [`attributionLogo`](api/interfaces/LayoutOptions.html#attributionLogo){target="_blank"
  rel="noopener noreferrer"} option to `LayoutOptions`. This feature
  displays the TradingView attribution logo on the main chart pane by
  default, helping users meet the library\'s licensing requirements for
  attribution.
  - The TradingView attribution logo can be easily hidden by setting the
    `attributionLogo` option to `false` in the chart\'s `layout` option.
- Improved data validation for `OhlcData` and `SingleValueData`.
  Introduced `isFulfilledBarData` for `OhlcData` and
  `isFulfilledLineData` for `SingleValueData`, ensuring more accurate
  validation of data types. Contributed by
  [\@mozeryansky](https://github.com/mozeryansky){target="_blank"
  rel="noopener noreferrer"} (PR
  [#1579](https://github.com/tradingview/lightweight-charts/pull/1579){target="_blank"
  rel="noopener noreferrer"}, fixes
  [#1526](https://github.com/tradingview/lightweight-charts/issues/1526){target="_blank"
  rel="noopener noreferrer"}).

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v4.1.7..v4.2.0){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 4.1.7[​](release-notes.html#417 "Direct link to 4.1.7"){.hash-link aria-label="Direct link to 4.1.7"} {#417 .anchor .anchorWithStickyNavbar_LWe7}

**Enhancements**

- Further Refinement of the Price Scale Label Alignment (PR
  [#1630](https://github.com/tradingview/lightweight-charts/pull/1630){target="_blank"
  rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v4.1.6..v4.1.7){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 4.1.6[​](release-notes.html#416 "Direct link to 4.1.6"){.hash-link aria-label="Direct link to 4.1.6"} {#416 .anchor .anchorWithStickyNavbar_LWe7}

**Enhancements**

- Improved Price Scale Label Alignment: Enhanced the alignment algorithm
  for price scale labels to ensure they do not move out of the viewport.
  This improves the visibility of price labels, particularly when they
  are near the edges of the scale. Fixes
  [#1620](https://github.com/tradingview/lightweight-charts/issues/1620){target="_blank"
  rel="noopener noreferrer"} (PR
  [#1621](https://github.com/tradingview/lightweight-charts/pull/1621){target="_blank"
  rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v4.1.5..v4.1.6){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 4.1.5[​](release-notes.html#415 "Direct link to 4.1.5"){.hash-link aria-label="Direct link to 4.1.5"} {#415 .anchor .anchorWithStickyNavbar_LWe7}

**Enhancements**

- Added `IHorzScaleBehavior.shouldResetTickmarkLabels`. (PR
  [#1614](https://github.com/tradingview/lightweight-charts/pull/1614){target="_blank"
  rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v4.1.4..v4.1.5){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 4.1.4[​](release-notes.html#414 "Direct link to 4.1.4"){.hash-link aria-label="Direct link to 4.1.4"} {#414 .anchor .anchorWithStickyNavbar_LWe7}

**Bug Fixes**

- Fixed hoveredSeries being undefined during series removal and
  creation. (PR
  [#1529](https://github.com/tradingview/lightweight-charts/pull/1529){target="_blank"
  rel="noopener noreferrer"}, fixes
  [#1406](https://github.com/tradingview/lightweight-charts/pull/1406){target="_blank"
  rel="noopener noreferrer"}, fixes
  [#1499](https://github.com/tradingview/lightweight-charts/pull/1499){target="_blank"
  rel="noopener noreferrer"})
- Fixed price label rendering artefact. (PR
  [#1585](https://github.com/tradingview/lightweight-charts/pull/1585){target="_blank"
  rel="noopener noreferrer"}, fixes
  [#1584](https://github.com/tradingview/lightweight-charts/pull/1584){target="_blank"
  rel="noopener noreferrer"})
- Fixed an issue that prevented primitives with `zOrder` set to `top`
  from drawing above the last price animation. (PR
  [#1576](https://github.com/tradingview/lightweight-charts/pull/1576){target="_blank"
  rel="noopener noreferrer"})
- Fixed possible ReDos. (PR
  [#1536](https://github.com/tradingview/lightweight-charts/pull/1536){target="_blank"
  rel="noopener noreferrer"})
- Fixed marker positioning, which could cause a space between histogram
  and bottom of the chart. (PR
  [#1538](https://github.com/tradingview/lightweight-charts/pull/1538){target="_blank"
  rel="noopener noreferrer"} &
  [#1539](https://github.com/tradingview/lightweight-charts/pull/1539){target="_blank"
  rel="noopener noreferrer"}, fixes
  [#1382](https://github.com/tradingview/lightweight-charts/pull/1382){target="_blank"
  rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v4.1.3..v4.1.4){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 4.1.3[​](release-notes.html#413 "Direct link to 4.1.3"){.hash-link aria-label="Direct link to 4.1.3"} {#413 .anchor .anchorWithStickyNavbar_LWe7}

**Minor Improvements**

- Added option to disable bold labels in the time scale. (PR
  [#1510](https://github.com/tradingview/lightweight-charts/pull/1510){target="_blank"
  rel="noopener noreferrer"})

**Bug Fixes**

- Fixed sub-pixel horizontal alignment of the crosshair marker and
  series markers. (PR
  [#1505](https://github.com/tradingview/lightweight-charts/pull/1505){target="_blank"
  rel="noopener noreferrer"}, fixes
  [#1504](https://github.com/tradingview/lightweight-charts/issues/1504){target="_blank"
  rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v4.1.2..v4.1.3){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 4.1.2[​](release-notes.html#412 "Direct link to 4.1.2"){.hash-link aria-label="Direct link to 4.1.2"} {#412 .anchor .anchorWithStickyNavbar_LWe7}

**Bug Fixes**

- Fix for \'Total canvas memory use exceeds the maximum limit\' error
  raised on iOS Safari. (PR
  [#1485](https://github.com/tradingview/lightweight-charts/pull/1485){target="_blank"
  rel="noopener noreferrer"})

**Minor Improvements**

- Improved error messages for price scale margins. (PR
  [#1489](https://github.com/tradingview/lightweight-charts/pull/1489){target="_blank"
  rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v4.1.1..v4.1.2){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 4.1.1[​](release-notes.html#411 "Direct link to 4.1.1"){.hash-link aria-label="Direct link to 4.1.1"} {#411 .anchor .anchorWithStickyNavbar_LWe7}

**Bug Fixes**

- Fixed `shiftVisibleRangeOnNewBar` behaviour for realtime updates to a
  series. Additionally, a new option
  `allowShiftVisibleRangeOnWhitespaceReplacement` has been added if you
  wish to have the old 4.0 behaviour for when new data replaces existing
  whitespace. (PR
  [#1444](https://github.com/tradingview/lightweight-charts/pull/1444){target="_blank"
  rel="noopener noreferrer"})
- When disabling touch scrolling on the chart via either the
  `vertTouchDrag` or `horzTouchDrag` setting in the `handleScroll`
  options, any touch scroll events over the corresponding scale will now
  be ignored so the page can be scrolled. (PR
  [#1445](https://github.com/tradingview/lightweight-charts/pull/1445){target="_blank"
  rel="noopener noreferrer"})

[Changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v4.1.0..v4.1.1){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 4.1.0[​](release-notes.html#410 "Direct link to 4.1.0"){.hash-link aria-label="Direct link to 4.1.0"} {#410 .anchor .anchorWithStickyNavbar_LWe7}

Version 4.1 of Lightweight Charts introduces exciting new features,
including the introduction of Plugins, which provide developers the
ability to extend the library\'s functionality. Additionally, this
release includes enhancements to customize the horizontal scale and
various minor improvements and bug fixes.

**Major Updates**

**Plugins**

Developers can now leverage the power of Plugins in Lightweight Charts.
Two types of Plugins are supported -  [Custom
Series](plugins/intro.html#custom-series) and [Drawing
Primitives](plugins/intro.html#primitives), offering the ability to
define new series types and create custom visualizations, drawing tools,
and annotations.

With the flexibility provided by these plugins, developers can create
highly customizable charting applications for their users.

To get started with plugins, please refer to our [Plugins
Documentation](plugins/intro.html) for a better understanding of what is
possible and how plugins work. You can also explore our collection of
[plugin
examples](https://github.com/tradingview/lightweight-charts/tree/master/plugin-examples){target="_blank"
rel="noopener noreferrer"} (with a [preview hosted
here](https://tradingview.github.io/lightweight-charts/plugin-examples/){target="_blank"
rel="noopener noreferrer"}) for inspiration and guidance on implementing
specific functionality.

To help you get started quickly, we have created an NPM package called
[create-lwc-plugin](https://www.npmjs.com/package/create-lwc-plugin){target="_blank"
rel="noopener noreferrer"}, which sets up a plugin project for you. This
way, you can hit the ground running with your plugin development.

**Horizontal Scale Customization**

The horizontal scale is no longer restricted to only time-based values.
The API has been extended to allow customization of the horizontal scale
behavior, and enable uses cases like options chart where price values
are displayed in the horizontal scale. The most common use-case would be
to customise the tick marks behaviour.

The [createChartEx](api/functions/createChartEx.html) function should be
used instead of the usual `createChart` function, and an instance of a
class implementing
[IHorzScaleBehavior](api/interfaces/IHorzScaleBehavior.html) should be
provided.

A simple example can be found in this test case:
[horizontal-price-scale.js](https://github.com/tradingview/lightweight-charts/blob/master/tests/e2e/graphics/test-cases/horizontal-price-scale.js){target="_blank"
rel="noopener noreferrer"}

**Enhancements**

- Added point markers styling option for line-based series. (closes
  [#365](https://github.com/tradingview/lightweight-charts/issues/365){target="_blank"
  rel="noopener noreferrer"})
  [Docs](api/interfaces/LineStyleOptions.html#pointmarkersvisible)
- Added double click subscriber for the main chart pane. (closes
  [#1385](https://github.com/tradingview/lightweight-charts/issues/1385){target="_blank"
  rel="noopener noreferrer"})
  [Docs](api/interfaces/IChartApi.html#subscribedblclick)
- Added `setCrosshairPosition` API, allowing programmatic setting of the
  crosshair position. (fixes
  [#1198](https://github.com/tradingview/lightweight-charts/issues/1198){target="_blank"
  rel="noopener noreferrer"},
  [#1163](https://github.com/tradingview/lightweight-charts/issues/1163){target="_blank"
  rel="noopener noreferrer"},
  [#438](https://github.com/tradingview/lightweight-charts/issues/438){target="_blank"
  rel="noopener noreferrer"})
  [Docs](api/interfaces/IChartApi.html#setcrosshairposition)
- Added an option to disable crosshair. Introduced the `Hidden` option
  in the `CrosshairMode` setting. (closes
  [#749](https://github.com/tradingview/lightweight-charts/issues/749){target="_blank"
  rel="noopener noreferrer"}, thanks to
  [\@luk707](https://github.com/luk707){target="_blank"
  rel="noopener noreferrer"})
- Allow overriding tick mark label length via the
  `tickMarkMaxCharacterLength` option. (closes
  [#1396](https://github.com/tradingview/lightweight-charts/issues/1396){target="_blank"
  rel="noopener noreferrer"})
  [Docs](api/interfaces/HorzScaleOptions.html#tickmarkmaxcharacterlength)
- Support for overriding the percentage formatter within the
  localization options. (fixes
  [#1328](https://github.com/tradingview/lightweight-charts/issues/1328){target="_blank"
  rel="noopener noreferrer"},
  [#1291](https://github.com/tradingview/lightweight-charts/issues/1291){target="_blank"
  rel="noopener noreferrer"})
  [Docs](api/interfaces/LocalizationOptions.html#percentageformatter)
- Added `paneSize` getter to `IChartApi`, returning the dimensions of
  the chart pane. (issue
  [#1411](https://github.com/tradingview/lightweight-charts/issues/1411){target="_blank"
  rel="noopener noreferrer"})
  [Docs](api/interfaces/IChartApi.html#panesize)
- Added options to set minimum dimensions for the price and time scales.
  (closes
  [#1062](https://github.com/tradingview/lightweight-charts/issues/1062){target="_blank"
  rel="noopener noreferrer"}, related to
  [#1163](https://github.com/tradingview/lightweight-charts/issues/1163){target="_blank"
  rel="noopener noreferrer"},
  [#50](https://github.com/tradingview/lightweight-charts/issues/50){target="_blank"
  rel="noopener noreferrer"})
  [Docs](api/interfaces/TimeScaleOptions.html#minimumheight),
  [Docs](api/interfaces/PriceScaleOptions.html#minimumwidth)

**Bug Fixes**

- Fixed chart layout when direction is set to RTL. (PR
  [#1338](https://github.com/tradingview/lightweight-charts/pull/1338){target="_blank"
  rel="noopener noreferrer"})
- Fixed re-enabling of `autoSize` after disabling it. (PR
  [#1274](https://github.com/tradingview/lightweight-charts/pull/1377){target="_blank"
  rel="noopener noreferrer"})
- Corrected percentage mode and zero first value. (fixes
  [#1386](https://github.com/tradingview/lightweight-charts/issues/1386){target="_blank"
  rel="noopener noreferrer"})
- Prevent chart shifting when new data replaces existing whitespace.
  (fixes
  [#1201](https://github.com/tradingview/lightweight-charts/issues/1201){target="_blank"
  rel="noopener noreferrer"})

Thanks to our Contributors for this Release:

- [\@luk707](https://github.com/luk707){target="_blank"
  rel="noopener noreferrer"}

You can always send us your feedback via GitHub. We look forward to
hearing from you! And as always, happy trading!

Team TradingView

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/24?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v4.0.1..v4.1.0){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 4.0.1[​](release-notes.html#401 "Direct link to 4.0.1"){.hash-link aria-label="Direct link to 4.0.1"} {#401 .anchor .anchorWithStickyNavbar_LWe7}

**Enhancements**

- Add the ability to specify font colour for the Priceline
  labels. [#1274](https://github.com/tradingview/lightweight-charts/issues/1274){target="_blank"
  rel="noopener noreferrer"}
  [#1287](https://github.com/tradingview/lightweight-charts/issues/1287){target="_blank"
  rel="noopener noreferrer"}
- Ignore resize method if `autoSize` is active, and added API to check
  if active.
  [#1301](https://github.com/tradingview/lightweight-charts/issues/1301){target="_blank"
  rel="noopener noreferrer"}

**Bug fixes**

- Typo in customization guide. Thanks
  [\@UcheAzubuko](https://github.com/UcheAzubuko){target="_blank"
  rel="noopener noreferrer"}.
  [#1284](https://github.com/tradingview/lightweight-charts/issues/1284){target="_blank"
  rel="noopener noreferrer"}
- Inability to immediately add markers when `autoSize` chart option is
  enabled. Thanks
  [\@victorbrambati](https://github.com/victorbrambati){target="_blank"
  rel="noopener noreferrer"}.
  [#1271](https://github.com/tradingview/lightweight-charts/issues/1271){target="_blank"
  rel="noopener noreferrer"}
  [#1281](https://github.com/tradingview/lightweight-charts/issues/1281){target="_blank"
  rel="noopener noreferrer"}
- First render when using `autosize` doesn\'t show the latest bars.
  Thanks
  [\@victorbrambati](https://github.com/victorbrambati){target="_blank"
  rel="noopener noreferrer"}
  [#1281](https://github.com/tradingview/lightweight-charts/issues/1281){target="_blank"
  rel="noopener noreferrer"}.
  [#1282](https://github.com/tradingview/lightweight-charts/issues/1282){target="_blank"
  rel="noopener noreferrer"}
- Series rendering bug when outside of visible
  range. [#1293](https://github.com/tradingview/lightweight-charts/issues/1293){target="_blank"
  rel="noopener noreferrer"}
  [#1294](https://github.com/tradingview/lightweight-charts/issues/1294){target="_blank"
  rel="noopener noreferrer"}
- Auto contrast text color for crosshair labels.
  [#1309](https://github.com/tradingview/lightweight-charts/issues/1309){target="_blank"
  rel="noopener noreferrer"}
  [#1310](https://github.com/tradingview/lightweight-charts/issues/1310){target="_blank"
  rel="noopener noreferrer"}
- Hit box from the text of marker incorrectly shifted to the right.
  [#1270](https://github.com/tradingview/lightweight-charts/issues/1270){target="_blank"
  rel="noopener noreferrer"}
  [#1305](https://github.com/tradingview/lightweight-charts/issues/1305){target="_blank"
  rel="noopener noreferrer"}

As always, we thank you for your support and help in making Lightweight
Charts™ the best product on the financial web. And a big shout out to
our hero
contributors [\@victorbrambati](https://github.com/victorbrambati){target="_blank"
rel="noopener noreferrer"}, and
[\@UcheAzubuko](https://github.com/UcheAzubuko){target="_blank"
rel="noopener noreferrer"}!

You can always send us your feedback via GitHub.

We look forward to hearing from you! And as always, happy trading! Team
TradingView

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/25?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v4.0.0..v4.0.1){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 4.0.0[​](release-notes.html#400 "Direct link to 4.0.0"){.hash-link aria-label="Direct link to 4.0.0"} {#400 .anchor .anchorWithStickyNavbar_LWe7}

Long overdue as it's been nearly 1 year since our last major update, but
behold before all the changes that have happened over the last 12
months.

In total, more than 20 tickets have been addressed with one of the most
HTML canvas in Lightweight Charts™.

Please view the migration guide here: [Migrating from v3 to
v4](migrations/from-v3-to-v4.html).

**Breaking changes**

- Fancy-canvas 2 \|
  [#818](https://github.com/tradingview/lightweight-charts/issues/818){target="_blank"
  rel="noopener noreferrer"}
- Added support for ES module exports \|
  [#613](https://github.com/tradingview/lightweight-charts/issues/613){target="_blank"
  rel="noopener noreferrer"}
- We are now generating two more build types: esm, standalone & cjs
- Updated scales design \|
  [#606](https://github.com/tradingview/lightweight-charts/issues/606){target="_blank"
  rel="noopener noreferrer"}
  - Changed scales look & feel according to the new design
- Add possibility to disable time axis ticks \|
  [#1043](https://github.com/tradingview/lightweight-charts/issues/1043){target="_blank"
  rel="noopener noreferrer"}
- Added `ticksVisible` to `TimeScaleOptions`, renamed `drawTicks` to
  `ticksVisible` in `PriceScaleOptions`.
- Custom price lines should be atop of the series \|
  [#684](https://github.com/tradingview/lightweight-charts/issues/684){target="_blank"
  rel="noopener noreferrer"}
  - Price line to be added on top of any series - shout out to thanhlmm
- Remove deprecated code \|
  [#626](https://github.com/tradingview/lightweight-charts/issues/626){target="_blank"
  rel="noopener noreferrer"}
- Fix types inconsistency on API level with time \|
  [#470](https://github.com/tradingview/lightweight-charts/issues/470){target="_blank"
  rel="noopener noreferrer"}
- Add API to get chart values (data, markers, etc) \|
  [#414](https://github.com/tradingview/lightweight-charts/issues/414){target="_blank"
  rel="noopener noreferrer"}
  - Added methods:
    - `ISeriesApi.markers`
    - `ISeriesApi.dataByIndex`
  - Changed time types everywhere in the public API to `Time`

**Enhancements**

- Handle resize with ResizeObserver if it\'s exist in window \|
  [#71](https://github.com/tradingview/lightweight-charts/issues/71){target="_blank"
  rel="noopener noreferrer"}
  - There was an issue when resizing the chart (such as rotating the
    screen of a phone/tablet).
- Add possibility to use default tick mark formatter implementation as a
  fallback \|
  [#1210](https://github.com/tradingview/lightweight-charts/issues/1210){target="_blank"
  rel="noopener noreferrer"}
  - Allow the custom tick mark formatter to return null so that it will
    use the default formatter for that specific mark.
- Add possibility to invert Area series filled area \|
  [#1115](https://github.com/tradingview/lightweight-charts/issues/1115){target="_blank"
  rel="noopener noreferrer"}
  - Adds invertFilledArea property to the AreaStyleOptions which when
    set to true will invert the filled area (draw above the line instead
    of below it).
- Documentation website improvements \|
  [#1001](https://github.com/tradingview/lightweight-charts/issues/1001){target="_blank"
  rel="noopener noreferrer"}
  [#1002](https://github.com/tradingview/lightweight-charts/issues/1002){target="_blank"
  rel="noopener noreferrer"}
  - Provides a way to apply theme-based colors to a chart whenever the
    Docusaurus theme is changed.
- Add ability to draw parts of area with different colors \|
  [#1100](https://github.com/tradingview/lightweight-charts/issues/1100){target="_blank"
  rel="noopener noreferrer"}
  - Add a possibility to change line, top and bottom colors for the
    different parts of an area series
- Add possibility to change price axis text color \|
  [#1114](https://github.com/tradingview/lightweight-charts/issues/1114){target="_blank"
  rel="noopener noreferrer"}
- Reset price and time scale double click options \|
  [#1118](https://github.com/tradingview/lightweight-charts/issues/1118){target="_blank"
  rel="noopener noreferrer"}
  - Distinguishing the reset between price & time scale vs having only
    one option
- Add curved lines \|
  [#506](https://github.com/tradingview/lightweight-charts/issues/506){target="_blank"
  rel="noopener noreferrer"}
  - Add a new line type that draws curved lines between series points.

**Chores**

- Replace deprecated String.prototype.substr \|
  [#1048](https://github.com/tradingview/lightweight-charts/issues/1048){target="_blank"
  rel="noopener noreferrer"}
  - Shout out to CommanderRoot

**Bug fixes**

- Refactoring resize the chart \|
  [#367](https://github.com/tradingview/lightweight-charts/issues/367){target="_blank"
  rel="noopener noreferrer"}
- The chart is blank on printed page in Chromium \|
  [#873](https://github.com/tradingview/lightweight-charts/issues/873){target="_blank"
  rel="noopener noreferrer"}
  - Chart was blank when printing
- Horizontal scroll animations improvements \|
  [#1136](https://github.com/tradingview/lightweight-charts/issues/1136){target="_blank"
  rel="noopener noreferrer"}
  - Fixes glitches when resetting the chart time scale while scrolling
- Draw series last price & price line labels on the top layer \|
  [#1046](https://github.com/tradingview/lightweight-charts/issues/1046){target="_blank"
  rel="noopener noreferrer"}
  - Fixes an issue where price line could be place over price scale
    labels
- Incorrect price line labels formatting \|
  [#1032](https://github.com/tradingview/lightweight-charts/issues/1032){target="_blank"
  rel="noopener noreferrer"}
  - When setting the price scale mode to anything than \'Normal\' the
    price for PriceLine wasn\'t properly calculated.
- lockVisibleTimeRangeOnResize does not work with fixLeftEdge \|
  [#991](https://github.com/tradingview/lightweight-charts/issues/991){target="_blank"
  rel="noopener noreferrer"}
  - The visible range is no longer changed after resizing the chart.
- Crosshair label text appears on the chart during initial render \|
  [#1255](https://github.com/tradingview/lightweight-charts/issues/1255){target="_blank"
  rel="noopener noreferrer"}
  - Small text artefacts from the crosshair no longer appear on the time
    axis before any interaction with the chart.

As always, we thank you for your support and help in making Lightweight
Charts™ the best product on the financial web. And a big shout out to
our hero contributors
[thanhlmm](https://github.com/thanhlmm){target="_blank"
rel="noopener noreferrer"},
[CommanderRoot](https://github.com/CommanderRoot){target="_blank"
rel="noopener noreferrer"},
[samhainsamhainsamhain](https://github.com/samhainsamhainsamhain){target="_blank"
rel="noopener noreferrer"} & colleague
[Nipheris](https://github.com/Nipheris){target="_blank"
rel="noopener noreferrer"}! You can always send us your feedback via
GitHub. We look forward to hearing from you! And as always, happy
trading! Team TradingView

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/18?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.8.0..v4.0.0){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.8.0[​](release-notes.html#380 "Direct link to 3.8.0"){.hash-link aria-label="Direct link to 3.8.0"} {#380 .anchor .anchorWithStickyNavbar_LWe7}

We\'re happy to announce the next release of Lightweight Charts™
library. This release includes many improvements and bug fixes (as
usual), but we are thrilled to say that from this version the library
has its own [documentation
website](https://tradingview.github.io/lightweight-charts/){target="_blank"
rel="noopener noreferrer"} that replaces the documentation in the
repository. Check it out and share your feedback in [this discussion
thread](https://github.com/tradingview/lightweight-charts/discussions/921){target="_blank"
rel="noopener noreferrer"}.

**Enhancement**

- Documentation website (see
  [#875](https://github.com/tradingview/lightweight-charts/issues/875){target="_blank"
  rel="noopener noreferrer"},
  [#918](https://github.com/tradingview/lightweight-charts/issues/918){target="_blank"
  rel="noopener noreferrer"},
  [#411](https://github.com/tradingview/lightweight-charts/issues/411){target="_blank"
  rel="noopener noreferrer"},
  [#919](https://github.com/tradingview/lightweight-charts/issues/919){target="_blank"
  rel="noopener noreferrer"},
  [#922](https://github.com/tradingview/lightweight-charts/issues/922){target="_blank"
  rel="noopener noreferrer"},
  [#983](https://github.com/tradingview/lightweight-charts/issues/983){target="_blank"
  rel="noopener noreferrer"},
  [#980](https://github.com/tradingview/lightweight-charts/issues/980){target="_blank"
  rel="noopener noreferrer"},
  [#1006](https://github.com/tradingview/lightweight-charts/issues/1006){target="_blank"
  rel="noopener noreferrer"})
- Quick tracking mode (see
  [#830](https://github.com/tradingview/lightweight-charts/issues/830){target="_blank"
  rel="noopener noreferrer"})
- Improved mouse behaviour on touch devices (like mouse connected to
  mobile phone/tablet) (see
  [#106](https://github.com/tradingview/lightweight-charts/issues/106){target="_blank"
  rel="noopener noreferrer"})
- Custom color for items of candlestick and line series (see
  [#195](https://github.com/tradingview/lightweight-charts/issues/195){target="_blank"
  rel="noopener noreferrer"})
- Labels might be cut off when disabling scale and scroll
  ([#947](https://github.com/tradingview/lightweight-charts/issues/947){target="_blank"
  rel="noopener noreferrer"})
- Add ability to disable visibility of price line line (see
  [#969](https://github.com/tradingview/lightweight-charts/issues/969){target="_blank"
  rel="noopener noreferrer"})

**Fixed**

- timeScale.fitContent is not working correctly (see
  [#966](https://github.com/tradingview/lightweight-charts/issues/966){target="_blank"
  rel="noopener noreferrer"})
- Delegate.unsubscribeAll method works in opposite way (see
  [#995](https://github.com/tradingview/lightweight-charts/issues/995){target="_blank"
  rel="noopener noreferrer"})
- Last price animation is active when no data added to the right (but to
  the left) (see
  [#886](https://github.com/tradingview/lightweight-charts/issues/886){target="_blank"
  rel="noopener noreferrer"})
- subscribeClick on mobile always get the last index of all the items
  (see
  [#657](https://github.com/tradingview/lightweight-charts/issues/657){target="_blank"
  rel="noopener noreferrer"})
- Incorrect crosshair position on scrolling by dragging by mouse (see
  [#987](https://github.com/tradingview/lightweight-charts/issues/987){target="_blank"
  rel="noopener noreferrer"})
- A painting slows down after a while with tons of updates (see
  [#946](https://github.com/tradingview/lightweight-charts/issues/946){target="_blank"
  rel="noopener noreferrer"})
- Bars disappear with devicePixelRatio less than 1 (see
  [#982](https://github.com/tradingview/lightweight-charts/issues/982){target="_blank"
  rel="noopener noreferrer"})
- There are no tick marks on the price axis (see
  [#939](https://github.com/tradingview/lightweight-charts/issues/939){target="_blank"
  rel="noopener noreferrer"})
- Disabling scrolling by disabled horzTouchDrag and vertTouchDrag
  options disables moving crosshair in tracking mode (see
  [#434](https://github.com/tradingview/lightweight-charts/issues/434){target="_blank"
  rel="noopener noreferrer"})
- Reducing precision doesn\'t update price scale width (see
  [#550](https://github.com/tradingview/lightweight-charts/issues/550){target="_blank"
  rel="noopener noreferrer"})
- Chart width is jumping on series change from area to candles (see
  [#943](https://github.com/tradingview/lightweight-charts/issues/943){target="_blank"
  rel="noopener noreferrer"})
- Log axis is not scaling on small number (see
  [#874](https://github.com/tradingview/lightweight-charts/issues/874){target="_blank"
  rel="noopener noreferrer"})
- Overlay series title is not rendered when no series use right price
  scale (see
  [#926](https://github.com/tradingview/lightweight-charts/issues/926){target="_blank"
  rel="noopener noreferrer"})
- scrollToPosition with big negative value and when no data breaks the
  chart (see
  [#889](https://github.com/tradingview/lightweight-charts/issues/889){target="_blank"
  rel="noopener noreferrer"})
- When rendering multiple charts with baseline series, baseValue of the
  last element is used on all charts series. (see
  [#898](https://github.com/tradingview/lightweight-charts/issues/898){target="_blank"
  rel="noopener noreferrer"})

Thanks to our contributors:

- [\@zaleGZL](https://github.com/zaleGZL){target="_blank"
  rel="noopener noreferrer"} zale

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/23?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.7.0..v3.8.0){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.7.0[​](release-notes.html#370 "Direct link to 3.7.0"){.hash-link aria-label="Direct link to 3.7.0"} {#370 .anchor .anchorWithStickyNavbar_LWe7}

**Enhancement**

- The new baseline series chart (see
  [#151](https://github.com/tradingview/lightweight-charts/issues/151){target="_blank"
  rel="noopener noreferrer"})
- Documentation about time zones support (see
  [#781](https://github.com/tradingview/lightweight-charts/issues/781){target="_blank"
  rel="noopener noreferrer"})
- Added methods to get time axis size and subscribe on size change (see
  [#853](https://github.com/tradingview/lightweight-charts/issues/853){target="_blank"
  rel="noopener noreferrer"})
- Improved performance of setting/updating series data (see
  [#418](https://github.com/tradingview/lightweight-charts/issues/418){target="_blank"
  rel="noopener noreferrer"} and
  [#838](https://github.com/tradingview/lightweight-charts/issues/838){target="_blank"
  rel="noopener noreferrer"})
- Use lowerbound in TimeScale timeToIndex search (see
  [#767](https://github.com/tradingview/lightweight-charts/issues/767){target="_blank"
  rel="noopener noreferrer"})
- Add JSDoc comments for existing API docs (see
  [#870](https://github.com/tradingview/lightweight-charts/issues/870){target="_blank"
  rel="noopener noreferrer"})

**Fixed**

- Increased min price tick mark step up to 1e-14 (from 1e-9) (see
  [#841](https://github.com/tradingview/lightweight-charts/issues/841){target="_blank"
  rel="noopener noreferrer"})
- Fix typo in customization docs (see
  [#844](https://github.com/tradingview/lightweight-charts/issues/844){target="_blank"
  rel="noopener noreferrer"})
- Do not paint time axis if it not visible (see
  [#865](https://github.com/tradingview/lightweight-charts/issues/865){target="_blank"
  rel="noopener noreferrer"})
- Remove color customisation from settings.json (see
  [#869](https://github.com/tradingview/lightweight-charts/issues/869){target="_blank"
  rel="noopener noreferrer"})

Thanks to our contributors:

- [\@thanhlmm](https://github.com/thanhlmm){target="_blank"
  rel="noopener noreferrer"} Thanh Le

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/22?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.6.1..v3.7.0){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.6.1[​](release-notes.html#361 "Direct link to 3.6.1"){.hash-link aria-label="Direct link to 3.6.1"} {#361 .anchor .anchorWithStickyNavbar_LWe7}

**Fixed**

- In v3.6.0 there was a typo in `LasPriceAnimationMode` const enum
  (`Last` without `t`), which was fixed in this release. The incorrect
  name is still available to import and could be used in your code so no
  breaking change so far (see e5133cb0c50fc557182aba4011e170aaf30a5b1a)

See [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.6.0..v3.6.1){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.6.0[​](release-notes.html#360 "Direct link to 3.6.0"){.hash-link aria-label="Direct link to 3.6.0"} {#360 .anchor .anchorWithStickyNavbar_LWe7}

On this day 10 years ago, 10th September 2011, the very first version of
the TradingView website was deployed. To celebrate 10th anniversary
we\'re happy to announce the new version of lightweight-charts library
v3.6.0 🎉🎉🎉

**Enhancement**

- Gradient chart background color (see
  [#831](https://github.com/tradingview/lightweight-charts/issues/831){target="_blank"
  rel="noopener noreferrer"})
- How to add buffer animation to price jump (see
  [#567](https://github.com/tradingview/lightweight-charts/issues/567){target="_blank"
  rel="noopener noreferrer"})
- Kinetic scroll (see
  [#832](https://github.com/tradingview/lightweight-charts/issues/832){target="_blank"
  rel="noopener noreferrer"})

**Fixed**

- Incorrect initial barSpacing when both fixRightEdge and fixLeftEdge
  are enabled (see
  [#823](https://github.com/tradingview/lightweight-charts/issues/823){target="_blank"
  rel="noopener noreferrer"})
- Time axis label get cut on the edge if a fix edge option is enabled
  (see
  [#835](https://github.com/tradingview/lightweight-charts/issues/835){target="_blank"
  rel="noopener noreferrer"})
- Price axis doesn\'t respect the width of crosshair label (see
  [#834](https://github.com/tradingview/lightweight-charts/issues/834){target="_blank"
  rel="noopener noreferrer"})
- Fixed both timescale edges make lockVisibleTimeRangeOnResize turn
  wrong (see
  [#814](https://github.com/tradingview/lightweight-charts/issues/814){target="_blank"
  rel="noopener noreferrer"})
- `Error: Value is null` error while set the data is container has 0x0
  size (see
  [#821](https://github.com/tradingview/lightweight-charts/issues/821){target="_blank"
  rel="noopener noreferrer"})

Thanks to our contributors:

- [\@thanhlmm](https://github.com/thanhlmm){target="_blank"
  rel="noopener noreferrer"} Thanh Le

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/21?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.5.0..v3.6.0){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.5.0[​](release-notes.html#350 "Direct link to 3.5.0"){.hash-link aria-label="Direct link to 3.5.0"} {#350 .anchor .anchorWithStickyNavbar_LWe7}

**A note about rendering order of series, which might be interpret as a
bug or breaking change since this release**

This is not really a breaking change, but might be interpret like that.
In
[#794](https://github.com/tradingview/lightweight-charts/issues/794){target="_blank"
rel="noopener noreferrer"} we\'ve fixed the wrong order of series, thus
now all series will be displayed in opposite order (they will be
displayed in order of creating now; previously they were displayed in
reversed order).

To fix that, just change the order of creating the series (thus instead
of create series A, then series B create series B first and then series
A) - see
[#812](https://github.com/tradingview/lightweight-charts/issues/812){target="_blank"
rel="noopener noreferrer"}.

**Fixed**

- Screenshot output missing piece on bottom right (see
  [#798](https://github.com/tradingview/lightweight-charts/issues/798){target="_blank"
  rel="noopener noreferrer"})
- Overlapped line chart show wrong color order when hover (see
  [#794](https://github.com/tradingview/lightweight-charts/issues/794){target="_blank"
  rel="noopener noreferrer"})
- Price line label show on both axis (see
  [#795](https://github.com/tradingview/lightweight-charts/issues/795){target="_blank"
  rel="noopener noreferrer"})

Thanks to our contributors:

- [\@thanhlmm](https://github.com/thanhlmm){target="_blank"
  rel="noopener noreferrer"} Thanh Le

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/20?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.4.0..v3.5.0){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.4.0[​](release-notes.html#340 "Direct link to 3.4.0"){.hash-link aria-label="Direct link to 3.4.0"} {#340 .anchor .anchorWithStickyNavbar_LWe7}

**Enhancement**

- Add option to fix right edge (see
  [#218](https://github.com/tradingview/lightweight-charts/issues/218){target="_blank"
  rel="noopener noreferrer"})
- Drop restriction for min bar spacing value (see
  [#558](https://github.com/tradingview/lightweight-charts/issues/558){target="_blank"
  rel="noopener noreferrer"})
- Round corners of the line-style plots (see
  [#731](https://github.com/tradingview/lightweight-charts/issues/731){target="_blank"
  rel="noopener noreferrer"})

**Fixed**

- AutoscaleProvider documentation error (see
  [#773](https://github.com/tradingview/lightweight-charts/issues/773){target="_blank"
  rel="noopener noreferrer"})
- Candlestick upColor and downColor is not changed on applyOptions (see
  [#750](https://github.com/tradingview/lightweight-charts/issues/750){target="_blank"
  rel="noopener noreferrer"})
- Cleared and reset data appears at visually different location (see
  [#757](https://github.com/tradingview/lightweight-charts/issues/757){target="_blank"
  rel="noopener noreferrer"})
- Remove unused internal method from SeriesApi (see
  [#768](https://github.com/tradingview/lightweight-charts/issues/768){target="_blank"
  rel="noopener noreferrer"})
- Removing data for the last series doesn\'t actually remove the data
  (see
  [#752](https://github.com/tradingview/lightweight-charts/issues/752){target="_blank"
  rel="noopener noreferrer"})
- `to` date of getVisibleRange contains partially visible data item and
  it\'s impossible to hover it (see
  [#624](https://github.com/tradingview/lightweight-charts/issues/624){target="_blank"
  rel="noopener noreferrer"})
- series.priceFormatter().format(price) does not work (see
  [#790](https://github.com/tradingview/lightweight-charts/issues/790){target="_blank"
  rel="noopener noreferrer"})

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/19?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.3.0..v3.4.0){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.3.0[​](release-notes.html#330 "Direct link to 3.3.0"){.hash-link aria-label="Direct link to 3.3.0"} {#330 .anchor .anchorWithStickyNavbar_LWe7}

**Enhancement**

- Add type predicates for series type (see
  [#670](https://github.com/tradingview/lightweight-charts/issues/670){target="_blank"
  rel="noopener noreferrer"})
- Create Grid instance for every pane (see
  [#382](https://github.com/tradingview/lightweight-charts/issues/382){target="_blank"
  rel="noopener noreferrer"})
- Add possibility to chose crosshairMarker color, so it will be
  independent from line-series color (see
  [#310](https://github.com/tradingview/lightweight-charts/issues/310){target="_blank"
  rel="noopener noreferrer"})
- Implement option not to shift the time scale at all when data is added
  with `setData` (see
  [#584](https://github.com/tradingview/lightweight-charts/issues/584){target="_blank"
  rel="noopener noreferrer"})

**Fixed**

- Incorrect bar height when its value is more than chart\'s height (see
  [#673](https://github.com/tradingview/lightweight-charts/issues/673){target="_blank"
  rel="noopener noreferrer"})
- Disabling autoScale for non-visible series (see
  [#687](https://github.com/tradingview/lightweight-charts/issues/687){target="_blank"
  rel="noopener noreferrer"})

Thanks to our contributors:

- [\@dubroff](https://github.com/dubroff){target="_blank"
  rel="noopener noreferrer"}
- [\@SuperPenguin](https://github.com/SuperPenguin){target="_blank"
  rel="noopener noreferrer"} Andree Yosua
- [\@mecm1993](https://github.com/mecm1993){target="_blank"
  rel="noopener noreferrer"} Manuel Cepeda

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/17?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.2.0..v3.3.0){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.2.0[​](release-notes.html#320 "Direct link to 3.2.0"){.hash-link aria-label="Direct link to 3.2.0"} {#320 .anchor .anchorWithStickyNavbar_LWe7}

**Enhancement**

- Feat/gzip friendly colors (see
  [#598](https://github.com/tradingview/lightweight-charts/issues/598){target="_blank"
  rel="noopener noreferrer"})
- Add coordinateToLogical and logicalToCoordinate (see
  [#587](https://github.com/tradingview/lightweight-charts/issues/587){target="_blank"
  rel="noopener noreferrer"})
- Add API to show/hide series without removing it (see
  [#471](https://github.com/tradingview/lightweight-charts/issues/471){target="_blank"
  rel="noopener noreferrer"})
- Add run-time validation of inputs in debug mode (see
  [#315](https://github.com/tradingview/lightweight-charts/issues/315){target="_blank"
  rel="noopener noreferrer"})
- Pixel perfect renderers fixes (see
  [#535](https://github.com/tradingview/lightweight-charts/issues/535){target="_blank"
  rel="noopener noreferrer"})
- Add title option to createPriceLine (see
  [#357](https://github.com/tradingview/lightweight-charts/issues/357){target="_blank"
  rel="noopener noreferrer"})

**Fixed**

- Set rightOffset and scrollToPosition async as well as setVisibleRange
  (see
  [#406](https://github.com/tradingview/lightweight-charts/issues/406){target="_blank"
  rel="noopener noreferrer"})
- timeScale() changes visible range on setData() (see
  [#549](https://github.com/tradingview/lightweight-charts/issues/549){target="_blank"
  rel="noopener noreferrer"})
- Remove chart\'s size restriction or make it smaller (see
  [#366](https://github.com/tradingview/lightweight-charts/issues/366){target="_blank"
  rel="noopener noreferrer"})
- LineStyle.Dotted make no effect (see
  [#572](https://github.com/tradingview/lightweight-charts/issues/572){target="_blank"
  rel="noopener noreferrer"})
- If priceScaleId is empty string, invalid price scale api is returned
  (see
  [#537](https://github.com/tradingview/lightweight-charts/issues/537){target="_blank"
  rel="noopener noreferrer"})
- Incorrect Selection seen on long press in ios webview on chart (see
  [#609](https://github.com/tradingview/lightweight-charts/issues/609){target="_blank"
  rel="noopener noreferrer"})
- One-point line series is invisible (see
  [#597](https://github.com/tradingview/lightweight-charts/issues/597){target="_blank"
  rel="noopener noreferrer"})
- Empty price scale after creating series with the same price range (see
  [#615](https://github.com/tradingview/lightweight-charts/issues/615){target="_blank"
  rel="noopener noreferrer"})

**Infra and dev env**

- Compress artifacts in graphics tests in CI (see
  [#145](https://github.com/tradingview/lightweight-charts/issues/145){target="_blank"
  rel="noopener noreferrer"})
- Run tests against production build (see
  [#503](https://github.com/tradingview/lightweight-charts/issues/503){target="_blank"
  rel="noopener noreferrer"})
- Add test to check code usage coverage (see
  [#495](https://github.com/tradingview/lightweight-charts/issues/495){target="_blank"
  rel="noopener noreferrer"})
- Migrate from codechecks (see
  [#356](https://github.com/tradingview/lightweight-charts/issues/356){target="_blank"
  rel="noopener noreferrer"})
- Updated dev deps

Thanks to our contributors:

- Andree Yosua
  [\@SuperPenguin](https://github.com/SuperPenguin){target="_blank"
  rel="noopener noreferrer"}
- Christos [\@christose](https://github.com/christose){target="_blank"
  rel="noopener noreferrer"}
- Shergin Rodion
  [\@beholderrk](https://github.com/beholderrk){target="_blank"
  rel="noopener noreferrer"}
- wenhoujx [\@wenhoujx](https://github.com/wenhoujx){target="_blank"
  rel="noopener noreferrer"}

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/11?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.1.5..v3.2.0){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.1.5[​](release-notes.html#315 "Direct link to 3.1.5"){.hash-link aria-label="Direct link to 3.1.5"} {#315 .anchor .anchorWithStickyNavbar_LWe7}

It\'s a just re-published accidentally published 3.1.4 version, which
didn\'t actually fix the issue
[#536](https://github.com/tradingview/lightweight-charts/issues/536){target="_blank"
rel="noopener noreferrer"}.

Version 3.1.4 has been deprecated.

**Fixed**

- TypeError `_internal_priceScale is not a function` while getting
  series price scale (see
  [#536](https://github.com/tradingview/lightweight-charts/issues/536){target="_blank"
  rel="noopener noreferrer"})

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/16?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.1.3..v3.1.5){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.1.3[​](release-notes.html#313 "Direct link to 3.1.3"){.hash-link aria-label="Direct link to 3.1.3"} {#313 .anchor .anchorWithStickyNavbar_LWe7}

**Fixed**

- `handleScroll` and `handleScale` options aren\'t applied (see
  [#527](https://github.com/tradingview/lightweight-charts/issues/527){target="_blank"
  rel="noopener noreferrer"})

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/14?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.1.2..v3.1.3){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.1.2[​](release-notes.html#312 "Direct link to 3.1.2"){.hash-link aria-label="Direct link to 3.1.2"} {#312 .anchor .anchorWithStickyNavbar_LWe7}

**Fixed**

- Crosshair doesn\'t work on touch devices (see
  [#511](https://github.com/tradingview/lightweight-charts/issues/511){target="_blank"
  rel="noopener noreferrer"})

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/13?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.1.1..v3.1.2){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.1.1[​](release-notes.html#311 "Direct link to 3.1.1"){.hash-link aria-label="Direct link to 3.1.1"} {#311 .anchor .anchorWithStickyNavbar_LWe7}

**Fixed**

- Fixed production build of 3.1 version (see
  [#502](https://github.com/tradingview/lightweight-charts/issues/502){target="_blank"
  rel="noopener noreferrer"} and
  [62aa93724e40fbb1b678d9b44655279a1df529c5](https://github.com/tradingview/lightweight-charts/commit/62aa93724e40fbb1b678d9b44655279a1df529c5){target="_blank"
  rel="noopener noreferrer"})

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/12?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.1.0..v3.1.1){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.1.0[​](release-notes.html#310 "Direct link to 3.1.0"){.hash-link aria-label="Direct link to 3.1.0"} {#310 .anchor .anchorWithStickyNavbar_LWe7}

**Enhancement**

- Whitespaces support (see
  [#209](https://github.com/tradingview/lightweight-charts/issues/209){target="_blank"
  rel="noopener noreferrer"})
- Custom font families for watermarks (see
  [#437](https://github.com/tradingview/lightweight-charts/issues/437){target="_blank"
  rel="noopener noreferrer"})

**Fixed**

- Added support for \'transparent\' color (see
  [#491](https://github.com/tradingview/lightweight-charts/issues/491){target="_blank"
  rel="noopener noreferrer"})
- Refactor DataLayer/ChartApi (see
  [#270](https://github.com/tradingview/lightweight-charts/issues/270){target="_blank"
  rel="noopener noreferrer"})
- Remove series then scroll to right after not working (see
  [#355](https://github.com/tradingview/lightweight-charts/issues/355){target="_blank"
  rel="noopener noreferrer"})
- Scaling via mouse click and drag doesn\'t work if chart is inside
  shadow root (see
  [#427](https://github.com/tradingview/lightweight-charts/issues/427){target="_blank"
  rel="noopener noreferrer"})
- Applying watermark in setTimeout doesn\'t make an effect (see
  [#485](https://github.com/tradingview/lightweight-charts/issues/485){target="_blank"
  rel="noopener noreferrer"})
- Importing the library in server-side context caused `ReferenceError`
  (see
  [#446](https://github.com/tradingview/lightweight-charts/issues/446){target="_blank"
  rel="noopener noreferrer"})

**Undocumented breaking changes**

We know that some of users probably used some hacky-workarounds calling
internal methods to achieve multi-pane support. In this release, to
reduce size of the bundle we [dropped out a code for pane\'s
separator](https://github.com/tradingview/lightweight-charts/pull/496){target="_blank"
rel="noopener noreferrer"} (which allows to resize panes).

As soon this workaround is undocumented and we don\'t support this
feature yet - we don\'t bump a major version. But we think it\'s better
to let you know that it has been changed.

**Development**

- Dropped support NodeJS \< 12.18
- Migrated from TSLint to ESLint (see
  [#314](https://github.com/tradingview/lightweight-charts/issues/314){target="_blank"
  rel="noopener noreferrer"})
- Migrated from clean-publish to in-house script to clear package.json
  (see
  [#474](https://github.com/tradingview/lightweight-charts/issues/474){target="_blank"
  rel="noopener noreferrer"})

Thanks to our contributors:

- Meet Mangukiya
  [\@meetmangukiya](https://github.com/meetmangukiya){target="_blank"
  rel="noopener noreferrer"}
- NekitCorp [\@NekitCorp](https://github.com/NekitCorp){target="_blank"
  rel="noopener noreferrer"}

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/9?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.0.1..v3.1.0){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.0.1[​](release-notes.html#301 "Direct link to 3.0.1"){.hash-link aria-label="Direct link to 3.0.1"} {#301 .anchor .anchorWithStickyNavbar_LWe7}

**Fixed**

- Correctly handle `overlay: true` in series options while create series
  to backward compat (see
  [#475](https://github.com/tradingview/lightweight-charts/issues/475){target="_blank"
  rel="noopener noreferrer"})

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/10?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v3.0.0..v3.0.1){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 3.0.0[​](release-notes.html#300 "Direct link to 3.0.0"){.hash-link aria-label="Direct link to 3.0.0"} {#300 .anchor .anchorWithStickyNavbar_LWe7}

**Breaking changes**

We have some breaking changes since the latest version due some features
and API improvements:

- Methods `subscribeVisibleTimeRangeChange` and
  `unsubscribeVisibleTimeRangeChange` has been moved from ChartApi to
  TimeScaleApi
- Since 3.0 you can specify price axis you\'d like to place the series
  on. The same for moving the series between price scales (see migration
  guide below)

See [breaking changes
doc](https://github.com/tradingview/lightweight-charts/blob/master/docs/3.0-breaking-changes.md){target="_blank"
rel="noopener noreferrer"} with migration guide to migrate smoothly.

**Enhancement**

- Added ability to customize time scale tick marks formatter (see
  [#226](https://github.com/tradingview/lightweight-charts/issues/226){target="_blank"
  rel="noopener noreferrer"})
- Added ability to put text for series markers (see
  [#207](https://github.com/tradingview/lightweight-charts/issues/207){target="_blank"
  rel="noopener noreferrer"})
- Added ability to specify your own date formatter (see
  [#368](https://github.com/tradingview/lightweight-charts/issues/368){target="_blank"
  rel="noopener noreferrer"})
- Improved tick marks generation algorithm for the first point (see
  [#387](https://github.com/tradingview/lightweight-charts/issues/387){target="_blank"
  rel="noopener noreferrer"})
- Made inbound types weakly (outbound ones should be strict) (see
  [#374](https://github.com/tradingview/lightweight-charts/issues/374){target="_blank"
  rel="noopener noreferrer"})
- Removed non-exported const enum\'s JS code (see
  [#432](https://github.com/tradingview/lightweight-charts/issues/432){target="_blank"
  rel="noopener noreferrer"})
- Introduced
  [ts-transformer-properties-rename](https://github.com/timocov/ts-transformer-properties-rename){target="_blank"
  rel="noopener noreferrer"} instead of
  [ts-transformer-minify-privates](https://github.com/timocov/ts-transformer-minify-privates){target="_blank"
  rel="noopener noreferrer"} (see
  [#436](https://github.com/tradingview/lightweight-charts/issues/436){target="_blank"
  rel="noopener noreferrer"})

**Added**

- Add ability to override series\' autoscale range (see
  [#392](https://github.com/tradingview/lightweight-charts/issues/392){target="_blank"
  rel="noopener noreferrer"})
- Add API to get price scale\'s width (see
  [#452](https://github.com/tradingview/lightweight-charts/issues/452){target="_blank"
  rel="noopener noreferrer"})
- Disabling/enabling scaling axis for both price and time (see
  [#440](https://github.com/tradingview/lightweight-charts/issues/440){target="_blank"
  rel="noopener noreferrer"})
- Get screen coordinate by a time point (see
  [#435](https://github.com/tradingview/lightweight-charts/issues/435){target="_blank"
  rel="noopener noreferrer"})
- Remove tick mark from price label (see
  [#378](https://github.com/tradingview/lightweight-charts/issues/378){target="_blank"
  rel="noopener noreferrer"})
- Support the second price axis (see
  [#129](https://github.com/tradingview/lightweight-charts/issues/129){target="_blank"
  rel="noopener noreferrer"})
- Visible time range should have bars count of the space from left/right
  (see
  [#335](https://github.com/tradingview/lightweight-charts/issues/335){target="_blank"
  rel="noopener noreferrer"})

**Fixed**

- `series.setMarkers` requires at least one data point (see
  [#372](https://github.com/tradingview/lightweight-charts/issues/372){target="_blank"
  rel="noopener noreferrer"})
- Impossible to override the only width or height in constructor (see
  [#353](https://github.com/tradingview/lightweight-charts/issues/353){target="_blank"
  rel="noopener noreferrer"})
- Incorrect alignment of markers if series has gaps (see
  [#464](https://github.com/tradingview/lightweight-charts/issues/464){target="_blank"
  rel="noopener noreferrer"})
- Multiple series: error while trying to scroll the chart (see
  [#373](https://github.com/tradingview/lightweight-charts/issues/373){target="_blank"
  rel="noopener noreferrer"})
- Replace const enums with enums to let use them in projects with
  enabled isolatedModules option (see
  [#375](https://github.com/tradingview/lightweight-charts/issues/375){target="_blank"
  rel="noopener noreferrer"})

Thanks to our contributors:

- Ben Guidarelli
  [\@barnjamin](https://github.com/barnjamin){target="_blank"
  rel="noopener noreferrer"}
- gkaindl [\@gkaindl](https://github.com/gkaindl){target="_blank"
  rel="noopener noreferrer"}
- scrwdrv [\@scrwdrv](https://github.com/scrwdrv){target="_blank"
  rel="noopener noreferrer"}
- Yusuf Sahin HAMZA
  [\@yusufsahinhamza](https://github.com/yusufsahinhamza){target="_blank"
  rel="noopener noreferrer"}

See [issues assigned to this version\'s
milestone](https://github.com/tradingview/lightweight-charts/milestone/7?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v2.0.0..v3.0.0){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 2.0.0[​](release-notes.html#200 "Direct link to 2.0.0"){.hash-link aria-label="Direct link to 2.0.0"} {#200 .anchor .anchorWithStickyNavbar_LWe7}

**Breaking changes**

- Removed unused `lineWidth` property from `HistogramStyleOptions`
  interface (it affects nothing, but could break your compilation)
- Changed order of `width` and `height` args in `resize` method
  ([#157](https://github.com/tradingview/lightweight-charts/issues/157){target="_blank"
  rel="noopener noreferrer"})
- Pattern for all non-solid (dotted, dashed, large dashed and sparse
  dotted) line styles was a bit changed
  ([#274](https://github.com/tradingview/lightweight-charts/issues/274){target="_blank"
  rel="noopener noreferrer"})

**Enhancement**

- Pixel-perfect rendering
  ([#274](https://github.com/tradingview/lightweight-charts/issues/274){target="_blank"
  rel="noopener noreferrer"})
- Time scale enhancements
  ([#352](https://github.com/tradingview/lightweight-charts/issues/352){target="_blank"
  rel="noopener noreferrer"})

**Added**

- Disable all kinds of scrolls and touch with one option
  ([#230](https://github.com/tradingview/lightweight-charts/issues/230){target="_blank"
  rel="noopener noreferrer"})
- Added to the acceptable date formats
  ([#296](https://github.com/tradingview/lightweight-charts/issues/296){target="_blank"
  rel="noopener noreferrer"})
- Add option to show the \"global\" last value of the series instead of
  the last visible
  ([#203](https://github.com/tradingview/lightweight-charts/issues/203){target="_blank"
  rel="noopener noreferrer"})

**Fixed**

- Price line didn\`t hightlight price
  ([#273](https://github.com/tradingview/lightweight-charts/issues/273){target="_blank"
  rel="noopener noreferrer"})
- CreatePriceLine not removed
  ([#285](https://github.com/tradingview/lightweight-charts/issues/285){target="_blank"
  rel="noopener noreferrer"})
- Crosshair line not visible when priceScale position set to none
  ([#302](https://github.com/tradingview/lightweight-charts/issues/302){target="_blank"
  rel="noopener noreferrer"})
- chart.resize parameter is inverted
  ([#157](https://github.com/tradingview/lightweight-charts/issues/157){target="_blank"
  rel="noopener noreferrer"})
- Removed unnecessary spacing from left/right (1 bar from each side) in
  `fitContent`
  ([#345](https://github.com/tradingview/lightweight-charts/issues/345){target="_blank"
  rel="noopener noreferrer"})

Thanks to our contributors:

- Andree Yosua
  [\@SuperPenguin](https://github.com/SuperPenguin){target="_blank"
  rel="noopener noreferrer"}
- kpaape [\@kpaape](https://github.com/kpaape){target="_blank"
  rel="noopener noreferrer"}
- Matt Conway [\@mattsre](https://github.com/mattsre){target="_blank"
  rel="noopener noreferrer"}

See [issues assigned to this version's
milestone](https://github.com/tradingview/lightweight-charts/milestone/6?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v1.2.2..v2.0.0){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 1.2.2[​](release-notes.html#122 "Direct link to 1.2.2"){.hash-link aria-label="Direct link to 1.2.2"} {#122 .anchor .anchorWithStickyNavbar_LWe7}

**Fixed**

- Bug while rendering few datasets with not equal timescale
  ([#321](https://github.com/tradingview/lightweight-charts/issues/321){target="_blank"
  rel="noopener noreferrer"})

------------------------------------------------------------------------

## 1.2.1[​](release-notes.html#121 "Direct link to 1.2.1"){.hash-link aria-label="Direct link to 1.2.1"} {#121 .anchor .anchorWithStickyNavbar_LWe7}

**Added**

- Add custom price lines
  ([#183](https://github.com/tradingview/lightweight-charts/issues/183){target="_blank"
  rel="noopener noreferrer"})
- Migrate canvas-related logic to fancy-canvas library
  ([#141](https://github.com/tradingview/lightweight-charts/issues/141){target="_blank"
  rel="noopener noreferrer"})
- Add coordinateToPrice method to ISeriesApi
  ([#171](https://github.com/tradingview/lightweight-charts/issues/171){target="_blank"
  rel="noopener noreferrer"})

**Fixed**

- Scrolling by price is incorrect
  ([#213](https://github.com/tradingview/lightweight-charts/issues/213){target="_blank"
  rel="noopener noreferrer"})
- Histogram (volume) does not honor color setting (sometimes)
  ([#233](https://github.com/tradingview/lightweight-charts/issues/233){target="_blank"
  rel="noopener noreferrer"})
- Logarithmic scaling is applied to volume
  ([#227](https://github.com/tradingview/lightweight-charts/issues/227){target="_blank"
  rel="noopener noreferrer"})
- hoveredSeries in mouse events params is always undefined
  ([#190](https://github.com/tradingview/lightweight-charts/issues/190){target="_blank"
  rel="noopener noreferrer"})
- `lineType` option does not work for area/line series
  ([#220](https://github.com/tradingview/lightweight-charts/issues/220){target="_blank"
  rel="noopener noreferrer"})
- Double clicking on time scale will reset fix left edge
  ([#224](https://github.com/tradingview/lightweight-charts/issues/224){target="_blank"
  rel="noopener noreferrer"})
- Series\' marker does not aligned after autoscale
  ([#212](https://github.com/tradingview/lightweight-charts/issues/212){target="_blank"
  rel="noopener noreferrer"})
- Error on setData empty array for overlay histogram series
  ([#267](https://github.com/tradingview/lightweight-charts/issues/267){target="_blank"
  rel="noopener noreferrer"})
- Added some missing docs
  ([#211](https://github.com/tradingview/lightweight-charts/issues/211){target="_blank"
  rel="noopener noreferrer"}
  [#193](https://github.com/tradingview/lightweight-charts/issues/193){target="_blank"
  rel="noopener noreferrer"}
  [#245](https://github.com/tradingview/lightweight-charts/issues/245){target="_blank"
  rel="noopener noreferrer"})

See [issues assigned to this version's
milestone](https://github.com/tradingview/lightweight-charts/milestone/4?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v1.1.0...v1.2.1){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 1.1.0[​](release-notes.html#110 "Direct link to 1.1.0"){.hash-link aria-label="Direct link to 1.1.0"} {#110 .anchor .anchorWithStickyNavbar_LWe7}

**Added**

- Apply localization to specific series
  ([#62](https://github.com/tradingview/lightweight-charts/issues/62){target="_blank"
  rel="noopener noreferrer"})
- Series-based markers
  ([#24](https://github.com/tradingview/lightweight-charts/issues/24){target="_blank"
  rel="noopener noreferrer"})
- Reduced size of the library by using
  [`ts-transformer-minify-privates`](https://github.com/timocov/ts-transformer-minify-privates){target="_blank"
  rel="noopener noreferrer"} transformer
  ([#98](https://github.com/tradingview/lightweight-charts/issues/98){target="_blank"
  rel="noopener noreferrer"})

**Fixed**

- The chart can\'t start from the left
  ([#144](https://github.com/tradingview/lightweight-charts/issues/144){target="_blank"
  rel="noopener noreferrer"})
- OHLC charts render incorrect when `value` is provided
  ([#165](https://github.com/tradingview/lightweight-charts/issues/165){target="_blank"
  rel="noopener noreferrer"})
- Price axis is not shown if series is created inside promise chain
  ([#164](https://github.com/tradingview/lightweight-charts/issues/164){target="_blank"
  rel="noopener noreferrer"})
- The line chart can\'t move to the left
  ([#143](https://github.com/tradingview/lightweight-charts/issues/143){target="_blank"
  rel="noopener noreferrer"})
- Lots of non-passive event listener warnings
  ([#139](https://github.com/tradingview/lightweight-charts/issues/139){target="_blank"
  rel="noopener noreferrer"})
- applyOptions of histogram series with color doesn\'t affect the data
  ([#112](https://github.com/tradingview/lightweight-charts/issues/112){target="_blank"
  rel="noopener noreferrer"})
- Price Axis Scaling Bug
  ([#122](https://github.com/tradingview/lightweight-charts/issues/122){target="_blank"
  rel="noopener noreferrer"})
- LineSeries is not displayed if starting x value is out of viewport
  ([#116](https://github.com/tradingview/lightweight-charts/issues/116){target="_blank"
  rel="noopener noreferrer"})
- Crosshair isn\'t updated when timescale is changed
  ([#120](https://github.com/tradingview/lightweight-charts/issues/120){target="_blank"
  rel="noopener noreferrer"})
- Pinch isn\'t prevented by long tap
  ([#95](https://github.com/tradingview/lightweight-charts/issues/95){target="_blank"
  rel="noopener noreferrer"})

Thanks to our contributors:

- zach [\@n8tb1t](https://github.com/n8tb1t){target="_blank"
  rel="noopener noreferrer"}
- Chris Kaczor
  [\@krzkaczor](https://github.com/krzkaczor){target="_blank"
  rel="noopener noreferrer"}

See [issues assigned to this version's
milestone](https://github.com/tradingview/lightweight-charts/milestone/2?closed=1){target="_blank"
rel="noopener noreferrer"} or [changes since the last published
version](https://github.com/tradingview/lightweight-charts/compare/v1.0.2...v1.1.0){target="_blank"
rel="noopener noreferrer"}.

------------------------------------------------------------------------

## 1.0.2[​](release-notes.html#102 "Direct link to 1.0.2"){.hash-link aria-label="Direct link to 1.0.2"} {#102 .anchor .anchorWithStickyNavbar_LWe7}

**Fixed**

- The histogram last bar not hide in chart
  ([#133](https://github.com/tradingview/lightweight-charts/issues/133){target="_blank"
  rel="noopener noreferrer"})

------------------------------------------------------------------------

## 1.0.1[​](release-notes.html#101 "Direct link to 1.0.1"){.hash-link aria-label="Direct link to 1.0.1"} {#101 .anchor .anchorWithStickyNavbar_LWe7}

**Fixed**

- Setting the data to series fails after setting the data to histogram
  series with custom color
  ([#110](https://github.com/tradingview/lightweight-charts/issues/110){target="_blank"
  rel="noopener noreferrer"})

------------------------------------------------------------------------

## 1.0.0[​](release-notes.html#100 "Direct link to 1.0.0"){.hash-link aria-label="Direct link to 1.0.0"} {#100 .anchor .anchorWithStickyNavbar_LWe7}

The first release.

The docs for this version are available
[here](https://github.com/tradingview/lightweight-charts/tree/v1.0.0/docs){target="_blank"
rel="noopener noreferrer"}.

[](android.html){.pagination-nav__link .pagination-nav__link--prev}

Previous

Android

- [5.1.0](release-notes.html#510){.table-of-contents__link
  .toc-highlight}
- [5.0.9](release-notes.html#509){.table-of-contents__link
  .toc-highlight}
- [5.0.8](release-notes.html#508){.table-of-contents__link
  .toc-highlight}
- [5.0.7](release-notes.html#507){.table-of-contents__link
  .toc-highlight}
- [5.0.6](release-notes.html#506){.table-of-contents__link
  .toc-highlight}
- [5.0.5](release-notes.html#505){.table-of-contents__link
  .toc-highlight}
- [5.0.4](release-notes.html#504){.table-of-contents__link
  .toc-highlight}
- [5.0.3](release-notes.html#503){.table-of-contents__link
  .toc-highlight}
- [5.0.2](release-notes.html#502){.table-of-contents__link
  .toc-highlight}
- [5.0.0](release-notes.html#500){.table-of-contents__link
  .toc-highlight}
- [4.2.3](release-notes.html#423){.table-of-contents__link
  .toc-highlight}
- [4.2.2](release-notes.html#422){.table-of-contents__link
  .toc-highlight}
- [4.2.1](release-notes.html#421){.table-of-contents__link
  .toc-highlight}
- [4.2.0](release-notes.html#420){.table-of-contents__link
  .toc-highlight}
- [4.1.7](release-notes.html#417){.table-of-contents__link
  .toc-highlight}
- [4.1.6](release-notes.html#416){.table-of-contents__link
  .toc-highlight}
- [4.1.5](release-notes.html#415){.table-of-contents__link
  .toc-highlight}
- [4.1.4](release-notes.html#414){.table-of-contents__link
  .toc-highlight}
- [4.1.3](release-notes.html#413){.table-of-contents__link
  .toc-highlight}
- [4.1.2](release-notes.html#412){.table-of-contents__link
  .toc-highlight}
- [4.1.1](release-notes.html#411){.table-of-contents__link
  .toc-highlight}
- [4.1.0](release-notes.html#410){.table-of-contents__link
  .toc-highlight}
- [4.0.1](release-notes.html#401){.table-of-contents__link
  .toc-highlight}
- [4.0.0](release-notes.html#400){.table-of-contents__link
  .toc-highlight}
- [3.8.0](release-notes.html#380){.table-of-contents__link
  .toc-highlight}
- [3.7.0](release-notes.html#370){.table-of-contents__link
  .toc-highlight}
- [3.6.1](release-notes.html#361){.table-of-contents__link
  .toc-highlight}
- [3.6.0](release-notes.html#360){.table-of-contents__link
  .toc-highlight}
- [3.5.0](release-notes.html#350){.table-of-contents__link
  .toc-highlight}
- [3.4.0](release-notes.html#340){.table-of-contents__link
  .toc-highlight}
- [3.3.0](release-notes.html#330){.table-of-contents__link
  .toc-highlight}
- [3.2.0](release-notes.html#320){.table-of-contents__link
  .toc-highlight}
- [3.1.5](release-notes.html#315){.table-of-contents__link
  .toc-highlight}
- [3.1.3](release-notes.html#313){.table-of-contents__link
  .toc-highlight}
- [3.1.2](release-notes.html#312){.table-of-contents__link
  .toc-highlight}
- [3.1.1](release-notes.html#311){.table-of-contents__link
  .toc-highlight}
- [3.1.0](release-notes.html#310){.table-of-contents__link
  .toc-highlight}
- [3.0.1](release-notes.html#301){.table-of-contents__link
  .toc-highlight}
- [3.0.0](release-notes.html#300){.table-of-contents__link
  .toc-highlight}
- [2.0.0](release-notes.html#200){.table-of-contents__link
  .toc-highlight}
- [1.2.2](release-notes.html#122){.table-of-contents__link
  .toc-highlight}
- [1.2.1](release-notes.html#121){.table-of-contents__link
  .toc-highlight}
- [1.1.0](release-notes.html#110){.table-of-contents__link
  .toc-highlight}
- [1.0.2](release-notes.html#102){.table-of-contents__link
  .toc-highlight}
- [1.0.1](release-notes.html#101){.table-of-contents__link
  .toc-highlight}
- [1.0.0](release-notes.html#100){.table-of-contents__link
  .toc-highlight}
