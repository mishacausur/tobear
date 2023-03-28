import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('visits.csv', sep='\t')
# делим количество заездов короче 60 секунд на общее число заездов


#data['too_fast'] = data['time_spent'] < 60

# THE SAME
#print(len(data.query('time_spent < 60')) / len(data))
#print(data['too_fast'].mean())

#too_fast_stat = data.pivot_table(values='too_fast', index='id')
#print(too_fast_stat.head())
#OR inversive
#print(too_fast_stat.sort_values('too_fast', ascending=False).head())

#too_fast_stat.hist(bins=30)
#plt.show()

#data['too_slow'] = data['time_spent'] > 1000
#too_slow_stat = data.pivot_table(values='too_slow', index='id')
#print(too_slow_stat.head())

#too_slow_stat.hist(bins=30)
#plt.show()


#data.query('id == "792b6ded"').describe()


#data['too_fast'] = data['time_spent'] < 60
#data['too_slow'] = data['time_spent'] > 1000
#too_fast_stat = data.pivot_table(index='id', values='too_fast')

#good_ids = too_fast_stat.query('too_fast < 0.5')
#good_data = data.query('id in @good_ids.index')
#good_data = good_data.query('(time_spent >= 60) and (time_spent) <= 1000')

#OR
# good_data = data.query('id in @good_ids.index and 60 <= time_spent <= 1000')


#good_stations_stat = good_data.groupby('id')['time_spent'].median()
#good_stations_stat.hist(bins=50)
#plt.show()
# THE SAME
#gdsttat = good_data.pivot_table(values='time_spent', index='id', aggfunc='median')
#gdsttat.hist(bins=50)
#plt.show()

#good_stat = good_data.pivot_table(index='name', values='time_spent', aggfunc='median')
#print(good_stat.sort_values('time_spent'))



#median_station_stat = data.pivot_table(
#    index='id', values='time_spent', aggfunc='median'
#)
#good_stations_stat = good_data.pivot_table(
#    index='id', values='time_spent', aggfunc='median'
#)

#ax = median_station_stat.plot(
 #   kind='hist',
 #   y='time_spent',
 #   histtype='step',
 #   range=(0, 500),
  #  bins=25,
  #  linewidth=5,
 #   alpha=0.7,
  #  label='raw',
#)
#good_stations_stat.plot(
#    kind='hist',
#    y='time_spent',
#    histtype='step',
#    range=(0, 500),
#    bins=25,
#    linewidth=5,
#    alpha=0.7,
#    label='filtered',
#    ax=ax,
#    grid=True,
#    legend=True,
#)
#plt.show()
#stat = data.pivot_table(index='name', values='time_spent')
#stat['good_time_spent'] = good_stat['time_spent']

#print(stat)

#id_name = good_data.pivot_table(index='id', values='name', aggfunc=['first', 'count'])

#print(id_name.head())

#station_stat_full = id_name.join(good_stations_stat, on='id')
#station_stat_full = id_name.join(good_stations_stat)
#print(station_stat_full.head())
#station_stat_full.columns = ['name', 'count']

#good_stat2 = (
#    station_stat_full
#    .query('count > 30')
#    .pivot_table(index='name', values='time_spent', aggfunc=['median', 'count'])
#)
#good_stat2.columns = ['median_time', 'stations', 'time_spent']

#final_stat = stat.join(good_stat2)

#print(final_stat)
#print(station_stat_full)
#station_stat_full.plot(kind='scatter', x='count', y='time_spent', grid=True, alpha=0.4)
#plt.show()

# фильтруем слишком быстрые и медленные заезды и АЗС
data['too_fast'] = data['time_spent'] < 60
data['too_slow'] = data['time_spent'] > 1000
too_fast_stat = data.pivot_table(index='id', values='too_fast')
good_ids = too_fast_stat.query('too_fast < 0.5')
good_data = data.query('id in @good_ids.index')
good_data = good_data.query('60 <= time_spent <= 1000')

# считаем данные по отдельным АЗС и по сетям
station_stat = data.pivot_table(index='id', values='time_spent', aggfunc='median')
good_stations_stat = good_data.pivot_table(index='id', values='time_spent', aggfunc='median')
stat = data.pivot_table(index='name', values='time_spent')
good_stat = good_data.pivot_table(index='name', values='time_spent', aggfunc='median')
stat['good_time_spent'] = good_stat['time_spent']

id_name = good_data.pivot_table(index='id', values='name', aggfunc=['first', 'count'])
id_name.columns = ['name', 'count']
station_stat_full = id_name.join(good_stations_stat)
#station_stat_full.plot(kind='scatter', x='count', y='time_spent', grid=True, alpha=0.4)
station_stat_full.plot(x='count', y='time_spent', kind='hexbin', gridsize=20, figsize=(8, 6), sharex=False, grid=True)
plt.show()
print(station_stat_full['count'].corr(station_stat_full['time_spent'])) # correlation

station_stat_multi = data.pivot_table(index='id', values=['time_spent', 'too_fast', 'too_slow'], aggfunc='mean')
#print(station_stat_multi.corr())
#pd.plotting.scatter_matrix(station_stat_multi, figsize=(9,9))

good_stat2 = (
    station_stat_full
    .query('count > 30')
    .pivot_table(index='name', values='time_spent', aggfunc=['median', 'count'])
)
good_stat2.columns = ['median_time', 'stations']
final_stat = stat.join(good_stat2)
final_stat = final_stat.dropna(subset=['median_time']) # remove NA values existin in median_time column
final_stat = final_stat.sort_values(by='median_time')
final_stat.plot(y='median_time', kind='bar', figsize=(10, 5), grid=True)

big_nets_stat = final_stat.query('stations > 10')

#groping station name (if it is big_nets_stat it stays the same, if not its gonna be changed)
station_stat_full['group_name'] = station_stat_full['name']\
    .where(
    station_stat_full['name']
        .isin(big_nets_stat.index),  # looking if it is big_nets_stat
    'Другие' #what it should be
)

# variable with only OTHER group stations
stat_grouped = (
    station_stat_full
    .query('count > 30')
    .pivot_table(index='group_name', values='time_spent', aggfunc=['median', 'count'])
)
stat_grouped.columns = ['time_spent', 'count']
stat_grouped = stat_grouped.sort_values(by='time_spent')
stat_grouped.plot(y='count', kind='pie', figsize=(8,8))

good_data['group_name'] = (
    good_data['name']
    .where(good_data['name'].isin(big_nets_stat.index), 'Другие')
)

for name, group_data in good_data.groupby('group_name'):
    group_data.hist(column='time_spent', bins=50)

# OR W/ TITLES

for name, group_data in good_data.groupby('group_name'):
    group_data.plot(y='time_spent', title= name, kind='hist', bins=50)
