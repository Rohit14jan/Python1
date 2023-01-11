import pandas as pd

obj = pd.Series([1,"Rohit",3,"Prateek"])
obj2= pd.Series([1,"Rohit",3,"Prateek"],index=['a','b','c','d'])
print("obj2=",obj2)

marks = {'rohit':100,'tushti':101,'prateek':102,'meenakshi':103}
marksDF = pd.Series(marks)
print("marksDF=",marksDF)
marksDF['rohit'] = marksDF['rohit'] - 1
print("marksDF=",marksDF)

marksDF[marksDF<=100] = 102
print("marksDF=",marksDF)

marksDF = marksDF/10
print("marksDF=",marksDF)

marksDF = marksDF**2
print("marksDF=",marksDF)

marksDF['newstudent'] = 82
print("marksDF=",marksDF)

marksDF = marksDF.drop('newstudent')
print("marksDF=",marksDF)