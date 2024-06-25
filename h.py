A = int(input("Enter first integer: "))
B = int(input("Enter second integer:"))

print(f"GCD({A},{B}) =>", end=" ")
while A > 0 or B > 0:
    if(A == 0):
        print(B)
        break
    elif(B==0):
        print(A)
        break
    else:
        temp = A % B
        A = B
        B = temp
        print(f"GCD({A},{B}) =>", end=" ")