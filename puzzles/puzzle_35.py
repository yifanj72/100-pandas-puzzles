"""
Puzzle 35: Filter Rows by Multiple Conditions

Given the DataFrame `df` from puzzle 4:

Task:
Select all rows where:
- animal is 'cat'
- age is not missing
- visits is greater than or equal to 2
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
# TODO: Apply all three conditions.

# Solution 1
mask = (
    (df['animal'] == 'cat') &
    (df['age'].notna()) &
    (df['visits'] >= 2)
)
result = df[mask]
print(result)

# Alternative:
# Solution 2: using query()
# result = df.query("animal == 'cat' and age == age and visits >= 2")
# print(result)

# In Python, particularly within libraries like Pandas and NumPy, the term "mask function" or "masking" refers to a technique for selectively manipulating or extracting data based on a given condition. It acts like a filter, allowing you to identify and target specific elements within a dataset.
# Here's a breakdown of how it works, primarily focusing on Pandas, where mask() is a dedicated method:
# 1. Boolean Condition:
# The core of masking is a boolean condition, which evaluates to True or False for each element in your data structure (e.g., a Pandas Series or DataFrame, or a NumPy array).
# 2. The mask() Method (in Pandas): 
# The mask() method in Pandas is an application of the "if-then" idiom.
# It takes a cond argument (the boolean condition) and an optional other argument.
# If cond is True for an element, that element is replaced: with the corresponding value from other (or NaN if other is not provided).
# If cond is False for an element, the original value is kept.
