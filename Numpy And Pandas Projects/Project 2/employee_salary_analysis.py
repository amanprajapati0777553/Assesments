"""
Project 2: Employee Salary Analysis
We analyze employee Salary, Experience, and Performance Score
using NumPy for calculations and Pandas for tabular display.
"""

import numpy as np
import pandas as pd

# Given Dataset
# Columns: Salary | Experience (Years) | Performance Score
salary = np.array([
    [25000, 2, 80],
    [45000, 5, 90],
    [30000, 3, 75],
    [60000, 8, 95],
    [35000, 4, 85]
])

# Splitting columns for easier use
salaries      = salary[:, 0]
experience    = salary[:, 1]
performance   = salary[:, 2]

print("=" * 60)
print("1. AVERAGE SALARY OF ALL EMPLOYEES")
print("=" * 60)
avg_salary = np.mean(salaries)
print("Average Salary =", avg_salary)


print("\n" + "=" * 60)
print("2. HIGHEST SALARY")
print("=" * 60)
highest_salary = np.max(salaries)
print("Highest Salary =", highest_salary)


print("\n" + "=" * 60)
print("3. LOWEST SALARY")
print("=" * 60)
lowest_salary = np.min(salaries)
print("Lowest Salary =", lowest_salary)


print("\n" + "=" * 60)
print("4. AVERAGE EXPERIENCE")
print("=" * 60)
avg_experience = np.mean(experience)
print("Average Experience =", avg_experience, "years")


print("\n" + "=" * 60)
print("5. EMPLOYEES WITH SALARY > 40,000")
print("=" * 60)
high_salary_employees = salary[salaries > 40000]
print(high_salary_employees)


print("\n" + "=" * 60)
print("6. EMPLOYEES WITH PERFORMANCE SCORE > 80")
print("=" * 60)
high_performers = salary[performance > 80]
print(high_performers)


print("\n" + "=" * 60)
print("7. EMPLOYEE WITH THE HIGHEST PERFORMANCE SCORE")
print("=" * 60)
best_index = np.argmax(performance)          # row index of best performer
best_employee = salary[best_index]
print("Employee row (Salary, Experience, Performance):", best_employee)


print("\n" + "=" * 60)
print("8. STANDARD DEVIATION OF SALARIES")
print("=" * 60)
salary_std = np.std(salaries)
print("Standard Deviation of Salary =", salary_std)


print("\n" + "=" * 60)
print("9. CLASSIFY EMPLOYEES AS HIGH SALARY / LOW SALARY (np.where)")
print("=" * 60)
# Rule: Salary >= average salary -> "High Salary", else "Low Salary"
salary_category = np.where(salaries >= avg_salary, "High Salary", "Low Salary")
print(salary_category)


print("\n" + "=" * 60)
print("10. CONVERT RESULTS INTO A PANDAS DATAFRAME")
print("=" * 60)
df = pd.DataFrame(salary, columns=["Salary", "Experience", "Performance"])
df["Salary Category"] = salary_category

print(df)

print("\nFinal Summary")
print("-" * 60)
print(f"Average Salary     : {avg_salary}")
print(f"Highest Salary      : {highest_salary}")
print(f"Lowest Salary       : {lowest_salary}")
print(f"Average Experience  : {avg_experience} years")
print(f"Salary Std Dev      : {salary_std:.2f}")
