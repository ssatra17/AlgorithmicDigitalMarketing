# **INFO7374AlgorithmicDigitalMarketing**


## Team Information

| Name | NEU ID 
| --- | --- 
|Prathamesh Vivek Limaye | 001051436
|Saurabh Rakesh Satra  | 001059412 

## Claat Link
https://codelabs-preview.appspot.com/?file_id=1KCObopTMKRYJpm6jbQEbQXefLpMMji95Ry__sh-Y71Q#1

## Google Docs Link
https://docs.google.com/document/d/1KCObopTMKRYJpm6jbQEbQXefLpMMji95Ry__sh-Y71Q/edit#heading=h.g2efnul4o9fu

## About Dataset
There are 2 datasets that contain information about all transactions of these cards buying from different merchants:

Historical_transactions.csv: up to 3 months' worth of historical transactions for each card_id

New_merchant_transactions.csv: two months' worth of data for each card_id containing ALL purchases that card_id made at merchant_ids that were not visited in the historical data.
Lastly, there is 1 dataset that contains information about the merchants:

Merchants.csv: additional information about all merchants / merchant_ids in the dataset.
Merchant_id is used to join Merchants file with Historical_transactions and New_merchant_transactions.

## Data Preprocessing and Cleaning

XSV:- We have used XSV for checking the headers of the tables, the frequency of each column data and to sample the data using select and sample commands.

Trifacta:- We have used Trifacta for joining the tables and for cleaning the data like removing missing values and inconsistent data. 

Pandas:- We have used pandas to do advanced preprocessing and cleaning of the data. We have also used this platform to visualize the data.

Snowflake:- We have used snowflake platform for staging the cleaned and processed data from Trifacta and Pandas.

## Marketing Concepts that we have applied
#### RFM Analysis
RFM segmentation is a powerful way to identify groups of customers for special treatment. RFM stands for recency, frequency, and monetary.

Recency - This represents the age of the customer when they made their latest transactions. (Current_date - last_transaction_date)

Frequency - This represents the total number of transactions/number of visits a customer has made. (Count of total transactions)

Monetary - This represents the total purchase amount that a specified customer has made. (Sum of purchase_amt)

Time - This represents the age of the customer. The time span between a customer’s first and last transactions.

#### Customer Lifetime Value (CLV)
The lifetime value of a customer, or customer lifetime value (CLV), represents the total amount of money a customer is expected to spend in your business, or on your products, during their lifetime. 
We calculated Customer Lifetime Values by calculating different parameters such as profit margin, purchase frequency, repeat rate, churn rate, etc. 

## Visualizations
We have used SalseForce: Einstein Analytics to create visualizations and dashboards for gaining marketing insights.

All the python scripts, dashboards and commands used are stored in respective folders.
