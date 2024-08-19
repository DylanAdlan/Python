
print("Convert Decimal number to Binary number")
number = int(input("Enter number:"))

binary = 0 
result = []
while number > 0:
    binary = number %2
    number //= 2
    result.append(binary)

print("Binary number")
for i in result[::-1]:
    print(i, end="")
