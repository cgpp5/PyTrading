# Get historical orders data

Rate limit: 6 req / 1m0s

Endpoint: GET /api/v0/equity/history/orders
Version: v0
Security: authWithSecretKey, legacyApiKeyHeader

## Query parameters:

  - `cursor` (integer)
    Pagination cursor

  - `ticker` (string)
    Ticker filter

  - `limit` (integer)
    Max items: 50
    Example: 21

## Response 200 fields (application/json):

  - `items` (array)

  - `items.fill` (object)

  - `items.fill.filledAt` (string)

  - `items.fill.id` (integer)

  - `items.fill.price` (number)

  - `items.fill.quantity` (number)

  - `items.fill.tradingMethod` (string)
    Enum: "TOTV", "OTC"

  - `items.fill.type` (string)
    Enum: "TRADE", "STOCK_SPLIT", "STOCK_DISTRIBUTION", "FOP", "FOP_CORRECTION", "CUSTOM_STOCK_DISTRIBUTION", "EQUITY_RIGHTS", "SCRIP_STOCK_DIVIDENDS", "STOCK_DIVIDENDS", "STOCK_ACQUISITION", "CASH_AND_STOCK_ACQUISITION", "SPIN_OFF"

  - `items.fill.walletImpact` (object)

  - `items.fill.walletImpact.currency` (string)

  - `items.fill.walletImpact.fxRate` (number)

  - `items.fill.walletImpact.netValue` (number)

  - `items.fill.walletImpact.realisedProfitLoss` (number)

  - `items.fill.walletImpact.taxes` (array)

  - `items.fill.walletImpact.taxes.chargedAt` (string)

  - `items.fill.walletImpact.taxes.name` (string)
    Enum: "COMMISSION_TURNOVER", "CURRENCY_CONVERSION_FEE", "FINRA_FEE", "FRENCH_TRANSACTION_TAX", "PTM_LEVY", "STAMP_DUTY", "STAMP_DUTY_RESERVE_TAX", "TRANSACTION_FEE"

  - `items.order` (object)

  - `items.order.createdAt` (string)
    The ISO 8601 formatted date of when the order was created.

  - `items.order.currency` (string)
    The currency used for the order in ISO 4217 format.

  - `items.order.extendedHours` (boolean)
    If true, the order is eligible for execution outside regular trading hours.

  - `items.order.filledQuantity` (number)
    The number of shares that have been successfully executed. Applicable to quantity orders.

  - `items.order.filledValue` (number)
    The total monetary value of the executed portion of the order. Applicable  to orders placed by value.Note: Placing orders by value is not currently supported via the API but can be done through other Trading 212 platforms.

  - `items.order.id` (integer)
    A unique, system-generated identifier for the order.

  - `items.order.initiatedFrom` (string)
    How the order was initiated.
    Enum: "API", "IOS", "ANDROID", "WEB", "SYSTEM", "AUTOINVEST"

  - `items.order.instrument` (object)
    Instrument information as given by /instruments endpoint.

  - `items.order.instrument.currency` (string)
    Instrument currency in ISO 4217 format.

  - `items.order.instrument.isin` (string)
    ISIN of the instrument.

  - `items.order.instrument.name` (string)
    Name of the instrument.

  - `items.order.instrument.ticker` (string)
    Unique instrument identifier.
    Example: "AAPL_US_EQ"

  - `items.order.limitPrice` (number)
    Applicable to LIMIT and STOP_LIMIT orders.

  - `items.order.quantity` (number)
    The total number of shares requested. Applicable to quantity orders.

  - `items.order.side` (string)
    Indicates whether the order is BUY or SELL.
    Enum: "BUY", "SELL"

  - `items.order.status` (string)
    The current state of the order in its lifecycle.
    Enum: "LOCAL", "UNCONFIRMED", "CONFIRMED", "NEW", "CANCELLING", "CANCELLED", "PARTIALLY_FILLED", "FILLED", "REJECTED", "REPLACING", "REPLACED"

  - `items.order.stopPrice` (number)
    Applicable to STOP and STOP_LIMIT orders.

  - `items.order.strategy` (string)
    The strategy used to place the order, either by QUANTITY or VALUE. The API currently only supports placing orders by QUANTITY.
    Enum: "QUANTITY", "VALUE"

  - `items.order.ticker` (string)
    Unique instrument identifier. Get from the /instruments endpoint
    Example: "AAPL_US_EQ"

  - `items.order.timeInForce` (string)
    Specifies how long the order remains active: 
* DAY: The order will automatically expire if not executed by midnight in the time zone of the instrument's exchange.
* GOOD_TILL_CANCEL: The order remains active indefinitely until it is either filled or explicitly cancelled by you.
    Enum: "DAY", "GOOD_TILL_CANCEL"

  - `items.order.value` (number)
    The total monetary value of the order. Applicable to value orders.

  - `nextPagePath` (string)


## Response 400 fields

## Response 401 fields

## Response 403 fields

## Response 408 fields

## Response 429 fields
