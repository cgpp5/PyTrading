# Request a CSV report

Initiates the generation of a CSV report containing historical account
data. This is an asynchronous operation. The response will include a
reportId which you can use to track the status of the generation
process using the GET /history/exports endpoint.

Rate limit: 1 req / 30s

Endpoint: POST /api/v0/equity/history/exports
Version: v0
Security: authWithSecretKey, legacyApiKeyHeader

## Request fields (application/json):

  - `dataIncluded` (object)

  - `dataIncluded.includeDividends` (boolean)

  - `dataIncluded.includeInterest` (boolean)

  - `dataIncluded.includeOrders` (boolean)

  - `dataIncluded.includeTransactions` (boolean)

  - `timeFrom` (string)

  - `timeTo` (string)

## Response 200 fields (application/json):

  - `reportId` (integer)


## Response 400 fields

## Response 401 fields

## Response 403 fields

## Response 408 fields

## Response 429 fields
