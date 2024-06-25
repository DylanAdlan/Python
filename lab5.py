"""
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

print("Convert roman numeral to integer")

def roman_to_integer(s):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    
    for char in s:
        current_value = roman_dict[char]
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        prev_value = current_value
    
    return total

# Example usage:
roman_numeral = "IX"
print(f"The integer value of {roman_numeral} is: {roman_to_integer(roman_numeral)}")


def roman_to_integer(s):
    # Define a dictionary to map Roman numeral characters to their integer values
    roman_dict = {
        'I': 1,   # 1
        'V': 5,   # 5
        'X': 10,  # 10
        'L': 50,  # 50
        'C': 100, # 100
        'D': 500, # 500
        'M': 1000 # 1000
    }
    
    # Initialize the total sum of the Roman numeral
    total = 0
    # Variable to keep track of the previous numeral's value
    prev_value = 0
    
    # Iterate through each character in the input string 's'
    for char in s:
        # Get the integer value corresponding to the current Roman numeral character
        current_value = roman_dict[char]
        
        # Compare the current value with the previous value
        if current_value > prev_value:
            # If the current numeral's value is greater than the previous one,
            # it means subtraction is needed (e.g., IV -> 5 - 1 = 4)
            total += current_value - 2 * prev_value
        else:
            # Otherwise, just add the current numeral's value to the total
            total += current_value
        
        # Update the previous value to the current value for the next iteration
        prev_value = current_value
    
    # Return the total sum, which is the integer representation of the Roman numeral
    return total

# Example usage:
roman_numeral = "IX"
print(f"The integer value of {roman_numeral} is: {roman_to_integer(roman_numeral)}")

"""
def roman_to_integer(roman):
    # Define a dictionary to map Roman numeral characters to their integer values
    numerals = {
        'I': 1,   # 1
        'V': 5,   # 5
        'X': 10,  # 10
        'L': 50,  # 50
        'C': 100, # 100
        'D': 500, # 500
        'M': 1000 # 1000
    }

    integer = 0

    for i in range(len(roman)):
        value = numerals[roman[i]]
        if i + 1 < len(roman) and numerals[roman[i + 1]] > value:
            integer -= value
        else:
            integer +=value

    return integer
    

roman = "XII"
print(roman_to_integer(roman))