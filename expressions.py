""" ARITHMATIC OPERATORS"""
x = 7
y = 2
#print function takes expressions as an argument
# result = x + y
# print("Addition: ", result)
print("Addidtion: ", x+y)
print("Subtraction: ", x-y)
print("Multiplication: ", x * y)
print("Division: ", x/y)

print("Quotient: ", x//y)
print("Remainder: ", x%y)

print("Exponent:", 10 **3)
print("What is the maximum number in 64 bit env: ", ( 2 ** 64) - 1)

#Assignment operator
x = 0 #first assignment
x += 1 # x = x + 1    (2nd assignment operator)
# y = mx + c
# y = 
x +=2
x +=5
# x = 108
x += x + 1 # x = x + (x + 1)
# x= 108 + 109 = 217
print(x)

x -= 1 # x = x - 1
x *= 1 # x = x * 1
x /= 1 # x = x / 1
x //=1 # x = x // 1
x %=1 # x = x % 1

# comparison operators
myheight = 5.2
yourheight = 5.3
mysisterheight = 5.2

#Let us create true statement
print(yourheight > myheight)
print(myheight == mysisterheight)
print(mysisterheight < yourheight)
print(myheight != yourheight)

print(yourheight >= myheight)
print(yourheight >= mysisterheight)

print(myheight <= yourheight)
print(mysisterheight <= myheight)

a = 21
b = 14
c = 7

print(a > b and a > c) # a is the greatest number
print(c < a and c < b) # c is the smallest number
print(( b > c and b < a) or ( b > a and b < c)) # b is the middle number between a and c 

# Negation operator
print(not (a>c)) # False
print(not (a<c)) # True

#truth table
print("The XOR:", (a>c) ^ (a>b))
