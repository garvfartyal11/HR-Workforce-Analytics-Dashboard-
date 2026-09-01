import pandas as pd

print("=" * 50)
print("HR WORKFORCE ANALYTICS")
print("EMPLOYEE DATA ANALYSIS")
print("=" * 50)

# Load Dataset
employee = pd.read_csv("../Data/Employee_Clean.csv")

# -----------------------------
# Basic Information
# -----------------------------

print("\nTotal Employees :", len(employee))

print("\nDepartments")
print(employee["Department"].value_counts())

print("\nGender Distribution")
print(employee["Gender"].value_counts())

print("\nAverage Salary")
print(round(employee["Salary"].mean(), 2))

print("\nHighest Salary")
print(employee["Salary"].max())

print("\nLowest Salary")
print(employee["Salary"].min())

print("\nAverage Age")
print(round(employee["Age"].mean(), 2))

print("\nAverage Experience")
print(round(employee["Experience"].mean(), 2))

# -----------------------------
# Department Wise Salary
# -----------------------------

print("\nDepartment Wise Average Salary")
print(employee.groupby("Department")["Salary"].mean())

# -----------------------------
# Performance Analysis
# -----------------------------

print("\nAverage Performance Score")
print(round(employee["PerformanceScore"].mean(),2))

# -----------------------------
# Attrition Analysis
# -----------------------------

print("\nEmployee Attrition")
print(employee["Attrition"].value_counts())

# -----------------------------
# Location Analysis
# -----------------------------

print("\nEmployees by Location")
print(employee["Location"].value_counts())

# -----------------------------
# Marital Status
# -----------------------------

print("\nMarital Status")
print(employee["MaritalStatus"].value_counts())

print("\nAnalysis Completed Successfully")
