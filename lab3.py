""""
# QUESTION 1
# 1.Calculate volume A and B for salts
final_concentration = int(input("Enter final concentration(%):"))
final_volume = int(input("Enter final volume (liter):"))
concentration_a = int(input("Enter concentration of solution A(%):"))
concentration_b = int(input("Enter concentration of solution B(%):"))

volume_b = int(((final_concentration * final_volume) - (concentration_a * final_volume))/ (concentration_b - concentration_a))
volume_a = int(final_volume - volume_b)

remain_a = int(volume_a - 3)
remain_b = int(volume_b - 3)

print(f"Volume of Solution A: {volume_a} liter")
print("Solution(A) is available can proceed") if(volume_a <= 3) else print(f"Solution(A) is not available, please order {remain_a} liter now")
print(f"Volume of Solution B: {volume_b} liter")
print("Solution(B) is available can proceed") if(volume_b <= 3) else print(f"Solution(B) is not available, please order {remain_b} liter now")


# QUESTION 2
#1) Extract lower 4 bits from x
x = 0b10101100
mask = 0b00001111
#print(x)
print(bin(x & mask))


# 2) check if y is even or odd number
y = 0b11011001
print("y:", y)
print("y is even number") if(y % 2 == 0) else print("y is odd number")

# 3) clear the upper 4 bits of x
x = 0b10101100
mask = 0b00001111
print(bin(x & mask))

# 4)check if 5th bit of y is set
y = 0b11011001
mask = 0b00010000

result = (y & mask)>>4

print("5th bit is a set") if(result == 1) else print("5th bit is not a set")

# QUESTION 3
A = int(input("Enter working time for first worker (hour):"))
B = int(input("Enter working time for second worker (hour):"))

work_rate_a = 1/ A
work_rate_b = 1/ B

total_work_rate = work_rate_a + work_rate_b

total_time_complete = 1/ total_work_rate

print(f"Total time for both worker to complete the project is {total_time_complete:.2f}")

# QUESTION 4
# 1. Set the lower 4 bits of a
a = 0b10101000
mask = 0b00001111

result = a | mask
print("Set lower 4 bits:", bin(result))

# 2. combine bits a and b using OR

a = 0b10101000
b = 0b01010100

result = a | b
print("Combination bits a and b", bin(result))

# 3. Create a mask to set 2nd and 6th bit of a
a = 0b10101000
mask = 0b00100010

result = a | mask
print("Set the 2nd and 6th bit of a: ", bin(result))

# QUESTION 5
totalAmount = int(input("Enter total amount(RM):"))
interest_rate_acc_1 = float(input("Enter annual interest rate for first account(%):"))
interest_rate_acc_2 = float(input("Enter annual interest rate for second account(%):"))
totalInterestrate = float(input("Enter total annual interest rate (RM):"))

# convert whole number to decimal
interest_rate_acc_1 = interest_rate_acc_1 / 100
interest_rate_acc_2 = interest_rate_acc_2 / 100

#totalInterestrate = (interest_rate_acc_1 * (totalAmount - account2)) + (interest_rate_acc_2 * account2)
#totalInterestrate = (interest_rate_acc_1 * totalAmount) - (interest_rate_acc_1 * account2) + (interest_rate_acc_2 * account2)
#totalInterestrate = (interest_rate_acc_1 * totalAmount) + (interest_rate_acc_2 * account2) - (interest_rate_acc_1 * account2)
#totalInterestrate - (interest_rate_acc_1 * totalAmount) = account2(interest_rate_acc_2 - interest_rate_acc_1)
account2 = (totalInterestrate - (interest_rate_acc_1 * totalAmount)) / (interest_rate_acc_2 - interest_rate_acc_1)
account1 = totalAmount - account2

print(f"Amount for first account: RM{account1:.2f}")
print(f"Amount for second account: RM{account2:.2f}")

"""
# QUESTION6
# 1. swap value between x and y without using temporary variable

x = 0b10101100
y = 0b11010010

x = x ^ y
y = x ^ y
x = x ^ y

print("New value for x:", bin(x))
print("New value for y:", bin(y))

# 2. toggle the third and fifth bit of x using XOR

x = 0b10101100
mask = 0b00010100

result = x^mask
print(bin(result))

# 3. check if value a = 29 and b = 15 is different (XOR)
a = 29
print(bin(a))

b = 15
print(bin(b))

result = a ^ b
print(bin(result))

print(f"The value of {a} and {b} is different == True") if(result !=0) else print(f"The value {a} and {b} is identical")
