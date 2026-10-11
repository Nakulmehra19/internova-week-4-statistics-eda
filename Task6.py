
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Amazon Sales dataset
df = pd.read_csv("Amazon Sale Report.csv", low_memory=False)

# Convert numerical columns
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce")

# Use a smaller sample for faster plotting
plot_data = df.sample(n=min(2000, len(df)), random_state=42).copy()

sns.set_theme(style="whitegrid")

# 1. COUNT PLOT: Number of orders by category
plt.figure(figsize=(10, 5))
sns.countplot(data=plot_data, x="Category",
              order=plot_data["Category"].value_counts().index)
plt.title("Order Count by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Number of Records")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# 2. BOX PLOT: Amount distribution by category
plt.figure(figsize=(10, 5))
sns.boxplot(data=plot_data, x="Category", y="Amount")
plt.title("Order Amount Distribution by Category")
plt.xlabel("Product Category")
plt.ylabel("Order Amount")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# 3. HEATMAP: Correlation between numerical variables
numeric_data = df[["Amount", "Qty"]].dropna()
correlation_matrix = numeric_data.corr()

plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True,
            cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f")
plt.title("Correlation Heatmap of Sales Variables")
plt.tight_layout()
plt.show()

# 4. PAIR PLOT: Relationships between numerical variables
pair_data = df[["Amount", "Qty"]].dropna()
pair_data = pair_data.sample(n=min(1000, len(pair_data)), random_state=42)

sns.pairplot(pair_data, diag_kind="hist")
plt.suptitle("Pair Plot: Amount and Quantity", y=1.02)
plt.show()

print("All four Seaborn visualizations completed.")
