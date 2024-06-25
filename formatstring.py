name = "David"
batch = 101
fee = 1245.6578

# traditionally how we do this
inputstring = "Hello " + name + ", welcome to python class " + str(batch)
print(inputstring)

# special string called f string
inputstring = f"Hello {name}, welcome to python class {batch}"
print(inputstring)

# putting space by 40
inputstring = f"Hello {name:40s}, welcome to python class {batch}"
print(inputstring)

#align David to the center
inputstring = f"Hello {name:^40s}, welcome to python class {batch}"
print(inputstring)

# align David to the right
inputstring = f"Hello {name:>40s}, welcome to python class {batch}"
print(inputstring)

# you also can provide padding characters
inputstring = f"Hello {name:*>40s}, welcome to python class {batch}"
print(inputstring)

# trucate to 3 characters (take only 3 character infront)
inputstring = f"Hello {name:.3}, welcome to python class {batch}"
print(inputstring)

# let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:10d} in KL"
print(inputstring)


inputstring = f"Hello {name:.3}, welcome to python class {batch:<10d} in KL for RM{fee:10.2f}"
print(inputstring)


#convert decimal to octal
inputstring = f"Hello {name:.3}, welcome to python class {batch:o} in KL for RM{fee:10.2f}"
print(inputstring)

#convert decimal to hexa
inputstring = f"Hello {name:.3}, welcome to python class {batch:x} in KL for RM{fee:10.2f}"
print(inputstring)

inputstring = f"Hello {name:.3}, welcome to python class {batch:x} in KL for RM{fee:,.2f}"
print(inputstring)