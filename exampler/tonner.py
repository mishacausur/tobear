import pandas as pd


our_dict = {0: 10, 1: 11, 2: 'X'}
df = pd.DataFrame({
    'a': [2, 3, 10, 11, 12],
    'b': [5, 4, 3, 2, 1],
    'c': ['X', 'Y', 'Y', 'Y', 'Z']
})
#print(df.query('a in @our_dict'))

our_series = pd.Series([2, 11, 12])
df = pd.DataFrame({
    'a': [2, 3, 10, 11, 12],
    'b': [5, 4, 3, 2, 1],
    'c': ['X', 'Y', 'Y', 'Y', 'Z']
})

print(df.query('a in @our_series.index'))

df1 = pd.DataFrame({
    'name': ['Mike', 'Sam', 'Bill'],
    'age': [23, 25, 29],
    'height': [176, 192, 182]
})

df2 = pd.DataFrame({
    'name': ['Mike', 'John', 'Bill'],
    'salary': [100, 120, 150]
})


print(df1.merge(df2, on='name', how='outer'))

df1 = pd.DataFrame({
    'name': ['Mike', 'Sam', 'Bill'],
    'age': [23, 25, 29],
    'height': [176, 192, 182]
})

df2 = pd.DataFrame({
    'name': ['Mike', 'John', 'Bill'],
    'salary': [100, 120, 150],
    'tax': [0, 13, 0]
})

print(df1.merge(df2, on='name', how='right'))

df1 = pd.DataFrame({
    'name': ['Mike', 'Sam', 'Bill'],
    'age': [23, 25, 29],
    'height': [176, 192, 182]
})

df2 = pd.DataFrame({
    'name': ['Mike', 'John', 'Bill'],
    'salary': [100, 120, 150],
    'tax': [0, 13, 0]
})

print(df1.merge(df2, on='name', how='right'))

df1 = pd.DataFrame({
    'name': ['Mike', 'Sam', 'Bill'],
    'age': [23, 25, 29],
    'height': [176, 192, 182]
})

df2 = pd.DataFrame({
    'name': ['Mike', 'John', 'Bill'],
    'salary': [100, 120, 150],
    'tax': [0, 13, 0]
})

print(df1.merge(df2, on='name'))
