import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv('flights_preprocessed.csv')

target = data['Arrival Delay']
features = data.drop(['Arrival Delay'] , axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

model = LinearRegression()
model.fit(features_train, target_train)
print(model.score(features_valid, target_valid))

for depth in range(1, 16, 1):
    model = RandomForestRegressor(n_estimators=20, max_depth=depth, random_state=12345)
    model.fit(features_train, target_train)
    print(model.score(features_valid, target_valid))

model = RandomForestRegressor(n_estimators=60,
    max_depth=10, random_state=12345)
model.fit(features_train, target_train)
print(model.score(features_train, target_train))
print(model.score(features_valid, target_valid))

model = RandomForestRegressor(n_estimators=100, random_state=12345)
model.fit(features_train, target_train)
