# TUPLE is nothing but readonly list
# tuple ()
# is not  modifiable (cannot append, delete and edit)

print("TUPLE")
x = (10, 20, 30, 40)
print(x)
print(type(x))

print("position of x in tuple:", x[0]) 

fruits = ("flower", "flower", "fruit", "kitchen")
print("How many flower in fruits tuple:", fruits.count("flower"))

# can delete an entire tuple
# but cannot delete certain position, eg:del(fruits[0])
x = (1,2,3,4)
del x
#print(x) # x is permanently deleted

#why use tuple?
# 1) take less space
# 2) faster than list

def returnFruits():
    return "apple", "orange"

print("Type of returnFruits", type(returnFruits()))

print("=" * 40)


def total(*numbers):
    print(type(numbers))
    result = 0
    for number in numbers:
        result = result + number
    return result

# to convert data to collection
# we use tuple
print(total(10, 20, 30, 40)) 


# tuple can also auto EXPLODE
# explode means create 1 variable for every item in the tuple
# no need to split
print("Feature in tuple : auto EXPLODE")
fruits = ("apple", "mango", "grapes")
fruit01, fruit02, fruit03 = fruits
print("Fruit1:",fruit01)
print("Fruit2:", fruit02)
print("Fruit3:", fruit03)

# there is a problem to highlight a tuple
# since using (), can be confused with expression (10+1)
x =(10)
# in python, it gives priority for expression than tuple
# automatically 10 (integer) is assigned to x
print(type(x))

# to ensure the data is in tuple format please add an extra comma
x = (10,)
print(type(x))

print(list(enumerate(fruits)))  # print fruits in tuple