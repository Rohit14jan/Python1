from builtins import int

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

# take user inputs and print in order
name = input("what is your name?")
print("Hi %s ,welcome to our game!" % name)

hasError = True

while (hasError):
    try:
        numGames = input("How many games do you want to play?")
        numGames = int(numGames)
        if (numGames > 1 and numGames < 100):
            hasError = False
        else:
            print("you have made an error, please retry")
    except:
        print("you have made an error, please retry")
        hasError = True

print("Thanks %s ,we will play %d games!" % (name, numGames))
ListOfChoices = ["Rock", "Paper", "Scissors"]

np.random.seed(7)


def playGame(ListOfChoices):
    computerChoiceNumber = np.random.randint(0, 3)
    computerChoice = ListOfChoices[computerChoiceNumber]


    hasError = True

    while (hasError):
        try:
            yourChoice = input("what is your choice? Please choose between 'Rock', 'Paper','Scissors':")
            if (yourChoice in ListOfChoices):
                hasError = False
            else:
                print("you have made an error, please retry")
        except:
            print("you have made an error, please retry")
            hasError = True
    print("humanChoice=", yourChoice)
    print("computerChoice=", computerChoice)

    if(yourChoice=="Rock" and computerChoice == "Rock") or (yourChoice=="Paper" and computerChoice == "Paper") or (yourChoice=="Scissors" and computerChoice == "Scissors"):
        return 0
    if(yourChoice=="Rock" and computerChoice == "Scissors") or (yourChoice=="Paper" and computerChoice == "Rock") or (yourChoice=="Scissors" and computerChoice == "Paper"):
        return 1
    if(yourChoice=="Rock" and computerChoice == "Paper") or (yourChoice=="Paper" and computerChoice == "Scissors") or (yourChoice=="Scissors" and computerChoice == "Rock"):
        return -1

numGamesWon = 0
for gamenumber in range(numGames):
    numGamesWon = numGamesWon+playGame(ListOfChoices)

if (numGamesWon>0):
    print("you are lucky, you won !")
elif (numGamesWon<0):
    print("So sorry, you lost")
else:
    print("the game is draw")
