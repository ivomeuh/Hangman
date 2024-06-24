import random

try :
    f = open("wordlist.txt", "rt")
except FileNotFoundError :
    print('Word list file not found.')
    exit()
lines = f.readlines()
wordList = ' '
for line in lines :
    line = line.replace('\n', ' ')
    wordList += line
wordList = wordList.split(' ')
word = random.choice(wordList)

while (len(word) < 4) :
    word = random.choice(wordList)

lettersGuessed = ' '
lettersTried = ' '
chances = len(word) + 5
correct = 0
replay = True

if __name__ == '__main__' :
    print('Welcome to my attempt at making a hangman game :)')
    try :
        while (replay == True) :
            print('Guess the word!')
            for char in word :
                print('_', end = ' ')
            print()
            print('Chances: {}'.format(chances))

            try :
                while (chances > 0) :
                    try :
                        guessInput = str(input('Enter a letter to guess: '))
                    except :
                        print('Invalid input, try again.')
                        print()
                        continue

                    if not guessInput.isalpha() :
                        print('The word contains letters, nothing else... try again!')
                        print()
                        continue
                    if len(guessInput) > 1 :
                        print('Slow down there buckaroo! One letter at a time... Try again!')
                        print()
                        continue
                    if guessInput in lettersGuessed :
                        print('You\'ve already found that letter! Try again.')
                        print()
                        continue
                    if guessInput in lettersTried :
                        print('You\'ve already tried that letter... it won\'nt be correct this time around either. Try again!')
                        print()
                        continue

                    if guessInput in word :
                        guessedLetterIterations = word.count(guessInput)
                        for i in range(guessedLetterIterations) :
                            lettersGuessed += guessInput
                            correct += 1
                    elif guessInput not in word :
                        lettersTried += guessInput
                        chances -= 1
                        print('Chances remaining: {}'.format(chances))

                    for char in word :
                        if char in lettersGuessed and (correct < len(word)) :
                            print(char, end = ' ')
                        elif (correct < len(word)) :
                            print('_', end = ' ')
                    print()
                    print()
                    if (correct == len(word)) :
                        print('The word is indeed {}, well done !'.format(word))
                        break
                if (chances == 0) :
                    print('You lost, but that doesn\'nt mean you suck... you\'ll do better next time!')
                correctInput = False
                while (correctInput == False) :
                    replayYesNo = str(input('Do you want to play again? y/n: '))
                    if (replayYesNo == 'n') :
                        replay = False
                        correctInput = True
                    elif (replayYesNo == 'y') :
                        word = random.choice(wordList)
                        while (len(word) < 4) :
                            word = random.choice(wordList)
                        chances = len(word) + 5
                        correct = 0
                        lettersGuessed = ' '
                        lettersTried = ' '
                        correctInput = True
                    else :
                        print('Please state your answer by using only the single lowercase character \'y\' or the single lowercase character \'n\'.')

            except KeyboardInterrupt :
                print('You\'ve interrupted the program.')
                exit()
    except KeyboardInterrupt :
        print('You\'ve interrupted the program.')
        exit()
