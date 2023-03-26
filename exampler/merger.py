import pandas as pd

first_pupil_df = pd.DataFrame({
    'author': ['Фонвизин', 'Грибоедов', 'Пушкин', 'Гоголь', 'Лермонтов'],
    'literary_work': ['Недоросль', 'Горе от ума', 'Капитанская дочка', 'Ревизор', 'Мцыри']
})
second_pupil_df = pd.DataFrame({
    'author': ['Пушкин', 'Гоголь','Лермонтов', 'Островский', 'Тургенев'],
    'literary_work': ['Евгений Онегин', 'Мёртвые души', 'Герой нашего времени', 'Гроза', 'Отцы и дети']
})

#print(first_pupil_df.merge(second_pupil_df, on='author')) # название столбца, по которому объединять, передают в параметре on
print()
#print(first_pupil_df.merge(second_pupil_df, on='author', how='outer'))
print()
#print(first_pupil_df.merge(second_pupil_df, on='author', how='left', suffixes=('_записал первый', '_записал второй')))


df1 = pd.DataFrame({'a': [1, 2, 3, 4], 'b': ['A', 'B', 'C', 'D']})
df2 = pd.DataFrame({'a': [2, 2, 2, 2], 'c': ['E', 'F', 'G', 'H']})
print(df1)
print()
print(df2)
print()
print (df1.join(df2, on='a', rsuffix='_y'))

