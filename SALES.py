""" A sales company wants to analyze daily sales data. Given an array of sales numbers, find the day with the highest sales. """
sales = [120, 450, 320, 560, 760, 800, 540]
size = len(sales)  # Pythonic way to get the size of the list
max_sales = sales[0]
max_day = 0

for i in range(1, size):  # Python's range starts at 0 by default, so start from 1
    if sales[i] > max_sales:
        max_sales = sales[i]
        max_day = i

print(f"Day {max_day + 1} had the highest sales: {max_sales}") # f-string for cleaner formatting
