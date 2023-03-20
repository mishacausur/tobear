import pandas as pd

data = pd.read_csv('visits.csv', sep='\t')
stat = data.pivot_table(index='name', values='time_spent', aggfunc='mean')
print(stat)
total_visits = data['time_spent'].count()
print(f'Количество заездов: {total_visits}')

# nhl_att['avg_home_att'] = nhl_att['home_att'] / nhl_att['home_games']
# nhl_pivot = nhl_att.pivot_table(index='season', values='avg_home_att')
