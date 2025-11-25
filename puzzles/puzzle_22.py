"""
Puzzle 22: Fill NA Values Using Mean

Given the DataFrame `df`:

Task:
Fill missing values in the 'age' column using the column's mean.
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
# TODO: Change 'snake' to 'python' in the 'animal' column

# Solution 1
df['age'] = df['age'].fillna(df['age'].mean())
print(df)

# Solution 2
# df['age'].fillna(df['age'].mean(), inplace=True)

# Solution 3
df['age'] = df['age'].replace(np.nan, df['age'].mean())
