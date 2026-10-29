# in-class coding from Wednesday, October 28

# dictionaries

# a dictionary maps a key to a value

# empty dictionary
dogs = { }
dogs["doug"] = ["beagle","bulldog"]  # adding: key is "doug"  value is the list
print(dogs)

dogs["wesley"] = "german shepherd"
print(dogs)

dogs["bentley"] = ["golden","ACD"]
print(dogs)

dogs["lizzie"] = "ACD"
dogs["baron"] = "beagle"
dogs["cleo"]    = "beagle"

print(dogs)

# each key - must be unique. keys cannot repeat
dogs["baron"] = "spaniel"
print(dogs)

#new dictionary
quarterbacks = {"ravens":"jackson", "browns":"watson", "steelers":"rodgers","bengals":"burrough", "ravens":"huntley"}
print(quarterbacks)

print(dogs.keys()) # give me a list of the keys in dogs

print(dogs.values()) # give me all the values in dogs

if "cinder" in dogs.keys():

    print(dogs["cinder"])
else:
    print("no cinder")

if "beagle" in dogs.values():
    print("you have beagle")
else:
    print("no beagle")

# keys must be unique, and must be immutable
# keys must be boolean, int, float, or string
# no lists or dictionaries as keys

# values can be any type
# values can repeat

# it is trivial to find a value given a key
# it is difficult (almost impossible) to find a key given a value


quarterbacks["bengals"] = "flacco"

# find the team that Joe Flacco plays for
quarterbacks["bengals"] = ["burrough", "flacco"]
#brute force search
if "flacco" in quarterbacks.values():
    for key in quarterbacks.keys():
        if quarterbacks[key] == "flacco":
            print(key, quarterbacks[key])
else:
    print("He's finally out of the game")