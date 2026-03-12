# Place a Market order

Creates a new Market order, which is an instruction to trade a security
immediately at the next available price. 

- To place a buy order, use a positive quantity. 

- To place a sell order, use a negative quantity.


- extendedHours: Set to true to allow the order to be filled
outside of the standard trading session.

- If placed when the market is closed, the order will be queued to
execute when the market next opens.

x
Order Limitations

* Orders can be executed only in the main account currency


Warning: Market orders can be subject to price slippage, where the
final execution price may differ from the price at the time of order
placement.


idempotent. Sending the same request multiple times may result in
duplicate orders.

Rate limit: 50 req / 1m0s

Endpoint: POST /api/v0/equity/orders/market
Version: v0
Security: authWithSecretKey, legacyApiKeyHeader

## Request fields (application/json):

  - `extendedHours` (boolean)
    Example: true

  - `quantity` (number)
    Example: 0.1

  - `ticker` (string)
    Example: "AAPL_US_EQ"

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


## Response 400 fields

## Response 401 fields

## Response 403 fields

## Response 408 fields

## Response 429 fields
