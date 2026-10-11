
import pandas as pd
import os

# ==========================================
# TASK 7: EDA - DATA INSPECTION AND CLEANING
# ==========================================

file_path = "Amazon Sale Report.csv"

# Load dataset
if not os.path.exists(file_path):
    print("ERROR: Amazon Sale Report.csv not found!")
    print("Keep the CSV file in the same folder as Task7.py.")
    raise SystemExit

df = pd.read_csv(file_path, low_memory=False)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# ==========================================
# PART 1: BEFORE CLEANING
# ==========================================

print("\n" + "=" * 60)
print("TASK 7: DATA INSPECTION AND CLEANING")
print("=" * 60)

print("\n========== BEFORE CLEANING ==========")

print("\n1. Number of Rows and Columns:")
print(df.shape)

print("\n2. Column Names:")
print(df.columns.tolist())

print("\n3. Data Types:")
print(df.dtypes.to_string())

print("\n4. Statistical Summary:")
print(df.describe(include="all").to_string())

print("\n5. First 5 Rows BEFORE Cleaning:")
print(df.head().to_string(index=False))

print("\n6. Missing Values by Column:")
print(df.isnull().sum().to_string())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

print("\n7. Duplicate Rows:")
print(df.duplicated().sum())

# ==========================================
# PART 2: DATA CLEANING
# ==========================================

clean_df = df.copy()

# Remove completely empty columns
empty_columns = clean_df.columns[
    clean_df.isnull().all()
].tolist()

if empty_columns:
    clean_df.drop(columns=empty_columns, inplace=True)
    print("\nCompletely empty columns removed:", empty_columns)
else:
    print("\nNo completely empty columns found.")

# Remove unnamed columns only if they are completely empty
unnamed_empty = [
    col for col in clean_df.columns
    if col.lower().startswith("unnamed")
    and clean_df[col].isnull().all()
]

if unnamed_empty:
    clean_df.drop(columns=unnamed_empty, inplace=True)
    print("Empty unnamed columns removed:", unnamed_empty)

# Clean spaces in text columns safely
text_columns = clean_df.select_dtypes(
    include=["object", "str"]
).columns

for col in text_columns:
    clean_df[col] = clean_df[col].map(
        lambda value: value.strip()
        if isinstance(value, str) else value
    )

    clean_df[col] = clean_df[col].replace("", pd.NA)

# Convert Amount and Qty to numeric
for col in ["Amount", "Qty"]:
    if col in clean_df.columns:
        clean_df[col] = pd.to_numeric(
            clean_df[col], errors="coerce"
        )

# Convert Date to datetime
if "Date" in clean_df.columns:
    clean_df["Date"] = pd.to_datetime(
        clean_df["Date"],
        errors="coerce"
    )

# Remove exact duplicate rows
duplicates_removed = int(clean_df.duplicated().sum())
clean_df = clean_df.drop_duplicates()

# Remove rows where Amount or Qty is missing/invalid
required_columns = [
    col for col in ["Amount", "Qty"]
    if col in clean_df.columns
]

rows_before_filter = len(clean_df)

if required_columns:
    clean_df = clean_df.dropna(subset=required_columns)

rows_removed_invalid = rows_before_filter - len(clean_df)

# Check and remove negative Amount or Qty values
rows_before_negative_check = len(clean_df)

if "Amount" in clean_df.columns:
    clean_df = clean_df[clean_df["Amount"] >= 0]

if "Qty" in clean_df.columns:
    clean_df = clean_df[clean_df["Qty"] >= 0]

rows_removed_negative = (
    rows_before_negative_check - len(clean_df)
)

# ==========================================
# PART 3: AFTER CLEANING
# ==========================================

print("\n" + "=" * 60)
print("========== AFTER CLEANING ==========")
print("=" * 60)

print("\n1. Number of Rows and Columns:")
print(clean_df.shape)

print("\n2. Column Names:")
print(clean_df.columns.tolist())

print("\n3. Updated Data Types:")
print(clean_df.dtypes.to_string())

print("\n4. Statistical Summary:")
print(clean_df.describe(include="all").to_string())

print("\n5. First 5 Rows AFTER Cleaning:")
print(clean_df.head().to_string(index=False))

print("\n6. Missing Values by Column:")
print(clean_df.isnull().sum().to_string())

print("\nTotal Missing Values Remaining:")
print(clean_df.isnull().sum().sum())

print("\n7. Duplicate Rows Remaining:")
print(clean_df.duplicated().sum())

# Check for negative values
print("\n8. Negative Values Check:")

if "Amount" in clean_df.columns:
    print(
        "Negative Amount values:",
        (clean_df["Amount"] < 0).sum()
    )

if "Qty" in clean_df.columns:
    print(
        "Negative Qty values:",
        (clean_df["Qty"] < 0).sum()
    )

# ==========================================
# PART 4: CLEANING SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("CLEANING SUMMARY")
print("=" * 60)

print("Original row count:", len(df))
print("Final row count:", len(clean_df))
print("Original column count:", len(df.columns))
print("Final column count:", len(clean_df.columns))
print("Duplicate rows removed:", duplicates_removed)
print("Rows removed due to missing/invalid values:", rows_removed_invalid)
print("Rows removed due to negative values:", rows_removed_negative)

# Save cleaned dataset
output_file = "Amazon_Sales_Cleaned.csv"
clean_df.to_csv(output_file, index=False)

print("\nCleaned dataset saved as:", output_file)
print("\nTask 7 completed successfully!")
