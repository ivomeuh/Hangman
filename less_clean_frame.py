from tkinter import *
from functools import partial
import random

try :
    f = open('wordlist.txt', 'rt')
except FileNotFoundError :
    print('Word list not found.')
    exit()
lines = f.readlines()
wordList = ' '
for line in lines :
    line = line.replace('\n', ' ')
    wordList += line
wordList = wordList.split(' ')
word = random.choice(wordList)
print(word)
while (len(word) < 4) :
    word = random.choice(wordList)
    print(word)

guessedLetters = ' '
triedLetters = ' '
redactedWord = ' '
letterGuessed = ' '
chances = 11
correct = 0
replay = True

def clickGuessButton(guess, guessedLetters, triedLetters) :
    letterGuessed = guess.get()
    if not letterGuessed.isalpha() :
        statusLabel['text'] = 'A word is only made of letters, nothing else... try again!'
    elif (len(letterGuessed) != 1) :
        statusLabel['text'] = 'Slow down there buckaroo ! Guess one letter at a time.'
    elif letterGuessed in guessedLetters :
        statusLabel['text'] = 'You\'ve already guessed that letter!'
    elif letterGuessed in triedLetters :
        statusLabel['text'] = 'You\'ve already tried that letter, and it\'s still not in the word!'
    else :
        statusLabel['text'] = f'You guessed: {letterGuessed}'
        return(letterGuessed)

def setupRedactedWord(word) :
    redactedWord = ' '
    for char in word :
        redactedWord += '_ '
    wordLabel['text'] = redactedWord

def getGuessedLetter(self) :
    letterGuessed = clickGuessButton(guess, guessedLetters, triedLetters)
    print(letterGuessed)

def checkWord(letterGuessed, guessedLetters, triedLetters, word) :


class MyFrame(Frame) :
    def __init__(self, master = None) :
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill = BOTH, expand = 1)

        exitButton = Button(self, text = 'Quit game', command = self.clickExitButton)
        exitButton.pack(anchor = 'nw', padx = 5, pady = 5)

        welcomeLabel = Label(self, text = 'Welcome to this hangman game!\nGuess the word :)')
        welcomeLabel.pack(anchor = 'center', padx = 10, pady = 10)

    def clickExitButton(self) :
        exit()

if __name__ == '__main__' :
    root = Tk()
    app = MyFrame()

    stickmanLabel = Label(app)
    try :
        stickman11 = PhotoImage(file = 'hangman11.png')
    except FileNotFoundError :
        print('Image file not found.')
        exit()
    stickmanLabel.image = stickman11
    stickmanLabel['image'] = stickmanLabel.image
    stickmanLabel.pack(anchor = 'n', padx = 50)

    wordLabel = Label(app, text = 'Your word will appear here')
    wordLabel.pack(anchor = 'center', padx = 10, pady = 10)

    guessLabel = Label(app, text = ' Enter a letter to guess:')
    guessLabel.pack(side = LEFT, padx = 10, pady = 10)
        
    guess = StringVar()
    guessEntry = Entry(app, textvariable = guess, width = 1)
    guessEntry.pack(side = LEFT, pady = 10)

    guessButton = Button(app, text = 'Guess', command = partial(clickGuessButton, guess, guessedLetters, triedLetters))
    guessButton.pack(side = LEFT, padx = 10, pady = 10)

    statusLabel = Label(app, text = 'Game status will appear here')
    statusLabel.pack(side = RIGHT, padx = 10, pady = 10)

    setupRedactedWord(word)        
    guessButton.bind('<Button>', getGuessedLetter + , add = '+')
    
        
    root.mainloop()
