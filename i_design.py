"""print("Welcome to Amphi Event Management System")

name = input("Enter you name: ")
print(f"Hello, {name} ! Welcome to Amphi Event Management System")


branding = int(input("Enter branding expenses: "))
travel = int(input("Enter travel expenses: "))
food = int(input("Enter food expenses: "))
logistic = int(input("Enter logistics expenses: "))

total = branding + travel + food + logistic
print(f"Total expenses : Rs.{total:9.2f}")

branding_percent = float((branding / total) * 100)
travel_percent = float((travel / total)* 100)
food_percent = float((food / total)* 100)
logistic_percent = float((logistic / total)*100)
print(f"Branding expenses percentage: {branding_percent:3.2f} % ")
print(f"Travel expenses percentage: {travel_percent:3.2f} % ")
print(f"Food expenses percentage: {food_percent:3.2f} % ")
print(f"Logistics expenses percentage: {logistic_percent:3.2f} % ")


#   QUESTION 4
x = int(input("Enter number of difference between child tickets and adult tickets: "))
y = int(input ("Enter the total number of all tickets sold:  "))

#y = (adult * 5) + (senior * 3) + (child * 2)
#y = ((x + child) * 5) + ((2*child)*3) + (child * 2)
#y = 50+ (13*child)
child = int((y - 50) / 13)
adult = int(x + child)
senior = int(2 * child)
print(f"Number of children tickets sold : {child}" )
print(f"Number of adult tickets sold : {adult}" )
print(f"Number of senior tickets sold : {senior}" )

"""
#   QUESTIION 7

arguments = ["Commands", "Argument"]
#arguments = input("Enter your command line argument")
#distribute = arguments.split(" ")

for argument in arguments:
    print(argument)

print("Number of arguments is ", len(arguments))




