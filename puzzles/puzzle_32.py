"""
Puzzle 32: Compute Mean Age by Animal and Priority

Given the DataFrame `df` from puzzle 4:

Task:
Create a pivot table showing the mean 'age' for each combination of 'animal' and 'priority'.
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
# TODO: Build pivot table of mean age by animal (rows) and priority (columns).

# Solution 1: using pivot_table
pivot = df.pivot_table(values='age', index='animal', columns='priority', aggfunc='mean')
print(pivot)

# Alternative:
# Solution 2: using groupby + unstack
res = df.groupby(['animal', 'priority'])['age'].mean().unstack()
print(res)


