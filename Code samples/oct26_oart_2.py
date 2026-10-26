# fun with strings

string_1 = "University of Maryland Baltimore County"

#case of a string
print(string_1.upper())
print(string_1.lower())
print(string_1.title())

#create a list of the words in the string using split function
wordlist = string_1.split()
print(wordlist)
wordlist[3] = "Garrett"
print(wordlist)

# the opposite of split is join
# join takes a list of strings and creates a string

newstring = " ".join(wordlist) # one blank space between words
print(newstring)
newerstring = "++".join(wordlist)
print(newerstring)

#.join with a list of integers fails
"""
l = [1,2,3]
s = " ".join(l)
print(s)
"""

#split can split the string on any character
list_2 = string_1.split("r")
print(list_2)

# strip - get rid of blank spaces at the beginning and/or end - not in the middle
# strip - gets rid of leading and trailing spaces
# lstrip - gets rid of leading spaces; leaves trailing spaces
# rstrip - leaves leading spaces; gets rid of trailing spaces

name = "     Arsenault    "
print(name)
if name == "Arsenault":
    print(name)
else:
    print("you messed up")

# getting rid of all blank spaces
print(name.strip()+"end")
print(name.lstrip()+"end")
print(name.rstrip()+"end")

othername = "Ars     enau   lt"
print(othername.strip())

#substring
print(string_1)

#to take a substring
state = string_1[14:22]
print(state)

#concatenation - uses +
s1 = "UM"
s2 = "BC"
s3 = s1 + s2
print(s3)

# "multiplication"
s4 = "UMBC"
s5 = 3*s4
print(s5)

print(string_1)
string_42 = string_1.replace("r","::::")
print(string_42)




