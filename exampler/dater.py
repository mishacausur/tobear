import pandas as pd

df = pd.DataFrame({'time': ['2011-03-01 17:34']})
df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M')
df['time_rounded'] = df['time'].dt.round('1H') # округляем до ближайшего значения с шагом в один час
print(df['time_rounded']) # 2011-03-01 18:00:00
print()

pf = pd.DataFrame({'time': ['2011-03-01 17:15']})
pf['time'] = pd.to_datetime(pf['time'], format='%Y-%m-%d %H:%M')
pf['time_rounded'] = pf['time'].dt.round('1H') # округляем до ближайшего значения с шагом в один час
print(pf['time_rounded']) # 2011-03-01 17:00:00
print()

sf = pd.DataFrame({'time': ['2011-03-01 17:15']})
sf['time'] = pd.to_datetime(sf['time'], format='%Y-%m-%d %H:%M')
sf['ceil'] = sf['time'].dt.ceil('1H') # округляем к потолку
sf['floor'] = sf['time'].dt.floor('1H') # округляем к полу
print('Время, округлённое вверх', sf['ceil']) # 2011-03-01 18:00:00
print('Время, округлённое вниз', sf['floor']) # 2011-03-01 17:00:00
print()

nf = pd.DataFrame({'time': ['2011-03-07 17:15', '2011-04-02 17:15']}) # пн и сб
nf['time'] = pd.to_datetime(nf['time'], format='%Y-%m-%d %H:%M')
nf['weekday'] = nf['time'].dt.weekday
print(nf['weekday']) # 1    5
print()

gf = pd.DataFrame({'time': ['11-03-07 17:15', '11-05-02 10:20']})
gf['moscow_time'] = pd.to_datetime(gf['time'], format='%y-%m-%d %H:%M')
gf['petropavlovsk-kamchatsky_time'] = gf['moscow_time'] + pd.Timedelta(hours=9)
print(gf['petropavlovsk-kamchatsky_time']) # 2011-03-08 02:15:00 2011-05-02 19:20:00
print()
