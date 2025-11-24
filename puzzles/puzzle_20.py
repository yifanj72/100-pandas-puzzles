"""
Puzzle 20: Replace Values in Column

Given the DataFrame `df` from puzzle 4:

Task:
In the 'animal' column, change the 'snake' entries to 'python'.
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

# Solution 1: Using replace() method (most common)
df['animal'] = df['animal'].replace('snake', 'python')
print(df)

# Alternative solutions:
# Solution 2: Using loc with boolean indexing
# df.loc[df['animal'] == 'snake', 'animal'] = 'python'

# Solution 3: Using map() method
# df['animal'] = df['animal'].map({'snake': 'python'}).fillna(df['animal'])

# Solution 4: Using apply() with lambda
# df['animal'] = df['animal'].apply(lambda x: 'python' if x == 'snake' else x)

