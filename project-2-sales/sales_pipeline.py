import pandas as pd
import numpy as np
import datetime
from sqlalchemy import create_engine

print(f"⏰ Execution Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("🚀 Project 2: Generating Indian Regional Sales & Profit logs...")

# 1. Setting up our cities and products across India
regions_list = ['North-Delhi', 'South-Bangalore', 'West-Mumbai', 'East-Kolkata', 'Central-Indore']
items_list = ['Executive Notebook A4', 'Gel Pen Blue 0.5mm', 'Premium Marker Black', 'A4 Copier Paper 75GSM', 'Plastic Ruler 30cm']

# 2. Generating 100 automatic sales receipts
np.random.seed(10)
rows_count = 100

ids_array = list(range(5001, 5001 + rows_count))
chosen_regions = [str(np.random.choice(regions_list)) for _ in range(rows_count)]
chosen_items = [str(np.random.choice(items_list)) for _ in range(rows_count)]
units_sold_array = [int(np.random.randint(10, 500)) for _ in range(rows_count)]

# Business logic: Price vs Manufacturing Cost for each stationery item
price_map = {'Executive Notebook A4': 120, 'Gel Pen Blue 0.5mm': 15, 'Premium Marker Black': 45, 'A4 Copier Paper 75GSM': 230, 'Plastic Ruler 30cm': 20}
cost_map = {'Executive Notebook A4': 70, 'Gel Pen Blue 0.5mm': 8, 'Premium Marker Black': 22, 'A4 Copier Paper 75GSM': 140, 'Plastic Ruler 30cm': 11}

revenue_array = []
cost_array = []

# Calculating money earned and money spent for every receipt
for item, units in zip(chosen_items, units_sold_array):
    rev = units * price_map[item]
    cst = units * cost_map[item]
    revenue_array.append(float(rev))
    cost_array.append(float(cst))

# 3. Putting everything into a neat table shape
sales_data = {
    'transaction_id': ids_array,
    'region': chosen_regions,
    'item_name': chosen_items,
    'units_sold': units_sold_array,
    'total_revenue_inr': revenue_array,
    'total_cost_inr': cost_array
}

df_sales = pd.DataFrame(sales_data)

print(f"✅ Successfully created {len(df_sales)} sales rows.")

print("\n🔌 Connecting to your PostgreSQL Server...")
# Using your password 'admin123'
engine = create_engine('postgresql://postgres:admin123@localhost:5432/stationery_db')

print("📤 Loading dataset into SQL as 'sales_performance_table'...")
df_sales.to_sql('sales_performance_table', engine, if_exists='replace', index=False)

print("\n🎉 SUCCESS! Open pgAdmin. Your 'sales_performance_table' is live in SQL!")
