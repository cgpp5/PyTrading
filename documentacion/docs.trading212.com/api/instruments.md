# Instruments

Discover what you can trade. These endpoints provide comprehensive lists
of all tradable instruments and the exchanges they belong to, including
details like tickers and trading hours.

## Get exchanges metadata

 - [GET /api/v0/equity/metadata/exchanges](https://docs.trading212.com/api/instruments/exchanges.md): Retrieves all accessible exchanges and their corresponding working schedules.
Data is refreshed every 10 minutes.

Rate limit: 1 req / 30s

## Get all available instruments

 - [GET /api/v0/equity/metadata/instruments](https://docs.trading212.com/api/instruments/instruments.md): Retrieves all accessible instruments.
Data is refreshed every 10 minutes.

Rate limit: 1 req / 50s

