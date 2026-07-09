"""The same teacher of the last challenge wants to sort
the order of work presentation of the students. 
Create a program that reads the name of the four students
and shows the chosen order"""

import random

students = []

while True:
    add = str(input("Type the name of the student to be addeed or type 0 to continue "))

    if add == "0":
        break
    else:
        students.append(add)

random.shuffle(students)
print(f"The chosen order to the work presentation is: {students}")