import pandas as pd

stock = pd.read_excel('stock.xlsx', sheet_name='storehouse')
print(stock['item'].value_counts())

xiaomi = stock[stock['item'] == 'Смартфон Xiaomi Redmi 6A 16GB']['count'].sum()
huawei = stock[stock['item'] == 'Смартфон HUAWEI P30 lite']['count'].sum()

stock = stock.drop_duplicates(subset=['item'], keep='first')
stock = stock.reset_index(drop=True)
stock.loc[0, 'count'] = xiaomi
stock.loc[3, 'count'] = huawei

stock['item_lowercase'] = stock['item'].str.lower()
apple = stock[stock['item_lowercase'] == 'смартфон apple iphone xr 64gb']['count'].sum()
samsung = stock[stock['item_lowercase'] == 'смартфон samsung galaxy a30 32gb']['count'].sum()

stock = stock.drop_duplicates(subset=['item_lowercase'], keep='first')
stock = stock.reset_index(drop=True)

stock.loc[3, 'count'] = apple
stock.loc[1, 'count'] = samsung

print(stock)

