import pandas as pd

data = pd.read_csv('heart_labeled.csv')

target = []
for i in range(data.shape[0]):
    labels = data.loc[i, ['label_1', 'label_2', 'label_3']]
    true_label = labels.mode().values[0]
    target.append(true_label.astype('int'))
data['target'] = target

print(data.head())
