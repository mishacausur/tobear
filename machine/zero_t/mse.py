import pandas as pd
from sklearn.metrics import mean_squared_error

answers = [623, 253, 150, 237]
predictions = [649, 253, 370, 148]

result = mean_squared_error(answers, predictions)
print(result)

df = pd.read_csv('train_data.csv')

features = df.drop(['last_price'], axis=1)
target = df['last_price'] / 1_000_000

predictions = pd.Series(target.mean(), index=target.index)
mse = mean_squared_error(target, predictions)
print("MSE:", mse)
rmse = mse ** 0.5
print("RMSE:", rmse)
