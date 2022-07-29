"""
Tes
"""
import random

STAGES = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

STAGES.reverse()


WORD_LIST = ['ardvark', 'baboon', 'camel']
CHOSEN_WORD = random.choice(WORD_LIST)
CHOSEN_BLANK = ['-'] * len(CHOSEN_WORD)


times = 0
end_of_the_game = False
LIVES = 6
guesses = "".join(CHOSEN_BLANK)

print(f"The solution is {CHOSEN_WORD}")

while end_of_the_game != True:
    guess = input("Gues a letter : ").lower()
    correct = 0

    for (index, letter) in enumerate(CHOSEN_WORD):
        if letter == guess:
            CHOSEN_BLANK[index] = guess
            correct += 1

    guesses = "".join(CHOSEN_BLANK)
    print(guesses)
    times += correct if correct > 0 else 1
    
    if LIVES <= 0 or guesses == CHOSEN_WORD:
        end_of_the_game = True

    if guess not in CHOSEN_WORD:
        LIVES -= 1
        print(STAGES[LIVES])

if "".join(CHOSEN_BLANK) != CHOSEN_WORD:
    print("You loose.")
else:
    end_of_the_game = True
    print("You win .")
