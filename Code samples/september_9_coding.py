# in-class coding from Wednesday, September 9 2026

# suppose I want to calculate 5!

factorial = 1

for i in range(1,6,1):
    factorial = factorial * i
    print("i is: ", i, "factorial is: ", factorial)

print(factorial)

#calculate the sum of the first 10 integers

sum = 0
for i in range(11):
    sum = sum + i

# we could have said for i in range (1,11,1):

print (sum)

# syntax: computer scientists are lazy.  Fewer keystrokes is better

# we can use += and *= to shorter our commands
prod = 10
prod *= 3 # the same as prod = prod * 3

s = 5
s += 6  # the same as sum = sum + 6

print("the sum is: ", s, "and the product is: ", prod)

#indenting one space
for i in range(5):
 print(i)
 for j in range(4):
  print(i," and ", j)
  
#floating point arithmetic
s = 0.0
for i in range(10000):
    s += 0.1

print(s)

