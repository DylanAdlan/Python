for i in range(4): # represent row 0 1 2 3
    for j in range(5): # represent column 0 1 2 3 4
        print(i, j, sep=",", end=" ")
    print() #after finish each loop, it'll create new line

print("="*40)

print("Nesting looping for loop in for loop\n")
for i in range(5):
    for j in range(5):
        print(j, end=" ")
    print()

print("="*40)

print("Nested loop by creating a pyramid of numbers")

count = 5 # 5 row

for i in range(1, count+1): # 1 2 3 4 5
    for j in range(1, i+1): # 1
        print(j, end=" ")
    print()


print("="*40)

print("Nested loop to print a pattern")

count = 13

for i in range(count):
    for j in range(count):
        if i==j or i + j == count -1: # bila value i sama mcm j or 
        # bila value i + value j = 6
            print("*", end=" ")
        elif i>j and i+j>count-1:
            print("#", end=" ")
        elif i<j and i+j<count-1:
            print("#", end=" ")
        else:
            print("$", end=" ")
    print()

print("="*40)

count = 5

for i in range(count):
    for j in range(count):
        if j<=i:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()

print("="*40)

count = 5

for i in range(count):
    for j in range(0, i+1):
        print("*", end=" ")
    print()


print("="*40)

count = 5

for i in range(count):
    for j in range(count-i):
        print("#", end=" ")
    print()