# Fetch all open positions

Fetch all open positions for your account

Rate limit: 1 req / 1s

Endpoint: GET /api/v0/equity/positions
Version: v0
Security: authWithSecretKey, legacyApiKeyHeader

## Query parameters:

  - `ticker` (string)
    Example: "AAPL_US_EQ"

## Response 200 fields (application/json):

  - `averagePricePaid` (number)
    Average price paid, in instrument currency, per share.

  - `createdAt` (string)
    The ISO 8601 formatted date of when the position was opened.

  - `currentPrice` (number)
    Current price, in instrument currency, of a single share.

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

  - `quantity` (number)
    Total quantity of shares owned.

  - `quantityAvailableForTrading` (number)
    Quantity of shares available for trading.

  - `quantityInPies` (number)
    Quantity of shares currently used in pie.

  - `walletImpact` (object)

  - `walletImpact.currency` (string)
    The currency code used to represent all the wallet impact information.

  - `walletImpact.currentValue` (number)
    The current market value of the position.

  - `walletImpact.fxImpact` (number)
    The positive or negative impact on the position's value due to currency rate changes.

  - `walletImpact.totalCost` (number)
    The total cost paid for the position.

  - `walletImpact.unrealizedProfitLoss` (number)
    The unrealized profit & loss for the position. Calculated as currentValue - totalCost.


## Response 401 fields

## Response 403 fields

## Response 408 fields

## Response 429 fields
