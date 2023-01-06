'''
This file will be used to explore dictionaries in python

This is a sample summary of this file. Here we will explain what this file does
1. Explore things you can do with dictionaries
'''

# import libraries
import numpy as np, pandas as pd
import time

time_start = time.time()
# code starts here

# run random loops
x = 0.0
# for i in range(10000000):
for i in range(10):
    x += i
print("the sum of first million numbers is =", x)

# 2. our first dictionary
height = {}
list = []

height['prateek'] = 167
height['rohit'] = 180
print("the height of rohit is =", height['rohit'])

# 3. Another way to start dictionary
hometowns = {
    'rohit': 'kakinada',
    'prateek':'jodhpur'
}
print("the home town of prateek is ", hometowns['prateek'])

# 4. Let's create dictionary from two lists
names = ['rohit','prateek','tushti']
month_of_birth = ['jan','july','may']
# initialize an empty dictionary
MOBs = {}
for i in range(len(names)):
    MOBs[names[i]] = month_of_birth[i]
print("MOBs =", MOBs)

for name in MOBs:
    print(name, "'s birthday is in", MOBs[name], sep='')

# Merge two dictionaries

dict1 = {'Ten':10, 'Tewnty': 20, 'Thirty': 30}
dict2 = { 'Thirty': 30, 'Forty':40, 'Fifty': 50,}

# Add dict2 to dict1 using a for loop
for key in dict2:
    dict1[key] = dict2[key]
print("dict1 =",dict1)

dict3 = dict1 | dict2
print("dict3",dict3)

# create a dictionary of lists
classISBM = {}
classISBM['names'] = ['prateek', 'rohit','tushti', 'meenakshi']
classISBM['marks'] = [100,100,100,99]
classISBM['section'] = ['A', 'B','D', 'C']

# convert to dictionary of students
students = {}
# for name in classISBM['names']:
for i in range(len(classISBM['names'])):
    name = classISBM['names'][i]
    marks = classISBM['marks'][i]
    section = classISBM['section'][i]
    students[name] = {'marks':marks, 'section': section}

print("students['tushti']=", students['tushti'])
print("students['prateek']=", students['prateek'])

print("students['tushti']['marks']=", students['tushti']['marks'])
print("students['tushti']['section']=", students['tushti']['section'])




# code ends here
time_end = time.time()
print("time taken to run the file =", time_end-time_start)





