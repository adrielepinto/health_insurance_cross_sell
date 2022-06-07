# Health Insurance Cross Sell
![health](https://user-images.githubusercontent.com/97919969/172404366-f7c6e1f0-c095-404f-bd7d-c186bfde6aab.jpeg)

# 1.0.CONTEXT
Insurance All is a company that offer health insurance services, and the product team is analyzing the possibility of offering policyholders a new product: Automobile Insurance.

# 2.0. BUSINESS PROBLEM
Know which customers would be interested in buying the new product.

Cause:

The company has a list of 380.000 of posssible interested customers;

The company has the capacity to make only 20.000 calls by period campaign.


Solution:

Use Machine Learning algorithm to sort a list priorizing the most interested customers;

The visualization of the list can be seen by Google Sheets;

# 3. Solution Development 
# Data Description
<img width="637" alt="Screen Shot 2022-06-07 at 9 05 03 AM" src="https://user-images.githubusercontent.com/97919969/172429015-1884ad62-8cad-48bf-a5c6-14b637749d27.png">


As we can see bellow, we have 2 data types: int64 and float64. It's important to explain that machine learning algorithms usually build a better learning with numerical data, this is one of the premises that we will assume.

# Descriptive Startistical 

<img width="836" alt="Screen Shot 2022-06-07 at 9 07 40 AM" src="https://user-images.githubusercontent.com/97919969/172429428-6184ef71-51e7-4546-bc0c-9d12d4263af2.png">

# Mind Map

![mindmap](https://user-images.githubusercontent.com/97919969/172429655-748108c0-61fa-4974-9916-3277edb83ff5.png)

# Hipothesys List 

- H1. 50% of female customers would be interested on the car insurance.
- H2. Customers over 50 years old would be interested on the car insurance.
- H3. 80% of Field customers wouldn't be interested on the car insurance.
- H4. Feature study - Policy Sales 
- H5. 30% of customers who has driver license would be insterested on the car insurance.
- H6. Customers who has cars less than one year are insterested on the car insurance.
- H7. H7. Feature Study - Vehicle Demage
- H8. 80% of customers who had a previously insurance wouldn't be interested on the car insurance.
- H9. Customers that paid for annually premmiun less than 40.000 would be insterested on the car insurance.
- H10. Customers up to 120 days of association on Health Insurance would be insterested on the car insurance.

# Exploratory Data Analisys
# Response variable

<img width="1085" alt="Screen Shot 2022-06-07 at 9 11 19 AM" src="https://user-images.githubusercontent.com/97919969/172430180-3fd9db60-fdb7-4a2c-90a6-d01d617c839c.png">

# Numerical Variable

<img width="1005" alt="Screen Shot 2022-06-07 at 9 12 45 AM" src="https://user-images.githubusercontent.com/97919969/172430586-4e46a7cd-82ad-45c2-8265-4eb7675d93de.png">


# Hypothesys validation

 # H1. 50% of female customers would be interested on the car insurance.
 FALSE
<img width="1090" alt="Screen Shot 2022-06-07 at 9 15 37 AM" src="https://user-images.githubusercontent.com/97919969/172434715-cb58ac55-7ae0-48f5-b0be-94b42aaf7963.png">

- 31% Female customers are not interested.
- 5.44% Female customers interested.
- 52% Male customers are not interested.
- 10% Male customers are interested.
- 
# H2. Customers over 50 years old would be interested on the car insurance.
FALSE 
<img width="1087" alt="Screen Shot 2022-06-07 at 9 20 09 AM" src="https://user-images.githubusercontent.com/97919969/172432069-867036bd-3539-4749-9e60-498e60c1a7d6.png">
- Customers over 50 years old are not interested.

# H3 - Customers who has cars less than one year are insterested on the car 
FALSE 
<img width="1081" alt="Screen Shot 2022-06-07 at 9 23 04 AM" src="https://user-images.githubusercontent.com/97919969/172434983-dd85c7fc-c51e-425c-9a75-15411eb36699.png">
<img width="449" alt="Screen Shot 2022-06-07 at 9 34 33 AM" src="https://user-images.githubusercontent.com/97919969/172435393-95515893-5901-40e5-b390-ea26f6c6af3c.png">
- Bellow 1 year = 0.07% of  interested customers.
- Between 1 and 2 yars = 13% of interested customers.
- Over years = 2.80% of interested customers.

# Hipothesys Resume

<img width="372" alt="Screen Shot 2022-06-07 at 9 37 54 AM" src="https://user-images.githubusercontent.com/97919969/172436341-a26380a9-d597-466c-bb9d-19e090e7dae8.png">

# Multivariable Analisys

<img width="996" alt="Screen Shot 2022-06-07 at 9 39 34 AM" src="https://user-images.githubusercontent.com/97919969/172436587-adc87c41-049c-4ad0-b2b5-1779ca1e38ef.png">

# Feature Importance
<img width="987" alt="Screen Shot 2022-06-07 at 9 42 38 AM" src="https://user-images.githubusercontent.com/97919969/172437182-1d75bc83-84f4-4c48-a149-bd32689373b9.png">
<img width="484" alt="Screen Shot 2022-06-07 at 9 44 54 AM 1" src="https://user-images.githubusercontent.com/97919969/172437716-1d697cfa-034e-4ef9-8853-f153459e94a0.png">


# Machine Learning Modelling 
Regression Logistic
<img width="1025" alt="Screen Shot 2022-06-07 at 9 55 45 AM" src="https://user-images.githubusercontent.com/97919969/172439694-bbd58fec-8c34-42e5-9592-0ca69a692649.png">

# Manually Lift Curve
<img width="861" alt="Screen Shot 2022-06-07 at 9 58 18 AM" src="https://user-images.githubusercontent.com/97919969/172440135-60fe7064-ad37-447c-a9cf-21113584d08a.png">

# 4. Conclusion and Demostration 
# Manually ROI Curve

<img width="621" alt="Screen Shot 2022-06-07 at 10 00 45 AM" src="https://user-images.githubusercontent.com/97919969/172440613-41fa1e0d-5f01-4d5f-8539-1ef396f2eacf.png">
<img width="874" alt="Screen Shot 2022-06-07 at 10 03 04 AM" src="https://user-images.githubusercontent.com/97919969/172440982-1679b056-419e-4a63-9da4-c512c0dca417.png"
     
# Result View

https://docs.google.com/spreadsheets/d/1b2JnB4h7wAknER5g156xD5ZxCZVTJwZkr9hRIYX75i0/edit#gid=1007729239
