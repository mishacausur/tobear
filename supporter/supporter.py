import pandas as pd

support = pd.read_csv('support.csv')
support = support.rename(columns={'Тип обращения': 'type_message', 'Время обращения': 'timestamp'})
support_log = support.loc[:,['user_id', 'type_id', 'timestamp']]

support_dict = support[['type_message','type_id']]
support_dict = support_dict.drop_duplicates().reset_index(drop=True)

support_log_grouped = support_log.groupby('type_id').count()

def alert_group(messages):
    if messages <= 300:
        return 'средний'
    elif messages <= 500:
        return 'высокий'
    else:
        return 'критичный'

support_log_grouped['alert_group'] = support_log_grouped['user_id'].apply(alert_group)

#print(support_log_grouped.groupby('alert_group').sum())

support_log_grouped = pd.read_csv('support_log_grouped.csv')
#print(support_log_grouped)

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

support_log_grouped['importance_status'] = support_log_grouped.apply(alert_group_importance, axis=1)
print(support_log_grouped['importance_status'].value_counts())
