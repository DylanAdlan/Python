#python has a built in function called inout
# the input function takes a single paramater (caption) ex:"Please enter your name"
# Input function will display the caption
# and wait for thr user input
# The user will provide the inout and press enter key
# the input is always of type string
# whatever the user provide, will be stored in a variable
firstnumber = input("Please key in the first number:")
print(firstnumber, "is my lucky number")
# the input always return the value of type string
print(type(firstnumber))

secondnumber = input("Please key in the second number:")
print(firstnumber + secondnumber) # string concatenation
print(int(firstnumber) + int(secondnumber)) # addition

numbers = input("Enter the number to do the Total:")
numberlist = numbers.split(",")
print(numberlist)
total = 0
for number in numberlist:
    # int function trim the string value
    # remove the spaces in the string and then convert 
    # string to integer
    total = total + int(number)
print(int(total))