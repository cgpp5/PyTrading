- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Panes]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Panes

Panes are essential elements that help segregate data visually within a
single chart. Panes are useful when you have a chart that needs to show
more than one kind of data. For example, you might want to see a
stock\'s price over time in one pane and its trading volume in another.
This setup helps users get a fuller picture without cluttering the
chart.

By default, Lightweight Charts™ has a single pane, however, you can add
more panes to the chart to display different series in separate areas.
For detailed examples and code snippets on how to implement panes in
your charts [see
tutorial](https://tradingview.github.io/lightweight-charts/tutorials/how_to/panes).

## Customization Options[​](panes.html#customization-options "Direct link to Customization Options"){.hash-link aria-label="Direct link to Customization Options"} {#customization-options .anchor .anchorWithStickyNavbar_LWe7}

Lightweight Charts™ offers a few [customization
options](api/interfaces/LayoutPanesOptions.html) to tailor the
appearance and behavior of panes:

- [Pane Separator
  Color](api/interfaces/LayoutPanesOptions.html#separatorcolor):
  Customize the color of the pane separators to match the chart design
  or improve visibility.

- [Separator Hover
  Color](api/interfaces/LayoutPanesOptions.html#separatorhovercolor):
  Enhance user interaction by changing the color of separators on mouse
  hover.

- [Resizable
  Panes](api/interfaces/LayoutPanesOptions.html#enableresize): Opt to
  enable or disable the resizing of panes by the user, offering
  flexibility in how data is displayed.

## Managing Panes[​](panes.html#managing-panes "Direct link to Managing Panes"){.hash-link aria-label="Direct link to Managing Panes"} {#managing-panes .anchor .anchorWithStickyNavbar_LWe7}

While the specific methods to manipulate panes are covered in the
detailed
[example](https://tradingview.github.io/lightweight-charts/tutorials/how_to/panes),
it\'s important to note that Lightweight Charts™ provides an [API for
pane management](api/interfaces/IPaneApi.html). This includes adding new
panes, moving series between panes, adjusting pane height, and removing
panes. The API ensures that developers have full control over the pane
lifecycle and organization within their charts.

[](time-scale.html){.pagination-nav__link .pagination-nav__link--prev}

Previous

Time scale

[](time-zones.html){.pagination-nav__link .pagination-nav__link--next}

Next

Time zones

- [Customization
  Options](panes.html#customization-options){.table-of-contents__link
  .toc-highlight}
- [Managing Panes](panes.html#managing-panes){.table-of-contents__link
  .toc-highlight}
