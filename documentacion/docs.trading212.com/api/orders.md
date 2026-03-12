# Orders

**⚠️ Order Limitations**

* Orders can be executed only in the **main account currency**


Place, monitor, and cancel equity trade orders. This section provides the
core functionality for programmatically executing your trading strategies
for stocks and ETFs.

## Get all pending orders

 - [GET /api/v0/equity/orders](https://docs.trading212.com/api/orders/orders.md): Retrieves a list of all orders that are currently active (i.e., not yet
filled, cancelled, or expired). This is useful for monitoring the status
of your open positions and managing your trading strategy.

Rate limit: 1 req / 5s

## Place a Limit order

 - [POST /api/v0/equity/orders/limit](https://docs.trading212.com/api/orders/placelimitorder.md): Creates a new Limit order, which executes at a specified price or
better.

- To place a buy order, use a positive quantity. The order will
fill at the limitPrice or lower.

- To place a sell order, use a negative quantity. The order will
fill at the limitPrice or higher.



Order Limitations

* Orders can be executed only in the main account currency


idempotent. Sending the same request multiple times may result in
duplicate orders.

Rate limit: 1 req / 2s

## Place a Market order

 - [POST /api/v0/equity/orders/market](https://docs.trading212.com/api/orders/placemarketorder.md): Creates a new Market order, which is an instruction to trade a security
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

## Place a Stop order

 - [POST /api/v0/equity/orders/stop](https://docs.trading212.com/api/orders/placestoporder_1.md): Creates a new Stop order, which places a Market order once the
stopPrice is reached.

- To place a buy stop order, use a positive quantity.

- To place a sell stop order (commonly a 'stop-loss'), use a
negative quantity.


- The stopPrice is triggered by the instrument's Last Traded Price
(LTP).




Order Limitations

* Orders can be executed only in the main account currency

idempotent. Sending the same request multiple times may result in
duplicate orders.

Rate limit: 1 req / 2s

## Place a StopLimit order

 - [POST /api/v0/equity/orders/stop_limit](https://docs.trading212.com/api/orders/placestoporder.md): Creates a new Stop-Limit order, combining features of a Stop and a Limit
order. The direction of the trade (buy/sell) is determined by the sign
of the quantity field.


Execution Logic:

1.  When the instrument's Last Traded Price (LTP) reaches the
specified stopPrice, the order is triggered.

2.  A Limit order is then automatically placed at the specified
limitPrice.


This two-step process helps protect against price slippage that can
occur with a standard Stop order.


Order Limitations

* Orders can be executed only in the main account currency


idempotent. Sending the same request multiple times may result in
duplicate orders.

Rate limit: 1 req / 2s

## Cancel a pending order

 - [DELETE /api/v0/equity/orders/{id}](https://docs.trading212.com/api/orders/cancelorder.md): Attempts to cancel an active, unfilled order by its unique ID.
Cancellation is not guaranteed if the order is already in the process of
being filled. A successful response indicates the cancellation request
was accepted.

Rate limit: 50 req / 1m0s

## Get a pending order by ID

 - [GET /api/v0/equity/orders/{id}](https://docs.trading212.com/api/orders/orderbyid.md): Retrieves a single pending order using its unique numerical ID. This is
useful for checking the status of a specific order you have previously
placed.

Rate limit: 1 req / 1s

