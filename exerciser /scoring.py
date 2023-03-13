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
    if ('жилья' in purpose) or ('жильем' in purpose) or ('недвижимости' in purpose) or ('недвижимость' in purpose) or ('недвижимостью' in purpose) or ('жилье' in purpose) or ('жилью' in purpose):
        return 'операции с недвижимостью'
    if ('автомобиля' in purpose) or ('автомобили' in purpose) or ('автомобилем' in purpose) or ('автомобиль' in purpose):
        return 'операции с автомобилем'
    if ('образование' in purpose) or ('образованием' in purpose) or ('образования' in purpose) or ('образованием' in purpose):
        return 'получение образования'
    else:
        return 'проведение свадьбы'

data['purpose_category'] = data['purpose'].apply(categorize_purpose)

print(data.head(20))






