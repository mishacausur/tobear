import pandas as pd
import matplotlib.pyplot as plt

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

#data['time_spent'].hist(bins=100, range = (0, 1500))
#data.boxplot()
#plt.ylim(-100, 1000)
#plt.show()

#print(data.describe())
#print(data.sort_values('time_spent', ascending=False).head(10))

sample = data.query('id == "3c1e4c52"') # only this gas
#print(len(sample)) # count of rows about sample

#data.hist('time_spent', bins=100, range=(0, 1500))
#plt.show()

#sample.hist('time_spent',bins=100, range=(0, 1500))
#plt.show()

#data['date_time'] = pd.to_datetime(data['date_time'], format='%Y-%m-%d %H:%M')
#print(data.head())

data['date_time'] = pd.to_datetime(data['date_time'], format='%Y-%m-%dT%H:%M:%S')
data['local_time'] = data['date_time'] + pd.Timedelta(hours=3)
#(data
#    .query('id == "3c1e4c52"')
 #   .plot(x='local_time', y='time_spent',
 #         ylim=(0, 1000), style='o', grid=True, figsize=(12, 6))
#)

data['date_hour'] = data['local_time'].dt.round('1H')
(
    data.query('id == "3c1e4c52"')
    .pivot_table(index='date_hour', values='time_spent', aggfunc='median')
    .plot(grid=True, figsize=(12, 5))
)

(
    data.query('id == "3c1e4c52" and time_spent < 1000')
    .pivot_table(index='date_hour', values='time_spent')
    .plot(grid=True, figsize=(12, 5))
)

(
    data
        .query('id=="3c1e4c52"')
        .pivot_table(index='date_hour', values='time_spent', aggfunc='count')
        .plot(grid=True, figsize=(12, 5))
)
plt.show()
