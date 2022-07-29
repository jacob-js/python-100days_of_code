"""
Tes
"""
import random

from art import LOGO, STAGES
from words import WORD_LIST

STAGES.reverse()

CHOSEN_WORD = random.choice(WORD_LIST)
CHOSEN_BLANK = ['-'] * len(CHOSEN_WORD)


times = 0
end_of_the_game = False
LIVES = 6
guesses = "".join(CHOSEN_BLANK)

print(LOGO)

print(f"The solution is {CHOSEN_WORD}")

while end_of_the_game != True:
    guess = input("Guess a letter : ").lower()
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
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(STAGES[LIVES])

if "".join(CHOSEN_BLANK) != CHOSEN_WORD:
    print("You loose.")
else:
    end_of_the_game = True
    print("You win .")
