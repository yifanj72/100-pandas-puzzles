"""
Puzzle 34: Find Rows with Maximum Visits per Animal

Given the DataFrame `df` from puzzle 4:

Task:
For each type of 'animal', find the row(s) where 'visits' is maximal for that animal.
Return the subset of df containing just those rows.
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
# TODO: Select rows with max visits for each animal.

# Solution 1: using groupby + transform
max_visits = df.groupby('animal')['visits'].transform('max')
result = df[df['visits'] == max_visits]
print(result)

# Alternative:
# Solution 2: using idxmax per group
# idx = df.groupby('animal')['visits'].idxmax()
# result = df.loc[idx]
# print(result)

