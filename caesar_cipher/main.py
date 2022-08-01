import string


alphabets = list(string.ascii_lowercase)
action = input("Enter the action to execute. d for decode and e for encoding \n")
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
    print(crypted)

encode_msg()
