import pandas as pd

# Load Amazon Sales dataset
df = pd.read_csv("Amazon Sale Report.csv")

# Select numerical sales data
sales = pd.to_numeric(df["Amount"], errors="coerce").dropna()

# Calculate statistics
print("Total Records:", len(df))
print("Mean Sales:", sales.mean())
print("Median Sales:", sales.median())
print("Mode of Sales:", sales.mode().tolist())