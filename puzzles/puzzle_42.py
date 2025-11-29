"""
Puzzle 42: Add a Column – Age Category

Given the DataFrame `df` from puzzle 4:

Task:
Add a new column 'age_group' with:
- 'young'  if age < 3
- 'adult'  if 3 <= age <= 6
- 'senior' if age > 6

For rows where 'age' is NaN, set 'age_group' to 'unknown'.
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
# TODO: Create the 'age_group' column based on age buckets

# Solution 1: Using apply with a custom function
def categorize_age(x):
    if np.isnan(x):
        return 'unknown'
    elif x < 3:
        return 'young'
    elif x <= 6:
        return 'adult'
    else:
        return 'senior'

df['age_group'] = df['age'].apply(categorize_age)
print(df)

# Solution 2: Using np.select
# conds = [
#     df['age'].isna(),
#     df['age'] < 3,
#     (df['age'] >= 3) & (df['age'] <= 6),
#     df['age'] > 6
# ]
# choices = ['unknown', 'young', 'adult', 'senior']
# df['age_group'] = np.select(conds, choices)
# print(df)

# Solution 3: Using pd.cut for non-NaN ages
# bins = [0, 3, 6, np.inf]
# labels_age = ['young', 'adult', 'senior']
# df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels_age)
# df['age_group'] = df['age_group'].astype(str).fillna('unknown')
