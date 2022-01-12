'''
Created on 8 Mar 2021

@author: hsth
'''
  
def squarer(x):
    return x*x

def showString(y):
    print(y)
    
def inputParameters(c,d,e,a=5,b=4):
    return a+b+c+d+e

def divideBy2(i):
    return int(i/2)

def multiplyBy4(j):
    return j*4

def strToFloat(inStr):
    """
    Prints the float of the string input number
    :param inputString, must be a number
    :return float
    """
    try:
        print(float(inStr))
        return(float(inStr))
    except ValueError:
        print("must enter a number as a string, not just any string")
    
def dividerMultiplier(cc):
    """
    Returns (x / y)*c for 2 inputs given.
    :param cc: int.
    :return: int
    """
    try:
        aa = input("type a number:")
        bb = input("type another:")
        aaa = int(aa)
        bbb = int(bb)
        print((aaa / bbb)*cc)
    except(ZeroDivisionError, ValueError):
        print("Invalid input.")
    
print("here is a result: ")
print(squarer(2))

showString("print this line, please ")

print(inputParameters(1,2,3))

initial = divideBy2(8)
print(multiplyBy4(initial))

strToFloat("999")
dividerMultiplier(77)







