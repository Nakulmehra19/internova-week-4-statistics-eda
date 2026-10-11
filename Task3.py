
import pandas as pd

# Load Amazon Sales dataset
df = pd.read_csv("Amazon Sale Report.csv", low_memory=False)

# Convert numerical columns
df["Qty"] = pd.to_numeric(df["Qty"], errors="coerce")
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

# Remove missing values
data = df[["Qty", "Amount"]].dropna()

# Part 1: Correlation
correlation = data["Qty"].corr(data["Amount"])

print("CORRELATION ANALYSIS")
print("Correlation between Quantity and Amount:", correlation)

if correlation > 0.5:
    print("Interpretation: Strong positive relationship")
elif correlation > 0:
    print("Interpretation: Weak positive relationship")
elif correlation < -0.5:
    print("Interpretation: Strong negative relationship")
elif correlation < 0:
    print("Interpretation: Weak negative relationship")
else:
    print("Interpretation: No linear correlation or very weak relationship")

# Part 2: Probability
# Example: Probability that a randomly selected order
# has an Amount greater than 1000
total_orders = len(data)
high_value_orders = (data["Amount"] > 1000).sum()

probability = high_value_orders / total_orders

print("\nPROBABILITY ANALYSIS")
print("Total valid records:", total_orders)
print("Orders above 1000:", high_value_orders)
print("Probability:", probability)
print("Probability percentage:", probability * 100, "%")
