# more in-class coding from November 2

first_list = [1, 2, 3, 4]
second_list = ["a", "b", "c", "d"]

x = zip(first_list, second_list) # creates an internal data structure
print(x)
y = dict(x)

print(y)

alpha = dict(zip(second_list, first_list))
print(alpha)

#what if the lists are different length?
third_list = [1,2,3]
x = zip(third_list, second_list)
y = dict(x)
print(y)

print(dict(zip(second_list, third_list)))