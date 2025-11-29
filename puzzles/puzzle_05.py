"""
Puzzle 5: Display DataFrame Summary Information

Given the DataFrame `df` from puzzle 4:

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

Task:
Display a summary of the basic information about this DataFrame and its data.
Hint: There is a single method that can be called on the DataFrame.
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
# TODO: Display summary information
print(df.info())
print(df.describe())
print(df.head())
print(df.tail())
print(df.sample(5))
print(df.count())
print(df.mean())
print(df.median())
print(df.mode())
print(df.std())
print(df.var())
print(df.min())
print(df.max())
print(df.sum()) #  sum of each column
print(df.prod()) # product of each column
print(df.cumsum()) # cumulative sum of each column
print(df.cumprod()) # cumulative product of each column
print(df.cummax()) # cumulative maximum of each column
print(df.cummin()) # cumulative minimum of each column
print(df.corr()) # correlation matrix
print(df.cov()) # covariance matrix
print(df.skew()) # skewness of each column
print(df.kurt()) # kurtosis of each column
print(df.isnull()) # check if there are any missing values
print(df.notnull()) # check if there are no missing values
print(df.fillna(0)) # fill missing values with 0
print(df.dropna()) # drop rows with missing values
print(df.dropna(axis=1)) # drop columns with missing values
print(df.dropna(how='all')) # drop rows where all values are missing
