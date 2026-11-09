#november 9 coding

with open("/Users/alfredarsenault/nov_9/data.txt", "w") as outfile:
    outfile.write("this is the first line of our file \n")
    outfile.write("this is the second line with no newline")
    outfile.write("this is the rest of the second line \n")
    outfile.write("this is the third line \n")

#with open("/Users/alfredarsenault/nov_9/data.txt", "w") as another_outfile:

with open("/Users/alfredarsenault/nov_9/data.txt", "a") as yet_another_outfile:
    yet_another_outfile.write("this is the fourth line of our file \n")
    yet_another_outfile.write("this is the fifth line of our file \n")
    yet_another_outfile.write("this is the sixth line \n")

with open("/Users/alfredarsenault/nov_9/lists.txt", "a") as outfile:
    l = ["apple", "banana", "cherry"]
    for i in range(len(l)):
        l[i] = l[i]+"\n"
    outfile.writelines(l)   #no newlines

print("the program is finished") #print to the screen

