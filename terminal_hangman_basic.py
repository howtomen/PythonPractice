import random
def WordSelec():
    wordBank = ["toyota","honda", "ford" ,"hyundai", "chevrolet", "volvo", "mercedes", "audi", "lamborghini","ferrari","maserati","buick"]
    listlen = len(wordBank)
    randomN = random.randint(0,(listlen-1))
    return wordBank[randomN]
# function for actual game play    
def GuessingLetters(word):
    blockedWord ="*" * len(gameWord)
    modWord = list(blockedWord)
    missingLet = wordLen = len(word)
    wrong_tries = 0
    right_tries = 0
    
    while missingLet != 0:
        letter = input("Enter a Letter: ")
        letter = letter.lower()
        i = 0   
        letterPresent = False
        for x in word:
            if letter == x:
                modWord[i] = letter
                i +=1
                missingLet -=1
                letterPresent = True
            else:
                i +=1

        if letterPresent == True:
        	right_tries +=1
        else:
        	wrong_tries +=1
        
        printWord = "".join(modWord)
        print("Number of correct guesses: ", right_tries, "\nNumber of incorrect guessess: ", wrong_tries)
        print("\n",printWord, "\n-------------------------")
        
# main program 
playagain = 'y' #variable to use during play again loop
print("Welcome to Hangman, we will be selecting a random word and you must guess letters!")

#while loop to play game as many times as you want. 
while playagain == 'y':
	print("\nThese are car brand names! Here is your word blocked out time to start Guessing letters!\n")
	gameWord = WordSelec()
	blockedWord ="*" * len(gameWord)
	print(blockedWord)
	GuessingLetters(gameWord)
	playagain = input("Would you like to play again? (y/n): ")
	playagain = playagain.lower()
print("Goodbye!")
