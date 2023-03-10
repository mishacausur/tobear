import pandas as pd

data = pd.read_excel('seo_data.xlsx', sheet_name='traffic_data')
#print(data['source'].unique())
#print(data.head())
subcategory_dict = pd.read_excel('seo_data.xlsx', sheet_name='subcategory_ids')
#print(subcategory_dict.head())
category_dict = pd.read_excel('seo_data.xlsx', sheet_name='category_ids')
#print(category_dict.head())
#data['visits'] = pd.to_numeric(data['visits'])
#print(data.loc[964])
#print(data.groupby('source')['visits'].sum())

string_count = data.loc[data['subcategory_id'] == 'total'].shape[0]
data = data[data['subcategory_id'] != 'total']
#print(f'Количество строк: {data.shape[0]}')
#print(data.loc[data['subcategory_id'] == 'total'])
data['visits'] = data['visits'].astype('int')
result = data.groupby('source')['visits'].sum()
print(result)
