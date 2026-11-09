# some clarification of Part 4, CW3

# what's the problem? Determine if a number (integer) is prime

# it's prime IF: the only numbers that divide it evenly are itself and 1
# key: if it's not prime, it must have a factor between 2 and its square root.

# start by assuming the number is prime
is_prime = True
import math

num = int(input("Please enter a positive integer"))

for i in range(2,int(math.sqrt(num))):
    if num%i == 0:
        is_prime = False
        print(i, "is a factor of:", num)
    print("this is the end of the if statement for ", i)

print("This is the end of the program")





    
    
