import random
import string

#list of random words we will select when the game starts
words = ["quit", "hunger", "sleep", "deprivation",
         "procrastination", "planning", "computer"]

#returns a random word from a list
def getRandWord(list):
    word = random.choice(list)
    return word.upper()

#display guessed letters
def displayStatus(guessed, tries):
    print(f"\nYou have {tries} lives and you've guessed: {' '.join(guessed)}") #format set of guessed chars

#display current word
def displayCurrentWord(guessed, word):
        currentWord = [letter if letter in guessed else '_' for letter in word]
        print(f"Current word: {' '.join(currentWord)}")

def startHangman():
    lives = 7 #user will have 7 lives to before hanged man
    randWord = getRandWord(words)  # tracks selected random word
    randLetters = set(randWord)  # tracks set of letters in our random word
    validChars = set(string.ascii_uppercase)  # list of valid uppercase characters'
    guessedLetters = set()  # empty set to track what the user has guessed


    #while the length of randLetters # of lives is not zero let user guess
    while len(randLetters) > 0 and lives > 0:

        displayStatus(guessedLetters, lives)
        displayCurrentWord(guessedLetters, randWord)

        #prompt userInput
        userInput = input("\nGuess a letter>> ").upper()

        #if userInput is a valid character that hasnt been guessed yet
        if userInput in validChars - guessedLetters:
            guessedLetters.add(userInput) #add it to our guessedLetters

            #&if userInput is in our random set of letters then remove it
            if userInput in randLetters: 
                randLetters.remove(userInput) 
            #else user loses a life
            else:
                lives -= 1 
                print(f"\n '{userInput}' is NOT in the word.")

        #else if userinput has already been guessed inform user
        elif userInput in guessedLetters:
            print(f"\nOOP! You've already guessed '{userInput}'. Please try again.")

        #anything else is invalid
        else:
            print(f"'{userInput}' is an INVALID character. Try again.")

    if lives == 0:
        print(f"\nEEK! You died! The word was {randWord}. Better luck next time.")
        
    else:
        print(f"\nWINNER WINNER!!! You guessed the word {randWord}")




if __name__ == '__main__':
    startHangman()
