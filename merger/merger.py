import pandas as pd

data = pd.read_excel('seo_data.xlsx', sheet_name='traffic_data')
subcategory_dict = pd.read_excel('seo_data.xlsx', sheet_name='subcategory_ids')
category_dict = pd.read_excel('seo_data.xlsx', sheet_name='category_ids')
merged = data.merge(subcategory_dict, on='subcategory_id', how='left')
final = merged.merge(category_dict, on='category_id', how='left')
data_pivot = final.pivot_table(index=['category_name', 'subcategory_name'], columns='source', values='visits', aggfunc='sum')
data_pivot['ratio'] = data_pivot['organic'] / data_pivot['direct']
print(data_pivot.sort_values('ratio', ascending=False))
