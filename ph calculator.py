#this code is to calculate the ph values of a solution
import math 
C = float(input("Enter the concentration of hydrogen ions: "))
PH = math.log10(C)
if (PH < 7):
    print("The solution is  acidic")
else:
    print("The solution is basic")
if (PH == 7):
    print("The solution is neutral")
