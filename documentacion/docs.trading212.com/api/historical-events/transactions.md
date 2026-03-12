# Get transactions

Fetch superficial information about movements to and from your account

Rate limit: 6 req / 1m0s

Endpoint: GET /api/v0/equity/history/transactions
Version: v0
Security: authWithSecretKey, legacyApiKeyHeader

## Query parameters:

  - `cursor` (string)
    Pagination cursor

  - `time` (string)
    Retrieve transactions starting from the specified time

  - `limit` (integer)
    Max items: 50
    Example: 21

## Response 200 fields (application/json):

  - `items` (array)

  - `items.amount` (number)
    Amount in the currency of the transaction

  - `items.currency` (string)
    Currency of the transaction

  - `items.dateTime` (string)

  - `items.reference` (string)
    ID

  - `items.type` (string)
    Enum: "WITHDRAW", "DEPOSIT", "FEE", "TRANSFER"

  - `nextPagePath` (string)


## Response 400 fields

## Response 401 fields

## Response 403 fields

## Response 408 fields

## Response 429 fields
