
import pandas as pd
import matplotlib.pyplot as plt

# Load Amazon Sales dataset
df = pd.read_csv("Amazon Sale Report.csv", low_memory=False)

# Clean numerical columns
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce")

# Remove rows with missing Amount or Qty
data = df.dropna(subset=["Amount", "Qty"]).copy()

# 1. LINE CHART: Monthly sales trend
data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
monthly_sales = (
    data.dropna(subset=["Date"])
    .groupby(data.dropna(subset=["Date"])["Date"].dt.to_period("M"))["Amount"]
    .sum()
)
monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(9, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Monthly Amazon Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales Amount")
plt.tight_layout()
plt.show()

# 2. BAR CHART: Sales by category
category_sales = data.groupby("Category")["Amount"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Top 10 Categories by Total Sales")
plt.xlabel("Product Category")
plt.ylabel("Total Sales Amount")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# 3. PIE CHART: Sales share by top 5 categories
top_categories = data.groupby("Category")["Amount"].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(8, 8))
plt.pie(top_categories.values, labels=top_categories.index, autopct="%1.1f%%", startangle=90)
plt.title("Sales Share of Top 5 Categories")
plt.tight_layout()
plt.show()

# 4. HISTOGRAM: Order amount distribution
plt.figure(figsize=(9, 5))
plt.hist(data["Amount"], bins=30, edgecolor="black")
plt.title("Distribution of Order Amounts")
plt.xlabel("Order Amount")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.show()

# 5. SCATTER PLOT: Quantity vs Amount
plt.figure(figsize=(9, 5))
plt.scatter(data["Qty"], data["Amount"], alpha=0.3)
plt.title("Relationship Between Quantity and Order Amount")
plt.xlabel("Quantity")
plt.ylabel("Order Amount")
plt.tight_layout()
plt.show()

print("All five visualizations created successfully.")
