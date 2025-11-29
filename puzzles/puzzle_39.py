"""
Puzzle 39: Reshape with Pivot Table

Given the DataFrame `df` from puzzle 4:

Task:
Create a pivot table with:
- index = 'animal'
- columns = 'priority'
- values = total 'visits'

Missing combinations should be filled with 0.
"""

import pandas as pd
import numpy as np

# Setup DataFrame
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)

# Your solution here
# TODO: Build pivot table (animal x priority) with sum of visits, fill missing with 0

# Solution 1: Using pivot_table
# table = pd.pivot_table(df,
#                        values='visits',
#                        index='animal',
#                        columns='priority',
#                        aggfunc='sum',
#                        fill_value=0)
# print(table)

# Solution 2: Using groupby + unstack
table = df.groupby(['animal', 'priority'])['visits'].sum().unstack(fill_value=0)
print(table)

# Solution 3: Using crosstab
# table = pd.crosstab(df['animal'], df['priority'], values=df['visits'], aggfunc='sum').fillna(0)
# print(table)
