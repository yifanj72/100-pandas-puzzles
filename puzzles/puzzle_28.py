"""
Puzzle 28: Summarize Visits by Category

Task:
Compute the total number of visits for each animal type.
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
# TODO: Compute the total number of visits for each animal type.

# Solution 1
print(df.groupby('animal')['visits'].sum())

# Solution 2
df.pivot_table(values='visits', index='animal', aggfunc='sum')

# Solution 3
df.groupby('animal').agg({'visits':'sum'})
