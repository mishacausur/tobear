import pandas as pd
from sklearn.tree import DecisionTreeClassifier

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
