import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

data = pd.read_csv('heart.csv')
features = data.drop(['target'], axis=1)
target = data['target']

scores = []

# зададим размер блока, если их всего три
sample_size = int(len(data) / 3)

for i in range(0, len(data), sample_size):
    valid_indexes = list(range(i, min(i + sample_size, len(data))))
    train_indexes = list(set(range(len(data))) - set(valid_indexes))

    features_train = features.iloc[train_indexes]
    target_train = target.iloc[train_indexes]
    features_valid = features.iloc[valid_indexes]
    target_valid = target.iloc[valid_indexes]

    model = DecisionTreeClassifier(random_state=0)
    model = model.fit(features_train, target_train)
    predictions = model.predict(features_valid)
    score = accuracy_score(target_valid, predictions)

    scores.append(score)

final_score = sum(scores) / len(scores)
print('Средняя оценка качества модели:', final_score)


#OR
scores = cross_val_score(model, features, target, cv=5)
# < посчитайте оценки, вызвав функцию cross_value_score с пятью блоками >
final_score = scores.mean()
print('Средняя оценка качества модели:', final_score)
