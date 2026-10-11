
import pandas as pd

# Load Amazon Sales dataset
df = pd.read_csv("Amazon Sale Report.csv", low_memory=False)

# Convert Amount column to numeric
sales = pd.to_numeric(df["Amount"], errors="coerce").dropna()

# Calculate Q1, Q3 and IQR
Q1 = sales.quantile(0.25)
Q3 = sales.quantile(0.75)
IQR = Q3 - Q1

# Define outlier limits using the IQR method
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

# Identify outliers
outliers = sales[(sales < lower_limit) | (sales > upper_limit)]

# Display results
print("OUTLIER DETECTION USING IQR METHOD")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("Number of Outliers:", len(outliers))
print("\nFirst 20 Outlier Values:")
print(outliers.head(20).to_string(index=False))

# Explain the method
print("\nOutliers are values below the lower limit or above the upper limit.")
