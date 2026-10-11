
import pandas as pd
import os

# ==========================================
# TASK 9: BUSINESS RECOMMENDATIONS
# ==========================================

# Load cleaned Amazon sales dataset
if os.path.exists("Amazon_Sales_Cleaned.csv"):
    df = pd.read_csv(
        "Amazon_Sales_Cleaned.csv",
        low_memory=False
    )
    print("Using cleaned Amazon sales dataset")
else:
    df = pd.read_csv(
        "Amazon Sale Report.csv",
        low_memory=False
    )
    print("Using original Amazon sales dataset")

# Clean column names
df.columns = df.columns.str.strip()

# Convert required columns
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce")

# ==========================================
# BUSINESS ANALYSIS
# ==========================================

# Category-wise sales
category_data = df.dropna(
    subset=["Category", "Amount"]
).copy()

category_data["Category"] = (
    category_data["Category"].astype(str).str.strip()
)

category_sales = (
    category_data.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

# Correlation between quantity and amount
numeric_data = df[["Amount", "Qty"]].dropna()
correlation = numeric_data["Amount"].corr(
    numeric_data["Qty"]
)

print("\n========== TASK 9: BUSINESS RECOMMENDATIONS ==========")

# Recommendation 1
if not category_sales.empty:
    top_category = category_sales.index[0]
    top_sales = category_sales.iloc[0]

    print("\nRECOMMENDATION 1: Focus on Top-Selling Categories")
    print(
        "Finding: The highest-selling category is",
        top_category,
        "with total sales of INR",
        round(top_sales, 2)
    )
    print(
        "Recommendation: Maintain sufficient stock of products "
        "in the top-selling category and use targeted promotions "
        "to support sales."
    )
    print(
        "Data support: Category-wise sales analysis shows that",
        top_category,
        "generated the highest total sales amount."
    )

# Recommendation 2
print("\nRECOMMENDATION 2: Improve Quantity and Revenue Analysis")
print(
    "Finding: The correlation between Quantity and Amount is",
    round(correlation, 4)
)
print(
    "Recommendation: Analyse product prices, discounts, product "
    "categories and order sizes before planning quantity-based offers."
)
print(
    "Data support: The weak correlation indicates that quantity "
    "alone does not strongly explain order amount in this dataset."
)

# Recommendation 3
print("\nRECOMMENDATION 3: Monitor Monthly Sales")
print(
    "Recommendation: Review monthly sales regularly and plan "
    "inventory and marketing campaigns around observed demand."
)
print(
    "Data support: Monthly sales analysis showed different sales "
    "totals across March, April, May and June 2022."
)
print(
    "Note: March and June cover partial periods in this dataset, "
    "so monthly comparisons should account for the number of days."
)

print("\n========== TASK 9 COMPLETED SUCCESSFULLY ==========")
