import pandas as pd

data = pd.read_csv('visits.csv', sep='\t')
stat = data.pivot_table(index='name', values='time_spent', aggfunc='mean')
#print(stat)
total_visits = data['time_spent'].count()
#print(f'Количество заездов: {total_visits}')
total_stations = len(data['id'].unique())
#print(f'Количество АЗС: {total_stations}')
# nhl_att['avg_home_att'] = nhl_att['home_att'] / nhl_att['home_games']
# nhl_pivot = nhl_att.pivot_table(index='season', values='avg_home_att')
total_days = 7
station_visits_per_day = total_visits / total_stations / total_days
print(f'Количество заездов на АЗС в сутки: {station_visits_per_day}')
name = data['name'].value_counts()
print(name.head(10))

data['time_spent'].hist(bins=100)
