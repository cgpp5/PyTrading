# Get account summary

Provides a breakdown of your account's cash and investment metrics,
including available funds, invested capital, and total account value.

Rate limit: 1 req / 5s

Endpoint: GET /api/v0/equity/account/summary
Version: v0
Security: authWithSecretKey, legacyApiKeyHeader

## Response 200 fields (application/json):

  - `cash` (object)

  - `cash.availableToTrade` (number)
    Funds available for investing.

  - `cash.inPies` (number)
    It’s the sum of the cash inside of all pies that is not yet invested.

  - `cash.reservedForOrders` (number)
    The amount of cash reserved for pending orders. This cash is not available for placing new trades.

  - `currency` (string)
    Primary account currency in ISO 4217 format.

  - `id` (integer)
    Primary trading account number. This is the same account ID you would see in the Trading 212 web or mobile application.

  - `investments` (object)

  - `investments.currentValue` (number)
    Current value of all the investments.

  - `investments.realizedProfitLoss` (number)
    The all-time realised profit loss from all of the trades executed.

  - `investments.totalCost` (number)
    The cost basis of your current investments. The total amount of funds you've invested in the shares you currently own.

  - `investments.unrealizedProfitLoss` (number)
    The potential profit/loss of your current investments, showing how much you could gain or lose if you were to sell them now.

  - `totalValue` (number)
    Investments value in your account's primary currency.


## Response 401 fields

## Response 403 fields

## Response 408 fields

## Response 429 fields
