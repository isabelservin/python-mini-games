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
def displayStatus(guessed, currLives):
    print(f"\nYou have {currLives} lives and you've guessed: {' '.join(guessed)}") #format set of guessed chars

#display current word
def displayCurrentWord(guessed, word):
        currentWord = [letter if letter in guessed else '_' for letter in word]
        print(f"Current word: {' '.join(currentWord)}")

#start the game
def playHangman(player):
    lives = 6 #user will have 7 lives to before hanged man
    randWord = getRandWord(words)  # tracks selected random word
    randLetters = set(randWord)  # tracks set of letters in our random word
    validChars = set(string.ascii_uppercase)  # list of valid uppercase characters'
    guessedLetters = set()  # empty set to track what the user has guessed

    print(f"\n{player} is now playing Hangman!!!")
    #while the length of randLetters # of lives is not zero let user guess
    while len(randLetters) > 0 and lives > 0:

        #visual status displayed
        displayStatus(guessedLetters, lives)
        print(displayHangman(lives))
        displayCurrentWord(guessedLetters, randWord)

        #prompt userInput
        userInput = input("Guess a letter>> ").upper()

        #if userInput is a valid character that hasnt been guessed yet
        if userInput in validChars - guessedLetters:
            guessedLetters.add(userInput) #add it to our guessedLetters

            #&if userInput is in our random set of letters then remove it
            if userInput in randLetters: 
                randLetters.remove(userInput) 
            #else user loses a life
            else:
                lives -= 1 
                print(f"\n Sorry {player} '{userInput}' is NOT in the word.")

        #else if userinput has already been guessed inform user
        elif userInput in guessedLetters:
            print(f"\nOOP! You've already guessed '{userInput}'. Please try again.")

        #anything else is invalid
        else:
            print(f"'{userInput}' is an INVALID character. Try again.")

    if lives == 0:
        print(displayHangman(lives))
        print(f"\nEEK! {player} died! The word was {randWord}. Better luck next time.")
        
    else:
        print("")
        displayCurrentWord(guessedLetters, randWord )
        print(f"\nWINNER WINNER!!! {player} guessed the word {randWord}!")

#display options menu
def displayOptions(options):
        choiceIndex = 1
        #list each option to our user and number it
        for option in options:
            print(f"{choiceIndex}. {option}")
            choiceIndex+=1

#main menu
def mainMenu():
    #menu options
    PLAY_HANGMAN = "Play Hangman"
    EXIT = "Exit"

    #list of our options
    options = []
    options.append(PLAY_HANGMAN)
    options.append(EXIT)

    #get players name
    player = input("What is your name? ").capitalize()

    choice = "" #tracks users choice
    #while user hasnt selected exit run the program
    while choice != EXIT:
        print(f"\nWelcome to our python mini games {player}!\n****")

        displayOptions(options)
        selectedOption = int(input("How can I help you? "))
        choice = options[selectedOption - 1]

        if choice == PLAY_HANGMAN:
            playHangman(player)
            
#ASCII for hangman display depending on current lives
def displayHangman(currLives):
    lifePhases = [
        #from final to starting phase
            """
            | .__________))______|
            | |/ /       ||
            | | /        ||.-''.
            | |/         |/  _  .
            | |          ||  `/,|
            | |          ( \`_.'
            | |         .-`--'.
            | |       ./Y . . Y\.
            | |      ./  |   |  \.
            | |     ')   |   |   (`
            | |          ||-||
            | |          || ||
            | |          || ||
            | |         . | | .
            | |        _`-' `-' 
            """, #life phase 1
            
            """
            | .__________))______|
            | |/ /       ||
            | | /        ||.-''.
            | |/         |/  _  .
            | |          ||  `/,|
            | |          ( \`_.'
            | |         .-`--'.
            | |       ./Y . . Y\.
            | |      ./  |   |  \.
            | |     ')   |   |   (`
            | |          ||-
            | |          || 
            | |          || 
            | |         . | 
            | |        _`-' 
            """, #life phase 2

            """
            | .__________))______|
            | |/ /       ||
            | | /        ||.-''.
            | |/         |/  _  .
            | |          ||  `/,|
            | |          ( \`_.'
            | |         .-`--'.
            | |       ./Y . . Y\.
            | |      ./  |   |  \.
            | |     ')   |   |   (`
            | |          
            | |          
            | |          
            | |                  
            """, #life phase 3
            """
            | .__________))______|
            | |/ /       ||
            | | /        ||.-''.
            | |/         |/  _  .
            | |          ||  `/,|
            | |          ( \`_.'
            | |         .-`--'
            | |        /Y . .|
            | |      ./  |   |  
            | |     ')   |   |   
            | |          
            | |          
            | |          
            | |          
            | |         
            """, #life phase 4

            """
            | .__________))______|
            | |/ /       ||
            | | /        ||.-''.
            | |/         |/  _  .
            | |          ||  `/,|
            | |          ( \`_.'
            | |          -`--'
            | |          |. .|
            | |          |   |  
            | |          |   |   
            | |          
            | |          
            | |          
            | |
            | |             
            """, #life phase 5

            """
            | .__________))______|
            | |/ /       ||
            | | /        ||.-''.
            | |/         |/  _  .
            | |          ||  `/,|
            | |          ( \`_.'
            | |          
            | |          
            | |          
            | |             
            | |          
            | |          
            | |          
            | | 
            | |                 
            """, #life phase 6

            """
            | .__________))______|
            | |/ /       ||
            | | /        ||
            | |/         
            | |          
            | |          
            | |          
            | |          
            | |          
            | |             
            | |          
            | |          
            | |          
            | |  
            | |                
            """ #life phase 7      
    ]
    return lifePhases[currLives]

if __name__ == '__main__':
    mainMenu()
