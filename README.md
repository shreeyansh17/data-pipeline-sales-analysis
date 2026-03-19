# 📊 End-to-End Data Pipeline & Sales Performance Analysis

## 🎯 Business Problem
How can we identify the most profitable months and products to improve overall sales performance?

## 📌 Overview
This project demonstrates an end-to-end data pipeline for processing, cleaning, and analyzing sales data using Python and SQL concepts.

## 🛠️ Tools & Technologies
- Python (Pandas, Matplotlib)
- SQL (for analytical queries)
- Data Cleaning & Transformation
- Data Visualization

## ⚙️ Workflow
1. Loaded raw dataset from CSV
2. Cleaned and standardized column names
3. Removed duplicates and handled missing values
4. Created new feature: profit per unit
5. Performed monthly profit analysis
6. Identified top-performing products
7. Visualized insights using bar charts
8. Saved processed outputs

## 📊 Key Insights
- November shows the highest profit among all months
- February has the lowest sales performance
- Certain products contribute significantly to total profit

## 🧾 Sample SQL Analysis
```sql
SELECT month, SUM(total_profit) AS profit
FROM sales_data
GROUP BY month
ORDER BY profit DESC;