from random import randint
from re import match


# image progresssion for the hangman
hangman = [
    """
---=
|  |
|  O
| /|\\ RIP
| / \\
|
=====
""",
    """
---=
|  |
|  O
| /|\\
|
|
=====
""",
    """
---=
|  |
|  O
|
|
|
=====
""",
    """
---=
|
|
|
|
|
=====
""",
    """

|
|
|
|
|
=====
""",
    """



|
|
|
=====
""",
    """






=====
""",
]
# guesses will draw from hangman[guesses_left]
guesses_left = 6

# logic for the word choice
wordlist = open("wordlist.txt", 'r').readlines()
num_of_lines = len(wordlist)

# pick a random word and remove new line from the end
r = randint(1, num_of_lines - 1)

word = []

for words in wordlist:
    word.append(words)

word = word[r].strip('\n')

# close the file
wordlist = open("wordlist.txt", 'r')
wordlist.close()

# make the word unseeable for the game e.g. cat would be _ _ _
hidden_word = []

for chars in range(len(word)):
    hidden_word.append('_')

display_hidden_word = ' '.join(hidden_word)

# set up list to display guesses made already
guesses_made = []
display_guesses_made = ' '.join(guesses_made)


# function to display game information
def display_game_information():
    print(display_hidden_word)
    print(hangman[guesses_left])
    print(f"Guesses left: {guesses_left}")
    print(f"Guessed so far: {display_guesses_made}")


# print the empty word and show the player how many they need to guess
print(
    f"Guess the word to save the man. The word has {len(word)} letters in it. Good luck!")

# game loop
game_over, game_won, valid_guess = False, False, False

while not game_over:
    # and there are guesses left
    while guesses_left > 0:
        # get player input and display the game information
        # only allow a-z
        # don't allow if already guessed
        while not valid_guess:
            player_guess = str(input("Make a guess: "))
            if not match("^[a-z]*$", player_guess) or len(player_guess) > 1:
                print("Only guess one character that is a - z.")
                continue
            if player_guess in guesses_made:
                print("You've already tried that letter...")
                continue
            break  # it's a valid guess
        # add it to the list of guesses made
        guesses_made.append(player_guess)
        display_guesses_made = ' '.join(guesses_made)
        # is the guess in the word?
        if player_guess in word:
            # find where and replace _ with the letter
            for n in range(len(word)):
                if player_guess == word[n]:
                    hidden_word[n] = player_guess
                    display_hidden_word = ' '.join(hidden_word)
                else:
                    pass
        else:
            print(f"{player_guess} is not in the word.")
            guesses_left -= 1
        # show the game information
        display_game_information()
        # is the game won?
        if '_' not in display_hidden_word:
            game_won = True
            break
        if '_' in display_hidden_word and guesses_left == 0:
            game_over = True
            break
    if game_won:
        print("Congratulations you guessed the word!")
    if game_over:
        print(f"Game Over! The word was {word}")
    break
