"""
Puzzle 3: Data Aggregation

Given the following DataFrame:
- Department: ['Sales', 'Sales', 'IT', 'IT', 'HR', 'HR']
- Employee: ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank']
- Salary: [50000, 60000, 70000, 80000, 45000, 50000]

Tasks:
1. Calculate the average salary by department
2. Find the maximum salary in each department
3. Count the number of employees in each department
4. Calculate the total salary cost by department
"""

import pandas as pd

# Your solution here
# TODO: Create the DataFrame
df = pd.DataFrame({
    'Department': ['Sales', 'Sales', 'IT', 'IT', 'HR', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Salary': [50000, 60000, 70000, 80000, 45000, 50000]
})
# TODO: Calculate average salary by department
print(df.groupby('Department')['Salary'].mean())
# TODO: Find maximum salary by department
print(df.groupby('Department')['Salary'].max())
# TODO: Count employees by department
print(df.groupby('Department')['Employee'].count())
# TODO: Calculate total salary by department


