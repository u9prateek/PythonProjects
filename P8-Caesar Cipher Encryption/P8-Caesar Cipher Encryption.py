from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caeser(message,shift,direction):
    message = message.lower()
    shift = shift%26
    if direction == "decode":
        shift *= -1
    cipher_message = ""
    for x in message:
        if x not in alphabet:
            cipher_message += x
            continue
        i = alphabet.index(x)
        i = i + shift
        if i < 26:
            cipher_message += alphabet[i]

        else:
            ni = i - 26
            cipher_message += alphabet[ni]
            print("else " + cipher_message) #debug
    print(f"Here's the {direction}d result: {cipher_message}")


while True:
    todo = input("Type encode to encrypt, decode to decrypt:\n")
    if todo == 'encode' or todo == 'decode':
        message = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        caeser(message,shift,todo)
    else:
        print(f"Unknown choice '{todo}'")
        continue
    goagain = input("Press enter if you want to go agian, other wise type 'no'\n")
    if goagain == 'no':
        print("Good Bye!")
        break
