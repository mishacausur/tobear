import pandas as pd

logs = pd.read_csv('logs.csv')
logs['email'] = logs['email'].fillna(value='')

rows = (logs['source'] == 'None') & (logs['email'] == '')
print(logs.loc[rows])
#logs.loc[logs['source'] == 'None', 'source'] = logs.loc[logs['source'] == 'None', 'source'].replace('None', 'email')
logs.loc[logs['source'] == 'None', 'source'] = 'email'
print(logs['source'].value_counts())
logs.loc[logs['source'] == 'undef', 'source'] = 'other'
logs_grouped = logs.groupby('source').agg({'purchase': ['count', 'sum']})
logs_grouped['conversion'] = logs_grouped['purchase']['sum'] / logs_grouped['purchase']['count']
print(logs_grouped)
