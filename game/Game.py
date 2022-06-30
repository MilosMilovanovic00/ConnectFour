from game.Board import Board
from game.Player import Player


class Game(object):
    def __init__(self):
        self._board = Board()
        self._players = [Player(0), Player(1)]
        self._current_player = 0

    def game_loop(self):
        valid_keys = ['1', '2', '3', '4', '5', '6', '7']
        player_won = False
        row = -1
        column = -1
        print("Welcome to the game of connect four")
        while not player_won:
            print()
            self._board.print_board()
            # if self._current_player == 1:
            #     self.computer_move()
            #     self._board.print_board()
            #     continue
            column = input("Choose column you want to place chip: ")
            if column not in valid_keys:
                print("Option is not valid. Type in number of column.")
            else:
                row = self._board.add_chip(self._players[self._current_player], int(column) - 1)
                if row == -1:
                    print("You can't place your chip in a column that's full")
                if self._board.check_if_player_won(self._players[self._current_player]):
                    self._board.print_board()
                    print(self._players[self._current_player].get_players_name(), "has won!")
                    player_won = True
            self.change_player()

    def change_player(self):
        self._current_player = (self._current_player + 1) % 2

