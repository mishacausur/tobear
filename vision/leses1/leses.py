import pandas as pd

data = pd.read_csv('visits.csv', sep='\t')
print(data.head())
