 1. import random
  2. HANGMAN_PICS = ['''
  3.   +---+
  4.       |
  5.       |
  6.       |
  7.      ===''', '''
  8.   +---+
  9.   O   |
 10.       |
 11.       |
 12.      ===''', '''
 13.   +---+
 14.   O   |
 15.   |   |
 16.       |
 17.      ===''', '''
 18.   +---+
 19.   O   |
 20.  /|   |
 21.       |
 22.      ===''', '''
 23.   +---+
 24.   O   |
 25.  /|\  |
 26.       |
 27.      ===''', '''
 28.   +---+
 29.   O   |
 30.  /|\  |
 31.  /    |
 32.      ===''', '''
 33.   +---+
 34.   O   |
 35.  /|\  |
 36.  / \  |
 37.      ===''']
 38. words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'.split()
 39.
 40. def getRandomWord(wordList):
 41.     # This function returns a random string from the passed list of
           strings.
 42.     wordIndex = random.randint(0, len(wordList) - 1)
 43.     return wordList[wordIndex]
 44.
 45. def displayBoard(missedLetters, correctLetters, secretWord):
 46.     print(HANGMAN_PICS[len(missedLetters)])
 47.     print()
 48.
 49.     print('Missed letters:', end=' ')
 50.     for letter in missedLetters:
 51.         print(letter, end=' ')
 52.     print()
 53.
 54.     blanks = '_' * len(secretWord)
 55.
 56.     for i in range(len(secretWord)): # Replace blanks with correctly
           guessed letters.
 57.         if secretWord[i] in correctLetters:
 58.             blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
 59.
 60.     for letter in blanks: # Show the secret word with spaces in between
           each letter.
 61.         print(letter, end=' ')
 62.     print()
 63.
 64. def getGuess(alreadyGuessed):
 65.     # Returns the letter the player entered. This function makes sure the
           player entered a single letter and not something else.
 66.     while True:
 67.         print('Guess a letter.')
 68.         guess = input()
 69.         guess = guess.lower()
 70.         if len(guess) != 1:
 71.             print('Please enter a single letter.')
72.         elif guess in alreadyGuessed:
 73.             print('You have already guessed that letter. Choose again.')
 74.         elif guess not in 'abcdefghijklmnopqrstuvwxyz':
 75.             print('Please enter a LETTER.')
 76.         else:
 77.             return guess
 78.
 79. def playAgain():
 80.     # This function returns True if the player wants to play again;
           otherwise, it returns False.
 81.     print('Do you want to play again? (yes or no)')
 82.     return input().lower().startswith('y')
 83.
 84.
 85. print('H A N G M A N')
 86. missedLetters = ''
 87. correctLetters = ''
 88. secretWord = getRandomWord(words)
 89. gameIsDone = False
 90.
 91. while True:
 92.     displayBoard(missedLetters, correctLetters, secretWord)
 93.
 94.     # Let the player enter a letter.
 95.     guess = getGuess(missedLetters + correctLetters)
 96.
 97.     if guess in secretWord:
 98.         correctLetters = correctLetters + guess
 99.
100.         # Check if the player has won.
101.         foundAllLetters = True
102.         for i in range(len(secretWord)):
103.             if secretWord[i] not in correctLetters:
104.                 foundAllLetters = False
105.                 break
106.         if foundAllLetters:
107.             print('Yes! The secret word is "' + secretWord +
                   '"! You have won!')
108.             gameIsDone = True
109.     else:
110.         missedLetters = missedLetters + guess
111.
112.         # Check if player has guessed too many times and lost.
113.         if len(missedLetters) == len(HANGMAN_PICS) - 1:
114.             displayBoard(missedLetters, correctLetters, secretWord)
115.             print('You have run out of guesses!\nAfter ' +
                   str(len(missedLetters)) + ' missed guesses and ' +
                   str(len(correctLetters)) + ' correct guesses,
                   the word was "' + secretWord + '"')
116.             gameIsDone = True
117.
118.     # Ask the player if they want to play again (but only if the game is
           done).
119.     if gameIsDone:
120.         if playAgain():
121.             missedLetters = ''
122.             correctLetters = ''
123.             gameIsDone = False
124.             secretWord = getRandomWord(words)
125.         else:
126.             break