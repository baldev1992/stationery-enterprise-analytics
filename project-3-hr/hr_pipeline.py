import pandas as pd
import numpy as np
import datetime
from sqlalchemy import create_engine

print(f"⏰ Execution Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("🚀 Project 3: Generating Enterprise HR Lifecycle & Performance Metrics...")

# 1. Defining departments and designations to prevent rendering issues
departments_list = ['Operations', 'Sales', 'Logistics', 'Accounts', 'HR']
status_list = ['Active', 'Active', 'Active', 'Active', 'Resigned'] # Simulates an ~80% retention rate

# 2. Generating 60 employee profile records
np.random.seed(25)
employee_count = 60

emp_ids = list(range(1001, 1001 + employee_count))
chosen_deps = [str(np.random.choice(departments_list)) for _ in range(employee_count)]
chosen_status = [str(np.random.choice(status_list)) for _ in range(employee_count)]

# Simulating productivity scores (0% to 100%) and training hours completed
productivity_scores = [int(np.random.randint(55, 100)) for _ in range(employee_count)]
training_hours = [int(np.random.randint(2, 40)) for _ in range(employee_count)]
tasks_planned = [int(np.random.randint(20, 50)) for _ in range(employee_count)]

# Calculate tasks completed based on their simulated productivity score
tasks_completed = []
for planned, score in zip(tasks_planned, productivity_scores):
    completed = int(round(planned * (score / 100.0)))
    tasks_completed.append(completed)

# 3. Packaging into a clean dataframe
hr_data = {
    'employee_id': emp_ids,
    'department': chosen_deps,
    'employment_status': chosen_status,
    'tasks_planned': tasks_planned,
    'tasks_completed': tasks_completed,
    'productivity_score_pct': productivity_scores,
    'training_hours_completed': training_hours
}

df_hr = pd.DataFrame(hr_data)

print(f"✅ Generated {len(df_hr)} employee performance profiles.")

print("\n🔌 Connecting to PostgreSQL Server...")
# Using your password admin123
engine = create_engine('postgresql://postgres:admin123@localhost:5432/stationery_db')

print("📤 Loading dataset into SQL as 'hr_performance_table'...")
df_hr.to_sql('hr_performance_table', engine, if_exists='replace', index=False)

print("\n🎉 SUCCESS! Open pgAdmin. Your 'hr_performance_table' is live in SQL!")
