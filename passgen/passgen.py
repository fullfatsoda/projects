# generate a secure passphrase n in length
from random import randint
from pyperclip import copy


def generate_passphrase(n):
    # open wordlist
    adjectives = open('english-adjectives.txt', 'r').readlines()
    animals = open('animals.txt', 'r').readlines()

    passphrase = []
    # choose words at random from each textfile
    # format - adj adj... animal
    for words in range(n-1):
        # get n - 1 adjectives from list
        passphrase.append(adjectives[randint(0, (len(adjectives)))])
    # end with an animal
    passphrase.append(animals[randint(0, (len(animals)))])

    # strip \n
    n -= 1
    passphrase = [n.strip('\n') for n in passphrase]
    passphrase = ' '.join(passphrase)
    # output
    print(passphrase)
    copy(passphrase)
    print("\nCopied to clipboard")

generate_passphrase(8)
