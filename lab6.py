
# def primeFactor(number):
   
#     # to store prime divisors
#     factor = [] 

#     # this prime will be used to be divided with the number input by user
#     prime = [2,3,5,7,11] 

#     # represent index of prime number 
#     i = 0

#     while number != 1 and i < len(prime):
#         if number % prime[i] == 0:
#             factor.append(prime[i])
#             number //= prime[i]
#         else:
#             i +=1


#     return factor


# # example usage

# number = int(input("Enter a number:"))
# result = primeFactor(number)

# for factor in result:
#     print(factor)    

# # number = int(input("Enter a number:"))

# # factors = []
# # prime = [2, 3, 5, 7, 11]
# # i = 0
# # while number != 1:
# #   #for divisor in range(2,number):
# #     if number % prime[i] == 0:
# #       factors.append(prime[i])
# #       number //= prime[i]
# #     else:
# #        i +=1

# # for integer in factors:
# #    print(integer)


# def Divisor(number):

#     divisors = []

#     for divisor in range(1, number):
#         if number % divisor == 0:
#             divisors.append(divisor)

#     return divisors

# # example usage

# number = int(input("Number:"))
# result = Divisor(number)

# print("The proper divisors:", end=" ")
# for integer in result:
#     print(integer, end=" ")

# number = int(input("Number:"))

# # utk store divisors
# divisors = []


# for divisor in range(1, number):
#     if number % divisor == 0:
#         divisors.append(divisor)

# print(divisors)

def PerfectNumbers(start, end):

    perfects = []

    for i in range(start, end):
    #while start >=  end:
        divisors = []
        for divisor in range(1, i):
          if i % divisor == 0:
            divisors.append(divisor)
        
        sum = 0
        for integer in divisors:
          sum = sum + integer
      
        if sum == i:
          perfects.append(i)

        i +=1

    return perfects


# example usage

start = 2
end = 9000
result = PerfectNumbers(start, end)

for j in result:
   print(j)

