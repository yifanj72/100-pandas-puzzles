"""
Puzzle 19: Replace Values with Boolean

Given the DataFrame `df` from puzzle 4:

Task:
The 'priority' column contains the values 'yes' and 'no'. 
Replace this column with a column of boolean values: 
'yes' should be `True` and 'no' should be `False`.
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
# TODO: Replace 'yes'/'no' with True/False
df['priority'] = df['priority'].map({"yes": True, "no": False})
print(df)

# Alternative solutions:
# Solution 2: Using replace() method
# df['priority'] = df['priority'].replace({'yes': True, 'no': False})

# Solution 3: Using apply() with lambda
# df['priority'] = df['priority'].apply(lambda x: True if x == 'yes' else False)

