import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Datasets/online_shoppers_intention.csv')

print(data.head()) # View the first few rows of the dataset
print(data.describe()) # Get summary statistics for the dataset
print(data.info()) # Get information about the variables and their data types
#%%
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Handle missing values
data = data.dropna()

# Encode categorical variables
label_encoder = LabelEncoder()
data['Month'] = label_encoder.fit_transform(data['Month'])
data['VisitorType'] = label_encoder.fit_transform(data['VisitorType'])
data['Weekend'] = label_encoder.fit_transform(data['Weekend'])

# Scale numerical variables
scaler = StandardScaler()
data['Administrative_Duration'] = scaler.fit_transform(data[['Administrative_Duration']])
data['Informational_Duration'] = scaler.fit_transform(data[['Informational_Duration']])
data['ProductRelated_Duration'] = scaler.fit_transform(data[['ProductRelated_Duration']])

#%%
from sklearn.model_selection import train_test_split

X = data.drop(['Revenue'], axis=1)
y = data['Revenue']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#%%
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# Train a decision tree classifier
dtc = DecisionTreeClassifier(random_state=42)
dtc.fit(X_train, y_train)
dtc_pred = dtc.predict(X_test)
print("Decision Tree Classifier Accuracy: ", accuracy_score(y_test, dtc_pred))

# Train a random forest classifier
rfc = RandomForestClassifier(random_state=42)
rfc.fit(X_train, y_train)
rfc_pred = rfc.predict(X_test)
print("Random Forest Classifier Accuracy: ", accuracy_score(y_test, rfc_pred))


# Train a logistic regression classifier
lr = LogisticRegression(random_state=42)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
print("Logistic Regression Classifier Accuracy: ", accuracy_score(y_test, lr_pred))

#%%
