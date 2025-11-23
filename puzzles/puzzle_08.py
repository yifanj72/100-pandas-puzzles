"""
Puzzle 8: Select Specific Rows and Columns

Given the DataFrame `df` from puzzle 4:

Task:
Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].
Note: The row indices are labels, so rows [3, 4, 8] refer to labels 'd', 'e', 'i'.
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
# TODO: Select rows ['d', 'e', 'i'] and columns ['animal', 'age']
print(df.loc[['d', 'e', 'i'], ['animal', 'age']]) -- loc is used to select rows and columns by label
