import pandas as pd
import numpy as np

# Load the dataset into a pandas dataframe
df = pd.read_csv('Datasets/online_shoppers_intention.csv')
#%%
# Check for missing values
print(df.isnull().sum())
#%%
# Check for duplicates
print(df.duplicated().sum())
#%%
# Remove duplicates
df = df.drop_duplicates()
#%%
# Impute missing values
df = df.fillna(df.mean())
#%%
import matplotlib.pyplot as plt
import seaborn as sns

# Visualize the distribution of the target variable
sns.countplot(x='Revenue', data=df)
plt.show()
#%%
# Visualize the correlation between the features
sns.heatmap(df.corr())
plt.show()
#%%
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# One-hot encode categorical features
categorical_features = ['Month', 'OperatingSystems', 'Browser', 'Region', 'TrafficType', 'VisitorType', 'Weekend']
encoder = OneHotEncoder(categories='auto', sparse=False, handle_unknown='ignore')
encoded_features = pd.DataFrame(encoder.fit_transform(df[categorical_features]))

# Standardize numerical features
numerical_features = ['Administrative', 'Administrative_Duration', 'Informational', 'Informational_Duration', 'ProductRelated', 'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues', 'SpecialDay']
scaler = StandardScaler()
scaled_features = pd.DataFrame(scaler.fit_transform(df[numerical_features]))

# Concatenate the encoded and scaled features
X = pd.concat([encoded_features, scaled_features], axis=1)

# Create the target variable
y = df['Revenue']

#%%
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#%%
# Create a logistic regression model
lr_model = LogisticRegression(random_state=42)
lr_model.fit(X_train, y_train)
lr_y_pred = lr_model.predict(X_test)
lr_accuracy = accuracy_score(y_test, lr_y_pred)
print('Logistic Regression Accuracy:', lr_accuracy)
#%%
# Create a decision tree model
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_y_pred = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_y_pred)
print('Decision Tree Accuracy:', dt_accuracy)
#%%
# Create a random forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
rf_y_pred = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_y_pred)
print('Random Forest Accuracy:', rf_accuracy)
#%%
# Create a support vector machine model
svm_model = SVC(random_state=42)
svm_model.fit(X_train, y_train)
svm_y_pred = svm_model.predict(X_test)
svm_accuracy = accuracy_score(y_test, svm_y_pred)
print('Support Vector Machine Accuracy:', svm_accuracy)
#%%
