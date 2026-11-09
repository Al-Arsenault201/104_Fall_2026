# in-class coding from Wednesday, October 7

# an illustration of how the function I gave yu in project 2 works
from random import randint

def break_out_numbers(num):
   n6 = num % 10
   n5 = (num // 10) % 10
   n4 = (num // 100) % 10
   n3 = (num // 1000) % 10
   n2 = (num // 10000) % 10
   n1 = (num // 100000) % 10
   return n1, n2, n3, n4, n5, n6

if __name__ == "__main__":
    n = randint(100000, 999999)
    print(n)
    #print(break_out_numbers(n))
    # for more detail:
    d1, d2, d3, d4, d5, d6 = break_out_numbers(n)
    print(d1, d2, d3, d4, d5, d6)

    #get the user's guess and then test each digit
    # give the user up to six guesses



    #I need to give the user up to 6 guesses
    found_answer = False
    guess_number = 1
    while found_answer == False and guess_number < 7: #I could write this as while not found_answer
        guess = int(input("please enter the six digits you're guessing"))
        print(guess)
        print ("Guess number: ", guess_number)
        g1, g2, g3, g4, g5, g6 = break_out_numbers(guess)
        #print(g1, g2, g3, g4, g5, g6)
        #check to see if the guess is right
        if g1 == d1 and g2 == d2 and g3 == d3 and g4 == d4 and g5 == d5 and g6 == d6:
            print("Yay! You guessed correctly!")
            found_answer = True
        else:
            print("Sorry, you didn't guess correctly.")
            guess_number += 1
    if guess_number == 7:  # if found_answer == False
        print("I'm sorry, you didn't guess correctly.")


