import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('visits.csv', sep='\t')
# делим количество заездов короче 60 секунд на общее число заездов


data['too_fast'] = data['time_spent'] < 60

# THE SAME
#print(len(data.query('time_spent < 60')) / len(data))
#print(data['too_fast'].mean())

too_fast_stat = data.pivot_table(values='too_fast', index='id')
print(too_fast_stat.head())
#OR inversive
print(too_fast_stat.sort_values('too_fast', ascending=False).head())

#too_fast_stat.hist(bins=30)
#plt.show()

data['too_slow'] = data['time_spent'] > 1000
too_slow_stat = data.pivot_table(values='too_slow', index='id')
print(too_slow_stat.head())

#too_slow_stat.hist(bins=30)
#plt.show()


#data.query('id == "792b6ded"').describe()


data['too_fast'] = data['time_spent'] < 60
data['too_slow'] = data['time_spent'] > 1000
too_fast_stat = data.pivot_table(index='id', values='too_fast')

good_ids = too_fast_stat.query('too_fast < 0.5')
good_data = data.query('id in @good_ids.index')
good_data = good_data.query('(time_spent >= 60) and (time_spent) <= 1000')

#OR
# good_data = data.query('id in @good_ids.index and 60 <= time_spent <= 1000')


good_stations_stat = good_data.groupby('id')['time_spent'].median()
good_stations_stat.hist(bins=50)
plt.show()
# THE SAME
gdsttat = good_data.pivot_table(values='time_spent', index='id', aggfunc='median')
gdsttat.hist(bins=50)
#plt.show()

good_stat = good_data.pivot_table(index='name', values='time_spent', aggfunc='median')
print(good_stat.sort_values('time_spent'))
