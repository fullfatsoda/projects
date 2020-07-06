# generate a secure passphrase n in length
import PySimpleGUI as sg
from random import randint


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

sg.theme('SystemDefault1')

layout = [
    [
        sg.Text("Specify how many words will be in your passphrase:"),
        sg.In(size=(5, 1), enable_events=True, key='-PASSLEN-'),
    ],
    [
        sg.Button("Generate"),
        sg.Button("Clear")
    ],
    [
        sg.Output(size=(40, 4), key='-PASSPHRASE-'),
    ],
]

# create the window
window = sg.Window("Passphrase Generator", layout)

# create event loop
while True:
    event, values = window.read()

    if event == "Generate":
        generate_passphrase(int(values["-PASSLEN-"]))
    if event == "Clear":
        window['-PASSPHRASE-'].update('')

    if event == sg.WIN_CLOSED or event == 'Quit':
        break


window.close()
