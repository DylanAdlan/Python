# product is the variable
# "Television" is the string value/literal
# to differentiate the values from the variables we use double quote ""
# or single quote ''
# product = 'Television'
product = "Television"
quantity = 2 # integer
price = 1455.25 # float
available = True # True / False (boolean value/literal)
print("Product:", product)
print("Quantity:", quantity)
print("Price:", price)
print("Available:", available)

# type is another built in function that tell us what is the 
# data type of the variable (dynamically typed programming language)
print(type(product))
print(type(quantity))
print(type(price))
print(type(available))
# the result are in the class because every literal is an object, we'll get back to it

total = quantity * price
print("Total", total)

# In real world use cases the 10 will not be hard coded
# the 10 is coming from an input device)keyboard)
# So the input value can be a string which needs to be converted
quantity = "10"
print(type(quantity))
price = "1455.55"

# type casting
# = convert one data type to another
# to convert string to integer we have built in function int
# to convert string to float we have built in function float
# to concert integer to string we have built in function str
total = int(quantity) * float(price)
print(total)

x = 100
# want to know where the location is 
# we can use built in function id to knw where the location of value x
print(id(x))

y = 100
#however in python, the object 100 is not created first
# python will sacn first if the object have already exists then
# pyhton will reuse the object instead of re-creating the object

a = "Adnin"
b = "Adnin"
print(id(a))
print(id(b))

# so far we have seen how to assigned 1 value to single variable
# in one line statement
# x = 100

# how to assign more than one values to more than one variables
# in one line of statement
x, y = 101, 102 # x = 101, y = 102

# also can do this
x, y = 101 + 1, 102 + 1
x, y = x + 1, y + 1
print(x, y)

# in some programming language, you can assign
# multiple variables with a single value
# x, y = 501 # however in Python, this is not allowed

#in other programming language we call these as "Variable initialization"
# But in python, there is now way for you to create a variable
# without assigning a value
y = 0 # numeric initialization
y = "" # string initialization / empty string / empty brain
y = None # no value, Nonetype ,no brain (kita just create y 
# bcs dont know what type of data type that kita akn received)
print(type(y))

# function can be make as variables but will have side effect
# print = 10
# print(print)
# keywords cannot be variables
# if = 10


"""
age = 34
age_as_str = str(age)
print("You are " + age_as_str)
"""