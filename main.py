import pandas as pd

df = pd.read_csv('logs.csv')
print(len(df['email'].unique()))
print(df['source'].unique())
