# Get exchanges metadata

Retrieves all accessible exchanges and their corresponding working schedules.
Data is refreshed every 10 minutes.

Rate limit: 1 req / 30s

Endpoint: GET /api/v0/equity/metadata/exchanges
Version: v0
Security: authWithSecretKey, legacyApiKeyHeader

## Response 200 fields (application/json):

  - `id` (integer)

  - `name` (string)

  - `workingSchedules` (array)

  - `workingSchedules.timeEvents` (array)

  - `workingSchedules.timeEvents.date` (string)

  - `workingSchedules.timeEvents.type` (string)
    Enum: "OPEN", "CLOSE", "BREAK_START", "BREAK_END", "PRE_MARKET_OPEN", "AFTER_HOURS_OPEN", "AFTER_HOURS_CLOSE", "OVERNIGHT_OPEN"


## Response 401 fields

## Response 403 fields

## Response 408 fields

## Response 429 fields
