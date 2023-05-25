import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder

random_state=12345

data = pd.read_csv('Churn.csv')
data.head()

data.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1, inplace=True)
data.dropna(inplace=True)

encodings = ['Geography', 'Gender']
rest = ['Exited', 'CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
encoder = OneHotEncoder(sparse=False)
data_encoded = encoder.fit_transform(data[encodings])
data_encoded_columns = encoder.get_feature_names(encodings)
data_encoded_df = pd.DataFrame(data_encoded, columns=data_encoded_columns)
data_ohe = pd.concat([data_encoded_df, data[rest]], axis=1)
data_ohe.dropna(inplace=True)

data_ohe.head()

target = data_ohe['Exited']
features = data_ohe.drop('Exited', axis=1)
target.value_counts()

features_train_valid, features_test, target_train_valid, target_test = train_test_split(features, target, test_size=0.2, random_state=random_state, stratify=target)
features_train, features_valid, target_train, target_valid = train_test_split(features_train_valid,  target_train_valid, test_size=0.25, random_state=random_state, stratify=target_train_valid)

print("Тренировочная выборка:", features_train.shape[0])
print("Валидационная выборка:", features_valid.shape[0])
print("Тестовая выборка:", features_test.shape[0])

numeric = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']
scaler = StandardScaler()
scaler.fit(features_train[numeric])
features_train[numeric] = scaler.transform(features_train[numeric])
features_valid[numeric] = scaler.transform(features_valid[numeric])
pd.options.mode.chained_assignment = None

model = LogisticRegression()
model.fit(features_train, target_train)
predicted_valid = model.predict(features_valid)

print("Accuracy:", accuracy_score(target_valid, predicted_valid))
print("Precision:", precision_score(target_valid, predicted_valid))
print("Recall:", recall_score(target_valid, predicted_valid))
print("F1:", f1_score(target_valid, predicted_valid))

for depth in range(1, 16, 1):
    model = RandomForestClassifier(n_estimators=20, max_depth=depth, random_state=random_state)
    model.fit(features_train, target_train)
    predictions_valid = model.predict(features_valid)
    print(depth, 'F1: ', f1_score(target_valid, predictions_valid))
    probabilities_valid = model.predict_proba(features_valid)
    probabilities_one_valid = probabilities_valid[:, 1]
    print('  ROC-AUC', roc_auc_score(target_valid, probabilities_one_valid))

balanced_model = LogisticRegression(class_weight='balanced')
balanced_model.fit(features_train, target_train)
balanced_predicted = balanced_model.predict(features_valid)
