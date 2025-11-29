"""
Puzzle 38: Multi-Level GroupBy Statistics

Given the DataFrame `df` from puzzle 4:

Task:
Group the data by both 'animal' and 'priority', and compute:
- the mean of 'age'
- the total of 'visits'

Return a DataFrame with MultiIndex (animal, priority).
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
# TODO: Group by ['animal', 'priority'] and compute mean age and total visits

# Solution 1: Using groupby with agg dict
result = df.groupby(['animal', 'priority']).agg(
    mean_age=('age', 'mean'),
    total_visits=('visits', 'sum')
)
print(result)

# Solution 2: Using groupby + agg with list and rename columns
grouped = df.groupby(['animal', 'priority']).agg({'age': 'mean', 'visits': 'sum'})
grouped.columns = ['mean_age', 'total_visits']
print(grouped)

# Solution 3: Using pivot_table
result = pd.pivot_table(df, values=['age', 'visits'],
                        index=['animal', 'priority'],
                        aggfunc={'age': 'mean', 'visits': 'sum'})
print(result)
