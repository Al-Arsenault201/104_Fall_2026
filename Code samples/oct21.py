# in - class coding from Wednesday, 21 October

def add_numbers(number):
    number = number + 1
    print(id(number))


def add_to_list(l):
    for num in range(0,len(l)):
        l[num] = l[num] + 1
    print(id(l))

if __name__ == '__main__':
    x = 1
    print(id(x))
    add_numbers(x)
    print(x)

    list_1 = [1, 2, 3]
    print(id(list_1))
    add_to_list(list_1)
    print(list_1)

