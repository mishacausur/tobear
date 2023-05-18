import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('travel_insurance.csv')
# train, valid = train_test_split(data, test_size=.25, random_state=12345)
# features_train = train.drop('Claim', axis=1)
# target_train = train['Claim']
# features_valid = valid.drop('Claim', axis=1)
# target_valid = valid['Claim']
# print(features_train.shape)
# print(features_valid.shape)
print(data.dtypes)

data_ohe = pd.get_dummies(data, drop_first=True)
target = data_ohe['Claim']
features = data_ohe.drop('Claim', axis=1)

features_train, target_train, features_valid, target_valid = train_test_split(features, target, test_size=.25, random_state=12345)
model = LogisticRegression(random_state=12345, solver='liblinear')
model.fit(features_train, features_valid)

encoder = OrdinalEncoder()
encoder.fit(data)
data_ordinal = pd.DataFrame(encoder.transform(data), columns=data.columns)
print(data_ordinal.head())
target = data_ordinal['Claim']
features = data_ordinal.drop('Claim', axis=1)
features_train, features_valid, target_train, target_valid = train_test_split(features, target, test_size=0.25, random_state=12345)
tree_model = DecisionTreeClassifier(random_state=12345)
tree_model.fit(features_train, target_train)

