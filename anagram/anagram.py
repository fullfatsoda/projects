# find an anagram for a single word from a list of words


def find_in_words(anagram):
    # seperate chars and sort in alphabetical order
    word = list(anagram)
    word.sort()

    # open the word file
    wordlist = open('words.txt', 'r')

    word_to_check = None
    possible_matches = []

    for line in wordlist:
        # len anagram +1 because \n counts in file
        if len(line) == (len(anagram)+1):
            # remove \n from word
            word_to_check = str(line).rstrip('\n')
            # add to list of possible matches for further check
            possible_matches.append(word_to_check)
            # seperate chars and sort in alphabetical order
            word_to_check = list(word_to_check)
            word_to_check.sort()
            if word_to_check == word:
                # its already in the list of possible matches
                continue
            else:
                # remove from the list of possible matches
                possible_matches.pop()

    print(f"Possible solutions for {anagram}:")
    for match in possible_matches:
        print(match)


find_in_words('ilra')
find_in_words('sntlei')
