# Given number is 97531
# I want you to reverse the number
# expected result 13579

print("To reverse the number")

number = input(f"Enter number:\n") # no need to be in integer type

for i in number[::-1]:
    print(i, end="")


# Akmal solution
a0 = 97531

result = (a0 % 10) * 10000
result = result + ((a0 // 10) % 10) * 1000
result = result + ((a0 //100) % 10) * 100
result = result + ((a0 //1000) % 10) * 10
result = result + ((a0 //10000) % 10) * 1




############################################################################
# str_numbers = input("Input anything separated by comma: ")
# str_numbers = str_numbers.split(",")
# print(str_numbers)


# # 1st method
# numbers = [int(str_number) for str_number in str_numbers]
# print(numbers)

# # 2nd method
# numbers = map(int, str_numbers)
# # print(list(numbers))

# print(set(list(numbers)))

########################################################################################

nestedlist = [
    [1,2,3],
    [3,4,5],
    [1,2,3]
]
nestedlist = [ tuple(item) for item in nestedlist]
print(set(nestedlist))

