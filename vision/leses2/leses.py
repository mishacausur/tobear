import pandas as pd

df = pd.DataFrame(
    {
        'From': [
            'Moscow',
            'Moscow',
            'St. Petersburg',
            'St. Petersburg',
            'St. Petersburg',
        ],
        'To': ['Rome', 'Rome', 'Rome', 'Barcelona', 'Barcelona'],
        'Is_Direct': [False, True, False, False, True],
        'Has_luggage': [True, False, False, True, False],
        'Price': [21032, 19250, 19301, 20168, 31425],
        'Date_From': [
            '01.07.19',
            '01.07.19',
            '04.07.2019',
            '03.07.2019',
            '05.07.2019',
        ],
        'Date_To': [
            '07.07.19',
            '07.07.19',
            '10.07.2019',
            '09.07.2019',
            '11.07.2019',
        ],
        'Airline': ['Belavia', 'S7', 'Finnair', 'Swiss', 'Rossiya'],
        'Travel_time_from': [995, 230, 605, 365, 255],
        'Travel_time_to': [350, 225, 720, 355, 250],
    }
)

filter_list = [True, True, False, False, False]

print(df[filter_list]) #the same with lower

print(df[df['From'] == 'Moscow']) # only from msc

print(df[df['Price'] < 21000]) # price lower then 21000

print(df[df['Travel_time_to'] > df['Travel_time_from']]) # time to is bigger then from

print(df[1.5 * df['Travel_time_to'] < df['Travel_time_from']]) # time to is lower in 1.5 times then tome from

print(df[1.5 * df['Travel_time_to'] < df['Travel_time_from']]) # time to is bigger in 1.5 times then tome from

print(df[df['Date_From'].isin(['04.07.2019', '05.07.2019'])]) # if the value is in

print(df[1.5 * df['Price'] < df['Price'].max()]) # cheeper then the most expen in 1.5 times

print(df[(df['Travel_time_from'] >= 365) | (df['Travel_time_to'] < 250)]) # time from is bigger or equal 365 OR time to is lower then 250

print(df[~(df['Is_Direct']) & ~(df['Date_To'].isin(['09.07.2019', '10.07.2019', '11.07.2019']))]) #indirect and 07.07

# QUERY
print(df.query('To == "Barcelona"'))
print(df.query('Is_Direct == True or Has_luggage == True'))
print(df.query('Has_luggage == False and (Airline != "S7" or Airline != "Rossiya")'))
print(df.query('Has_luggage == False and Airline not in ["S7", "Rossiya"]'))

max_time = 300
print(df.query('Airline in ["Belavia", "S7", "Rossiya"] and Travel_time_from < @max_time'))
