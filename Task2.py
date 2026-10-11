import pandas as pd

# Load Amazon Sales dataset
df = pd.read_csv("Amazon Sale Report.csv", low_memory=False)

# Convert Amount column to numeric
sales = pd.to_numeric(df["Amount"], errors="coerce").dropna()

# Calculate variance and standard deviation
variance_value = sales.var()
std_value = sales.std()

# Display results
print("Total Records:", len(df))
print("Variance of Sales:", variance_value)
print("Standard Deviation of Sales:", std_value)