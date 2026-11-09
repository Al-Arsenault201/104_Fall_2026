# in class coding for Wednesday, September 23

# main thing to take from this class: write a little, test a little

# break  up code into pieces that can be tested and reused

# in Python that's called "functions"

"""
pseudocode: write a Python program that asks the user to enter their
last name, their GPA, and their year - 1 for Freshman, 2 for Sophomore, etc.
Then add 0.25 to their GPA and add 1 to their year.
Then print out the new data.
"""

"""
write code to get the data
"""
def print_data( name, newGPA, newYear):
    """
    comment block
    """
    print("Here are the result of our program", end=":")
    print("for your data:")
    print("name is:", name, "your new GPA is:", newGPA, end=";")
    print("and your new class year is:", newYear)
                

def get_values():
    """
    This function asks the user for specific values and returns them
    to the main program.
    parameters: none
    returns: name, GPA, year
    """

    name = input("Please enter your last name")
    GPA = float(input("Please enter your current GPA"))
    year = int(input("Please enter your current class year; 1 for Freshman"))

    return name, GPA, year

def process_data(gpa,yr ):
    """
    this function processes data
    parameters:
    returns
    """
    gpa += 0.25  # add 0.25 to your GPA
    yr += 1 # add 1 year to your class

    return gpa, yr


    

"""
We need a main program
"""

if __name__ == "__main__":

    # please don't use 'def main():'

    print("This is the first thing that gets executed")
    n, g, y = get_values()
    # print("n", n, "g", g, "y", y)
    # call the process_data function
    g, y = process_data(g, y)
    # print("new g", g, "new y", y)
    print_data(n, g, y)
    
    
    
    
