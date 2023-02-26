import pandas as pd

df = pd.read_csv('callers.csv')
df = df.rename(columns = { user id: user_id})
df.info()
