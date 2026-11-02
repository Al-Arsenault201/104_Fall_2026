# in-class coding from Monday, November 2

dogs = ["doug",["beagle","bulldog"],"lizzie","ACD", "penny","spaniel"]
# even-numbered elements are all dog names; odd-numbered elements are all dog breeds
# count 0 as "even"

#but this would get awkward - to print out a dog and breed
"""
name = dogs[i] # where i is some even number
breed = dogs [i+1] 
print(name, breed) # I could make this work
"""
#dictionary
dogs = {
    "doug":["Beagle","bulldog"],
    "lizzie":["ACD"],
    "penny":["spaniel"]
}

# to print all dogs:
for dog in dogs.keys():
    print(dog, dogs[dog])

print(dogs.get("penny"))
print(dogs.get("wesley"))

"""
if dogs.get("wesley") == None:
    print("wesley is not in the database")
"""

print(dogs.get("wesley", "wesley is not in the database"))

dogs["cinder"] = ["doberman"]
print(dogs)
del dogs["cinder"]
print(dogs)

if "lady" in dogs.keys():

    del dogs["lady"]
print(dogs)

