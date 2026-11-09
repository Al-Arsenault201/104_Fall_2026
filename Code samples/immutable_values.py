# python calls by value for int, float, boolean and string

# remember that the built-in function id() returns the address in memory of that variable

def cut_in_half(n):
    n = n/2
    print(id(n))
    return(n)

if __name__ == "__main__":
    num = int(input("enter a number"))
    print(id(num))
    new_num = cut_in_half(num)
    print(id(new_num))
    print (new_num)
