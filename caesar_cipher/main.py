import string


alphabets = list(string.ascii_lowercase)
action = input("Enter the action to execute. 'd' to decode and e for encoding \n")

while action not in ("d", "e"):
    action = input("Please enter a valid action letter. 'd' to decode and e for encoding \n")

message = input("Type your message : \n")
shift = int(input("Shift number : \n"))

def encode_msg():
    crypted = ""
    for l in message:
        try:
            rel = alphabets[alphabets.index(l)+shift]
        except IndexError:
            rel = alphabets[alphabets.index(l)-shift]
        crypted += rel
    print(f"The encoded message is : {crypted}")

def decode_msg():
    decoded = ""
    for l in message:
        try:
            rel = alphabets[alphabets.index(l)-shift]
        except IndexError:
            rel = alphabets[alphabets.index(l)+shift]
        decoded += rel
    
    print(f"The decoded message is : {decoded}")

if action == "d":
    decode_msg()
else:
    encode_msg()
