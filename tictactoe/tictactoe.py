from random import randint
from sys import exit


class Game():
    def __init__(self):
        self.playing = True
        self.board = [" " for x in range(9)]
        self.player = None
        self.computer = None

    def reset(self):
        self.board = [" " for x in range(9)]
        self.player = None
        self.computer = None
        self.loop()

    def prompt_new_game(self):
        print("Play again? (y/n)")
        while True:
            choice = str(input())
            if choice == 'y':
                break
            elif choice == 'n':
                exit("Thanks for playing!")
            else:
                continue
        self.reset()

    def choose_char(self):
        print("Choose a character to play as, can be any letter, number or character you choose: ")
        choice = str(input())
        self.player = Player("Player", choice[0])
        self.computer = Player("Computer", "$")


    def draw(self):
        b = self.board
        # draw positions relative to numpad [0] is left blank
        print(f'\n {b[6]} | {b[7]} | {b[8]}\n{"-" * 11}\n {b[3]} | {b[4]} | {b[5]}\n{"-" * 11}\n {b[0]} | {b[1]} | {b[2]}')

    def get_move(self, move_from):
        # check if a move is possible
        if " " not in self.board:
            make_move = False
            print("There are no spaces left, the game is a draw.")
            self.playing = False
            self.draw()
            self.prompt_new_game()
        # allow a move if possible
        make_move = True
        while make_move:
            if move_from == self.player:
                print("Choose an empty space: ")
                move = int(input())-1
                if self.board[move] == " ":
                    self.board[move] = self.player.char
                    self.player.moves[move] = move
                    self.player.check_board()
                    break
                else:
                    continue
            elif move_from == self.computer:
                move = randint(0, 8)
                if self.board[move] == " ":
                    self.board[move] = self.computer.char
                    self.computer.moves[move] = move
                    self.computer.check_board()
                    break
                else:
                    continue
    
    def loop(self):
        self.playing = True
        self.choose_char()
        while self.playing:
            self.draw()
            self.get_move(self.player)
            self.get_move(self.computer)



class Player:
    def __init__(self, name, char):
        self.name = name
        self.char = char
        self.moves = [" " for x in range(9)]

    def check_board(self):
        # winning lines
            # 012, 345, 678 horizontal
            # 036, 147, 258 vertical
            # 048, 246      diagonal
        wins = (
            '012', '345', '678',
            '036', '147', '258',
            '048', '246')
        b, m = game.board, self.moves
        for n in range(len(wins)):
            a, b, c = int(wins[n][0]), int(wins[n][1]), int(wins[n][2])
            if a in m and b in m and c in m:
                print(f"{self.name} wins!")
                game.playing = False
                game.draw()
                game.prompt_new_game()
                
if __name__ == "__main__":
    game = Game()
    game.loop()