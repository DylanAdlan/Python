# UNTUK CREATE OUR OWN FUNCTIONS TO ORGANIZE THE CODE MORE ORGANIZED

def sayHelloWorld():
    print("Hello World !!!")

# function created using keyword def 
# followed by function names and paranthesis () and colon:
# then place your block of code inside the fx with indentation

# how to call the function
sayHelloWorld()

# if the created function want to take some value(s)
# then kita create variable / placeholder inside the paranthesis ()
# if more than 1 variable(S) then we create the variables separated by comma (,)
# these variables called as PARAMETER

def greeting(name, age):
    print("Good Morning", name, age)

# number of arguments must match with the number of parameters
greeting("Adnin", 40) # 2 parameters, then 2 arguments

def total(x,y,z):
    result = x + y + z
    print("Result:", result)

total(20, 40, 50)

def buyLunch(makan, minum):
    prices = []
    for food in makan:
        if( food == "nasi"):
            prices.append(2.80)
        elif(food =="sayur"):
            prices.append(2.20)
    for food in minum:
        if(food =="nescafe"):
            prices.append(2.50)
        
    #print(prices)
    return prices

itemprices = buyLunch(["nasi", "sayur"], ["nescafe"])
total = 0
for price in itemprices:
    total = total + price

print("Amount to be paid:", total)


# whether the return value must be in list

def simpleInterest(principle, period, rate):
    interest = principle * period* rate / 100
    return interest


print("The simple interest:", simpleInterest(1000, 1, 3.3))



# RETURN MORE THAN ONE VALUE SEPARATED BY COMMA (,)
def participantlist(nameone, nametwo, namethree):
    nameone = nameone + "data Scei"
    nametwo = nametwo + "daa"
    namethree = namethree + "fdfd"

    return nameone, nametwo, namethree


# you can also make the rate parameter optional by having a default value
def calculateSimpleInterest(principle, period=80, rate=6):
    interest = principle * period* rate / 100
    return interest


# since we are not passing the value for period and rate parameter
# the period will automatically become 1 and rate = 6
print(calculateSimpleInterest(1000)) # number of arguments also must be in positional

print(calculateSimpleInterest(1000, 2)) 

# is there a way to pass values for principle and rate only
# we can use something called "Named Argument/Keyword Argument"
# here the name is refering to parameter
print(calculateSimpleInterest(principle=1000, rate=5))

def findTotal(givenNumbers):
    total = 0
    for givenNumber in givenNumbers:
        total = total + givenNumber
    return total

# variable length argument
#the number of arguments which we pass varry
# caller can pass the value in a list
print(findTotal([10, 20, 30]))
print(findTotal([10, 20, 30, 40, 50, 60]))
print(findTotal([10, 20, 30, 40, 50, 60, 70, 80, 90]))

# kalau caller lupa nk ltak arguments in a list
# then kita just letak star (*) dkat parameter so
# dia akan take the values as in a list
# melibatkan integer
def calculateTotal(*givenNumbers):
    total = 0
    for givenNumber in givenNumbers:
        total = total + givenNumber
    return total

print(calculateTotal(10, 20, 30))
print(calculateTotal(10, 20, 30, 40, 50, 60))
print(calculateTotal(10, 20, 30, 40, 50, 60, 70, 80, 90))


# melibatkan string pun as the same
def listSixLetterFruits(*fruits):
    for fruit in fruits:
        if len(fruit)==6: print(fruit)

# we are sending the items/fruits individually (not a list)
# however python will convert them to a list of fuits and pass it
listSixLetterFruits("apple", "orange", "mango", "banana", "durian", "grapes")


def listFruitDetails(*fruits):
    print("Combination datatypes of arguments")
    for fruit in fruits:
        print(fruit)

# datatypes in arguments also can be mixed (integer, string, float)
listFruitDetails("apple", 40, 4.5, "durian", 50, 6.5)

def sum(a, b):
    return a + b

print(sum(10, 20)) 
# sum function will executed first followed by print function

# in the above statement it looks like we are passing
# sum funstion as argument to print function
# but in python, when we have a function followed by ()
# which mean sum functio is executed first
# the function takes 10, 20 as argument and returns 30
# that 30 becomes argument to print function

def minus(a, b):
    return a - b

# Basically in this case, we want to hide the sum and minus function
# from the user. we want to use the function arithematic 
# to perform sum and minus
def arithematic(func, a, b):
    return func(a, b)
    
# Notice there is no() after the function name
# this is how we pass function as an argument to another function
arithematic(sum, 10, 20)
arithematic(minus, 10, 20)


# sbb function baru created compared to arithmetic function, 
# then its not possible to call from arithematic
def mul(a, b):
    return a*b

# after modifying, now the function 
print("Arithemetic mul:", arithematic(mul, 20, 30))


