"""
Puzzle 43: MultiIndex – Total Visits by Animal and Priority

Given the DataFrame `df` from puzzle 4:

Task:
Group the data by both 'animal' and 'priority' and compute the total number of 
visits for each (animal, priority) pair. Return the result as a Series with a 
MultiIndex.
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
# TODO: Get a MultiIndex Series of total visits per (animal, priority)

# Solution 1: Using groupby on two columns
visits_multi = df.groupby(['animal', 'priority'])['visits'].sum()
print(visits_multi)

# Solution 2: Using pivot_table + stack
# visits_multi = df.pivot_table(values='visits',
#                               index='animal',
#                               columns='priority',
#                               aggfunc='sum').stack()
# print(visits_multi)

# Solution 3: Using set_index + groupby(level=...)
# visits_multi = (df
#                 .set_index(['animal', 'priority'])['visits']
#                 .groupby(level=[0,1])
#                 .sum())
# print(visits_multi)

