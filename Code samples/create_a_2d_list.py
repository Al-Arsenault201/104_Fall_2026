

# create a new 1-d list
new_row = []
for i in range(1,11):
    new_row.append(i)

print(new_row)
sixth_row = []
for i in range(51,61):
    sixth_row.append(i)
print(sixth_row)

# create an empty 2-d list
two_d_list = []

for j in range(1,11):
    row_to_append = []   # this will be a new row that I will append to two_d_list when it's ready
    for i in range(1,11):
        row_to_append.append(10 * (j-1) + i)
    two_d_list.append(row_to_append)

    
print(two_d_list)
