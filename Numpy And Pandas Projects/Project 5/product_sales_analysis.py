"""
Project 5: Product Sales Analysis
Combines NumPy calculations with Pandas DataFrame operations
"""

import numpy as np
import pandas as pd


# Given Dataset
# Rows = Products (P1 to P5), Columns = Jan, Feb, Mar
sales = np.array([
    [100, 120, 150],
    [80, 100, 130],
    [150, 160, 180],
    [70, 90, 110],
    [120, 140, 160]
])

products = ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"]
months = ["January", "February", "March"]

print("Sales Data:\n", sales)
print("-" * 60)


# 1. Total sales for every product (row-wise sum)
total_sales_per_product = sales.sum(axis=1)
print("1. Total sales for every product:")
for p, t in zip(products, total_sales_per_product):
    print(f"   {p}: {t}")
print("-" * 60)


# 2. Average monthly sales for every product (row-wise mean)
avg_sales_per_product = sales.mean(axis=1)
print("2. Average monthly sales for every product:")
for p, a in zip(products, avg_sales_per_product):
    print(f"   {p}: {a:.2f}")
print("-" * 60)


# 3. Best-selling product (highest total sales)
best_index = np.argmax(total_sales_per_product)
print(f"3. Best-selling product: {products[best_index]} "
      f"with total sales = {total_sales_per_product[best_index]}")
print("-" * 60)


# 4. Worst-selling product (lowest total sales)
worst_index = np.argmin(total_sales_per_product)
print(f"4. Worst-selling product: {products[worst_index]} "
      f"with total sales = {total_sales_per_product[worst_index]}")
print("-" * 60)


# 5. Highest sales in each month (column-wise max)
highest_per_month = sales.max(axis=0)
print("5. Highest sales in each month:")
for m, h in zip(months, highest_per_month):
    print(f"   {m}: {h}")
print("-" * 60)


# 6. Lowest sales in each month (column-wise min)
lowest_per_month = sales.min(axis=0)
print("6. Lowest sales in each month:")
for m, l in zip(months, lowest_per_month):
    print(f"   {m}: {l}")
print("-" * 60)


# 7. Products whose average sales are greater than 120
mask = avg_sales_per_product > 120
good_products = [p for p, m in zip(products, mask) if m]
print("7. Products with average sales greater than 120:")
print(f"   {good_products}")
print("-" * 60)


# 8. Total sales for each month (column-wise sum)
total_sales_per_month = sales.sum(axis=0)
print("8. Total sales for each month:")
for m, t in zip(months, total_sales_per_month):
    print(f"   {m}: {t}")
print("-" * 60)


# 9. Standard deviation of monthly sales (per month, column-wise)
std_per_month = sales.std(axis=0)
print("9. Standard deviation of sales for each month:")
for m, s in zip(months, std_per_month):
    print(f"   {m}: {s:.2f}")
print("-" * 60)


# 10. High/Low product classification using np.where()
# Rule: if total sales > average of all totals -> High, else Low
overall_avg_total = total_sales_per_product.mean()
classification = np.where(total_sales_per_product > overall_avg_total, "High", "Low")
print("10. High/Low classification of products:")
for p, c in zip(products, classification):
    print(f"   {p}: {c}")
print("-" * 60)


# 11. Pandas DataFrame with Product, Total Sales, Average Sales
df = pd.DataFrame({
    "Product": products,
    "Total Sales": total_sales_per_product,
    "Average Sales": avg_sales_per_product,
    "Category": classification
})
print("11. Sales DataFrame:")
print(df)
print("-" * 60)

# 12. Sort the DataFrame by Total Sales (descending)
df_sorted = df.sort_values(by="Total Sales", ascending=False).reset_index(drop=True)
print("12. DataFrame sorted by Total Sales (highest to lowest):")
print(df_sorted)
