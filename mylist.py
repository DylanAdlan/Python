# 4 types of builtin data structure in python
# list, tuple, set and dictionary

# list uses[]
# list is midifieble (append, edit and delete)
# list is ordered (items retain its position)
# list is indexed(0,1,2,3,4...)
# list allows duplicates

fruits = ["apple", "orange", "mango", "banana", "grapes"]
# fruits is a variable assigned w multiple value(s)
# fruits is also called an object
# if anything called as object, which mean it is instance of a class
# Adnin, Syu, Farah are objects, instance of Human Class
# adnin has 2 eyes, 1 nose, 2 legs --> properties
# Adnin can wlk, run, eat, listen --> methods
# fruits object also has its own properties and methods
print(fruits)

#Indexing and Selection
# Refer to variablesparttwo.py

#Modifiable
fruits.append("durian")
# the item get added as last item
print(fruits)

#insert items inside the existing list
fruits.insert(1, "rambutan") # in position 1 =>rambutan
print(fruits)
fruits.insert(3, "cempedak")
fruits.insert(5, "dummy")
print(fruits)

#update item in the list
fruits[5] = "mangosteen"
print(fruits)

# how to remove an item from the list
fruits.remove("durian")
print(fruits)

# to remove the last item, use "pop" method
fruits.pop()
print(fruits)

# delete an item by index
# we can delete anything from memory permanently using keyword del
greeting ="Good Morning"
del greeting
# did you notice there is no () after del so its confirm KEYWORD
# print(greeting) #NameError
# print([1,2,3,4] + 5) # TypeError
del fruits[3]
print(fruits)

# if u want to clear the list (remove all the items in the list)
fruits.clear()
print(fruits)

# delete entire list of fruits
del fruits
# print(fruits)

fruits = ["apple","mango", "orange", "mango", "apple", "banana", "grapes"]
print(fruits.index("mango"))

#newfruits = fruits[2:]
#print(fruits.index())


# sort by ascending order a-z
fruits.sort()
print(fruits)

# from ascending order, we reverse it
fruits.reverse()
print(fruits)

for fruit in fruits:
    print(fruit, end=" ")


print("=" * 40)


# using this way, one variable changed,
# both followed
# they shared the same list
print("USING ASSIGN OPERATOR TO SHARE SAME LIST")
x = [10, 20, 30, 40, 50]
y = x
print("x:", x)
print("y:", y)
x[2] = 35
print("x:", x)
print("y:", y)

print("=" * 40)

# to perform deep copy
# dont create y = x
# but create new list for y and input the values of x 
# inside y list
print("USING FOR LOOP")
x = [1,2,3,4,5]
y = []
for i in x:
    y.append(i)
print("x:", x)
print("y:", y)
x[2] = 35
print("x:", x)
print("y:", y)

print("=" * 40)

# instead of make a loop to insert values of x into y
# use "copy" method
print("USING copy METHOD")
x = [3,4,5,6,7]
y = x.copy()
print("x:", x)
print("y:", y)
x[2]= 35
print("x:", x)
print("y:", y)

print("=" * 40)

# list is actually a class, not a function
# thses 2 is different
# (this method used to create object)
# technical, we supposed to create like this
x = list([10, 20, 30, 40])
print(x)
# but we using like this
x = [12,22,34,42,52]
print(x)


print("="*40)

def total(numbers):
    result = 0
    numbers[2] = 35
    for number in numbers:
        result += number
    return result


x = [10, 20, 30, 40]
print(x)
print(total(x))
print(x)

print("="*40)

# to convert list to tuple
x = tuple(x)
#print("After convert list to tuple:", total(x))

print("="*40)


# last feature in list
# list can auto EXPLODE
# explode means create 1 variable for every item in the list
print("Feature in list : auto EXPLODE")
fruits = ["apple", "mango", "grapes"]
fruit01, fruit02, fruit03 = fruits
print("Fruit1:",fruit01)
print("Fruit2:", fruit02)
print("Fruit3:", fruit03)


