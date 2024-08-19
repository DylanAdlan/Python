# Python dictionary is also called JSON in other programming languages
# Javascript Object Notation (JSON)
# Dictionary is also using curly bracket {}
# the data is ordered
# the data is indexed by key (not by number)
# Every single data is associated with a key
# for example firstname is a key and Peter is a data
# Key cannot be duplicated, Data can
# It is modifiable

foreigner = {
    "firstname":"Peter",
    "lastname": "Parker",
    "passportnumber": "E4234432",
    "incometaxnumber": "SG576466",
    "pcbamount": 892,
    "lastmonth": 5,
    "lastyear": 2024,
    "previousmonth": [(4, 2024, 891), (3, 2024, 895), (2, 2024, 893), (1, 2024, 892)],
    "addresses": {
        "office": {
            "street": "15, Lot 5100",
            "taman": "Taman Cempaka" # last line dont have comma


        },
        "home": {
            "street": "16, Lot 5000",
            "taman": "Taman Bunga" # last item dont have comma


        }
    } # don have comma too bcs last line
}

# to pull out from dictionary

print("First name: ",foreigner["firstname"])
print("Last name: ",foreigner["lastname"])
print("Passport Number: ",foreigner["passportnumber"])
print("Income Tax Number: ",foreigner["incometaxnumber"])
print("PCB Amount: ",foreigner["pcbamount"])
print("Last Month: ",foreigner["lastmonth"])
print("Last Year: ",foreigner["lastyear"])

print("="*40)

# for item in foreigner["previousmonth"]
# item will hold tuple (4, 2024, 891)
# howver we know tuple is auto explodable
# as long as we have 3 variables we can epxlode and hold the 3 values
for month, year, amount in foreigner["previousmonth"]:
    print(f"Transaction: {month} - {year} RM{amount}")

print("="*40)

officeAddress = foreigner["addresses"]["office"]
print("Street:", officeAddress["street"])
print("Taman:", officeAddress["taman"])
homeAddress = foreigner["addresses"]["home"]
print("Street:", homeAddress["street"])
print("Taman:", homeAddress["taman"])

print("="*40)
# can access directly as follows
print(foreigner["addresses"]["office"]["street"])

print("="*40)

# sometime we dont know the keys
print(foreigner.keys())

print("="*40)

# tpi dia print out values in the keys
for key in foreigner.keys():
    # isinstance is a built in function to determine the type of the variable
    if (isinstance(foreigner[key], list)):
        for item in foreigner[key]:
            print(item)
    else:
        print(foreigner[key]) 

    # when you use the method items, you will get the key, value
    for key, value in foreigner.items():
        print(key, value)

    # how can i modify the dictionary
    # since the key car doest not exist in the dictionary, it gets added automatically
print("="*40)


foreigner["car"] = {
    "brand": "Proton",
    "model": "SAGA",
    "carplate": "JXY456"

}
foreigner["salary"] = 4890
print(foreigner)

print("="*40)


# if i want to modify the salary
# since the salary is alreday there it modifies/update the existing salary

foreigner["salary"] = 5120
print(foreigner)

# remove key "car"
foreigner.pop("car")
print(foreigner)

t = (1,2,3)
s = set(t)
print(s)

