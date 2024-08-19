
# q1

count = 100

for i in range(count):
    if i>0:
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

print("="*40)

# q2
num = int(input("Enter a number: "))

while num > 1:
    if num % 2 == 0:
        num = int(num/2)
    else:
        num = int((3 * num) +1)
    print(num, end=" => ")


#q3 using function (tpi kluar None)
def CollatzSequence(number):
    while number>1:
        if number % 2 == 0:
            number = int(number/2)
        else:
            number = int((3*number) + 1)
        
        return number

print(CollatzSequence(64))


# q3
print("Greatest Common Divisor, GCD using Euclidean Algorithm")
A = int(input("Enter first integer: "))
B = int(input("Enter second integer:"))

print(f"GCD({A},{B}) =>", end=" ")
while A > 0 or B > 0:
    if(A == 0):
        print(B)
        break
    elif(B==0):
        print(A)
        break
    else:
        temp = A % B
        A = B
        B = temp
        print(f"GCD({A},{B}) =>", end=" ")


# q3 using function

def ComputeGCD(a,b):
    if b==0:
        return a
    elif a==0:
        return b
    else:
        return ComputeGCD(b, a%b) #return ComputeGCD means keep on executing until reach b==0 or a == 0
        # (18, 4%18=4)
        # (4, 18%4=2)
        # (2, 4%2=0)
        
print("Greatest Common Divisor, GCD using Euclidean Algorithm")
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
print(ComputeGCD(num1, num2))



# q4
#https://www.youtube.com/watch?v=fn68QNcatfo


import random
print("Let's Play Rock Paper Scissor!")

options = ("rock", "paper", "scissor")

running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissor): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "paper":
        print("You win!")
    elif player == "paper" and computer =="rock":
        print("You win!")
    elif player == "scissor" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (y/n): ").lower() 
    #lower function so that if 
    #user input uppercase, it'll convert to lowercase

    if not play_again == "y": #dont wanna play anymore
        running = False


print("Thanks for playing!")


#q4 rock paper scissor
import random
print("Let's Play Rock Paper Scissor!")

numbers = random.randint(1,3) # random picked by computer
# range from 1 - 3 (included)

player = None
computer = numbers

while player not in range(numbers):
    player = input("Enter a choice (1 - rock, 2- paper, 3 - scissor): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "paper":
        print("You win!")
    elif player == "paper" and computer =="rock":
        print("You win!")
    elif player == "scissor" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

#q5
# https://www.youtube.com/watch?v=piJc18hcH0Y
import random

print("Let's play Game: Guess a Number!")

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number between {low} - {high}: "))
    guesses +=1

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is correct!")
        break

print(f"This round took you {guesses} guesses")


#q6

print("Generate 10 perfect numbers")

numbers = range(6, 100000000) # 6 is smallest perfect number
count = 0
while (count < 10):
    for i in numbers:
        divisors = []
        for divisor in range(1, i):
            if(i % divisor == 0):
                divisors.append(divisor)

        #print(divisors)
        sum = 0
        for k in divisors:
            sum = sum + int(k)

        if(sum == i):
            print("The perfect numbers: ", i)
            count +=1

# q6
print("10 perfect numbers using prime numbers")

count = 0

prime= []

givenNumber = 2
while(count<10):
    isPrime = True
    divisors = range(2, givenNumber)
    for divisor in divisors:
        if(givenNumber % divisor == 0):
            isPrime = False
            break

    if(isPrime == True):
        #print(givenNumber, end=" ")
        prime.append(givenNumber)
        count +=1

    givenNumber +=1

for i in prime:
    q = (2 ** i) - 1
    perfect = (2 ** (i-1))* q
    print(perfect)




# q7

# do it in fraction

print("Harmonic Series!")

number = int(input("Enter a number: "))

sum =0
for i in range(1, number):
    sum = sum + (1 / i)
    print(f"1/{i} + ", end=" ")

print(f"= {sum:.3f}")

# q8 

print("Convert Numbers to Words!")

number = int(input("Enter a number: "))

digit = 0 
temp = number
while temp

numtoWord = []

while number > 0:
    rem = number % 10
    if rem == 0:
        numtoWord.append("zero")
    elif rem == 1:
        numtoWord.append("one")
    elif rem == 2:
        numtoWord.append("two")
    elif rem == 3:
        numtoWord.append("three")
    elif rem == 4:
        numtoWord.append("four")
    elif rem == 5:
        numtoWord.append("five")
    elif rem == 6:
        numtoWord.append("six")
    elif rem == 7:
        numtoWord.append("seven")
    elif rem == 8:
        numtoWord.append("eight")
    else:
        numtoWord.append("nine")

    if number = number // 10

for i in numtoWord[::-1]:
    print(i, end=" ")



# q8
print("Convert number to words")

first = [" ", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", \
          "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = [" ", " ", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

multiplier = ["hundred", "thousand", "million", "billion", "trillion"]

number = int(input("Enter number 1 > 99999:"))

if number < 20:
    print(first[number])
elif number > 19 and number <=99: #45
    quotient = number // 10 #4
    print(tens[quotient],end =" ")
    remainder = number % 10 #5
    print(first[remainder])
elif number > 99 and number <1000:
    digit1 = number // 100
    digit2 = (number % 100) // 10
    digit3 = (number % 100) % 10

    print(f"{first[digit1]} {multiplier[0]} and {tens[digit2]} {first[digit3]}")

elif number > 1000 and number <10000: # 3525
    digit1 = number // 1000 #3
    digit2 = (number % 1000) // 100 #5
    digit3 = ((number % 1000) % 100 )// 10 #2
    digit4 = ((number % 1000) % 100 )% 10 #2
    print(f"{first[digit1]} {multiplier[1]} {first[digit2]} {multiplier[0]} and {tens[digit3]} {first[digit4]}")

elif number >= 10000 and number <20000: # 11769 
    digit1 = number // 1000 # 11
    digit2 = (number % 1000) // 100 #7
    digit3 = ((number % 1000) % 100 )// 10 #6
    digit4 = ((number % 1000) % 100 )% 10 #9
    print(f"{first[digit1]} {multiplier[1]} {first[digit2]} {multiplier[0]} and {tens[digit3]} {first[digit4]}")

elif number >= 20000 and number <100000: # 21575
    digit1 = number // 10000 # 2
    digit2 = (number % 10000) // 1000 #1
    digit3 = ((number % 10000) % 1000 )// 100 #5
    digit4 = ((number % 10000) % 1000 )% 100 //10 #7
    digit5 = ((number % 10000) % 1000 )% 100 % 10 #5
    print(f"{tens[digit1]} {first[digit2]} {multiplier[1]} {first[digit3]} {multiplier[0]} and {tens[digit4]} {first[digit5]}")
else:
    print("Invalid number")


# q9 

# roman to number
def romanToInteger(s):
    # Dictionary to map Roman numeral characters to their integer values
    roman_dict = {
        'I': 1,    'V': 5,    'X': 10,   'L': 50,
        'C': 100,  'D': 500,  'M': 1000
    }

    # Initialize variables
    total = 0        # To store the total integer value
    prev_value = 0   # To store the value of the previous Roman numeral character

    # Iterate through each character in the Roman numeral string
    for char in s:
        current_value = roman_dict[char]  # Get integer value of the current character

        # If current value is greater than previous value, it means a subtractive combination
        if current_value > prev_value:
            total += current_value - 2 * prev_value  # Adjust total accordingly
        else:
            total += current_value

        # Update prev_value for next iteration
        prev_value = current_value

    return total

def integerToRoman(number):
    # define numbers and their corresponding symbols
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


    # assigned to empty to store roman numeral
    roman_numeral = "" 

    # currentavlue will hold the number
    currentNumber = number
    # the current position assigned with 0 bcs we want to 
    # to start with first index of numbers and symbols
    position = 0

    # currentnumber = 12
    while currentNumber > 0: # 12 > 0
        if currentNumber - numbers[position] >=0: # if 12 - 1000 >=0
            roman_numeral += symbols[position]
            currentNumber -= numbers[position]
        else:
            position +=1

    return roman_numeral

option = int(input("Choose your options: \n 1. Convert roman numerals to numbers \n 2. Convert numbers to roman numerals:\n"))
if option == 1:
  roman = input("Input your roman numerals:")
  print(romanToInteger(roman))
elif option == 2:
  number = int(input("Enter your number:"))
  print(integerToRoman(number))
else:
  print("Invalid option!")



# # Example usage:
# print(integer_to_roman(3))        # Output: "III"
# print(integer_to_roman(4))        # Output: "IV"
# print(integer_to_roman(9))        # Output: "IX"
# print(integer_to_roman(58))       # Output: "LVIII"
# print(integer_to_roman(1994))     # Output: "MCMXCIV"
# # Example usage:
# print(roman_to_integer("III"))      # Output: 3
# print(roman_to_integer("IV"))       # Output: 4
# print(roman_to_integer("IX"))       # Output: 9
# print(roman_to_integer("LVIII"))    # Output: 58
# print(roman_to_integer("MCMXCIV"))  # Output: 1994


# q10 string compression

def compress_string(s):
    compressed_string = []  # List to store compressed characters and counts
    count_consecutive = 0    # Counter for consecutive occurrences of a character

    # Traverse through the input string `s`
    for i in range(len(s)): # aabcccccaaa (0,11)
        count_consecutive += 1  # Increment the count for consecutive occurrences
        # 1

        # kalau next character still same, dia xlepas if condition and will keep count_counsecutive +1
        # Check if the next character is different or if we've reached the end of the string
        if (i + 1 >= len(s)) or (s[i] != s[i + 1]):
          # 0 + 1 >= 11 x         a != a x

            compressed_string.append(s[i]) # Append current character
            # kalau next character diferrent, then append the character
            compressed_string.append(str(count_consecutive))  # Append its count as a string
            count_consecutive = 0  # Reset the count of consecutive occurrences

    # Join the list into a string (It concatenates each element of compressed_string into a single string,
    # using the empty string '' as the separator between elements.)
    compressed_string = ''.join(compressed_string)

    # Return the compressed string only if it's shorter than the original string `s`
    return compressed_string if len(compressed_string) < len(s) else s
    # to make sure length compressed string shorter than length of original string
    # then it will return the compressed string
    # if False, original string will return

# Example usage:
#input_string = "aabcccccaaa"
input_string = input("Enter string of character eg:aabbccc: ")
print(f"Original string: {input_string}")
print(f"Compressed string: {compress_string(input_string)}")
