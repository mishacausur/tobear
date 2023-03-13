import pandas as pd
row_values = ['высокий', 1]
row_columns = ['alert_group', 'importance']
row = pd.Series(data=row_values, index=row_columns)

def alert_group_importance(row):
    messages = row['alert_group']
    if messages == 'средний':
        if row['importance'] == 1:
            return 'обратить внимание'
        return 'в порядке очереди'
    elif messages == 'высокий':
        if row['importance'] == 1:
            return 'высокий риск'
        return 'в порядке очереди'
    else:
        if row['importance'] == 1:
            return 'блокер'
        return 'в порядке очереди'

print(alert_group_importance(row))

