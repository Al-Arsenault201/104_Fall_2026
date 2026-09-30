###############################


# Name:  (insert your name here)


def print_welcome():
    print("Welcome, user. You enter your height in centimeters and your weight in kilograms")
    print("and we will calculate your Body Mass Index - your BMI")


def get_input(value):
    def convert_units(t, v):

    # write an if/else statement based on the value of t
    # if t == "h" calculate the user's height in meters as v/39.37
    # else calculate the user's weight in kilograms as v/2.2
    # return the calculated value, either height or weight

    if value == "height":
        ft = int(input("Please enter your height in feet and inches. First, how many feet tall are you?"))
    inch = ???
    h = 12 * ft + inch
    answer = convert
    units("h", h)
    print("You are: ", answer, " meters tall, for future reference")
    return ???
    elif value == "weight":
    lbs = int(input("Please enter your weight in pounds. Use whole pounds only; do not include ounces"))
    answer = convert_units("w", ???)
    print("You weigh: ", answer, " kilograms, for your future reference")
    return ???

    def calc_bmi(height, weight):
        bmi = ???
        return bmi

    def print_output(ans):
        print
        {"Your BMI is: ", ans}
        """
        Now, write an if-elif-else statement that prints the appropriate message:
        - if the user's BMI is under below 18.5, tell the user that they are underweight
        - else if the user's BMI is between 18.5 and 24.9, inclusive, tell the user that they are maintaining a healthy weight
        - else if the user's BMI is greater than 24.9 but less than or equal to 29.9, tell the user that they are considered to be overweight
        - else tell the user that they are considered to be obese
        """

    if __name__ == "__main__":
        print_welcome()
        meters = get_input("height")
        kg = get_input("weight")
        bmi = calc_bmi(???)
        print_output(???)

