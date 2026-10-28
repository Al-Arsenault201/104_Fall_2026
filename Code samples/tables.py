medal_table = [
   ["United States",10,5,5],
   ["Kenya",7,2,2],
   ["Canada",3,1,1],
   ["Netherlands",2,2,2],
   ["Botswana",2,2,2]
    ]

#print(medal_table)

# a row of the table
print(medal_table[0])

# an individual element
print(medal_table[0][0])

for entry in medal_table:
    print(entry[0])


# do this with a for i loop:
for i in range(0,len(medal_table)):
    print(medal_table[i][0])

"""

for item in medal_table[0]:
    print(item)
"""

# adding a new row
medal_table.append(["Spain", 2, 0, 1])
print(medal_table)

# add a new element in each row - the total - the sum of gold, silver, bronze

for i in range(0,len(medal_table)):
    medal_table[i].append(medal_table[i][1]+medal_table[i][2]+medal_table[i][3])
    print(medal_table[i])