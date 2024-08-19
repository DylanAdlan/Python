# when we called python to execute our program
# our program in the command line is also called command line arguments
# these arguments separated by space
# all these arguments inside the list are string type
#Remember the arguments for function is separated by comma


# sys.argv give us a list which contains command line argument
# to passed to python
# in the list you can see the items at position 0 in program name itself

import sys
cmdarguments = sys.argv
# we use .(dot) operator to access the variable which is inside the module sys

print(cmdarguments)
length = len(cmdarguments)
print(length)
# find the total of all the argument
# if we know the total number of arguments, then we can hardcode it
# total = int(cmdarguments[1]) + int(cmdarguments[2])

# In this case we have to use loops (since we do not know the sum of all of arguments)
# total =0
# for number in cmdarguments[1:]:
#     total = total + int(number)
# print(total)

