
name = input("Enter your name: ")
print(name)

 """function split utk splitkan kpd set of lists in string
 -argument by space atau by comma atau by single quote
 -cth Nur satu list, Adnin satu list
 -list jgk utk position kan
 """
name_split = name.split()
print(name_split)

print(type(name))

a,b = map(str, name_split)
print(type(a))


""" format specifier
int - %d
float - %f
str - %s
"""
a = 12.34567
b = 123
c = "Hello"

print("%.3f" %a)
print("%d - %.2f : %s" %(b,a,c))