
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# TASK 8: EDA - CORRELATION AND INSIGHTS
# ==========================================

# Load the cleaned dataset
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

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Convert numerical columns
df["Amount"] = pd.to_numeric(
    df["Amount"], errors="coerce"
)
df["Qty"] = pd.to_numeric(
    df["Qty"], errors="coerce"
)

# Convert Date column
# Handles dates such as 03-31-22 and similar formats
df["Date"] = pd.to_datetime(
    df["Date"].astype(str).str.strip(),
    format="mixed",
    errors="coerce",
    dayfirst=False
)

print("\n========== DATASET INFORMATION ==========")
print("Rows and columns:", df.shape)
print("Numerical variables: Amount and Qty")
print("Valid dates:", df["Date"].notna().sum())

# ==========================================
# 1. CORRELATION ANALYSIS
# ==========================================

numeric_data = df[["Amount", "Qty"]].dropna()

correlation = numeric_data["Amount"].corr(
    numeric_data["Qty"]
)

print("\n========== 1. CORRELATION ANALYSIS ==========")
print(
    "Correlation between Amount and Qty:",
    round(correlation, 4)
)

if correlation >= 0.7:
    print("Interpretation: Strong positive relationship")
elif correlation >= 0.3:
    print("Interpretation: Moderate positive relationship")
elif correlation > 0:
    print("Interpretation: Weak positive relationship")
elif correlation <= -0.7:
    print("Interpretation: Strong negative relationship")
elif correlation <= -0.3:
    print("Interpretation: Moderate negative relationship")
elif correlation < 0:
    print("Interpretation: Weak negative relationship")
else:
    print("Interpretation: No linear correlation")

# Correlation heatmap
plt.figure(figsize=(7, 5))

sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    fmt=".2f"
)

plt.title("Correlation Heatmap of Amazon Sales")
plt.tight_layout()
plt.show()

# ==========================================
# 2. SCATTER PLOT
# ==========================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=numeric_data,
    x="Qty",
    y="Amount",
    alpha=0.4
)

plt.title("Relationship Between Quantity and Order Amount")
plt.xlabel("Quantity")
plt.ylabel("Order Amount (INR)")
plt.tight_layout()
plt.show()

# ==========================================
# 3. TOP 10 PRODUCT CATEGORIES
# ==========================================

category_data = df.dropna(
    subset=["Category", "Amount"]
).copy()

category_data["Category"] = (
    category_data["Category"]
    .astype(str)
    .str.strip()
)

category_sales = (
    category_data.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

top_categories = category_sales.head(10)

print("\n========== 3. TOP PRODUCT CATEGORY ==========")

if not top_categories.empty:
    print("Highest-selling category:", top_categories.index[0])
    print(
        "Total sales amount (INR):",
        round(top_categories.iloc[0], 2)
    )

plt.figure(figsize=(10, 6))

sns.barplot(
    x=top_categories.values,
    y=top_categories.index
)

plt.title("Top 10 Product Categories by Total Sales Amount")
plt.xlabel("Total Sales Amount (INR)")
plt.ylabel("Product Category")
plt.tight_layout()
plt.show()

# ==========================================
# 4. MONTHLY SALES TREND
# ==========================================

monthly_data = df.dropna(
    subset=["Date", "Amount"]
).copy()

monthly_data["Month"] = (
    monthly_data["Date"].dt.to_period("M")
)

monthly_sales = (
    monthly_data.groupby("Month")["Amount"]
    .sum()
    .sort_index()
)

print("\n========== 4. MONTHLY SALES TREND ==========")

if not monthly_sales.empty:
    print(monthly_sales)

    plt.figure(figsize=(9, 5))

    plt.plot(
        monthly_sales.index.astype(str),
        monthly_sales.values,
        marker="o"
    )

    plt.title("Monthly Amazon Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales Amount (INR)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("No valid dates available for monthly analysis.")

# ==========================================
# 5. KEY INSIGHTS
# ==========================================

print("\n========== 5. KEY INSIGHTS ==========")

# Insight 1: Correlation
print(
    "Insight 1: The correlation between Amount and Qty is",
    round(correlation, 4)
)

if 0 < correlation < 0.3:
    print(
        "This indicates a weak positive linear relationship "
        "between quantity and order amount."
    )
elif correlation >= 0.3:
    print(
        "There is a positive relationship between quantity "
        "and order amount."
    )
elif correlation < 0:
    print(
        "There is a negative relationship between quantity "
        "and order amount."
    )
else:
    print("There is no linear relationship between these variables.")

# Insight 2: Highest-selling category
if not top_categories.empty:
    print(
        "\nInsight 2: The highest-selling category is",
        top_categories.index[0],
        "with total sales of INR",
        round(top_categories.iloc[0], 2)
    )

# Insight 3: Monthly sales
if not monthly_sales.empty:
    highest_month = monthly_sales.idxmax()
    lowest_month = monthly_sales.idxmin()

    print(
        "\nInsight 3: Highest monthly sales occurred in",
        str(highest_month),
        "with INR",
        round(monthly_sales.max(), 2)
    )

    print(
        "Lowest monthly sales occurred in",
        str(lowest_month),
        "with INR",
        round(monthly_sales.min(), 2)
    )
else:
    print(
        "\nInsight 3: Monthly sales insight could not be calculated "
        "because valid dates were unavailable."
    )

print("\n========== TASK 8 COMPLETED SUCCESSFULLY ==========")
