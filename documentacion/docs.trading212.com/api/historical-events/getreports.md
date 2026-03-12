# List generated reports

Retrieves a list of all requested CSV reports and their current status. 


Asynchronous Workflow:

1. Call POST /history/exports to request a report. You will receive a
reportId.

2. Periodically call this endpoint (GET /history/exports) to check the
status of the report corresponding to your reportId.

3. Once the status is Finished, the downloadLink field will contain
a URL to download the CSV file.

Rate limit: 1 req / 1m0s

Endpoint: GET /api/v0/equity/history/exports
Version: v0
Security: authWithSecretKey, legacyApiKeyHeader

## Response 200 fields (application/json):

  - `dataIncluded` (object)

  - `dataIncluded.includeDividends` (boolean)

  - `dataIncluded.includeInterest` (boolean)

  - `dataIncluded.includeOrders` (boolean)

  - `dataIncluded.includeTransactions` (boolean)

  - `downloadLink` (string)

  - `reportId` (integer)

  - `status` (string)
    Enum: "Queued", "Processing", "Running", "Canceled", "Failed", "Finished"

  - `timeFrom` (string)

  - `timeTo` (string)


## Response 400 fields

## Response 401 fields

## Response 403 fields

## Response 408 fields

## Response 429 fields
