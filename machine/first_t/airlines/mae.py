import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def mae(target, predictions):
    return 1/len(target) * sum(abs(target - predictions))

target = pd.Series([-0.5, 2.1, 1.5, 0.3])
predictions = pd.Series([-0.6, 1.7, 1.6, 0.2])

print(mae(target, predictions))

data = pd.read_csv('flights_preprocessed.csv')

target = data['Arrival Delay']
features = data.drop(['Arrival Delay'] , axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

model = LinearRegression()
model.fit(features_train, target_train)
predicted_valid = model.predict(features_valid)

print(mean_absolute_error(target_valid, predicted_valid))
