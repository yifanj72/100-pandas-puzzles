"""
Puzzle 44: Stack and Unstack – Reshape Animal/Priority Table

Given the DataFrame `df` from puzzle 4:

Task:
1. Create a pivot table of total visits by animal (rows) and priority (columns).
2. Convert this pivot table to a stacked Series (MultiIndex) using stack().
3. Then unstack it back to the original pivot table using unstack().
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
# TODO: 1) pivot -> 2) stack -> 3) unstack back

# Solution 1
pivot = df.pivot_table(values='visits', index='animal', columns='priority', aggfunc='sum')
print("Pivot table:\n", pivot)
# Pivot table:
#  priority   no  yes
# animal            
# cat       3.0  5.0
# dog       5.0  3.0
# snake     3.0  NaN

stacked = pivot.stack()
print("\nStacked Series:\n", stacked)
# Stacked Series:
#  animal  priority
# cat     no          3.0
#         yes         5.0
# dog     no          5.0
#         yes         3.0
# snake   no          3.0

unstacked = stacked.unstack()
print("\nUnstacked back to pivot:\n", unstacked)
# Unstacked back to pivot:
#  priority   no  yes
# animal            
# cat       3.0  5.0
# dog       5.0  3.0
# snake     3.0  NaN

# Alternative: using groupby + unstack/stack directly
# pivot = df.groupby(['animal', 'priority'])['visits'].sum().unstack()
# stacked = pivot.stack()
# unstacked = stacked.unstack()
