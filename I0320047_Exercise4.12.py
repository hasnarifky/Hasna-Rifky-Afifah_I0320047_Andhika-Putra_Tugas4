#!/usr/bin/python

a = 60 #60 = 0011 1100
b = 13 #13 = 0000 1101
c = 0

c = a & b
print("Line 1 - Value of c is ", c)

c = a | b
print("Line 2 - Value of c is ", c)

c = a ^ b
print("Line 3 - Value of c is ", c)

c = ~a
print("Line 4 - Value of c is ", c)

c = a << 2
print("Line 5 - Value of c is ", c)

c = a >> 2
print("line 6 - Value of c is ", c)
