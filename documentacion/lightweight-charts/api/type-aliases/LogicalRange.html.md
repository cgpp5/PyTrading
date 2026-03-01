- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Type Aliases]{.breadcrumbs__link}
- [LogicalRange]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

# Type alias: LogicalRange

> **LogicalRange**: [`IRange`](../interfaces/IRange.html)
> \<[`Logical`](Logical.html)\>

A logical range is an object with 2 properties: `from` and `to`, which
are numbers and represent logical indexes on the time scale.

The starting point of the time scale\'s logical range is the first data
item among all series. Before that point all indexes are negative,
starting from that point - positive.

Indexes might have fractional parts, for instance 4.2, due to the
time-scale being continuous rather than discrete.

Integer part of the logical index means index of the fully visible bar.
Thus, if we have 5.2 as the last visible logical index (`to` field),
that means that the last visible bar has index 5, but we also have
partially visible (for 20%) 6th bar. Half (e.g. 1.5, 3.5, 10.5) means
exactly a middle of the bar.
