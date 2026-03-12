# Historical events

Review your account's trading history. Access detailed records of past
orders, dividend payments, and cash transactions, or generate downloadable
CSV reports for analysis and record-keeping.

## Get paid out dividends

 - [GET /api/v0/equity/history/dividends](https://docs.trading212.com/api/historical-events/dividends.md): Rate limit: 6 req / 1m0s

## List generated reports

 - [GET /api/v0/equity/history/exports](https://docs.trading212.com/api/historical-events/getreports.md): Retrieves a list of all requested CSV reports and their current status. 


Asynchronous Workflow:

1. Call POST /history/exports to request a report. You will receive a
reportId.

2. Periodically call this endpoint (GET /history/exports) to check the
status of the report corresponding to your reportId.

3. Once the status is Finished, the downloadLink field will contain
a URL to download the CSV file.

Rate limit: 1 req / 1m0s

## Request a CSV report

 - [POST /api/v0/equity/history/exports](https://docs.trading212.com/api/historical-events/requestreport.md): Initiates the generation of a CSV report containing historical account
data. This is an asynchronous operation. The response will include a
reportId which you can use to track the status of the generation
process using the GET /history/exports endpoint.

Rate limit: 1 req / 30s

## Get historical orders data

 - [GET /api/v0/equity/history/orders](https://docs.trading212.com/api/historical-events/orders_1.md): Rate limit: 6 req / 1m0s

## Get transactions

 - [GET /api/v0/equity/history/transactions](https://docs.trading212.com/api/historical-events/transactions.md): Fetch superficial information about movements to and from your account

Rate limit: 6 req / 1m0s

