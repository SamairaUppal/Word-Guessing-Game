### Project: Word Guessing Game ###

# global variables and arrays
secretWord=""                   # secret word
maskedWord=""                   # masked word
usedLetters=""                  # used letters
lives=0                         # number of remaining lives
finish=0                        # status of the game - {-1:in progress,0:player lost,1:player won}
letter=""                       # the letter that the player chose in the current turn

def setupGame():
    global secretWord,maskedWord,lives,finish
    secretWord = input()
    maskedWord = '*' * len(secretWord)
    lives = 5
    finish = -1

def drawScreen():
    global maskedWord, lives, usedLetters
    print(maskedWord)
    print('Remaining lives:',lives)
    print('Used letters:',usedLetters)
    print()

def getMove():
    global letter, usedLetters
    print('Enter a lower case letter:')
    letter = input()
    while True:
        if letter in usedLetters:
            print('Invalid! This letter is used before.')
            print('Enter a lower case letter:')
            letter = input()
        else:
            break
        

def makeMove():
    global letter, secretWord,maskedWord, usedLetters, lives,finish
    indices = []
    if letter in secretWord:
        for i in range(len(secretWord)):
            if secretWord[i] == letter:
                indices.append(i)
        masked_list = list(maskedWord)
        for j in indices:
            masked_list[j] = letter
        maskedWord = ''.join(masked_list)
        usedLetters+=letter
    else:
        lives-=1
        usedLetters+=letter

def checkEndGame():
    global lives, maskedWord, secretWord
    if lives == 0:
        return 0
    elif maskedWord == secretWord:
        return 1
    else:
        return -1

setupGame()                     # step 1

# main game loop
while True:
    drawScreen()                # step 2
    getMove()                   # step 3
    makeMove()                  # step 4
    finish = checkEndGame()     # step 5
    if finish>-1:
        break

# step 6: end game information
# *** TO BE FILLED
print(maskedWord)
print('Remaining lives:', lives)
print('Used letters:', usedLetters)
print()
if finish == 0:
    print('You lost! The secret word was:',secretWord )
elif finish == 1:
    print('You won!')
