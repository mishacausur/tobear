import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
print(data.isna().count())
income_types_mean = data.groupby('income_type')['total_income'].transform('median')
data['total_income'] = data['total_income'].fillna(income_types_mean)
# the same but longer
#for t in data['income_type'].unique():
#    data.loc[(data['income_type'] == t) & (data['total_income'].isna()), 'total_income'] = \
#    data.loc[(data['income_type'] == t), 'total_income'].median()

data['days_employed'] = data['days_employed'].abs()
employed_days_mean = data.groupby('income_type')['days_employed'].transform('median')
data = data.drop(data[(data['children'] == 20) | (data['children'] == -1)].index)
#data = data[(data['children'] != -1) & (data['children'] != 20)]
data['days_employed'] = data['days_employed'].fillna(employed_days_mean)
data['total_income'] = data['total_income'].astype(int)
data['education'] = data['education'].str.lower()
data = data.drop_duplicates()

def categorize_income(income):
    if income <= 30000:
        return 'E'
    elif income <= 50000:
        return 'D'
    elif income <= 200000:
        return 'C'
    elif income <= 1000000:
        return 'B'
    else:
        return 'A'

data['total_income_category'] = data['total_income'].apply(categorize_income)

def categorize_purpose(purpose):
    try:
        if 'автом' in purpose:
            return 'операции с автомобилем'
        elif 'жил' in purpose or 'недвиж' in purpose:
            return 'операции с недвижимостью'
        elif 'свад' in purpose:
            return 'проведение свадьбы'
        elif 'образов' in purpose:
            return 'получение образования'
    except:
        return 'нет категории'

data['purpose_category'] = data['purpose'].apply(categorize_purpose)

data.groupby('children')['debt'].mean().plot(kind='bar')

data['incomes_group'] = pd.qcut(data['total_income'], 6)

data['total_debt'] = data[data['debt'] == 1].count()

print(data[data['children'] > 4 ]['debt'].count())
print(data.groupby('children')['debt'].mean())
