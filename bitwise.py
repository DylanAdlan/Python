print("How to represent binary number in python")

# CAN USE 0b and follwed by binary number
# however when print out,it's in their decimal number
# by adding 0b, python read it as one one one 
# instead of one hundred and eleven
ownerpermission = 0b111 #ob represent whatever number come after him as "BINARY" number
print(ownerpermission) # print execute it's decimal number

#-------------------------------------------------------------------------------------------------------

filepermission = 0b111101001 
# now owner can read, write and execute
# group can read and execute
# others can execute only

#---------------------------------------------------------------------------------------------------------

# in data science/machine learning where you were given 
# categorical data you must convert them into binary numbers
# which machine can understand which only (0,1)
# this itself called "feature engineering"
# example for gender representation (01 | female), (10 | male)
# example race representation (1000 | malay) (0100 | chinese)

# this bit extraction can be use using bitwise and operator
mask = 0b000111000
print((filepermission & mask) >> 3)
# shift = used for extract the certain bits

# in order to perform bit extraction we can use bitwise & operator
# original data              111101001  (& operator) BITWISE AND
# our mask                   000111000
# 4, 5, 6 bits extracted     000101000  (result)
# shift to the right 3 times 000000101   >> 3

# in order to set or modify certain bit to certain bit using bitwise | operator
# original data              111101001   ( | operator) BITWISE OR
# our mask                   000111000
# 4, 5, 6 bit extracted      111111001
print(bin(filepermission | mask))
# the or operator is used to set a specific bit to 1
# please remember there is no way to set a specific bit to 0 using | operator
# | operator also used in extracting region of interest in an image

# original data              111101001   ( ^ operator) BITWISE XOR
# our mask                   000111000
# 4, 5, 6 bit extracted      111010001
# xor used for encryption


# xor used for encryption
message = 0b01001010 #for my content "J"
key = 0b00101100 # encryption key (,)
encrypted_message = message ^ key
print(bin(encrypted_message))
# original data              01001010   ( ^ operator) XOR
# key                        00101100
# encrypted message          01100110

decrypted_message = encrypted_message ^ key
print(bin(decrypted_message))
# encrypted message          01100110 ( ^ operator) XOR
# key                        00101100
# decrypted message          01001010

# 1S COMPLEMENT
givennumber = 5
# 5                 0101
# 1s complement     1010
# 2s complement     1s complement + 1  # for (-ve number)
print(~givennumber + 1) # ~ for 1s complement
print(-givennumber)     # 2s complement # - unary negative
print(+givennumber)     # + unary positive

#0,1,2,3,4,5,6,7,8,9, A,B,C,D,E,F
#
# 0x represent hexadecimal


hexadecimalnumber = 0xF
print(hexadecimalnumber)
print(hex(hexadecimalnumber))

#0,1,2,3,4,5,6,7,  10,11, 12, 13, 14, 15, 16, 17
#0,1,2,3,4,5,6,7,   8, 9, 10, 14, 15
octalnumber = 0o10
print(octalnumber)
print(oct(octalnumber))







