#age = int(input("please enter your age in years"))

age = input("please enter your age in years:" )

# a method to check whether the user entered a number

if age.isdigit():
    age = int(age)
    if age >= 18:
       print("Please vote; it's so important")
    else:
       print("You can still get involved")

else:
    print("We're sorry; you did not enter a number")

    
