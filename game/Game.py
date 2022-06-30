import copy
import math

from game.Board import Board
from game.Player import Player
from game.Tree import Tree, TreeNode


class Game(object):
    def __init__(self):
        self.board = Board()
        self.__players = [Player(0), Player(1)]
        self.__current_player = 0

    def game_loop(self):
        valid_keys = ['1', '2', '3', '4', '5', '6', '7']
        player_won = False
        row = -1
        column = -1
        print("Welcome to the game of connect four")
        while not player_won:
            print()
            self.board.print_board()
            if self.__current_player == 1:
                print("AI move")
                self.board = self.computer_move(4)
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

    # minimax(0, 0, true, -INFINITY, +INFINITY) ovako pozivamo

    # def minimax(self, node, depth, isMaximizingPlayer, alpha, beta, player):
    #     if depth <= 0 or node.data.check_if_player_won(self.__players[player]):
    #         return node.data.eval_board(self.__players[player],
    #                                       self.__players[(player + 1) % 2])
    #     player = (player + 1) % 2
    #     if isMaximizingPlayer:
    #         bestVal = -math.inf
    #         for child in self.form_game_tree(node.data, player).root.children:
    #             value = self.minimax(child, depth + 1, False, alpha, beta, player)
    #             bestVal = max(bestVal, value)
    #             alpha = max(alpha, bestVal)
    #             if beta <= alpha:
    #                 break
    #         return bestVal
    #
    #     else:
    #         bestVal = math.inf
    #         for child in self.form_game_tree(node.data, player).root.children:
    #             value = self.minimax(child, depth + 1, True, alpha, beta, player)
    #             bestVal = min(bestVal, value)
    #             beta = min(beta, bestVal)
    #             if beta <= alpha:
    #                 break
    #         return bestVal
