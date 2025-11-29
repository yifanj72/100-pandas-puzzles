"""
Puzzle 18: Sort DataFrame by Multiple Columns

Given the DataFrame `df` from puzzle 4:

Task:
Sort `df` first by the values in the 'age' in descending order, 
then by the value in the 'visits' column in ascending order 
(so row `i` should be first, and row `d` should be last).
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
# TODO: Sort by age descending, then visits ascending
print(df.sort_values(by=['age', 'visits'], ascending=[False, True]))
