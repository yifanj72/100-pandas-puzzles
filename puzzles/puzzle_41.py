"""
Puzzle 41: Pivot Table – Average Age per Animal/Priority

Given the DataFrame `df` from puzzle 4:

Task:
Create a pivot table that shows the **average age** for each combination of 
'animal' (rows) and 'priority' (columns).
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
# TODO: Build a pivot table of mean age by animal (index) and priority (columns)

# Solution 1: Using pivot_table
pt = df.pivot_table(values='age', index='animal', columns='priority', aggfunc='mean')
print(pt)
# values, index, columns, aggfunc (vica)

# Solution 2: Using groupby + unstack
# pt = df.groupby(['animal', 'priority'])['age'].mean().unstack()

# Solution 3: Using pivot + groupby when duplicates exist
# pt = (df
#       .groupby(['animal','priority'])['age']
#       .mean()
#       .reset_index()
#       .pivot(index='animal', columns='priority', values='age'))
