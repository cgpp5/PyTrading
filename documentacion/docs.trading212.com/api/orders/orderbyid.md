# Get a pending order by ID

Retrieves a single pending order using its unique numerical ID. This is
useful for checking the status of a specific order you have previously
placed.

Rate limit: 1 req / 1s

Endpoint: GET /api/v0/equity/orders/{id}
Version: v0
Security: authWithSecretKey, legacyApiKeyHeader

## Path parameters:

  - `id` (integer, required)
    The unique identifier of the order you want to retrieve.

## Response 200 fields (application/json):

  - `createdAt` (string)
    The ISO 8601 formatted date of when the order was created.

  - `currency` (string)
    The currency used for the order in ISO 4217 format.

  - `extendedHours` (boolean)
    If true, the order is eligible for execution outside regular trading hours.

  - `filledQuantity` (number)
    The number of shares that have been successfully executed. Applicable to quantity orders.

  - `filledValue` (number)
    The total monetary value of the executed portion of the order. Applicable  to orders placed by value.Note: Placing orders by value is not currently supported via the API but can be done through other Trading 212 platforms.

  - `id` (integer)
    A unique, system-generated identifier for the order.

  - `initiatedFrom` (string)
    How the order was initiated.
    Enum: "API", "IOS", "ANDROID", "WEB", "SYSTEM", "AUTOINVEST"

  - `instrument` (object)
    Instrument information as given by /instruments endpoint.

  - `instrument.currency` (string)
    Instrument currency in ISO 4217 format.

  - `instrument.isin` (string)
    ISIN of the instrument.

  - `instrument.name` (string)
    Name of the instrument.

  - `instrument.ticker` (string)
    Unique instrument identifier.
    Example: "AAPL_US_EQ"

  - `limitPrice` (number)
    Applicable to LIMIT and STOP_LIMIT orders.

  - `quantity` (number)
    The total number of shares requested. Applicable to quantity orders.

  - `side` (string)
    Indicates whether the order is BUY or SELL.
    Enum: "BUY", "SELL"

  - `status` (string)
    The current state of the order in its lifecycle.
    Enum: "LOCAL", "UNCONFIRMED", "CONFIRMED", "NEW", "CANCELLING", "CANCELLED", "PARTIALLY_FILLED", "FILLED", "REJECTED", "REPLACING", "REPLACED"

  - `stopPrice` (number)
    Applicable to STOP and STOP_LIMIT orders.

  - `strategy` (string)
    The strategy used to place the order, either by QUANTITY or VALUE. The API currently only supports placing orders by QUANTITY.
    Enum: "QUANTITY", "VALUE"

  - `ticker` (string)
    Unique instrument identifier. Get from the /instruments endpoint
    Example: "AAPL_US_EQ"

  - `timeInForce` (string)
    Specifies how long the order remains active: 
* DAY: The order will automatically expire if not executed by midnight in the time zone of the instrument's exchange.
* GOOD_TILL_CANCEL: The order remains active indefinitely until it is either filled or explicitly cancelled by you.
    Enum: "DAY", "GOOD_TILL_CANCEL"

  - `type` (string)
    Enum: "LIMIT", "STOP", "MARKET", "STOP_LIMIT"

  - `value` (number)
    The total monetary value of the order. Applicable to value orders.


## Response 401 fields

## Response 403 fields

## Response 404 fields

## Response 408 fields

## Response 429 fields
