import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.dummy import DummyClassifier
from sklearn.tree import plot_tree

df = pd.read_csv('users_behavior.csv')

counts = df['is_ultra'].value_counts()
plt.bar([0, 1], counts.values)
plt.xticks([0, 1], ['0', '1'])
plt.xlabel('is_ultra')
plt.ylabel('Количество примеров')
plt.title('Распределение значений в столбце "is_ultra"')
plt.show()

features = df.drop(['is_ultra'], axis=1)
target = df['is_ultra']

features_train_valid, features_test, target_train_valid, target_test = train_test_split(features, target, test_size=0.2, random_state=12345, stratify=target)
features_train, features_valid, target_train, target_valid = train_test_split(features_train_valid,  target_train_valid, test_size=0.25, random_state=12345, stratify=target_train_valid)

print("Тренировочная выборка:", features_train.shape[0])
print("Валидационная выборка:", features_valid.shape[0])
print("Тестовая выборка:", features_test.shape[0])

best_tree_model = None
tree_best_result = 0
train_scores = []
valid_scores = []

for depth in tqdm(range(1, 11)):
    tree_model = DecisionTreeClassifier(random_state=12345, max_depth=depth)
    tree_model.fit(features_train, target_train)
    train_predictions = tree_model.predict(features_train)
    valid_predictions = tree_model.predict(features_valid)

    train_accuracy = accuracy_score(target_train, train_predictions)
    valid_accuracy = accuracy_score(target_valid, valid_predictions)

    train_scores.append(train_accuracy)
    valid_scores.append(valid_accuracy)

    if valid_accuracy > tree_best_result:
        best_tree_model = tree_model
        tree_best_result = valid_accuracy

print("Accuracy лучшей модели:", tree_best_result)

depths = range(1, 11)
plt.plot(depths, train_scores, label='Train Accuracy')
plt.plot(depths, valid_scores, label='Validation Accuracy')
plt.xlabel('max_depth')
plt.ylabel('Accuracy')
plt.title('Accuracy vs max_depth')
plt.legend()
plt.show()

tree_model = DecisionTreeClassifier(random_state=12345, max_depth=3)
tree_model.fit(features_train, target_train)

plt.figure(figsize=(12, 8))
plot_tree(tree_model, feature_names=features_train.columns, filled=True)
plt.show()

best_est = 0
best_forest_model = None
best_forest_result = 0
for est in range(1, 11):
    forest_model = RandomForestClassifier(random_state=12345, n_estimators=est)
    forest_model.fit(features_train, target_train)
    result = forest_model.score(features_valid, target_valid)
    if result > best_forest_result:
        best_forest_model = forest_model
        best_forest_result = result
        best_est = est

print(f"Accuracy наилучшей модели на валидационной выборке: {best_forest_result}")
print(f'Параметр: {best_est}')

log_reg_model = LogisticRegression(random_state=12345, solver='lbfgs', max_iter=1000)
log_reg_model.fit(features_train, target_train)
predictions_valid = log_reg_model.predict(features_valid)
log_reg_result = log_reg_model.score(features_valid, target_valid)
print(log_reg_result)

test_model_score = best_forest_model.score(features_test, target_test)
print(f'Accuracy модели на тестовой выборке: {test_model_score}')

dummy_model = DummyClassifier(strategy='uniform')
dummy_model.fit(features_train, target_train)

dummy_accuracy = dummy_model.score(features_valid, target_valid)
print(f"Оценка пустой модели: {dummy_accuracy}")

tree_accuracy = best_tree_model.score(features_valid, target_valid)
if tree_accuracy > dummy_accuracy:
    print("Дерево решений лучше. чем пустая модель.")
else:
    print("Пустая модель лучше, чем дерево решений.")

forest_accuracy = best_forest_model.score(features_valid, target_valid)
if forest_accuracy > dummy_accuracy:
    print("Лес деревьев лучше, чем пустая модель.")
else:
    print("Пустая модель лучше, чем лес деревьев.")

logreg_accuracy = log_reg_model.score(features_valid, target_valid)
if logreg_accuracy > dummy_accuracy:
    print("Логистическая регрессия лучше, чем пустая модель.")
else:
    print("Пустая модель лучше, чем логистическая регрессия.")
