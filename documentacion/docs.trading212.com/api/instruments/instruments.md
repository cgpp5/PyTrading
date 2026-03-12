# Get all available instruments

Retrieves all accessible instruments.
Data is refreshed every 10 minutes.

Rate limit: 1 req / 50s

Endpoint: GET /api/v0/equity/metadata/instruments
Version: v0
Security: authWithSecretKey, legacyApiKeyHeader

## Response 200 fields (application/json):

  - `addedOn` (string)
    On the platform since

  - `currencyCode` (string)
    ISO 4217
    Example: "USD"

  - `extendedHours` (boolean)

  - `isin` (string)

  - `maxOpenQuantity` (number)

  - `name` (string)

  - `shortName` (string)

  - `ticker` (string)
    Unique identifier
    Example: "AAPL_US_EQ"

  - `type` (string)
    Enum: "CRYPTOCURRENCY", "ETF", "FOREX", "FUTURES", "INDEX", "STOCK", "WARRANT", "CRYPTO", "CVR", "CORPACT"

  - `workingScheduleId` (integer)
    Get items in the /exchanges endpoint


## Response 401 fields

## Response 403 fields

## Response 408 fields

## Response 429 fields
