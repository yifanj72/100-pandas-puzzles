"""
Puzzle 21: Drop Rows with Any NaN

Given the DataFrame `df` from puzzle 4:

Task:
Remove all rows that contain at least one missing value.
"""

import pandas as pd
import numpy as np

# Setup DataFrame
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(data, index=labels)

# Your solution here
# TODO: Remove all rows that contain at least one missing value.

# Solution 1 (recommended)
df_clean = df.dropna()
print(df_clean)

# Solution 2
# df_clean = df[df.notna().all(axis=1)]

# Solution 3
# df_clean = df.dropna(how='any')
