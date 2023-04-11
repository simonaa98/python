import random
def hangman():

    list_of_words = ["shadow", "duty", "improvement", "betray", "chorus", "licence", "timber", "terrace", "grass", "couple",
                 "pneumonia", "wrong", "mobile", "push", "consideration", "bulletin", "snuggle", "embark",
                 "association", "software", "fountain", "width", "install", "access", "expression"] # list of possible words, gotten from a random word generator

    word = list_of_words[random.randrange(0, 24)] # picks a random word from the list
    # print(word) # reveals the word for testing
    print("Your word is", len(word), "letters long... start guessing and good luck")
    lives = 10
    guessed_wrong = []
    lines = "_" * len(word)

    while True: # will go forever as is always true, only stops when hitting an (exit) end point
        print(lines)
        print("Lives:", lives-len(guessed_wrong)) # you lose a life when you guess wrong (lose condition)
        guess = input("Guess a letter: ")
        if guess not in word: # appends wrong guesses to the list of wrong letters
            guessed_wrong.append(guess)

        print("wrong letters:", guessed_wrong) # display the wrong letters so user know and wont guess the same letter

        for i in range(len(word)): # adds the letter from the guess to the lined displayed to the user
            if guess in word[i]:
                lines = lines[:i] + word[i] + lines[i+1:]

        if len(guessed_wrong) == lives: # if wrong guess list is the same lenght as the lives variable you get a lifeline
            print("You get one finally guess, what is the word?")
            lifeline = input("Will you save your life with this guess? ")
            if lifeline == word: # if you get it right you win and can play again y/n
                print("You did it! The word was:", word, "...and you got it right saving your life!")
                play_again = input("Do you fancy your chances again? (y/n)")
                if play_again == "y":
                    hangman()
                else:
                    print("Good choice, see you later...")
                    exit()
            else: # or you fail and lose, play again y/n
                print("- - - The word was:", word, "- - - - - - \n- - - You lose and the hangman awaits... - - -")
                play_again = input("Do you fancy your chances again? (y/n)")
                if play_again == "y":
                    hangman()
                else:
                    print("I wouldnt want to lose again either...")
                    exit()

        if "_" not in lines: # if there is no more lines you also win, can play again
            print("- - - The word was:", word, "- - - - - - \n- - - You were spared...This time - - -")
            repeat = input("Do you fancy your chances again? (y/n)").lower()
            if repeat == "y":
                hangman()
            else:
                print("See you later...")
                exit()

hangman()