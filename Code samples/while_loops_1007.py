# more coding from October 7 - use of the while loop

# if you don't know how many times the loop should run:

# ask the user to enter a number between 1 and 10:

num = int(input("Please enter a number between 1 and 10"))

# how do we know the user did it right?
valid = False
while not valid:  # this is equivalent to while valid == False
    if num<1 or num >10:
        print("Sorry, I was serious about that.")
        num = int(input("Please enter a number between 1 and 10"))
    else:
        valid = True

print("The number you entered was :", num)


    
