import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('travel_insurance.csv')
train, valid = train_test_split(data, test_size=.25, random_state=12345)
features_train = train.drop('Claim', axis=1)
target_train = train['Claim']
features_valid = valid.drop('Claim', axis=1)
target_valid = valid['Claim']
print(features_train.shape)
print(features_valid.shape)


