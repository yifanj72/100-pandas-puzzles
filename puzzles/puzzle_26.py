"""
Puzzle 26: Create New Column Condition

Task:
Add a new column 'is_old' = True if age > 3 else False.
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
# TODO: Add a new column 'is_old' = True if age > 3 else False.

# Solution 1
df['is_old'] = df['age'] > 3
print(df)

# Solution 2
df['is_old'] = df['age'].apply(lambda x: x > 3)

# Solution 3
df['is_old'] = np.where(df['age'] > 3, True, False)

