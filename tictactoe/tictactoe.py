#! python3
import random
import sys

# game loop variable
game_over = False

# the game object - starts a new game


class Game():
    """A new game"""

    def __init__(self):
        pass

    # variables and functions to handle any game board
    board = b = [
        " ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]

    # create boards that will check for wins
    # 0 is used in win conditions so -1 is a blank space
    moves = {
        "player": [
            -1, -1, -1,
            -1, -1, -1,
            -1, -1, -1],
        "computer": [
            -1, -1, -1,
            -1, -1, -1,
            -1, -1, -1]
    }


# draw board


def draw_board():
    b = game.b
    print(f"""
  {b[0]} | {b[1]} | {b[2]}
 {"-" * 11}
  {b[3]} | {b[4]} | {b[5]}
 {"-" * 11}
  {b[6]} | {b[7]} | {b[8]}
""")


# variables and functions to handle any moves on a board
# whose move is it?
player_move = True
computer_move = False


def get_move(_from):
    b = game.b
    moves = game.moves
    # always show the board first
    draw_board()

    while not game_over:
        # if it's the players turn
        if _from:  # player (True)
            player_move = p = int(input())
            # if space is empty move is valid
            if b[p] == " ":
                b[p] = "o"  # will be visible in the game board when drawn
                # fills the position on players move board
                moves['player'][p] = p
                check_board('player')  # did this move win?
                break
            else:
                # move is not valid
                continue
        else:  # False
            # its the computer's turn
            computer_move = c = random.randint(0, 8)
            # if space is empty move is valid
            if b[c] == " ":
                b[c] = "x"  # will be visible in the game board when drawn
                # fills the position on players move board
                moves['computer'][c] = c
                check_board('computer')  # did this move win?
                break
            else:
                # move is not valid
                continue


# check the board for an end game condition


def check_board(move_from):
    b = game.b
    moves = game.moves
    # winning lines
    # 012, 345, 678 horizontal
    # 036, 147, 258 vertical
    # 048, 246      diagonal
    wins = (
        '012', '345', '678',
        '036', '147', '258',
        '048', '246')

    n = 0
    while n < 8:  # number of win possibilities
        if move_from == 'player':
            movelist = moves['player']
        else:
            movelist = moves['computer']

        # use n as tuple position to iterate through possible win scenarios
        # wins[n][0] is 0 from first position '012' at the start of the loop
        # if x and y and z are in the players moves on the board
        # then that is a win condition
        x, y, z = int(wins[n][0]), int(wins[n][1]), int(wins[n][2])
        if x in movelist and y in movelist and z in movelist:
            if move_from == 'player':
                print("You won.")
            else:
                print("Computer wins.")
            draw_board()
            sys.exit(0)
        else:
            n += 1

    # is it a draw?
    if " " not in b:
        # if the board contains no empty spaces it will be a draw because the loop would have found a win before this line
        print("It's a draw")
        draw_board()
        sys.exit(0)


# main game loop
game = Game()
while not game_over:
    get_move(player_move)
    get_move(computer_move)
