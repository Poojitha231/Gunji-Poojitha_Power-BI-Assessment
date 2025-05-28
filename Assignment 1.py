inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]

# calculate the TotalRevenue
Total_revenue=sum(item[2]*item[3] for item in inventory)
print(f'Total Revenue : {Total_revenue}')

# List Low stock item if stock is less than 5
Low_stock = [inventory[0] for item in inventory if item[4] < 5]
print(f'Low Stock : {Low_stock}')

# calculte the categorywise Revenue
category_revenue = {}
for item in inventory:
    category = item[1]
    revenue = item[2] * item[3]
    category_revenue[category] = category_revenue.get(category, 0) + revenue

# print("Category-wise Revenue:")
for category, revenue in category_revenue.items():
    print(f"{category}: ${round(revenue,2)}")