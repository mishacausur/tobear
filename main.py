import pandas as pd

hogwarts_points = pd.read_csv('hogwarts_points.csv')

print(hogwarts_points)
print()
print(hogwarts_points['points'].sum())
print(hogwarts_points.groupby('faculty_name')['points'].sum().sum())
print('Winner is', hogwarts_points.groupby('faculty_name')['points'].sum().idxmax())

hogwarts_points = hogwarts_points.fillna('Гриффиндор')
print('Winner is', hogwarts_points.groupby('faculty_name')['points'].sum().idxmax())
