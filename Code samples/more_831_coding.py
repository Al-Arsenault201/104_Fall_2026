# additional code from 8/31 class

# a simple program

"""
num = input("Please enter a number")
print(int(num))
num = input("Please enter a number")
print(int(num))
num = input("Please enter a number")
print(int(num))
"""

# but that's somewhat awkward

# a for loop does something multiple times

# the syntax of the range is: start, stop, step
# start is the value assigned to i the first time through the loop
# step is how much you increment i each time
# stop is the first value where you DO NOT run when you encounter that
# when i gets to 10 the loop DOES NOT execute

for i in range(0,10,1):
    num = input("Please enter a number")
    print(i, "=", int(num))

    

