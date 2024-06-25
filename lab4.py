"""#   QUESTION 8

# 1. Write a python program that takes few numbers as command line argument. 
import sys

arguments = sys.argv

# 2. Use a loop to display all elements. 

for argument in arguments[:]:
    print(argument, end=" ")

print()

# 3. Use another loop to display all elements in the even position. 
position = str(len(arguments))
for place in range(1, int(position)):
    if(place % 2 == 0):
        print(arguments[place])
print()

    
# 4. Use another loop to display all elements in the odd position.
position = str(len(arguments))
for place in range(1, int(position)):
    if(place % 2 != 0):
        print(arguments[place])
print()

#   QUESTION 9
# 1. Write a python program that takes few numbers as command line argument. 
import sys

numbers = sys.argv
print(numbers)

# 2. Find average of those numbers
count = len(numbers)
sum = 0 # initialize sum
for place in range(1, int(count)):
    sum = sum + int(numbers[place])


average = sum / (count-1)
print(f"The average of all numbers: {average:.2f} ")

#   QUESTION 12
num1 = int(input("Enter first positive number:"))
num2 = int(input("Enter second positive number:"))

sum = 0
# represent number yang perlu diulang berapa kali dri 1 hingga num2
for count in range(1, num2 + 1):
  # represent hasil tambah num1 yang berulang kali tambah mgikut brapa num2
  sum = sum + num1


print(f"The total multiplication between two numbers is {sum}")




for number in range(2, 31):
  if((number == 2) or (number == 3)):
    print(number)
  elif((number >3) and (number % number == 0) and (number%2 !=0)):
    print(number)
  elif(number > 10):
    quotient = number //10
    remainder = number % 10
    sum = quotient + remainder
    if(sum % 3 != 0):
        print(number)



number = input("Enter list of numbers separated by comma(,): ")

number_split = number.split(",")
print(f"The list of numbers: {number_split} \n ")

unique = []


for i in number_split:
  if i in unique:
    continue
  elif not i in unique:
    unique.append(i)


print(f"List of unique numbers: {unique}")

x,y,z = 0,1,2
for i in unique[x:]:
  for j in unique[y:]:
    for k in unique[z:]:
      sum = 0
      sum = int(i) + int(j) + int(k)
      if(sum == 100):
        print(f"Sum of {i}, {j}, and {k} is {sum}")
      else:
        continue



count = int(input())

givenNumber = 2
while(count>0):
  isPrime = True
  divisors = range(2, givenNumber)
  for divisor in divisors:
    if(givenNumber % divisor == 0):
      isPrime = False
      break
  
  if(isPrime == True):
      print(givenNumber, end=" ")
      count -=1
  givenNumber +=1
  
count = int(input())

even = 30
odd = 35
x= 8
y=6
print(even, odd, sep=" ", end=" ")
for i in range(0, count-2):
  if (i % 2 == 0):
    even += x
    print(even, end=" ")
    x +=8
  else:
    odd +=y
    print(odd, end=" ")
    y +=6

"""






