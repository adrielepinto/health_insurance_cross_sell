# Insurance Service Purchase Prediction and Propensity


![car](https://github.com/adrielepinto/health_insurance_cross_sell/assets/97919969/f24973e9-50c9-4601-b2ec-ec1f4979475a)


NOTE: The business context is fictitious, however all planning and development of the solution is implemented following all the steps of a real market project.

# 1.0 BUSINESS PROBLEM

Insurance All is a company that offer health insurance services, and the product team is analyzing the possibility of offering policyholders a new product: Automobile Insurance. However, the business team needs to Know which customers would be interested in buying the new product with follow facts:
- The company has a list of 380.000 of posssible interested customers;
- The company has the capacity to make only 20.000 calls by period campaign.
- The product team selected 127,000 new customers who did not respond to the survey to participate in a campaign.
## 1.1 Understanding the Business Problem

- Business Problem/Question: What?

Classify the customers with potential interest in purchasing a new service and measure this interest in order to prioritize them.

- Root Cause of the Problem: Why carry out this project?

Be assertive in approaching customers most likely to purchase the new service by extracting knowledge from research with the customer base that the company has collected. Thus, reducing operation costs and efforts, maximizing profit.


# 2.0 Data
The data for this project is available on the [Kaggle platform](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction)

# 3.0 Business Assumptions
- Every customer collected in the survey has a 100% probability of purchasing new car insurance;
- The total average cost of the operation is 20.00 dollars;
- The company's average revenue when selling a vehicle insurance product to a customer is 100.00 dollars.

  
# 4.0 Business Solution:

## 4.1 Solution Planning 
The strategy adopted to resolve the problem is based on the Cross-industry standard process for data mining ( CRISP-DM )  project management methodology.


![crisp](https://github.com/adrielepinto/health_insurance_cross_sell/assets/97919969/aa7159a1-de8d-4038-add4-8d08a2ac1887)

## 5.0 Solution Process

<img width="678" alt="Captura de Tela 2022-09-28 às 9 31 17 AM" src="https://user-images.githubusercontent.com/97919969/192836667-0063a785-d763-4ea0-9578-44ab97de1c53.png">



### 5.1 Step 01 - Data Extraction 
-  Extract data from a database on AWS Cloud with PostgresSQL via Python.
  
### 5.2 Step 02 - Data Cleaning
Fix or remove incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. 
- Understand the meaning of each attribute;
- Check the size of the data;
- Rename columns;
- Identify and treat null and duplicate data;
- Analyze and ensure correct data types;
- Apply descriptive statistics to analyze attributes;
- Identify and treat outlier data;

### 5.3 Step 03 - Exploratory Data  
Analyze and understand data. 

The objective is to understand the variables/attributes that impact the phenomenon (target) of analysis and generate business insights.This step involves Feature Engineering, Variable Filtering and Exploratory Data Analysis (EDA)

#### 5.3.1 Feature Engineering
- Create the hypothesis map;
-  Create the Hyphotesis;
-  Validate the hyphotesis;

#### 5.3.2 Variable Filtering
Here the objective is to define attributes and their values according to a real business scenario and of interest for analyzing the phenomenon.

#### 5.3.3  Exploratory Data Analysis  (EDA):
 It consists of measuring the impact of features/attributes on the response variable (phenomenon being evaluated).

- Perform univariate analysis to understand the distribution of data for each attribute;
- Perform bivariate analysis, to validate hypotheses, generate insights by understanding the impact of attributes on the analysis of the phenomenon;
- Create a summary table of the results of the hypotheses, and the estimated relevance of the attributes for model learning;
- Perform multivariate analysis, to visualize linearly dependent columns through correlation analysis.

 ###  5.4 Step 04. Data Modeling

The objective is to prepare the data to teach Machine Learning algorithms the patterns, involving Data Preparation and Feature Selection of a Data Science project.

#### 5.4.1 Data Preparation:

The objective is to ensure that the data is numerical and on the same scale to facilitate learning of the algorithms.

- Evaluate the distribution of numerical attributes to apply the appropriate form of standardization; (Normalization, Rescale)
- Apply transformations on data; (categorical and numerical variables (Encoding's), response variable, cyclical in nature)
- Apply the preparations under the validation data as well.
- 
#### 5.4.2 Feature Selection:

The objective is to select the most relevant attributes for the model.

- Exclude attributes that were transformed into others in the feature engineering and data preparation stages;
- Define feature selection method;
- Compare suggestions from the method used with the result of the estimated relevance of the attributes for learning made in the EDA stage;
- Define the attributes that will train the machine learning algorithms.

### 5.5 Step 05 -  Machine Learning and Assessment Algorithms:

It comprises the stages of algorithm training and parameter optimization (validation stage), evaluation of the final algorithms on never-before-seen data.

The goal is to teach machine learning algorithms with training data, so that they can learn the behavior of a phenomenon with the best parameters and then generalize them to never-before-seen examples. And thus, bring the expected business return for the required application.

- Define algorithms to be applied, from simple to more complex;
- Define performance evaluation metrics and apply them to validation data using a cross-validation method;
- Define parameter optimization strategy to detect parameters that make models perform better;
- Define best algorithm(s) and their best parameters to apply to test data and evaluate performance;
- Define an algorithm with its best parameters to put into production;
- Evaluate the performance of the final algorithm from a Machine Learning perspective.

### 5.6 Step 06 - Translation and Interpretation:

Convert machine learning model results into business metrics, that is, if the model is implemented, how effective it is in the intended task, converting it into financial values.

- Answer the business questions required under the test data;
- Evaluate the performance of the final algorithm implemented in the business context from a financial aspect (revenue, cost and profit).
### 5.7 Model in Production ( Deploy ):

The objective is to make the model results accessible to any consumer (person, cell phone, app, website, Google Sheets, Excel, any software connected to the internet that can make an API request).

-  Create a class with all the necessary methods so that the final algorithm receives the transformed production data in the same way it was trained and performs the prediction;
- Build API to put the data model and project to be accessed;
- Test the API locally;
- Publish API on cloud server;
- Test the API locally in production;
- Define and develop a tool to access/query data in production.

  
# Attribute List
- Id: unique customer identifier.
- Gender: Gender of the customer.
- Age: customer's age.
- Driving License: 0, the client isn't allowed to drive and 1, the client has to drive.
- Region Code: Customer's region code.
- Previously Insured: 0, the customer doesn't have auto insurance and 1, the customer already has auto insurance.
- Vehicle Age: vehicle age.
- Vehicle Damage: 0, customer has never had his vehicle damaged in the past and 1, customer has had his vehicle damaged in the past.
- Annual Premium: amount the customer paid the company for annual health insurance.
- Policy sales channel: anonymous code for the customer contact channel.
- Vintage: number of days that the customer was associated with the company through the purchase of health insurance.
- Response: 0, the customer isn't interested and 1, the customer is interested.

# Questions to answer:
- 1. What are the main insights into the most relevant attributes of customers interested in purchasing auto insurance?
- 2. What percentage of customers interested in purchasing auto insurance will the sales team be able to contact by making 20,000 calls?
- 3. If the sales team's capacity increases to 40,000 calls, what percentage of customers interested in purchasing auto insurance will the sales team be able to contact?


# 6.0 Three Data Insigths

 # H1. 50% of female customers would be interested on the car insurance.
# FALSE #

According to the graphs, they show that only 31% of women are interested, while men show 52% interest. 21% more compared to women.
 
<img width="1090" alt="Screen Shot 2022-06-07 at 9 15 37 AM" src="https://user-images.githubusercontent.com/97919969/172434715-cb58ac55-7ae0-48f5-b0be-94b42aaf7963.png">

- 31% Female customers are not interested.
- 5.44% Female customers interested.
- 52% Male customers are not interested.
- 10% Male customers are interested.
-
# H2. Customers over 50 years old would be interested on the car insurance.
FALSE 
- Of the customers in the database, the graphs show that customers over 50 years of age reduce their interest in purchasing car insurance, which can be explained by the fact that, due to their age, these customers tend not to drive more.
- On the other hand, customers under 50 tend to buy car insurance.

<img width="1087" alt="Screen Shot 2022-06-07 at 9 20 09 AM" src="https://user-images.githubusercontent.com/97919969/172432069-867036bd-3539-4749-9e60-498e60c1a7d6.png">


# H3 - Customers who has cars less than one year are insterested on the car 
FALSE 
- Customers who own cars between 1 and 2 years old would be more interested in purchasing car insurance.
- However, customers who have owned cars for less than a year show less tha 1% of interest in buying car insurance.
<img width="1081" alt="Screen Shot 2022-06-07 at 9 23 04 AM" src="https://user-images.githubusercontent.com/97919969/172434983-dd85c7fc-c51e-425c-9a75-15411eb36699.png">
<img width="449" alt="Screen Shot 2022-06-07 at 9 34 33 AM" src="https://user-images.githubusercontent.com/97919969/172435393-95515893-5901-40e5-b390-ea26f6c6af3c.png">

- Bellow 1 year = 0.07% of  interested customers.
- Between 1 and 2 yars = 13% of interested customers.
- Over years = 2.80% of interested customers.


# 7.0 Machine Learning

This is the moment when the chosen algorithms learn the behavior of the data to predict a certain future behavior. Machine Learning Algorithms are capable of automating the data analysis process and making predictions in real time.

## 7.1 Tested Machine Learning Models
- Boruta
- KNN;
- Regression Logistic;
- Extra Trees;
- Random Forest;

Among all machine learning models trained,  Extra Trees was one that showed a better result, which classifies all details using only 67% of the database, with a Lyft of approximately 1.70 better than random customer selection.

## 7.2 Extra Tree Performance
This step in the process helps to identify possible errors and measure the model's performance according to the task for which it was designed. Which includes the metrics of Precision, Recall and Accuracy.

Obs : k = 20 000
The metrics are meansuring to work with 20 000 clients

 ### 7.2.1 Preciosn Precision 
 Of all the customers that the model predicted were interested, how many were actually interested.

 <img width="687" alt="Screen Shot 2023-09-17 at 1 37 50 PM" src="https://github.com/adrielepinto/health_insurance_cross_sell/assets/97919969/986cb191-7196-4522-81da-6dfcc917bb19">

 
 Means that the algorithm has a 100% probability of hitting interested customers

 
 ### 7.2.2 Recall 
 Of all the customers who are actually interested, how many did the model predict to be interested. (Class 1)

<img width="687" alt="Screen Shot 2023-09-17 at 1 37 50 PM" src="https://github.com/adrielepinto/health_insurance_cross_sell/assets/97919969/89b5b2f4-1d87-44f2-b8fd-680bbd4f2f1b">


 It means that the Algorithm has a 95% chance of catching all interested customers
 
 ### 7.2.3 Accuracy
 Accuracy tells you how often the model's predictions are correct.
 
 <img width="484" alt="Screen Shot 2023-09-17 at 1 48 32 PM" src="https://github.com/adrielepinto/health_insurance_cross_sell/assets/97919969/9e91c533-fdc8-40a6-a479-12ac950200f2">

 
Simulating that the company will only work with customers who have a probability of over 60% of purchasing insurance, the model is getting 84% of its predictions right.
## 7.3 Model Performance - Roy Curve
Roy curve, is a line graph that shows the model's gain behavior.

    <img width="887" alt="Screen Shot 2023-09-17 at 2 04 31 PM" src="https://github.com/adrielepinto/health_insurance_cross_sell/assets/97919969/3d4dad04-98eb-4eb8-9c1d-ee54e448a701">


# 8.0 Model Results 

<img width="686" alt="Screen Shot 2023-09-17 at 2 09 04 PM" src="https://github.com/adrielepinto/health_insurance_cross_sell/assets/97919969/2256c397-12ba-430a-ba96-1f1da856b155">

## * considering only working with customers who have a probability above 30% of purchasing the product, with a customer cost of 500.00 and the sale of each policy worth 2,300.00 for each interested customer.**

- Total Number of customer to work with: 1,409.00
- Total Cost of customer to work with: $704,500.00
- Total Gross Revenue of customer to work with: $1,100,011.80
- Total Expected Revenue from customers to work with: $395,511.80

# 9.0 Business questions

## 9.1 What are the main insights into the most relevant attributes of customers interested in purchasing auto insurance?

- Only 1% of the database is interested in purchasing a new car service.
- The expected revenue is $395,511.80.
- Customers between 30-50 are more interested in a Vehicle Insurance;
- Custumer withy newest cars are more interested in a Vehicle Insurance;

## 9.2 What percentage of customers interested in purchasing auto insurance will the sales team be able to contact by making 20,000 calls?

-YES, the sales team will be able to contact all interested customers, using only 1409 calls, which represents 1% of the database

<img width="607" alt="Screen Shot 2023-09-17 at 2 15 51 PM" src="https://github.com/adrielepinto/health_insurance_cross_sell/assets/97919969/2392a1a5-9860-477a-9d01-01e1040ed35a">

## 9.3 If the sales team's capacity increases to 40,000 calls, what percentage of customers interested in purchasing auto insurance will the sales team be able to contact?

Unfortunately, it will not be necessary to increase calls because due to the low number of interested parties, the sales team's capacity is more than sufficient to serve all interested customers.


## 9.4 How to access the prediction


Click on the link bellow.

https://docs.google.com/spreadsheets/d/1b2JnB4h7wAknER5g156xD5ZxCZVTJwZkr9hRIYX75i0/edit#gid=1007729239
     
<img width="1440" alt="Screen Shot 2022-07-19 at 9 35 28 AM" src="https://user-images.githubusercontent.com/97919969/179803305-e667a4a3-2cec-4d20-87d0-d8eabd99e96a.png">


# 10.0  Conclusion 


# 11.0 Next StepTo enhance the Model Results


- Check which external variables increase the likelihood of the customer wanting car insurance.
- Collect more data regarding the customer, such as salaries, where they live, number of children, whether they have their own home or not, to help the model select interested customers with more precision.
- Check what can lower customer costs.
- Categorize what types of insurance services would be offered. (complete policy or just for third parties)

  # Tools:
  - Jupyter Notebook;
  - Pandas, Numpy, seaborn, matplot libraries
  - Sklearn Libraries
  - Picle;
  - Google Sheets;
    
## contact me at [LinkedIn](adrielepinto.github.io/portfolio/) if you have any question abou this project.  

Thank you for reding my project :)
