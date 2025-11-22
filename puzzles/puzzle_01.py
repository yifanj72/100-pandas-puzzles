"""
Puzzle 1: Basic DataFrame Creation

Create a pandas DataFrame with the following data:
- Name: ['Alice', 'Bob', 'Charlie', 'Diana']
- Age: [25, 30, 35, 28]
- City: ['New York', 'London', 'Tokyo', 'Paris']

Then:
1. Display the DataFrame
2. Get basic information about the DataFrame
3. Select only the 'Name' and 'Age' columns
"""

import pandas as pd

# Your solution here
# TODO: Create the DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Tokyo', 'Paris']
})
# TODO: Display the DataFrame
print(df)
# TODO: Get basic information
print(df.info())
# TODO: Select Name and Age columns
print(df[['Name', 'Age']])
