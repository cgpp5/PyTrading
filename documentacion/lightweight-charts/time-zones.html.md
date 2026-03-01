- [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+){.breadcrumbHomeIcon_YNFT}](https://tradingview.github.io/lightweight-charts/){.breadcrumbs__link
  aria-label="Home page"}
- [Time zones]{.breadcrumbs__link itemprop="name"}

[Version: 5.1]{.theme-doc-version-badge .badge .badge--secondary}

On this page

# Time zones

## Overview[​](time-zones.html#overview "Direct link to Overview"){.hash-link aria-label="Direct link to Overview"} {#overview .anchor .anchorWithStickyNavbar_LWe7}

Lightweight Charts™ **does not** natively **support** time zones. If
necessary, you should handle time zone adjustments manually.

The library processes all date and time values in UTC. To support time
zones, adjust each bar\'s timestamp in your dataset based on the
appropriate time zone offset. Therefore, a UTC timestamp should
correspond to the local time in the target time zone.

Consider the example. A data point has the `2021-01-01T10:00:00.000Z`
timestamp in UTC. You want to display it in the `Europe/Moscow` time
zone, which has the `UTC+03:00` offset according to the [IANA time zone
database](https://www.iana.org/time-zones){target="_blank"
rel="noopener noreferrer"}. To do this, adjust the original UTC
timestamp by adding 3 hours. Therefore, the new timestamp should be
`2021-01-01T13:00:00.000Z`.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]{.admonitionIcon_Rf37}info

When converting time zones, consider the following:

- Adding a time zone offset could change not only the time but the date
  as well.
- An offset may vary due to DST (Daylight Saving Time) or other regional
  adjustments.
- If your data is measured in business days and does not include a time
  component, in most cases, you should not adjust it to a time zone.

## Approaches[​](time-zones.html#approaches "Direct link to Approaches"){.hash-link aria-label="Direct link to Approaches"} {#approaches .anchor .anchorWithStickyNavbar_LWe7}

Consider the approaches below to convert time values to the required
time zone.

### Using pure JavaScript[​](time-zones.html#using-pure-javascript "Direct link to Using pure JavaScript"){.hash-link aria-label="Direct link to Using pure JavaScript"} {#using-pure-javascript .anchor .anchorWithStickyNavbar_LWe7}

For more information on this approach, refer to
[StackOverflow](https://stackoverflow.com/a/54127122/3893439){target="_blank"
rel="noopener noreferrer"}.

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
function timeToTz(originalTime, timeZone) {
    const zonedDate = new Date(new Date(originalTime * 1000).toLocaleString('en-US', { timeZone }));
    return zonedDate.getTime() / 1000;
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

If you only need to support a client (local) time zone, you can use the
following function:

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}
function timeToLocal(originalTime) {
    const d = new Date(originalTime * 1000);
    return Date.UTC(d.getFullYear(), d.getMonth(), d.getDate(), d.getHours(), d.getMinutes(), d.getSeconds(), d.getMilliseconds()) / 1000;
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

### Using the date-fns-tz library[​](time-zones.html#using-the-date-fns-tz-library "Direct link to Using the date-fns-tz library"){.hash-link aria-label="Direct link to Using the date-fns-tz library"} {#using-the-date-fns-tz-library .anchor .anchorWithStickyNavbar_LWe7}

You can use the `utcToZonedTime` function from the
[`date-fns-tz`](https://github.com/marnusw/date-fns-tz){target="_blank"
rel="noopener noreferrer"} library as follows:

``` {.prism-code .language-js .codeBlock_bY9V .thin-scrollbar tabindex="0" style="color:#393A34;background-color:#f6f8fa"}

function timeToTz(originalTime, timeZone) {
    const zonedDate = utcToZonedTime(new Date(originalTime * 1000), timeZone);
    return zonedDate.getTime() / 1000;
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl95OTdOIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==){.copyButtonIcon_y97N}![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fTGpkUyI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==){.copyButtonSuccessIcon_LjdS}]{.copyButtonIcons_eSgA
aria-hidden="true"}

### Using the IANA time zone database[​](time-zones.html#using-the-iana-time-zone-database "Direct link to Using the IANA time zone database"){.hash-link aria-label="Direct link to Using the IANA time zone database"} {#using-the-iana-time-zone-database .anchor .anchorWithStickyNavbar_LWe7}

If you process a large dataset and approaches above do not meet your
performance requirements, consider using the
[`tzdata`](https://www.npmjs.com/package/tzdata){target="_blank"
rel="noopener noreferrer"}.

This approach can significantly improve performance for the following
reasons:

- You do not need to calculate the time zone offset for every data point
  individually. Instead, you can look up the correct offset just once
  for the first timestamp using a fast binary search.
- After finding the starting offset, you go through the rest data and
  check whether an offset should be changed, for example, because of DST
  starting/ending.

## Why are time zones not supported?[​](time-zones.html#why-are-time-zones-not-supported "Direct link to Why are time zones not supported?"){.hash-link aria-label="Direct link to Why are time zones not supported?"} {#why-are-time-zones-not-supported .anchor .anchorWithStickyNavbar_LWe7}

The approaches above were not implemented in Lightweight Charts™ for the
following reasons:

- Using [pure JavaScript](time-zones.html#using-pure-javascript) is
  slow. In our tests, processing 100,000 data points took over 20
  seconds.
- Using the [date-fns-tz
  library](time-zones.html#using-the-date-fns-tz-library) introduces
  additional dependencies and is also slow. In our tests, processing
  100,000 data points took 18 seconds.
- Incorporating the [IANA time zone
  database](time-zones.html#using-the-iana-time-zone-database) increases
  the bundle size by [29.9
  kB](https://bundlephobia.com/package/tzdata){target="_blank"
  rel="noopener noreferrer"}, which is nearly the size of the entire
  Lightweight Charts™ library.

Since time zone support is not required for all users, it is
intentionally left out of the library to maintain high performance and a
lightweight package size.

[](panes.html){.pagination-nav__link .pagination-nav__link--prev}

Previous

Panes

[](plugins/intro.html){.pagination-nav__link
.pagination-nav__link--next}

Next

Overview

- [Overview](time-zones.html#overview){.table-of-contents__link
  .toc-highlight}
- [Approaches](time-zones.html#approaches){.table-of-contents__link
  .toc-highlight}
  - [Using pure
    JavaScript](time-zones.html#using-pure-javascript){.table-of-contents__link
    .toc-highlight}
  - [Using the date-fns-tz
    library](time-zones.html#using-the-date-fns-tz-library){.table-of-contents__link
    .toc-highlight}
  - [Using the IANA time zone
    database](time-zones.html#using-the-iana-time-zone-database){.table-of-contents__link
    .toc-highlight}
- [Why are time zones not
  supported?](time-zones.html#why-are-time-zones-not-supported){.table-of-contents__link
  .toc-highlight}
