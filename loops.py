fruits =["apple", "rambutan", "orange", "durian", "mango", "cempedak", "banana", "mangosteen", "grapes"]

# whenever you want to iterate a list of items, you must "for" loop
# print all the items in the list

for fruit in fruits:
    print(fruit)

# print all the items in the even position
for fruit in fruits[::2]:
    print(fruit)

# print only fruit with 6 letters
for fruit in fruits:
    if(len(fruit) == 6):
        print(fruit)

# To print each of fruit together with the index
position =0
for fruit in fruits:
    print(position,fruit)
    position +=1


# i want to create a multiplication table of 5
# i want to go until 12
# 1 x 5 = 5
# 2 x 5 = 10

multipliers = [1,2,3,4,5,6,7,8,9,10,11,12]
multiplicant = 5
for multiplier in multipliers:
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)

# however this is not practical when until is 200 instead of 12
# we have to go for range option start_index:end_index
# but the : operator can work only on a list
# we have a built in function called range which can generate list of numbers
# range function takes start index and end index and generate numbers between them
# start index is included but end index is not included
print(range(1,13))
# however when i print it, i cannot see the numbers
# range is an iterable object,
# which means we can use it in a "for" loop together with "in" operataor
# however print funtion do not know how to iterate range object
# so it prints as range(1, 13)
# any iterable object can be typecast to a list using list function
# print function knows how to iterate the list
print(list(range(1, 13)))

# let us do the multiplication table using range
multiplicant = 6
for multiplier in range(1, 13):
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)

# split the digit in the input and print them
# 
# while loop
#givenNumber = input("Give me the number:")
givenNumber = 97409
while(givenNumber > 0):
    print(givenNumber % 10)
    givenNumber = givenNumber // 10


givenNumber = 12345
numberofdigit = len(str(givenNumber)) -1  # panjang digit givennumber tolak satu
while(givenNumber > 0):
    print(givenNumber // 10 ** numberofdigit)
    givenNumber%= 10 ** numberofdigit
    numberofdigit -=1



givenNumber = 67891
strgivenNumber = str(givenNumber)
for digit in strgivenNumber:
    print(digit)

# for loop and while loop can also have "else" block
fruits = {"apple", "orange", "mango", "banana", "grapes"}
# the code in the else block will get executed only when all the fruits iterated\
for fruit in fruits:
    print(fruit)
    # since we added this condition now when it sees mango
    # jumps out of the loop(list iteration)
    if(fruit == "mango"): break
else:
    print("All fruits printed")

multiplicant = 6
multiplier = 1
while(multiplier <=12):
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)
    multiplier +=1
    # since we added this condition now when it sees mango
    # jumps out of the loop(codition not fai yet 11 <= 12 true)
    # the code in the else block not executed
    if(multiplier == 11): break
else:
    print("Multiplication table done")


# USING CONTINUE UTK GO BACK TO THE LOOP WITHOUT EXECUTE THE FOLLOWING LINE
multiplicant = 10
multiplier = range(1, 13)
for multiplier in multipliers:
    if(multiplier % 5 ==0): continue
    print(multiplier, "x", multiplicant, "=", multiplier * multiplicant)