import pandas as pd

transactions = pd.read_excel('ids.xlsx')
transactions['id'] = pd.to_numeric(transactions['id'], errors='coerce')
transactions['amount'] = pd.to_numeric(transactions['amount'], errors='coerce')
print(transactions['amount'].sum())

transactions_per_category = transactions.groupby('category')['amount'].sum()
print(transactions_per_category)
