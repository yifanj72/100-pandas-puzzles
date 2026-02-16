"""
Puzzle 45: Sort Animals by Custom Order

Given the DataFrame `df` from puzzle 4:

Task:
Sort the rows by 'animal' in the following custom order:
['snake', 'dog', 'cat']

Keep the original index labels.
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
# TODO: Sort df by animal in the custom order: snake -> dog -> cat

# Solution 1: Using CategoricalDtype
order = ['snake', 'dog', 'cat']
# Because sort_values sorts strings alphabetically, without specifying a custom order.
df['animal'] = pd.Categorical(df['animal'], categories=order, ordered=True)
df_sorted = df.sort_values('animal')
print(df_sorted)

# Solution 2: Using map to temporary numeric key
order_map = {'snake': 0, 'dog': 1, 'cat': 2}
df_sorted = df.assign(animal_order=df['animal'].map(order_map)).sort_values('animal_order').drop(columns='animal_order')
print(df_sorted)

# Solution 3: Using reindex on groupby order (more manual)
groups = [df[df['animal'] == a] for a in order]
df_sorted = pd.concat(groups)
print(df_sorted)
