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


# Feature Importance
<img width="987" alt="Screen Shot 2022-06-07 at 9 42 38 AM" src="https://user-images.githubusercontent.com/97919969/172437182-1d75bc83-84f4-4c48-a149-bd32689373b9.png">
<img width="484" alt="Screen Shot 2022-06-07 at 9 44 54 AM 1" src="https://user-images.githubusercontent.com/97919969/172437716-1d697cfa-034e-4ef9-8853-f153459e94a0.png">

The model shows that the most important feature is Vintage, and Vehicle Damage doesn’t have any importance.

# Tested Machine Learning Models
- Boruta
- KNN;
- Regression Logistic;
- Extra Trees;
- Random Forest;

# Machine Learning Modelling 
- Regression Logistic:

Among all machine learning models trained,  Extra Trees was one that showed a better result, which classifies all details using only 67% of the database, with a Lyft of approximately 1.70 better than random customer selection.

# Curve Cumulative Gain
<img width="886" alt="Captura de Tela 2022-09-29 às 9 04 40 AM" src="https://user-images.githubusercontent.com/97919969/193082213-bc8bbb3c-c92d-4858-9651-ce8bd4053713.png">
- Insights:
Impacting 40% of customers base we will be impacting more than 60% of all interested customers in purchase a new car insurance;


- To reach all interested customers in purchase a new car insurance it's needed utilize just  around 68% of customers base, being possible to rule out more than 30% of customers who will not be interested in buying car insurance. With this information, the business team can make some decisions such as reduce the team, or even double to make more calls, reduce the number of machines used, directly impacting the company's revenue.

# Manually Lift Curve
<img width="861" alt="Screen Shot 2022-06-07 at 9 58 18 AM" src="https://user-images.githubusercontent.com/97919969/172440135-60fe7064-ad37-447c-a9cf-21113584d08a.png">

 The Lift Curve shows how the results of the trained model is better than random model. As showed above, if the calls are made using the Randon Forest Model trained, impacting 20% of customers, the results will be 1.8 better than if the calls are made randomly.
 
# 4. Conclusion and Demostration 
# Manually ROI Curve

<img width="621" alt="Screen Shot 2022-06-07 at 10 00 45 AM" src="https://user-images.githubusercontent.com/97919969/172440613-41fa1e0d-5f01-4d5f-8539-1ef396f2eacf.png">

<img width="874" alt="Screen Shot 2022-06-07 at 10 03 04 AM" src="https://user-images.githubusercontent.com/97919969/172440982-1679b056-419e-4a63-9da4-c512c0dca417.png">


<img width="832" alt="Screen Shot 2023-09-07 at 10 27 48 AM" src="https://github.com/adrielepinto/health_insurance_cross_sell/assets/97919969/9d0a8f6f-ff6e-47da-81b5-bb7b7b533446">


     
# How to access the prediction

Click on the link bellow.

https://docs.google.com/spreadsheets/d/1b2JnB4h7wAknER5g156xD5ZxCZVTJwZkr9hRIYX75i0/edit#gid=1007729239
     
<img width="1440" alt="Screen Shot 2022-07-19 at 9 35 28 AM" src="https://user-images.githubusercontent.com/97919969/179803305-e667a4a3-2cec-4d20-87d0-d8eabd99e96a.png">
     
