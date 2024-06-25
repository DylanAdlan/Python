# CHAPTER LOOPING

a = int(input())
b = int(input())

prime = []

for i in range(a, b+1):
  if i > 1:
    isPrime = True
    divisors = range(2, i)
    for divisor in divisors:
        if(i % divisor == 0):
            isPrime = False
            break
    
    if(isPrime == True):
        prime.append(i)

for i in prime:
  print(i, end=" ")