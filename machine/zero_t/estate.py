import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('train_data.csv')

df['price_class'] = df['last_price'].apply(lambda x: 1.0 if x > 5650000 else 0.0)

features = df.loc[:, ['total_area', 'rooms', 'ceiling_height', 'floors_total',
       'living_area', 'floor', 'is_apartment', 'studio', 'open_plan',
       'kitchen_area', 'balcony', 'airports_nearest', 'cityCenters_nearest']]
#OR
# features = df.drop(['last_price', 'price_class'], axis=1)
target = df['price_class']

model = DecisionTreeClassifier()
model.fit(features, target)

new_features = pd.DataFrame(
    [[None, None, 2.8, 25, None, 25, 0, 0, 0, None, 0, 30706.0, 7877.0],
     [None, None, 2.75, 25, None, 25, 0, 0, 0, None, 0, 36421.0, 9176.0]],
    columns=features.columns)

new_features.loc[0, ['total_area', 'rooms', 'living_area', 'kitchen_area']] = [900.0, 12, 409.7, 112]
new_features.loc[1, ['total_area', 'rooms', 'living_area', 'kitchen_area']] = [109, 2, 32, 40.5]
answers = model.predict(new_features)
print(answers)

test_df = pd.read_csv('/datasets/test_data.csv').head(3)

test_df.loc[test_df['last_price'] > 5650000, 'price_class'] = 1
test_df.loc[test_df['last_price'] <= 5650000, 'price_class'] = 0
test_features = test_df.drop(['last_price', 'price_class'], axis=1)
test_target = test_df['price_class']
test_predictions = model.predict(test_features)
print(f'Предсказания: {test_predictions}')
print('Правильные ответы:', test_target.values.flatten())

def error_count(answers, predictions):
    counter = 0
    for index in answers.index:
    #for i in range(len(answers)):
        if answers[index] != predictions[index]:
            counter += 1
    return counter

def accuracy(answers, predictions):
    total = len(answers) - error_count(answers, predictions)
    return total / len(answers)

print("Ошибок:", error_count(test_target, test_predictions))
print("Accuracy:", accuracy(test_target, test_predictions))

print("Accuracy")
print("Обучающая выборка:", accuracy_score(target, answers))
print("Тестовая выборка:", accuracy_score(test_target, test_predictions))

best_model = None
best_result = 0
for depth in range(1, 6):
	model = DecisionTreeClassifier(random_state=12345, max_depth=depth)
	model.fit(features, target)
	predictions = model.predict(features)
	result = accuracy_score(target, predictions)
    print(f'max_depth = {depth} : {result}')
	if result > best_result:
		best_model = model
		best_result = result

print("Accuracy лучшей модели:", best_result)

df_train, df_valid = train_test_split(df, test_size=.25, random_state=12345)

features_train = df_train.drop(['last_price', 'price_class'], axis=1)
target_train = df_train['price_class']
features_valid = df_valid.drop(['last_price', 'price_class'], axis=1)
target_valid = df_valid['price_class']

print(features_train.shape)
print(target_train.shape)
print(features_valid.shape)
print(target_valid.shape)

#FOREST
for est in range(1, 11):
    model = RandomForestClassifier(random_state=12345, n_estimators=est)
    model.fit(features_train, target_train)
    result = model.score(features_valid, target_valid)
    if result > best_result:
        best_model = model
        best_result = result

print("Accuracy наилучшей модели на валидационной выборке:", best_result)
