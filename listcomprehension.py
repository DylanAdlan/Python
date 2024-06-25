# LIST COMPREHENSION => because we have for loop 
fruits = ["apple", "orange", "mango", "banana", "grapes"]
prices = [1.60, 1.2, 2.2, 4.8, 6.2]

# for loop with some statement
for fruit in fruits:
    print(fruit)

print("="* 40)

overseafruits = []

for fruit in fruits:
    overseafruits.append(fruit)

# using list comprehension
overseafruits = [ fruit for fruit in fruits]
# without expression we append fruit into overseafruits

print(overseafruits)

print("="* 40)

prices = [1.60, 1.2, 2.2, 4.8, 6.2]
priceswithsst = []

for price in prices:
    pricewithsst = price + (price * 0.06)
    priceswithsst.append(pricewithsst)
print(priceswithsst)

# using list comprehension
priceswithsst = [price + (price * 0.06) for price in prices]
print(priceswithsst)

# task which we need to do is find pricewithsst
# we need price 
# now using the above information, creat a function

def calculateSST(price):
    pricewithsst = price + (price * 0.06)
    return pricewithsst

#this map function takes 2 parameter
# 1st parameter is function 
# 2nd parameter is the list
prices = [1.60, 1.2, 2.2, 4.8, 6.2]
priceswithaat = map(calculateSST, prices)

# what map does?
#def map(func, values):
#   result = []
#    for value in values:
#        result.append(func(value))
#    return result





print("="* 40)


farenheitvalues= [32, 33, 34, 35, 36, 37, 38, 39, 40]
celciusvalues = []

for farenheit in farenheitvalues:
    celciusvalue = (farenheit - 32) * 5/9
    celciusvalues.append(celciusvalue)

# # using list comprehension
celciusvalues = [ (farenheit - 32) * 5/9 for farenheit in farenheitvalues]
print(celciusvalues)

def farenheitvalueToCelcius(farenheit):
    return (farenheit -32)* 5/9
celciusvalues = map(farenheitvalueToCelcius, farenheitvalues)
print(list(celciusvalues))


# all the three above example are trying to create a new list
# the number of items in both list are same
# INstead of writing the traditonal for loops
# we can use something called list comprehension or map class


print("="* 40)


# convert to list
numbers = list(range(1, 50))

multipleofthree = [] # to get the multiple of three
for number in range(1, 50): # list of 50 items
    if (number % 3 == 0):
        multipleofthree.append(number)

# using list comprehension
#newlist = [expression for number in numbers condition]

multipleofthree = [number for number in range(1, 50) if number % 3 == 0 ]
print(multipleofthree)

# using filter class # akan return value if True
def findMultipleOfThree(number):
    return True if (number % 3 == 0) else False

# using filter class # akan return value if True
multipleofthree = filter(findMultipleOfThree, range(1, 50))
print(list(multipleofthree))


print("="* 40)


# to get odd number from the list
numbers = [2, 5, 7, 3, 4, 6, 10, 11, 15, 17, 24, 22] # in integer
oddnumbers = []

for number in numbers:
    if number % 2 !=0:
        oddnumbers.append(number)
print("Traditional way", oddnumbers)

# using list comprehension
oddnumbers = [number for number in numbers if number %2!=0]
print("List comprehension way", oddnumbers)

def isOddNumber(number):
    return True if (number % 2 != 0) else False

oddnumbers = filter(isOddNumber, numbers) 
print("Filter way", list(oddnumbers))
    
# all the above two examples are trying to create a new list
# the number of items in the created list is less than or equals to original list
# instead of writing it traditionally for loops
# we use soething called list comprehension or filter class
print("="* 40)


sum = 0
for number in range(1, 10):
    sum = sum + number

print("Sum", sum)

print("="* 40)


mean = 0 # nak cari average of all numbers
for number in range(1, 11):
    mean = mean + number
mean = mean / len(range(1, 11))
print("Mean", mean)


# in the above 2 examples we are trying to reduce the list to a single value

# reduce is not a built function
# it is inside a module called itertools
from functools import reduce

numbers = [1,2,3]
def findTotal(oldvalue, currentvalue):
    return oldvalue + currentvalue


print("Reduce function:", reduce(findTotal, numbers))
# reduce function takes another function as 1st parameter 
# that function suppose to take 2 parameter
# reduce function takes list as second parameter
"""
def reduce(func, numbers):
    sum = 0 
    # however the original reduce function is smart
    # it will initialize the sum variable with 1 if you use multiplication
    for number in numbers:
        sum = func(sum, number)
    return sum
"""

def factorial(oldvalue, currentvalue):
    return oldvalue * currentvalue

print(reduce(factorial, numbers))

# we initializing the sum variable with 5
print(reduce(factorial, numbers, 5))






# using tuple comprehension
#newlist = (expression for number in numbers condition)

overseafruits = (fruit for fruit in fruits)

# to use list comprehension in 2 problems