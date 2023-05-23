import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

data = pd.read_csv('flights_preprocessed.csv')

target = data['Arrival Delay']
features = data.drop(['Arrival Delay'] , axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

model = LinearRegression()
model.fit(features_train, target_train)
predictions_valid = model.predict(features_valid)

print(mean_absolute_error(target_valid, predictions_valid))

for depth in range(1, 16, 1):
    model = RandomForestRegressor(n_estimators=20, max_depth=depth, random_state=12345)
    model.fit(features_train, target_train)
    predictions_valid = model.predict(features_valid)
    print(mean_absolute_error(target_valid, predictions_valid))


#%%time
model = RandomForestRegressor(n_estimators=100, max_depth=12, random_state=12345)
model.fit(features_train, target_train)
predictions_train = model.predict(features_train)
predictions_valid = model.predict(features_valid)
print(mean_absolute_error(target_train, predictions_train))
print(mean_absolute_error(target_valid, predictions_valid))
