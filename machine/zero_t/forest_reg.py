import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv('train_data.csv')

features = df.drop(['last_price'], axis=1)
target = df['last_price'] / 1_000_000

features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=.25, random_state=12345)

best_model = None
best_result = 10000
best_est = 0
best_depth = 0
for est in range(10, 51, 10):
    for depth in range(1, 11):
        model = RandomForestRegressor(
            random_state=12345,
            n_estimators=est,
            max_depth=depth
        )
        model.fit(features_train, target_train)
        predictions_valid = model.predict(features_valid)
        result = (mean_squared_error(target_valid, predictions_valid)) ** .5
        if result < best_result:
            best_model = model
            best_result = result
            best_est = est
            best_depth = depth

print(f'RMSE наилучшей модели на валидационной выборке:, {best_result}, Количество деревьев:, {best_est}, Максимальная глубина: {depth}')
