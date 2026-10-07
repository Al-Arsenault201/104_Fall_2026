try:
    x = int(input("Please enter a number: "))
    #break
except ValueError:
    print("Oops!  That was no valid number.  Try again...")

# error checking. The program does not crash; the user gets an
# error message and can try to do better

try:
    x = int(input("Please enter a number: "))
    y = "UMBC"
    print(x + y + x)

except ValueError:
   print("Oops!  That was no valid number.  Try again...")
except TypeError:
   print("Oops!  That was a list; not a valid number.  Try again...")

