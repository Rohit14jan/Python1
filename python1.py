# This is our first lesson in Python

# 1. Variable Declaration: Number
someNumber = 1
print(someNumber)

print('someNumber = ', someNumber)

# 2. Variable Declaration: String
print('-' * 50)
name = 'Rahul'
print("My name is: ", name)
print('-' * 50)

# 3. Simple For Loop: Type all numbers from 1 to 10
print('-' * 50)
for num in range(10):
    print(num + 1)

print('-' * 50)

# 4. Simple If:
# Print only even integers from 1 to 10
print('-' * 50)
for num in range(10):
    remainderWhenDividingBy2 = num % 2
    # Debugging Code
    # print("num=", num)
    # print("remainderWhenDividingBy2=", remainderWhenDividingBy2)
    # Now we will use the if condition on the remainder.
    # If the remainder is 1 then we will print num+1, for even numbers
    if(remainderWhenDividingBy2==1):
        print(num+1)

print('-' * 50)

# 5. If using a function!
# Print only even integers from 1 to 10
# We learn here about if, else, for loops and functions:
def isEven(num):
    remainderWhenDividingBy2 = num%2
    if remainderWhenDividingBy2==1:
        return False
    else:
        return True


print('-' * 50)
for num in range(10):
    if isEven(num+1):
        print(num+1)

print('-' * 50)