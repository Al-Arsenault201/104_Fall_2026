# print statements

#print some literals

print("Hello, world")

print(42)

print(1/3)

# print variables

x = 4

print(x)

# print multiple items in a single print statement

print("The answer to life the universe and everything is",       42)

print("The answer to life the universe and everything is"+"42")


#print a bunch of blank spaces
print("These are", "       ", "blank spaces")


#input statements

"""
Whenever you're told to 'prompt' the user for something
that means you should use an input statement
"""

# first thing: the prompt - the string in the input statement
# can only be a single string

lastname = input("please enter your last name")

print ("The user said", lastname)

"""
this will not work
firstname = input("please enter", "your", "first name")
print ("The user said ", firstname)
"""

# to make it work right
firstname = input("Please enter your first name  ")
print ("The user said ", firstname)


# using a variable in an input statement
prompt = "Please enter the value I asked for, darn it"
answer = input(prompt)

"""
this will fail
new_prompt = 65
newanswer = input(new_prompt)
"""


