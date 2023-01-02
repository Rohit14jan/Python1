import numpy as np

listofNumbers = list(range(10))
print("listofNumbers=", listofNumbers)

# create list with alt nos
listofNumbers = list(range(1, 10, 2))
print("listofNumbers=", listofNumbers)

# list in reverse
listofNumbers = list(range(10, 1, -2))
print("listofNumbers=", listofNumbers)

# Print if multiple of 3
listofNumbers = list(range(1, 100, 1))
for num in listofNumbers:
    if num % 3 == 0:
        print(num)

listofNumbers = list(range(1, 100, 1))
listOfMultiplesOf3 = []
for num in listofNumbers:
    if num % 3 == 0:
        listOfMultiplesOf3.append(num)

print("listOfMultiplesOf3=", listOfMultiplesOf3)

listOfMultiplesOf3 = list(range(3, 100, 3))
listOfMultiplesOf5 = list(range(5, 100, 5))
print("listOfMultiplesOf3=", listOfMultiplesOf3, "listOfMultiplesOf5=", listOfMultiplesOf5)

listOfMultiplesOf3and5 = []
for num in listOfMultiplesOf3:
    listOfMultiplesOf3and5.append(num)
print("listOfMultiplesOf3and5 =", listOfMultiplesOf3and5)

listOfMultiplesOf3or5 = listOfMultiplesOf3 + listOfMultiplesOf5
print("listOfMultiplesOf3or5 =", listOfMultiplesOf3 + listOfMultiplesOf5)

sortedListOfMultiplesOf3or5 = sorted(listOfMultiplesOf3or5)
print("sortedListOfMultiplesOf3or5=", sortedListOfMultiplesOf3or5)

# remove duplicates
deduplicatedList = []
for numIndex in range(1, len(sortedListOfMultiplesOf3or5), 1):
    num = sortedListOfMultiplesOf3or5[numIndex - 1]
    next_num = sortedListOfMultiplesOf3or5[numIndex]
    if num != next_num:
        deduplicatedList.append(num)

print("deduplicatedList =", deduplicatedList)

listOfWords = ["rahul", "rohit", "tushti", "prateek"]
print("karan" in listOfWords)
print("rohit" in listOfWords)
