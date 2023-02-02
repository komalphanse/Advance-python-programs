print("python import statement")
import math
print("the value of eulers number is",math.e)

print("python from...import statement")
from math import e
print("the value of eulers number is",e)

print("importing and also renaming")
import math as mt
print("the value of eulers number is",mt.e)

print("from math import e,tau")
from math import e,tau
print("the value of tau constant is",tau)
print("the value of eulers number is",e)

print("import all files using 'from import* statement")
from math import*
print("calculating square root:",sqrt(25))
print("calculating tangent of an angle:",tan(pi/6))

print("location of module")
import sys
print(sys.path)
print("list of function:\n",dir(str))

