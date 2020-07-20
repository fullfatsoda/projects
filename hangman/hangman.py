from random import randint


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
# guesses will draw from hangman[guesses]
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

player_guesses = []
display_player_guesses = ' '.join(player_guesses)


# function to display game information
def display_game_information():
    print(display_hidden_word)
    print(hangman[guesses_left])
    print(f"Guesses left: {guesses_left}")
    print(f"Guessed so far: {display_player_guesses}")


# game loop
game_over = False
game_won = False
# print the empty word and show the player how many they need to guess
print(
    f"Guess the word to save the man. The word has {len(word)} letters in it. Good luck!")
print(word)
while not game_over:
    # and there are guesses left
    while guesses_left > 0:
        # get player input and display the game information
        player_guess = str(input("Make a guess: "))
        player_guesses.append(player_guess)
        display_player_guesses = ' '.join(player_guesses)
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
        if hidden_word != word and guesses_left == 0:
            game_over = True
            break
    if game_won:
        print("Congratulations you guessed the word!")
    if game_over:
        print(f"Game Over! The word was {word}")
    break
