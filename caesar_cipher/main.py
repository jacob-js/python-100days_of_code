import re
import string
from art import logo

should_continue = True

print(logo)

alphabets = list(string.ascii_lowercase)

def caesar(start_text, shift_amount, direction):
    end_text = ""
    msg = "The encoded text"
    letters = alphabets + alphabets
    if direction == "d":
        shift_amount *= -1
        msg = "The decoded text"
    for l in start_text:
        if re.match('[a-z]', l):
            rel = letters[alphabets.index(l)+shift_amount]
            end_text += rel
        else:
            end_text += l
    print(f"{msg} is : {end_text}")

while should_continue:
    action = input("Enter the action to execute. 'd' to decode and 'e' for encoding : \n")

    while action not in ("d", "e"):
        action = input("Please enter a valid action letter. 'd' to decode and 'e' for encoding : \n")

    message = input("Type your message : \n").lower()

    shift = int(input("Shift number : \n"))
    while shift > alphabets.__len__():
        shift = int(input(f"Please enter a number less than {len(alphabets)} : \n"))

    caesar(message, shift, action)

    choice = input("Do you want to go again ? y/n : \n").lower()
    if choice == "n":
        should_continue = False
    elif choice == "y":
        should_continue = True
    else:
        should_continue = False
        print("You entered a bad choice")


print("Good bye!")
