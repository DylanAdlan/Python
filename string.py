# dalam string, each huruf adalah character trmasuk comma, space and symbol
# ada 13 characters
my_string = "Hello, world!"

# Escaping = letak backslash depan character utk buang makna dia cth kita letak depan double quotation mark You are amazing
another_with_quotes = "He said \"You are amazing!\" yesterday."
print(another_with_quotes)


# Multiline = digunanakn utk tulis byk line  ayat dlm satu variable & blh guna as comment
"""
This is comment section

"""

name = """Hai, my name is Nur Adnin 

I studied at Ieg under Yayasan Peneraju

"""

print(name)

# to concert integer to string we have built in function str
age = 34
age_as_str = str(age) # convert integer to string
print("You are " + age_as_str) # kalau guna + variables xleh mix string-integer

print("You are", age) 

# using f strings utk blhkan penggunaan string + integer value sekali
age = 34
print(f"My age is {age}")

name = "Adnin"
greeting = f"How are you, {name}" #
print(greeting)

name = "Adam"
print(greeting)

""" Result still execute nama Adnin bcs value in name variable 
still Adnin and Adam not replace
"""

print("hey")
print("hello")

# insert end= parameter utk specify a string yg akn printed after output
print("hey", end="-") #specify the string output by dash (-)
print("adnin")

print("hey","miss", end="Welcome")
print("adnin")

print("hey", end="\n") # specify the string by making a new line (\n)
print("adnin")

# insert sep= parameter (utk separatekan the items)

print("hey", "adnin", "adlan", sep="-") # separate each items by dash (-)

print("hey", "ieg", "yp", sep="NO") #separate ecah items by NO

print("hey", "ieg", "yp", sep="\n") #separate ecah items by making a new line (\n)

print("The assignment", "is", "easy", sep=" . ", end=" ONE ")
 # type: ignore