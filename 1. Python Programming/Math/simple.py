def add(a , b):
    return a + b
def sub(a, b):
     return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a//b\

print(__name__) # Specifis the file , importing the module
if __name__ == '__main__':
# The piece of code is executed if and only if the command line input is as Math/simple.py 
# The piece is not executed if the command line input is as mainMath.py
        print("Hello I am simple.py")
        # The file works as a 'script' as well as a 'module'
        a  = int(input())
        b  = int(input())
        print(add(a, b))
