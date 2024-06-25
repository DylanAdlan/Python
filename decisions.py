# Write a program to find whether the given number is positive, negative, or zero
# Write a program to find whether our business is making profit, loss and breakeven

expenses = 1000
sales = 1100

# Objective 1: Just say whether we are making profit (single condition)
#atau if ( sales - expenses > 0)
if (sales > expenses):
    #block of code
    print("You are making a profit") # executed conditionally only if it make profit

# Objective 2: Say whether we are making profit or loss ( 2 conditions)
if( sales > expenses): # ifyou have colen, you MUST have the statement, if not, ada error "indentation error
    print("You are making Profit")
else:
    print("You are making Losses")

# Objective 3: Say whether we are making profit or loss or breakeven (3 conditions)
if( sales > expenses): 
    print("You are making Profit")
else:
    if(sales == expenses):
        print("You are making a breakeven")
    else:
        print("You are making a Loss")

# Created nested if using elif
if( sales > expenses): 
    print("You are making Profit")
elif(sales == expenses):
    print("You are making a breakeven")
else:
    print("You are making a Loss")

print("Thank You") # akan always executed even xmake profit



#           DECISION MAKING
# find whether the given number is even or odd
givennumber = 4

# if the statement to be executed is not a block of code
# if it is a single statement then we can write the if and statement 
# in the same line

# WITH ONE CONDITION
if(givennumber % 2 ==0): print("Even number")

# ONLY FOR SINGLE STATEMENT WITH 2 CONDITION
print("Even number") if (givennumber % 2 == 0) else print("Odd number")

# FOR 3 CONDITION
givennumber = 1
print("+ve") if(givennumber >0) else print("-ve") if (givennumber <0) else print("zero")