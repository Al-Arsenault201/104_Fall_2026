# how not to cover multiple cases

# this will actually work, but it's inefficient and ugly

score = int(input("Please enter the student's score"))
if score > 90:
    print("The student got an A")
    grade = "A"
if score < 90 and score >= 80:
    print("The student got a B")
    grade = "B"
if score < 80 and score >= 70:
    print("The student got a C")
    grade = "C"
if score < 70 and score >= 60:
    print("The student got a D")
    grade = "D"
if score < 60:
    print("The student got an F")
    grade = "F"

    
