
string_1 = "University of Maryland Baltimore County"
list_1 = list(string_1)
print(id(string_1),"\n", id(list_1))
#print the string and the list to show what we're starting with
print(string_1)
print(list_1)

#for i in range(0, len(list_1)):
#    print(string_1[i], ":", list_1[i])

#where strings and lists are different
list_1[10] = "Q"
#string_1[10] = "Q" - not permitted in Python

string_1 = "UMBC"
print(id(string_1),"\n", id(list_1))
print(list_1)



