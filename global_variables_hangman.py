from tkinter import *
import random

root = Tk()

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
redactedWord = []
chances = 11
replay = True
correct = 0
guess = StringVar()

def modifyImage() :
    global chances
    try :
        if (chances == 10) :
            stickman10 = PhotoImage(file = 'hangman10.png')
            stickmanLabel.configure(image = stickman10)
            stickmanLabel.image = stickman10
        if (chances == 9) :
            stickman9 = PhotoImage(file = 'hangman9.png')
            stickmanLabel.configure(image = stickman9)
            stickmanLabel.image = stickman9
        if (chances == 8) :
            stickman8 = PhotoImage(file = 'hangman8.png')
            stickmanLabel.configure(image = stickman8)
            stickmanLabel.image = stickman8
        if (chances == 7) :
            stickman7 = PhotoImage(file = 'hangman7.png')
            stickmanLabel.configure(image = stickman7)
            stickmanLabel.image = stickman7
        if (chances == 6) :
            stickman6 = PhotoImage(file = 'hangman6.png')
            stickmanLabel.configure(image = stickman6)
            stickmanLabel.image = stickman6
        if (chances == 5) :
            stickman5 = PhotoImage(file = 'hangman5.png')
            stickmanLabel.configure(image = stickman5)
            stickmanLabel.image = stickman5
        if (chances == 4) :
            stickman4 = PhotoImage(file = 'hangman4.png')
            stickmanLabel.configure(image = stickman4)
            stickmanLabel.image = stickman4
        if (chances == 3) :
            stickman3 = PhotoImage(file = 'hangman3.png')
            stickmanLabel.configure(image = stickman3)
            stickmanLabel.image = stickman3
        if (chances == 2) :
            stickman2 = PhotoImage(file = 'hangman2.png')
            stickmanLabel.configure(image = stickman2)
            stickmanLabel.image = stickman2
        if (chances == 1) :
            stickman1 = PhotoImage(file = 'hangman1.png')
            stickmanLabel.configure(image = stickman1)
            stickmanLabel.image = stickman1
        if (chances == 0) :
            stickman0 = PhotoImage(file = 'hangman0.png')
            stickmanLabel.configure(image = stickman0)
            stickmanLabel.image = stickman0
            wordLabel['text'] = 'You lost...'
            statusLabel['text'] = f'The word was {word}'
            guessEntry.pack_forget()
            guessButton.pack_forget()
    except FileNotFoundError :
        print('Image file not found.')
        exit()

def clickGuessButton(self) :
    global guessedLetters
    global triedLetters
    global redactedWord
    global word
    global chances
    global guess
    global correct

    letterGuessed = guess.get()
    if not letterGuessed.isalpha() :
        statusLabel['text'] = 'A word is only made of letters, nothing else... try again!'
    elif (len(letterGuessed) != 1) :
        statusLabel['text'] = 'Slow down there buckaroo ! Guess one letter at a time.'
    elif letterGuessed in guessedLetters :
        statusLabel['text'] = 'You\'ve already guessed that letter!'
    elif letterGuessed in triedLetters :
        statusLabel['text'] = 'You\'ve already tried that letter, and it\'s still not in the word!'

    elif letterGuessed in word and (correct < len(word)) :
        guessedLetters += letterGuessed
        statusLabel['text'] = f'You guessed: {guessedLetters}'
        letterGuessedIterations = word.count(letterGuessed)
        for i in range(letterGuessedIterations) :
            correct += 1        
        x = 0
        for char in word :
            if char in guessedLetters :
                redactedWord[x] = char
            x += 1
        redactedWordString = ' '.join(redactedWord)
        wordLabel['text'] = redactedWordString

    elif not letterGuessed in word and (correct < len(word)) :
        triedLetters += letterGuessed
        statusLabel['text'] = f'You tried: {triedLetters}'
        chances -= 1
        modifyImage()

    if (correct == len(word)) :
        statusLabel['text'] = 'You won! Congrats :)'
        guessEntry.pack_forget()
        guessButton.pack_forget()
        try :
            victory = PhotoImage(file = 'victory.png')
            stickmanLabel.configure(image = victory)
            stickmanLabel.image = victory
        except FileNotFoundError :
            print('Victory image not found')
            exit()

    guessEntry.delete(0, END)

def clickReplayButton() :
    global word
    global wordList
    global chances
    global correct
    global guessedLetters
    global triedLetters
    global redactedWord

    guessEntry.pack(side = LEFT, pady = 10)
    guessButton.pack(side = LEFT, padx = 10, pady = 10)

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


    chances = 11
    correct = 0
    guessedLetters = ' '
    triedLetters = ' '
    redactedWord = []

    setupRedactedWord(word)

    try :
        stickman11 = PhotoImage(file = 'hangman11.png')
    except FileNotFoundError :
        print('Image file not found.')
        exit()
    stickmanLabel.image = stickman11
    stickmanLabel['image'] = stickmanLabel.image
 
    
def setupRedactedWord(word) :
    global redactedWord
    for char in word :
        redactedWord += '_'
    redactedWordString = ' '.join(redactedWord)
    print(redactedWordString)
    wordLabel['text'] = redactedWordString

class MyFrame(Frame) :
    def __init__(self, master = None) :
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill = BOTH, expand = 1)

        exitButton = Button(self, text = 'Quit game', command = self.clickExitButton)
        exitButton.pack(anchor = 'nw', padx = 5, pady = 5)

        replayButton = Button(self, text = 'Restart game', command = clickReplayButton)
        replayButton.pack(anchor = 'nw', padx = 5, pady = 5)

        welcomeLabel = Label(self, text = 'Welcome to this hangman game!\nGuess the word :)')
        welcomeLabel.pack(anchor = 'center', padx = 10, pady = 10)

    def clickExitButton(self) :
        exit()

if __name__ == '__main__' :
    try :  
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
        
        guessEntry = Entry(app, textvariable = guess, width = 1)
        guessEntry.pack(side = LEFT, pady = 10)

        guessButton = Button(app, text = 'Guess', command = clickGuessButton)
        guessButton.pack(side = LEFT, padx = 10, pady = 10)

        statusLabel = Label(app, text = 'Game status will appear here')
        statusLabel.pack(side = RIGHT, padx = 10, pady = 10)

        setupRedactedWord(word)
        root.bind(sequence = '<Return>', func = clickGuessButton)
        
        root.mainloop()

    except KeyboardInterrupt :
        print('User ended the program.')
        exit()
