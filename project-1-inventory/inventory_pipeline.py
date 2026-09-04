import pandas as pd
import numpy as np
import datetime
from sqlalchemy import create_engine

print(f"⏰ Execution Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("🚀 Step 1: Simulating dynamic daily factory changes...")

# 1. Defining lists separately to prevent rendering bugs
items_list = [
    'Executive Notebook A4', 
    'Gel Pen Blue 0.5mm', 
    'Premium Marker Black', 
    'A4 Copier Paper 75GSM', 
    'Plastic Ruler 30cm'
]

ids_list = [101, 102, 103, 104, 105]
reorder_levels_list = [150, 150, 100, 120, 100]
prices_list = [120.00, 15.00, 45.00, 230.00, 20.00]

# 2. Feeding variables directly into the dictionary structure
data = {
    'item_id': ids_list,
    'item_name': items_list,
    'current_stock': [int(np.random.randint(5, 500)) for _ in range(5)],  # Generates a new random number every time!
    'reorder_level': reorder_levels_list,
    'unit_price_inr': prices_list
}

df = pd.DataFrame(data)

# 3. Apply the alert logic rule (True if stock drops below reorder level)
df['requires_reorder'] = df['current_stock'] < df['reorder_level']

print("\n📊 Current Dynamic Stock Status:")
print(df[['item_name', 'current_stock', 'requires_reorder']])

print("\n🔌 Step 2: Overwriting the SQL Database with fresh numbers...")
# Connecting using your password admin123
engine = create_engine('postgresql://postgres:admin123@localhost:5432/stationery_db')

# Overwrites the table in SQL with fresh dynamic data
df.to_sql('inventory_table', engine, if_exists='replace', index=False)

print("\n🎉 SUCCESS! Now open Power BI and hit the 'Refresh' button to see the magic!")
