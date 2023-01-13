import numpy as np, pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import seaborn as sns
#%%
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
diabetes = pd.read_csv('Datasets/pima-indians-diabetes.csv', header=None, names=col_names)
#%%
diabetes.head()
#%%
x_cols = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
y_col = ['label']
#%%
xVals = diabetes[x_cols]
#%%
xVals.head()
#%%
yVal = diabetes[y_col]
#%%
yVal.head()
#%%
randomSeed=7
xVals_train, xVals_test, yVal_train, yVal_test = train_test_split(xVals,yVal,test_size=0.25, random_state=randomSeed)
#%%
# initialize thge LR model
lr = LogisticRegression(random_state=randomSeed)
#%%
lr.fit(xVals_train,yVal_train)
#%%
yPred = lr.predict(xVals_test)
#%%
# create a confusion matrix
from sklearn.metrics import confusion_matrix, classification_report
conf_matrix= confusion_matrix(yVal_test, yPred)
#%%
print("conf_matrix=",conf_matrix)
#%%
import matplotlib.pyplot as plt

class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(conf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
#%%
clf = classification_report(yVal_test,yPred,target_names=['without diabetes','with diabetes'])
print("Classification report=",clf)
#%%
# ROC Curve
yPreds_variations= lr.predict_proba(xVals_test)
from sklearn.metrics import roc_curve

#%%
yPreds_variations = yPreds_variations[::,1]
fpr,tpr,other= roc_curve(yVal_test,yPreds_variations)
#%%
from sklearn.metrics import roc_auc_score
auc = roc_auc_score(yVal_test,yPreds_variations)
#%%
plt.plot(fpr,tpr,label="auc"+str(auc))
plt.legend(loc= 4)
plt.show()

#%%
