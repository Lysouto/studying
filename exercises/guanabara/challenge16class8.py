"""Create a program that reads 
any Real number and shows its integer part."""

from math import trunc



real_num = float(input("Type a real number: "))
integer = trunc(real_num)
print(f"The integer part of {real_num}, is {integer}")