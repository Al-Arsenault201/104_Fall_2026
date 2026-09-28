# in class coding from Monday, September 28

def circ_and_area(radius):
    circ = 2 * 3.14159 * radius
    area = 3.14159 * radius**2
    return (circ, area)

def volume(radius):
    print("This function computes the volume of a sphere of radius")
    v = (4/3)*3.14159*radius**3
    return
#    return v

if __name__ == "__main__":
    r = int(input("Please enter the radius of your circle"))
#    c, a = circ_and_area(r)
    circ_and_area(r)
    print ("The program has completed")
    """
    print("Your circle has a circumference of :", c)
    print("Your circle has an area of:", a)
    v = volume(r)
    print("Your sphere has a volume of:", v)
    """

    

    
    
