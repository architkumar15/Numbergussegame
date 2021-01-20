
#In this practice i'm try to make number guess game for two players where both player have there own random number which is generated with help of ramdom mudule

import random
def guessgame(a, b, actual):
    #this fucntion as from user for a limit end check is guess numberis euqal to actual number or not
    guess = int(input(f"Guess a number between {a} and {b}\n"))
    numguess = 1
    while guess != actual:
        if guess < actual:
            guess = int(input(f"Enter a bigger number\n"))
            numguess += 1
        else:
            guess = int(input(f"Enter a smaller number\n"))
            numguess += 1

    print(f"You guessed the number in {numguess} guesses\n")
    return numguess


if __name__ == "__main__":
    print("*******welcome To Number guess game*******" )
    a = int(input("Enter the value of a to set lower limit:\n"))
    b = int(input("Enter the value of b to set upper limit:\n"))
if a<b :
    actual1 = random.randint(a, b)
    print("Player 1's turn\n")
    g1 = guessgame(a, b, actual1)
    print("Player 2's turn\n")
    actual2 = random.randint(a, b)
    g2 = guessgame(a, b, actual2)

    if g1 < g2:
        print("Player 1 won the match congratulation!\n")

    elif g1 > g2:
        print("Player 2 won the match congratulation!\n")

    else:
        print("Its a Tie!  Try again\n")

    print(f"The number for player 1 was {actual1} and for player 2 was {actual2}. Thanks for your time")
else:
    print("plese enter lower limite less then upper limit.")

