#some of the in-class coding from MOnday, October 19

# a new list
l = [ ] # creates a new, empty list
print("empty list", l, id(l))
l.append("milk") # adds "milk" to the end of the list
print(l)
l.append("eggs")
print(l, id(l))
l.insert(1,"fruit")
print(l, id(l))
print(l[0])




non_empty_list = ["milk", "eggs", "fruit", "cereal", "pasta"]
#the above is a non-empty list


counties = ["Allegany", "Anne Arundel","Baltimore", "Baltimore City", "Calvert", "Carroll", "Caroline", "Cecil", "Charles", "Dorchester",
"Frederick", "Garrett", "Harford", "Howard", "Kent", "Montgomery", "Prince George's", "Queen Anne's", "Somerset", "St. Mary's",

"Talbot", "Washington", "Wicomico", "Worcester"]

#check to see if we got them all
print(len(counties))
print(counties[0])
#print(counties[24])

#the last element in the list is always len(list) - 1
#print(counties[23])
print(counties[len(counties)-1])
print(counties[-1])

print(counties[len(counties)-2])
print(counties[-2])

#removing an item from the list - by value
counties.remove("Baltimore")
print(counties)

#counties.remove("Tippecanoe")
if "Tippecanoe" in counties:
    counties.remove("Tippecanoe")
else:
    print("Sorry, you're in the wrong state")

#if you want to remove something by index, use pop
print(counties.pop(1))
print(counties)

# delete a whole bunch of things from the list at once

#del counties[0,5] I owe you the proper syntax on this
print(counties)