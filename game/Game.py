import copy
import math
import time

from game.Board import Board
from game.Player import Player
from game.Tree import Tree, TreeNode


class Game(object):
    def __init__(self):
        self.board = Board()
        self.__players = [Player(0), Player(1)]
        self.__current_player = 0
        self.__game_turn = 0

    def game_loop(self):
        valid_keys = ['1', '2', '3', '4', '5', '6', '7']
        player_won = False
        row = -1
        column = -1
        ukupno_vreme = 0
        print("Welcome to the game of connect four")
        depth = 4
        while not player_won:
            if self.__game_turn == 17:
                depth += 1
            if self.__game_turn == 30:
                depth += 2
            if self.__game_turn == 33:
                depth += 3
            self.board.print_board()
            if self.__game_turn == self.board.rows * self.board.columns:
                print("It's a tie")
                break
            if self.__current_player == 1:
                print("AI move")
                self.board = self.computer_move(depth)
                if self.board.check_if_player_won(self.__players[self.__current_player]):
                    self.board.print_board()
                    print("AI has won!")
                    player_won = True
                self.change_player()
                continue
            column = input("Choose column you want to place chip: ")
            if column not in valid_keys:
                print("Option is not valid. Type in number of column.")
            else:
                row = self.board.add_chip(self.__players[self.__current_player], int(column) - 1)
                if row == -1:
                    print("You can't place your chip in a column that's full")
                if self.board.check_if_player_won(self.__players[self.__current_player]):
                    self.board.print_board()
                    print(self.__players[self.__current_player].get_players_name(), "has won!")
                    player_won = True
                self.change_player()

    def change_player(self):
        self.__current_player = (self.__current_player + 1) % 2
        self.__game_turn += 1

    def form_game_tree(self, board, player_id):
        possible_moves = Tree()
        start = TreeNode(board)
        possible_moves.root = start
        for column in range(7):
            board_state = copy.deepcopy(board)
            row = board_state.add_chip(self.__players[player_id], int(column) - 1)
            if row != -1:
                possible_move = TreeNode(board_state)
                possible_moves.root.add_child(possible_move)
        return possible_moves

    def computer_move(self, depth):
        best_move = None
        alpha = -math.inf
        for child in self.form_game_tree(copy.deepcopy(self.board), self.__current_player).root.children:
            if child.data.check_if_player_won(self.__players[self.__current_player]):
                return child.data
            result = self.minscore(child, depth - 1, alpha, math.inf, self.__current_player)  # max
            if result > alpha:
                alpha = result
                best_move = child.data
        return best_move

    def minscore(self, child, depth, alpha, beta, player):
        if depth <= 0 or child.data.check_if_player_won(self.__players[player]):
            return child.data.eval_board(self.__players[player], self.__players[(player + 1) % 2])
        for child in self.form_game_tree(child.data, (player + 1) % 2).root.children:
            score = self.maxscore(child, depth - 1, alpha, beta, (player + 1) % 2)
            beta = min(beta, score)
            if alpha >= beta:
                return alpha
        return beta

    def maxscore(self, child, depth, alpha, beta, player):
        if depth <= 0 or child.data.check_if_player_won(self.__players[player]):
            return child.data.eval_board(self.__players[player], self.__players[(player + 1) % 2])
        for child in self.form_game_tree(child.data, player).root.children:
            score = self.minscore(child, depth - 1, alpha, beta, (player + 1) % 2)
            alpha = max(alpha, score)
            if alpha >= beta:
                return beta
        return alpha
