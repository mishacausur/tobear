import pandas as pd

data = pd.read_csv('data.csv')

income_types_mean = data.groupby('income_type')['total_income'].transform('median')
data['total_income'] = data['total_income'].fillna(income_types_mean)
data['days_employed'] = data['days_employed'].abs()
employed_days_mean = data.groupby('income_type')['days_employed'].transform('median')
data = data.drop(data[(data['children'] == 20) | (data['children'] == -1)].index)
data['days_employed'] = data['days_employed'].fillna(employed_days_mean)
data['total_income'] = data['total_income'].astype(int)
data['education'] = data['education'].str.lower()
print(data.duplicated().sum())

