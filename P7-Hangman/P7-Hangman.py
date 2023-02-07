import random, hangman_words , hangman_art
#Initilize a word list, then chose a word randomly from the list, 
# and determine the len of that word.
# word_l = ["ardvark","baboon","camel"]
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_l)
word_len = len(chosen_word)

lives = 7

#Initilize a list of length = word_len where each of 
# list element is a underscore(_)
print("chosen word is " + chosen_word) #debug
blanks = ["_" for a in range(word_len)]
already_guessed = []
while "_" in blanks and lives != 0:
#Ask user to guess a letter and if the letter present in "chosen_word" 
#replace the underscores in "blanks" list with the letter at correct index. 
    guess = input("Guess the letter: ").lower()
    if guess[0] in already_guessed:
      print(f"You have already guessed letter {guess[0]}")
      continue
    already_guessed.append(guess[0])
    for i in range(word_len):
        if guess[0] == chosen_word[i]:  #using index 0 of string guess to make sure it only pick up one letter if user put multiple
            blanks[i] = guess[0]
    print(" ".join(blanks))
    if guess[0] not in blanks:
        lives -= 1
        print(f"Letter '{guess[0]}' is not in the word.You've lost a life")
    print(hangman_art.stages[lives])
if lives == 0:
    print("You lose")
else:
    print("You won the game")

