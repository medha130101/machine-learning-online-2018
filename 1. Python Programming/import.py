# import calculator
# instead use
import calculator as lib

def calculator(a, b):
    print(a, b)

print(lib.add(10, 30)) # Error -> Does not refers to ' calculator ' Module.
