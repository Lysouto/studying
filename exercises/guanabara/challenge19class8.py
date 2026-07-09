"""A teacher wants to sort one of his 4 students to erase
the blackboard. Create a program that helps him reading 
the students names and showing the name of the chosen one 
(anakin skywalker btw)
 """

import random 

students = []

while True:
    add = str(input("Type the name of the student to be addeed or type 0 to continue "))

    if add == "0":
        break
    else:
        students.append(add)


chosen = random.choice(students)
print(f"The chosen student is {chosen} ")