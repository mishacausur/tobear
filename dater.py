import pandas as pd #'%d.%m.%YZ%H:%M:%S'

position = pd.read_csv('position.csv')
position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S')
#print(position.sort_values('level', ascending=False))
position['month'] = pd.DatetimeIndex(position['timestamp']).month
print(position.groupby('month')['level'].mean())
