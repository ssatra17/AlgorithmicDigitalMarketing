# **INFO7374AlgorithmicDigitalMarketing :- Argos E-commerce Data Analysis**


## Team Information

| Name | NEU ID 
| --- | --- 
|Prathamesh Vivek Limaye | 001051436
|Saurabh Rakesh Satra  | 001059412 

## Google Docs Link
https://docs.google.com/document/d/1Ojf1NcvHhou5R6zGlAt3T11zkUpobgm6xQD-oEEI7Gg/edit?ts=5f35d420#heading=h.7sa4zxkhmsum

## Application Link
https://argos-finalproject.herokuapp.com/

## Goals of the project
1.Argos wants to analyze customer shopping patterns and transactions. Based on these insights the analyst will use various algorithms to predict various key metrics:

-RFM Analysis

-Customer Lifetime Value

-Customer Segmentation

-Next Purchase Day

2.Build a recommendation system for the customers to help them ease choosing the products.

3.Create Dashboards for Business Analysts to study the company’s sales patterns and make better decisions for targeting the customers.

4.Create a web application to demonstrate predictions and results.

5.Hosting the web application on AWS/Heroku.


## About Dataset
#### Attribute Information:

InvoiceNo: Invoice number, a 6-digit integral number uniquely assigned to each transaction. If this code starts with the letter ‘c’, it indicates a cancellation.

StockCode: Product (item) code, a 5-digit integral number uniquely assigned to each distinct product.

Description: Product (item) name.

Quantity: The quantities of each product (item) per transaction, Numeric.

InvoiceDate: Invoice Date and time. Numeric, the day and time when each transaction was generated. UnitPrice: Unit price. Numeric, Product price per unit in sterling.

CustomerID: Customer number. a 5-digit integral number uniquely assigned to each customer.

Country: Country name. the name of the country where each customer resides.

## Marketing Concepts 
#### RFM Analysis

RFM segmentation is a powerful way to identify groups of customers for special treatment. RFM stands for recency, frequency, and monetary.

Recency - This represents the age of the customer when they made their latest transactions. (Current_date - last_transaction_date)

Frequency - This represents the total number of transactions/number of visits a customer has made. (Count of total transactions)

Monetary - This represents the total purchase amount that a specified customer has made. (Sum of purchase_amt)


#### Customer Lifetime Value (CLV)
The lifetime value of a customer, or customer lifetime value (CLV), represents the total amount of money a customer is expected to spend in your business, or on your products, during their lifetime.
Lifetime Value: - Total Gross Revenue - Total Cost

#### Next Purchase Date
With the help of predictive analysis, we can predict the next purchase date for a customer. Basically, the next purchase date can help us build strategies for customers such as the customer who is going to buy the product, we will not offer any promotions. But the customer who probably is not going to buy anything in the next certain time period, we can offer some promotions or discount offers for them.
We have classified the customers on the basis of next purchase date into three groups, first is customers who are going to buy products in the range of 0-20 days, customers who will buy products in next 21-49 days and customers who will buy the product after 50 days. 

## Recommendation System
The recommendation system is to recommend customers the best products based on their choice and the ratings given by other customers. We have used the Riemannian Low-rank Matrix Completion (RLRMC) algorithm for predicting the ratings for several products and recommendations.

Riemannian Low-rank Matrix Completion (RLRMC) is a matrix factorization based (vanilla) matrix completion algorithm that solves the optimization problem using Riemannian conjugate gradients algorithm. The ratings matrix of items and users is modeled as a low-rank matrix. Let the number of items be d and the number of users be T. The RLRMC algorithm assumes that the ratings matrix M (of size d * T) is partially known. The entry at M(i, j) represents the rating given by the j-th user to the i-th item. RLRMC learns matrix M as M=L * R(Transpose), where L is a d * r matrix and R is a T * r matrix. Here, r is the rank hyper-parameter which needs to be provided to the RLRMC algorithm. Typically, it is assumed that r << d, T.
