# in-class coding for 16 September

# determine if a number is prime

# pseudocode:
# start by seeing if that number, num, is evenly divisible by another number,y
# we can tell that using % modulus operator

# if num%y == 0  then y evenly divides num
is_prime = True
num = 8
y = 3
"""
if num%y == 0:
    print("num is not prime because it's divisible by y")
else:
    print("It might be divisible")
"""
if num%y == 0:
    is_prime = False
    print("We changed is_prime")

print("The if-else is over")
