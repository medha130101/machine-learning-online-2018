# How to import a Module ?
# Method - 1 import calculator # calculator -> Module 1
# Method -2 from calculator import add
# Method 3
from calculator import *

print(globals()) # View Import(s)
print(add(10,11)) # For Method -2
print(sub(20, 10))
print(mul(2, 3))
print(div(1, 2))


# Do not work for Method - 3
print(calculator.add(1, 2)) #SUccess
print(calculator.sub(1, 2)) #SUccess
print(calculator.mul(1, 2)) #SUccess
print(calculator.div(1, 2)) #SUccess


print(type(calculator)) # For Method -2 ; ' calculator ' Not Defined -> Error

 # print( add (1, 2)) # ERROR
