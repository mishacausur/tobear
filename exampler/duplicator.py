import pandas as pd

df = pd.DataFrame({
    'name': ['Сырок Мечта', 'Молоко Отличное', 'Сырок Мечта', 'Сырок Дружба',\
             'Сырок Дружба', 'Молоко Вкусное'],
    'count': [120, 200, 125, 100, 35, 500]
})

print(df.head())

print(df['name'].duplicated().sum()) # кол-во дубликатов
print(df['name'].value_counts()) # количество повторений значений в столбце 'name'

mechta = df[df['name'] == 'Сырок Мечта']['count'].sum() # Найдём общее количество сырков «Мечта» на складе
print(mechta)
druzhba = df[df['name'] == 'Сырок Дружба']['count'].sum()
print(druzhba)

df = df.drop_duplicates(subset=['name'], keep='first') # Теперь удалим строки с дубликатами в столбце name из исходной таблицы df
df = df.reset_index(drop=True)
# передаем верные значения количества товара
df.loc[0, 'count'] = mechta
df.loc[2, 'count'] = druzhba

print(df)

registers = pd.Series(['Нервы — ',
                       'БОЛЬШИЕ,',
                       'маленькие,',
                       'многие! —',
                       'скачут БеШеНыЕ,',
                       'и уже',
                       'у нервов ПОДКАшиваются ноги!'])
registers = registers.str.lower()
print(registers)
