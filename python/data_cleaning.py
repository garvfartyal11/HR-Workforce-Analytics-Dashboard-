import pandas as pd

print("======================================")
print("HR Workforce Analytics Project")
print("Data Cleaning Process Started...")
print("======================================")

# Load Employee Dataset
employee = pd.read_csv("../Data/Employee.csv")

print("\nDataset Loaded Successfully!")

# Display first 5 rows
print("\nFirst 5 Rows")
print(employee.head())

# Dataset information
print("\nDataset Information")
print(employee.info())

# Shape of dataset
print("\nDataset Shape")
print(employee.shape)

# Column Names
print("\nColumn Names")
print(employee.columns)

# Check Missing Values
print("\nMissing Values")
print(employee.isnull().sum())

# Check Duplicate Rows
print("\nDuplicate Rows")
print(employee.duplicated().sum())

# Remove duplicate rows
employee.drop_duplicates(inplace=True)

# Fill missing values
employee.fillna("Unknown", inplace=True)

# Convert Joining Date into Date Format
employee["JoiningDate"] = pd.to_datetime(employee["JoiningDate"])

# Data Types
print("\nData Types")
print(employee.dtypes)

# Statistical Summary
print("\nStatistical Summary")
print(employee.describe(include="all"))

# Save Clean Dataset
employee.to_csv("../Data/Employee_Clean.csv", index=False)

print("\n======================================")
print("Employee_Clean.csv Created Successfully")
print("======================================")
