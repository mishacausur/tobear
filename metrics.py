import pandas as pd

metrica = pd.read_csv('metrica_data.csv')
age_avg = metrica['age'].mean()
metrica['age'] = metrica['age'].fillna(value=age_avg)
time_avg = metrica['time'].mean()
#print(time_avg)
desktop_data = metrica.loc[metrica['device_type'] == 'desktop']
#print(desktop_data.head())
desktop_data_time_avg = desktop_data['time'].mean()
print(desktop_data_time_avg)
mobile_data = metrica.loc[metrica['device_type'] == 'mobile']
#print(mobile_data.head())
mobile_data_time_avg = mobile_data['time'].mean()
print(mobile_data_time_avg)


for device in metrica['device_type'].unique():
    metrica.loc[(metrica['device_type'] == device) & (metrica['time'].isna()), 'time'] = metrica.loc[(metrica['device_type'] == device), 'time'].mean()

print(metrica.head(50))


people_df = pd.DataFrame({
    "name": ["Mikhail", None, "Boris"],
    "age": [23, 25, 29],
    "city": ['Moscow', 'Chelyabinsk', 'Moscow']
})

print(people_df["name"].count() )
