"""Create a program that reads the size of the opposite and 
the adjacent side of a right triangle, calculates
and shows the size of the hypotenuse."""

import math

opposite_side = float(input("Type the value of the" \
" opposite side: "))
adjacent_side = float(input("Type the value of the " \
"adjacent side: "))

sumofthesquare = math.pow(opposite_side,2) + math.pow(adjacent_side,2)
hypotenuse = math.sqrt(sumofthesquare)

print(f"The hypostenuse of the triangle is {hypotenuse:.2f}.")