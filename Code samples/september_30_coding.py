# in class coding from Wednesday, September 30

score = int(input("Please enter the student's score"))
"""
if score >= 90:
    print("The student gets an A")
    grade = "A"

else:
    print("The student did not get an A")
    grade = "not A"
"""

# elif:  short for 'else if'


if score >= 90:
    print("The student gets an A")
    grade = "A"
elif score >= 80:
    print("The student gets a B")
    grade = "B"
elif score >= 70:
    print("The student gets a C")
    grade = "C"
elif score >= 60:
    print("The student gets a D")
    grade = "D"
else:
    print("The student gets an F")
    grade = "F"

    
print("End of the program")
