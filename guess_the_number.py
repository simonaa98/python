import random

def guess_number():

    max_guess = 100
    attempt = 1

    correct = random.randrange(0, max_guess) # creates the random number the user guess
    # print(correct) # prints answer for testing
    print("Guess the number to win! The number is between 0 and", max_guess)
    user_input = int(input("Your guess: "))

    while user_input != correct: # closes when correct and the users guess is the same
        if user_input > correct: # checks if user guess is higher or lower than the number
            print("Lower")
        else:
            print("Higher")
        user_input = int(input("Your guess: "))
        attempt = attempt + 1

    print("You guessed the number! You used", attempt, "attempts to guess it!") # end of game chance of repeat
    repeat = input("Want to play again? (y/n)").lower()
    if repeat == "y":
        guess_number()
    else:
        print("Okay see you later!")


guess_number()