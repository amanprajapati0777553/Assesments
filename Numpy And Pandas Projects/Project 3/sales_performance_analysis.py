import numpy as np
import pandas as pd

# Project 3: Sales Performance Analysis
# Given dataset
sales = np.array([
    [12000, 15000, 18000],
    [10000, 14000, 16000],
    [18000, 20000, 22000],
    [9000, 12000, 15000],
    [15000, 17000, 19000]
])

salespersons = ["Person A", "Person B", "Person C", "Person D", "Person E"]
months = ["January", "February", "March"]

print("Sales Data:")
print(sales)
print()


# 1. Total sales of each salesperson (row-wise sum, axis=1)
total_sales_per_person = sales.sum(axis=1)
print("1. Total sales per salesperson:", total_sales_per_person)


# 2. Average monthly sales for each salesperson (row-wise mean)
avg_sales_per_person = sales.mean(axis=1)
print("2. Average sales per salesperson:", avg_sales_per_person)


# 3. Highest sales in each month (column-wise max, axis=0)
highest_per_month = sales.max(axis=0)
print("3. Highest sales per month:", highest_per_month)


# 4. Lowest sales in each month (column-wise min, axis=0)
lowest_per_month = sales.min(axis=0)
print("4. Lowest sales per month:", lowest_per_month)


# 5. Salesperson with the highest total sales
best_index = np.argmax(total_sales_per_person)
best_salesperson = salespersons[best_index]
print("5. Salesperson with highest total sales:", best_salesperson,
      "with", total_sales_per_person[best_index])


# 6. Salespersons whose average sales are above 15000
above_15k_mask = avg_sales_per_person > 15000
above_15k_names = [salespersons[i] for i in range(len(salespersons)) if above_15k_mask[i]]
print("6. Salespersons with average sales above 15000:", above_15k_names)


# 7. Total company sales for each month (column-wise sum)
total_company_sales_per_month = sales.sum(axis=0)
print("7. Total company sales per month:", total_company_sales_per_month)


# 8. Standard deviation of monthly sales (per salesperson, across months)
std_dev_per_person = sales.std(axis=1)
print("8. Standard deviation per salesperson:", std_dev_per_person)


# 9. Classify salespersons using np.where()
#    Excellent: avg >= 18000
#    Good: 14000 <= avg < 18000
#    Needs Improvement: avg < 14000
performance = np.where(
    avg_sales_per_person >= 18000, "Excellent",
    np.where(avg_sales_per_person >= 14000, "Good", "Needs Improvement")
)
print("9. Performance classification:", performance)


# 10. Convert final results into a Pandas DataFrame
df = pd.DataFrame({
    "Salesperson": salespersons,
    "January": sales[:, 0],
    "February": sales[:, 1],
    "March": sales[:, 2],
    "Total Sales": total_sales_per_person,
    "Average Sales": avg_sales_per_person,
    "Std Dev": std_dev_per_person,
    "Performance": performance
})

print("\n10. Final DataFrame:")
print(df)

# Bonus: monthly summary as a separate small DataFrame
monthly_summary = pd.DataFrame({
    "Month": months,
    "Total Company Sales": total_company_sales_per_month,
    "Highest Sale": highest_per_month,
    "Lowest Sale": lowest_per_month
})

print("\nBonus - Monthly Summary:")
print(monthly_summary)
