# more coding from Monday, September 28

def fourth_root(num):
    ans = num**(1/4)
    return ans
    print("The function has successfully completed") # this was never printed

def sum_some_numbers(n):
    sum = 0
    for i in range(0,100):
        if i >= n:
            return sum
        else:
            sum += i


if __name__ == "__main__":
    """
    n = int(input("Enter a number we'll calculate the fourth root"))
    root = fourth_root(n)
    print("your answer is:", root)
    """

    n = int(input("Give me a number; we'll sum all the integers between 0 and that"))
    answer = sum_some_numbers(n)
    print(answer)
    

    
