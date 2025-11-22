"""
Puzzle 2: Data Filtering

Given the following DataFrame:
- Name: ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
- Age: [25, 30, 35, 28, 32]
- Salary: [50000, 60000, 70000, 55000, 65000]

Tasks:
1. Filter rows where Age is greater than 28
2. Filter rows where Salary is between 55000 and 65000 (inclusive)
3. Filter rows where Name starts with 'C'
"""

import pandas as pd

# Your solution here
# TODO: Create the DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'Salary': [50000, 60000, 70000, 55000, 65000]
})
# TODO: Filter by Age > 28
print(df[df['Age'] > 28])
# TODO: Filter by Salary between 55000 and 65000
print(df[(df['Salary'] >= 55000) & (df['Salary'] <= 65000)])
# TODO: Filter by Name starting with 'C'
print(df[df['Name'].str.startswith('C')])
print(df[df['Name'].str[0] == 'C'])
print(df[df['Name'].str.contains('^C', regex=True)])
print(df.loc[df['Name'].apply(lambda x: x.startswith('C'))])
