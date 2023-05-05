import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv('train_data.csv')

features = df.drop(['last_price'], axis=1)
target = df['last_price'] / 1_000_000

features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=.25, random_state=12345)

model = LinearRegression()
model.fit(features_train, target_train)
predictions_valid = model.predict(features_valid)

result = (mean_squared_error(target_valid, predictions_valid)) ** .5
print(f'RMSE модели линейной регрессии на валидационной выборке:, {result}')
