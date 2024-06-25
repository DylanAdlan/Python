# so far we have learn to assign single value to single variable
# we also learn how to assign multiple values to multiple variables in the same line
# x=10
#x,y = 10, 11

#now we're going to learn to assign multiple values to single variable

# new data struvture called list to assign multiple values in single variable
# in other programming language called as array

fruits =["apple", "orange", "mango", "banana", "grapes"]

# indexing and selection
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

# to know how many items are there in the list
# there is a built in function called "len"
print("Number of items: ", len(fruits))

# how to find the maximum index
print("Maximum index: ", len(fruits)- 1)

# does the index must be a positive number?
# not necessary bcs in can be in -ve number (in python)

print(fruits[-1]) 
#-start with -1 dri belakang

# Range = start_index:end_index
# in python when we refer to range, the end_index is not included
print(fruits[1:3]) # only print oramge and mango bcs banana is excluded 

# if we did not mention the start index, it will take 0 as start index
print(fruits[:3])

# if we did not mention the end index, it will go until the last item
print(fruits[1:])

fruits =["apple", "rambutan", "orange", "durian", "mango", "cempedak", "banana", "mangosteen", "grapes"]
print(fruits[0:9]) #as we want to conclude the last item, then add an extra number of position

# only want even number position
print(fruits[0:9:2]) # :2 at last represent the step up means from 0->2->4->6->8

# this feature useful utk take samples in data
# cth: data have 1million records
# but we only want 50 samples
# so we can use step up argument to make the selection evenly

# also can use -ve numbers in the range
print(fruits[-5:-1]) #-1 is end_index so grapes is excluded

print(fruits[-1:-5]) # bcs -1 is greater then -5 results to empty list
print(fruits[-1:-5:-1]) # -5 index is not included

print(fruits[::-1]) # kalau nk start from back and nk mention all the items, 
# xperlu mention start and end index and just mention step up argument

