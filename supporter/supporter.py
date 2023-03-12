import pandas as pd

support = pd.read_csv('support.csv')
support = support.rename(columns={'Тип обращения': 'type_message', 'Время обращения': 'timestamp'})
print(support.head(10))
