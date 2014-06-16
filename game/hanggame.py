import sys


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word = raw_input("Enter a word")
wordlist = []
wordlist.append(word)
print word
wrongGuess = ""
rightGuess = ""
hidden = "-" * len(word)
print hidden
print HANGMANPICS[0]

def display(HANGMANPICS, wrongGuess):
    global hidden
    print HANGMANPICS[len(wrongGuess)] 
    for i in range(len(word)):
        if word[i] in rightGuess:
            hidden = hidden[:i] + word[i] +hidden[i+1:]
    print hidden   
        
def getChar(wrongGuess, allreadyGuess):
    leng = 0
    while leng < 10:
        print " Please enter a character"
        guess = raw_input()
        guess = guess.lower()
        
        if len(guess) == 1 and guess in "abcdefghijklmnopqrstuvwxyz" and guess not in allreadyGuess: 
            return guess
            
        else:
            print "You should enter only one character from the alphabet without repeating it"
            
            
while True:
    allreadyGuess = wrongGuess + rightGuess
    guess = getChar(wrongGuess, allreadyGuess)
    
    if guess in word:
        rightGuess += guess
    else:
        wrongGuess += guess
        print "You already used: " , wrongGuess, rightGuess
    display(HANGMANPICS, wrongGuess)
    if len(wrongGuess) == len(HANGMANPICS)-1:
        print " You loose the word was \" {word} \" try next time".format(word=word)
        sys.exit()
    if hidden == word:
        print " You are smart the word was \" {word} \" Good job".format(word = word)
        sys.exit()