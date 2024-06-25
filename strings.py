firstName = "Adnin"
lastName = "Adlan"
# usually both sides of the operator is numbers
# if they are number we can perform addition

# If both sides are string we can perform "string concatenation"
fullName = firstName + " " + lastName

carPlate = "WC"
number = 405
#however this use case we cannot add them because 
# one is a number and another one is a string
# i can only concatenate string (not "int") to string
# in this case we cannot convert string(carPlate) to numbre
# so let us convert number to string using str function
carPlateNumber = carPlate + str(number)
print(carPlateNumber)

#In python you can multiply string with integer
#When we do this it will product "times" effect
product = "book"
print(product * 5) 
print("=" * 40)

# so far we know strings are enclosed with double quote
# or single quote
# we can also use triple double quote or triple single quote
# they are used to create multiline strings
# slash r means carriage return

message = """hai 
please im tired already
FIGHTING!!!!!"""

print(message)

message = "As im not feeling well\n"
message = message + "I won't be able to attend \tmeeting\n"
message = message + "Please proc\reed....\n"

print(message)

myfile = "c:\newfolder\table\read.txt"
print(myfile)
# we suppose to tell python to igonre escape sequence
# you can add extra escape sequence
myfile = "c:\\newfolder\\table\\read.txt"
print(myfile)
# however in python w aslos have special tring called raw string (r)
myfile = r"c:\newfolder\table\read.txt"
print(myfile)

# relationship between string and list
# strings are nothing but  list of characters

mygreeting = "Hello World!"
print(mygreeting[0])
print(mygreeting[0:6])
print(mygreeting[::2])
print(mygreeting[::-1])

# to know how many caharcter in mygreeting
print(len(mygreeting))

number = 97592
strgivennumber = str(number)
print (strgivennumber)

print(int(strgivennumber[::-1]))


# when i started this python class, i said all these literals are objects
# "Television" -> string literal/value
# "Television" -> also called string object
# Objects have functions inside 

product = "Television Cloths Vegetables Fruits"
print(product.split())

# split function takes the literal
# assigned to the variable 
# product and split them or (tokenize them)
# into multiple words (separated by space)
# using space as separator
# since it is going to return more than 1 words
#so itl will be list if words
# Function insde the object also called as "Method"
# from now you must said "print is a function"
# where "split is a method"



# "Television". # jarang guna sbb selalunya object input from user
