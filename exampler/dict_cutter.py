import pandas as pd

our_list = [1, 2, 3]
df = pd.DataFrame({
    'a': [2, 3, 10, 11, 12],
    'b': [5, 4, 3, 2, 1],
    'c': ['X', 'Y', 'Y', 'Y', 'Z']
})

print(df.query('a in @our_list')) # строим срез, в котором значения столбца a равны элементам списка our_list

print()

our_dict = {0: 10, 1: 11, 2: 12}
uf = pd.DataFrame({
    'a': [0, 1, 10, 11, 12],
    'b': [5, 4, 3, 2, 1],
    'c': ['X', 'Y', 'Y', 'Y', 'Z']
})

print(uf.query('a in @our_dict')) # строим срез, в котором значения столбца a равны ключам словаря

print()

our_series=pd.Series([10,11,12])
sf = pd.DataFrame({
    'a': [0, 1, 10, 11, 12],
    'b': [5, 4, 3, 2, 1],
    'c': ['X', 'Y', 'Y', 'Y', 'Z']
})
print(sf.query('a in @our_series')) # строим срез, в котором значения столбца a равны значениям Series, но не их индексам

print()

our_series = pd.Series([10,11,12])
xf = pd.DataFrame({
    'a': [0, 1, 10, 11, 12],
    'b': [5, 4, 3, 2, 1],
    'c': ['X', 'Y', 'Y', 'Y', 'Z']
})
print(xf.query('a in @our_series.index')) # строим срез, в котором значения столбца a равны индексам Series, т. е. 0, 1 или 2

print()

ef = pd.DataFrame({
    'a': [0, 1, 10, 11, 12],
    'b': [5, 4, 3, 2, 1],
    'c': ['X', 'Y', 'Y', 'Y', 'Z']
})
our_df = pd.DataFrame ({
    'a1': [2, 4, 6],
    'b1': [3, 2, 2],
    'c1': ['A', 'B', 'C']
})
print(ef.query('a in @our_df.index')) # строим срез, в котором значения столбца a равны индексам датафрейма our_df, т. е. 0, 1 или 2

print()

wf = pd.DataFrame({
    'a': [0, 1, 10, 11, 12],
    'b': [5, 4, 3, 2, 1],
    'c': ['X', 'Y', 'Y', 'Y', 'Z']
})
our_wf = pd.DataFrame ({
    'a1': [2, 4, 6],
    'b1': [3, 2, 2],
    'c1': ['A', 'B', 'C']
})
print(wf.query('b in @our_df.b1')) # строим срез, в котором значения столбца b равны значениям столбца b1 датафрейма our_df
