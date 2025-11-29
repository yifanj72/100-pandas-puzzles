"""
Puzzle 33: Reorder Columns

Given the DataFrame `df` from puzzle 4:

Task:
Reorder the columns to the following order:
['priority', 'animal', 'age', 'visits'].
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
# TODO: Reorder the columns.

# Solution 1
df = df[['priority', 'animal', 'age', 'visits']]
print(df)

# Alternative:
# Solution 2
new_order = ['priority', 'animal', 'age', 'visits']
df = df.reindex(columns=new_order)
print(df)


