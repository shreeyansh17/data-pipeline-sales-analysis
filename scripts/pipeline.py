import pandas as pd
import matplotlib.pyplot as plt

# =========================
# STEP 1: Load Data
# =========================
df = pd.read_csv("data/Product Sales Data.csv")

# =========================
# STEP 2: Data Cleaning
# =========================
# Column names clean
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values (if any)
df.fillna(0, inplace=True)

# =========================
# STEP 3: Data Transformation
# =========================
# New column
df['profit_per_unit'] = df['total_profit'] / df['total_units']

# =========================
# STEP 4: Basic Analysis
# =========================
print("\n📊 DATA INFO:")
print(df.info())

print("\n📊 MISSING VALUES:")
print(df.isnull().sum())

print("\n📊 SUMMARY STATS:")
print(df.describe())

# Total metrics
print("\n📊 TOTAL UNITS:", df['total_units'].sum())
print("📊 TOTAL PROFIT:", df['total_profit'].sum())

# =========================
# STEP 5: Month-wise Analysis
# =========================
monthly_profit = df.groupby('month')['total_profit'].sum()
print("\n📊 MONTHLY PROFIT:\n", monthly_profit)

# =========================
# STEP 6: Top Products Analysis
# =========================
product_sales = df.select_dtypes(include='number').sum()
product_sales = product_sales.drop(['total_units', 'total_profit'])

print("\n📊 TOP PRODUCTS:\n", product_sales.sort_values(ascending=False))

# =========================
# STEP 7: Visualization
# =========================
monthly_profit.plot(kind='bar')

plt.title("Monthly Profit Analysis")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.tight_layout()

# Save graph instead of showing (professional way)
plt.savefig("output/monthly_profit.png")
plt.show()

# =========================
# STEP 8: Save Clean Data
# =========================
df.to_csv("output/clean_data.csv", index=False)
plt.title("Monthly Profit Analysis", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Profit")
plt.xticks(rotation=45)

print("\n✅ Project Completed Successfully!")