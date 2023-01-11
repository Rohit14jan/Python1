import pandas as pd, numpy as np

#%%
# import dataset
games = pd.read_csv('datasets/vgsales.csv')

# view the top 5 rows
games.head()
#%%
# find the type of columns
games.dtypes

#%%
# describe genres
games.Genre.describe()
#%%
games.Genre.value_counts()
#%%
games.head()
#%%
games.Year.value_counts()
#%%
games.Platform.value_counts()
#%%
games.Publisher.value_counts()
#%%
type(games.Year.value_counts())

#%%
games.Genre.value_counts().head
#%%
games.Genre.value_counts().head(3)
#%%
games.Genre.unique()
#%%
games.Genre.nunique()
#%%
# generate a simple pivot table
pd.crosstab(games.Genre,games.Year)
#%%
pd.crosstab(games.Publisher,games.Year)
#%%
# Description of sales
games.Global_Sales.describe()
#%%
# get the mean
games.Global_Sales.mean
#%%
games.Global_Sales.mean()
#%%
games.Global_Sales.sd()
#%%
games.Global_Sales.std()
#%%
games.Year.plot(kind= 'hist')
#%%
games.Genre.value_counts().plot(kind="hist")
#%%
