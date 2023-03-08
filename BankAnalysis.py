import numpy as np, pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import seaborn as sns

#%%
# Load the data
data = pd.read_csv('Datasets/bank.csv')
# Split the data into training and testing sets
train = data.sample(frac=0.7, random_state=1)
test = data.drop(train.index)#%%

#%%
# Define the features and target variable
X_train = train[['age', 'job', 'marital', 'education', 'default', 'balance', 'housing', 'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays', 'previous', 'poutcome']]
y_train = train['y']
X_test = test[['age', 'job', 'marital', 'education', 'default', 'balance', 'housing', 'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays', 'previous', 'poutcome']]
y_test = test['y']

#%%
