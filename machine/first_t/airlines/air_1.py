import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

data = pd.read_csv('flights.csv')
data_ohe = pd.get_dummies(data, drop_first=True)

target = data_ohe['Arrival Delay']
features = data_ohe.drop(['Arrival Delay'] , axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

numeric = ['Day', 'Day Of Week', 'Origin Airport Delay Rate',
       'Destination Airport Delay Rate', 'Scheduled Time', 'Distance',
       'Scheduled Departure Hour', 'Scheduled Departure Minute']

scaler = StandardScaler()
scaler.fit(features_train[numeric])
features_train[numeric] = scaler.transform(features_train[numeric])
features_valid[numeric] = scaler.transform(features_valid[numeric])
print(features_train.shape)
print(features_valid.shape)

model = LinearRegression()
model.fit(features_train, target_train)
predicted_valid = model.predict(features_valid)
mse = mean_squared_error(target_valid, predicted_valid)
print("MSE =", mse)
print("RMSE =", mse ** 0.5)

predicted_valid = pd.Series(target_train.mean(), index=target_valid.index)
mse = mean_squared_error(target_valid, predicted_valid)

print("Mean")
print("MSE =", mse)
print("RMSE =", mse ** 0.5)

print("R2 =", r2_score(target_valid, predicted_valid))
