# Cancel a pending order

Attempts to cancel an active, unfilled order by its unique ID.
Cancellation is not guaranteed if the order is already in the process of
being filled. A successful response indicates the cancellation request
was accepted.

Rate limit: 50 req / 1m0s

Endpoint: DELETE /api/v0/equity/orders/{id}
Version: v0
Security: authWithSecretKey, legacyApiKeyHeader

## Path parameters:

  - `id` (integer, required)
    The unique identifier of the order you want to cancel.


## Response 200 fields

## Response 400 fields

## Response 401 fields

## Response 403 fields

## Response 404 fields

## Response 408 fields

## Response 429 fields
