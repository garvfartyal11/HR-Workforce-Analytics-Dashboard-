import pandas as pd
import random
from faker import Faker

fake = Faker("en_IN")

departments = [
    "IT",
    "HR",
    "Finance",
    "Sales",
    "Marketing",
    "Operations"
]

designations = [
    "Executive",
    "Manager",
    "Analyst",
    "Engineer",
    "Officer",
    "Assistant"
]

education = [
    "B.Tech",
    "MBA",
    "B.Com",
    "MCA",
    "BBA",
    "M.Tech"
]

locations = [
    "Delhi",
    "Noida",
    "Lucknow",
    "Mumbai",
    "Pune",
    "Jaipur",
    "Bangalore"
]

marital = [
    "Single",
    "Married"
]

employee_data = []

for i in range(1001, 2001):

    gender = random.choice(["Male", "Female"])

    employee_data.append({

        "EmployeeID": i,

        "Name": fake.name_male() if gender=="Male" else fake.name_female(),

        "Gender": gender,

        "Age": random.randint(22,60),

        "Department": random.choice(departments),

        "Designation": random.choice(designations),

        "Education": random.choice(education),

        "Experience": random.randint(0,20),

        "JoiningDate": fake.date_between(start_date="-10y", end_date="today"),

        "Salary": random.randint(25000,150000),

        "Location": random.choice(locations),

        "MaritalStatus": random.choice(marital),

        "PerformanceScore": random.randint(1,10),

        "Attrition": random.choice(["Yes","No"])
    })

employee = pd.DataFrame(employee_data)

employee.to_csv("../Data/Employee.csv",index=False)

print("Employee Dataset Created Successfully")
attendance_data = []

months = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

for emp_id in employee["EmployeeID"]:
    for month in months:
        present = random.randint(20,26)
        absent = random.randint(0,4)
        leaves = random.randint(0,3)

        attendance_data.append({
            "EmployeeID": emp_id,
            "Month": month,
            "Present": present,
            "Absent": absent,
            "Leaves": leaves
        })

attendance = pd.DataFrame(attendance_data)

attendance.to_csv("../Data/Attendance.csv", index=False)

print("Attendance Dataset Created Successfully")
salary_data = []

for index, row in employee.iterrows():

    basic = row["Salary"]

    bonus = random.randint(2000,15000)

    tax = int((basic + bonus) * 0.10)

    net = basic + bonus - tax

    salary_data.append({

        "EmployeeID": row["EmployeeID"],

        "BasicSalary": basic,

        "Bonus": bonus,

        "Tax": tax,

        "NetSalary": net

    })

salary = pd.DataFrame(salary_data)

salary.to_csv("../Data/Salary.csv", index=False)

print("Salary Dataset Created Successfully")
recruitment_data = []

for i in range(201,251):

    applied = random.randint(50,200)

    interviewed = random.randint(20, applied)

    selected = random.randint(5, interviewed)

    rejected = interviewed - selected

    recruitment_data.append({

        "CandidateID": i,

        "Department": random.choice(departments),

        "Applied": applied,

        "Interviewed": interviewed,

        "Selected": selected,

        "Rejected": rejected

    })

recruitment = pd.DataFrame(recruitment_data)

recruitment.to_csv("../Data/Recruitment.csv", index=False)

print("Recruitment Dataset Created Successfully")
