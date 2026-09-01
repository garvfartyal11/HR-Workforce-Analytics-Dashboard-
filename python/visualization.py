import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
employee = pd.read_csv("../Data/Employee_Clean.csv")

# ------------------------------
# Department Wise Employees
# ------------------------------

dept = employee["Department"].value_counts()

plt.figure(figsize=(8,5))
dept.plot(kind="bar")

plt.title("Department Wise Employees")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.show()

# ------------------------------
# Gender Distribution
# ------------------------------

gender = employee["Gender"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    gender,
    labels=gender.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Gender Distribution")

plt.show()

# ------------------------------
# Salary Distribution
# ------------------------------

plt.figure(figsize=(8,5))

plt.hist(employee["Salary"], bins=20)

plt.title("Salary Distribution")

plt.xlabel("Salary")

plt.ylabel("Employees")

plt.show()

# ------------------------------
# Performance Score
# ------------------------------

performance = employee["PerformanceScore"].value_counts().sort_index()

plt.figure(figsize=(8,5))

performance.plot(kind="line", marker="o")

plt.title("Performance Score")

plt.xlabel("Score")

plt.ylabel("Employees")

plt.grid(True)

plt.show()

# ------------------------------
# Attrition
# ------------------------------

attrition = employee["Attrition"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    attrition,
    labels=attrition.index,
    autopct="%1.1f%%"
)

plt.title("Employee Attrition")

plt.show()

print("Charts Created Successfully")
