"""
# q3 LEAP YEAR

# leap year is where if year%4 == 0 for none century years
#and year%400 == 0 for century years(year end with 00)
# xdpt lagi do

year = 1900

if(year%400 == 0 and year%100 == 0): # utk century year
  print("It's a leap year")
elif(year%100 != 0 and year%4 ==0): # utk noncentury year
  print("It's a leap year")
else:
  print("It's a normal year")

#q5 VOWEL AND CONSONENT

character = input("Enter a character: ")

if(character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u'):
    print("The character is a vowel ")
elif(character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U'):
    print("The character is a vowel")
else:
    print("The character is a consonant")


#q6

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

BMI = weight/ (height **2)

if (BMI < 18.5):
    print("You are underweight!")
elif(BMI >= 18.5 and BMI < 24.9):
    print("You have a fit body")
elif(BMI >=25 and BMI < 29.9):
    print("Oh, no! You are overweight")
else:
    print("You are obese!")

    
# q7 TYPE OF TRIANGLE

length1 = int(input("Enter a value of 1st length for a triangle: "))
length2 = int(input("Enter a value of 2nd length for a triangle: "))
length3 = int(input("Enter a value of 3rd length for a triangle: "))

if ( length1 == length2 and length2 == length3 and length1 == length3):
    print("The triangle is equilateral")
elif( length1 == length2 or length1 == length3 or length2 == length3):
    print("The triangle is an isosceles")
else:
    print("The triangle is a scalene")



# q8 WITHDRAWAL

amount = int(input("Enter an amount of withdrawal: "))

piece_of_50 = amount // 50
remain50 = amount % 50
piece_of_20 = remain50 // 20
remain20 = remain50 % 20
piece_of_10 = remain20 // 10
remain10 = remain20 % 10

if(amount % 10 == 0):
    print("The amount of piece for RM50: ", piece_of_50)
    print("The amount of piece for RM20: ", piece_of_20)
    print("The amount of piece for RM10: ", piece_of_10)

else:
    print("The amount is invalid. You can only withdraw the money in RM50, RM20 and RM10")
"""

# q9 (Adam Number)

num = int(input("Enter a 2 digit number: ")) #56

reverse = (num % 10) * 10 + (num // 10) #65
square = (num ** 2) #3136
square_reverse = (reverse ** 2) #4225
print(f"Square of the number: {square} \nSquare of the reverse number: {square_reverse}")

strsquare_reverse = str(square_reverse)

rev_reverse_square =int(strsquare_reverse[::-1])
print("Reverse to square of reverse number: ", rev_reverse_square)

if(square == rev_reverse_square):
    print(f"The value {square} = {rev_reverse_square} is an Adam number")
else:
    print(f"The value {square} != {rev_reverse_square} is not an Adam number")
""""

#CARA KIRA SATU-SATU
rev_square_reverse = square_reverse % 10 # 5
quotient = square_reverse // 10 #422
rev_square_reverse = (rev_square_reverse * 10) + (quotient % 10) #52
quotient = quotient // 10 #4
rev_rev_x = (rev_rev_x * 10) + (quotient % 10) #144
"""


"""

#q10
num = int(input("Enter the number between 0 and 9999: "))

if(num>=0 and num<=9):
  result = num **1
  if(num == result):
    print(f"The sum of {num}^1 is {result} and it is an Amstrong number")

# for two digit number
elif(num>=10 and num<=99): #eg: 23
  d0 = num // 10 # eg:2
  d1 = num % 10  # eg:3
  result = (d0 ** 2) + (d1 ** 2)
  if(num == result):
    print(f"The sum of {d0}^2 and {d1}^2 is {result} and it is an Amstrong number")
  else:
    print("The number is not an Amstrong number")


# for three digit number
elif(num>=100 and num<=999): # eg: 435
  d0 = num // 100 # for value 4
  d1 = (num % 100) // 10 # for value 3
  d2 = (num % 100) % 10 # for value 5
  result = (d0 ** 3) + (d1 ** 3) + (d2 ** 3)
  if(num == result):
    print(f"The sum of {d0}^3 and {d1}^3 and {d2}^3 is {result} and it is an Amstrong number")
  else:
    print("The number is not an Amstrong number")

# for four digit number
elif(num>=1000 and num<=9999): # eg: 1234
  d0 = num // 1000 # for value 1
  d1 = (num % 1000) // 100 # for value 2
  d2 = ((num % 1000) % 100) // 10 # for value 3
  d3 = ((num % 1000) % 100) % 10 # for value 4
  result =( d0 ** 4) + (d1 ** 4) + (d2 ** 4) + (d3 ** 4)
  if(num == result):
    print(f"The sum of {d0}^4 and {d1}^4 and {d2}^4 and {d3}^4 is {result} and it is an Amstrong number")
  else:
    print("The number is not an Amstrong number")

else:
  print("The number you enter is not between 0 and 9999")
"""