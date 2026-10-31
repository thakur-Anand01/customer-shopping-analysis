# Customer Shopping Behavior Analysis

An end-to-end Data Analytics project using Python, Pandas, MySQL, SQL and Power BI to analyze customer shopping behavior and identify business insights.

## Project Overview

This project analyzes a retail shopping dataset containing 3,900 records and 18 columns.

The goal is to understand customer purchasing patterns, product preferences, spending behavior, payment methods, discount usage and seasonal trends.

## Technologies Used

- **Python:** Data cleaning and exploratory data analysis
- **Pandas:** Data manipulation and analysis
- **MySQL:** Database management and SQL business analysis
- **Power BI:** Interactive dashboard development
- **VS Code:** Development environment

## Project Workflow

1. Data loading and inspection using Python.
2. Data cleaning and missing value treatment using Pandas.
3. Exploratory Data Analysis (EDA).
4. Importing the cleaned dataset into MySQL.
5. Writing SQL queries to answer business questions.
6. Building an interactive Power BI dashboard.
7. Documenting findings and business recommendations.

## Dataset Information

- Total records: 3,900
- Total columns: 18
- Unique Customer IDs: 3,900
- Missing values before cleaning: 37
- Duplicate rows: 0

Missing Review Rating values were replaced with the column mean (approximately 3.75).

## Key Business Insights

- Clothing is the most frequently purchased category, with 1,737 records.
- Footwear has the highest average purchase amount at $60.26.
- PayPal is the most frequently used payment method.
- The overall average purchase amount is $59.76.
- Fall has the highest average purchase amount at $61.56.
- Records without discounts have a slightly higher average purchase amount than discounted records.

## Power BI Dashboard

The dashboard contains two pages:

**Page 1 – Customer Overview**
- Total purchase amount
- Customer records
- Average purchase amount
- Average review rating
- Category analysis
- Age-group distribution
- Gender comparison

**Page 2 – Shopping Preferences**
- Discount usage
- Payment method distribution
- Seasonal spending
- Subscription status

Interactive slicers allow users to explore the data.

## Project Structure

```text
customer-shopping-analysis/
│
├── data/
│   ├── customer_shopping_behavior_raw.csv
│   └── cleaned/
│       └── customer_shopping_behavior_cleaned.csv
│
├── python/
│   ├── data_cleaning.py
│   ├── import_data_to_mysql.py
│   └── mysql_connection.py
│
├── sql/
│   └── business_analysis.sql
│
├── README.md
└── customer_shopping_analysis.pbix
```

## Limitations

- The dataset contains one record per Customer ID, so detailed repeat-transaction analysis is limited.
- Online versus offline sales cannot be compared because the dataset does not contain a sales channel column.
- The analysis identifies patterns and associations, not causal relationships.

## Conclusion

This project demonstrates an end-to-end data analytics workflow involving data preparation, exploratory analysis, SQL querying and interactive visualization.

It showcases practical skills in Python, Pandas, MySQL, SQL and Power BI.

## Author

Thakur Anand Kashyap

Data Analytics | Python | SQL | Power BI
