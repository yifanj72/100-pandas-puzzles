"""
Puzzle 36: Filter by Multiple Conditions

Given the DataFrame `df` from puzzle 4:

Task:
Select all rows where:
- animal is 'cat'
- age is greater than 2
- visits is at least 2
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
# TODO: Filter rows where animal == 'cat', age > 2, and visits >= 2

# Solution 1: Using boolean indexing
result = df[(df['animal'] == 'cat') & (df['age'] > 2) & (df['visits'] >= 2)]
print(result)

# Solution 2: Using query()
result = df.query("animal == 'cat' and age > 2 and visits >= 2")

# Solution 3: Using np.logical_* functions
mask = (df['animal'].eq('cat') &
        df['age'].gt(2) &
        df['visits'].ge(2))
result = df[mask]

