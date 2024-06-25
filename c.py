"""givenNumber = 97409
while(givenNumber > 0):
    print(givenNumber % 10)
    givenNumber = givenNumber // 10


adam = 0
for number in range(10, 100):


  square = (number**2) #100
  strreverse = str(number)
  reverse = int(strreverse[::-1])
  reverse_square = (reverse** 2) #1
  strreverse_square = str(reverse_square)
  reverse_reverse_square = int(strreverse_square[::-1])

  if(square == reverse_reverse_square):
    adam = str(adam) + " " + str(number)



print("The Adam numbers are: ", adam, end=" ")


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



for number in range(1, 9999):
  sum = 0
  strnumber = str(number)
  length = len(strnumber)
  for i in str(number):
    sum = sum +((int(i))*length)

if(number == sum):
  print(number)



numbers = int(input("Enter number of items to generate Armstrong Numbers:"))

armstrong = []
number = 1

while( len(armstrong) < numbers):
#for number in range(1, 9999):

  # utk tahu berapa digit dalam number
  strnumber = str(number)
  length = len(strnumber)

  # utk calculate the sum of each number times with the length
  sum = 0
  for i in strnumber:
    j = int(i)
    sum = sum + ( j ** length)

  #condition for armstrong number
  if(number == sum):
    armstrong.append(number)

  number +=1


print("Amstrong numbers:")
for i in armstrong:
  print(i, end=" ")



import sys
arguments = sys.argv

for argument in arguments:
    print(argument)

print("Number of arguments is ", len(arguments))


x = True
y = False
z = False
if x or y and z:
  print("Hello")
else:
  print("World")


x = True
y = False
z = False
if not x or y:
  print(1)
elif not x or not y and z:
  print(2)
elif not x or y or not y and x:
  print(3)
else:
  print(4)


count = int(input())

child = []

for i in range(count):
    child[i] = int(input())
print(child[i], end=" ")

"""

list = [5,3,3,13,-1,25,-7,39,-15]

num= 30
x = 0 
print(num, end=" ")
for i in list[x:]:
    num = num + int(i)
    print(num, end=" ")
    x +=1

    