class Board(object):
    def __init__(self):
        self.columns = 7
        self.rows = 6
        self.board = [[' ' for i in range(self.columns)] for j in range(self.rows)]

    def print_board(self):
        print("+---" * 7, end='')
        print('+')
        for i in range(self.rows):
            for j in range(self.columns):
                print("| " + self.board[i][j], end=' ')
            print('|')
            print("+---" * 7, end='')
            print('+')
        print("  1   2   3   4   5   6   7 ")

    def check_if_player_won(self, player):
        for i in range(self.rows):
            for j in range(self.columns - 3):
                if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] \
                        == self.board[i][j + 3] == player.get_color():
                    return True

        for i in range(self.rows - 3):
            for j in range(self.columns):
                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] \
                        == self.board[i + 3][j] == player.get_color():
                    return True

        for i in range(self.rows - 3):
            for j in range(self.columns - 3):
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] \
                        == self.board[i + 3][j + 3] == player.get_color():
                    return True

        for j in range(self.columns - 3):
            for i in range(3, self.rows):
                if self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 2][j + 2] \
                        == self.board[i - 3][j + 3] == player.get_color():
                    return True

        return False

    def add_chip(self, player, column):
        for row in range(self.rows - 1, -1, -1):
            cell_value = self.board[row][column]
            if cell_value is ' ':
                self.board[row][column] = player.get_color()
                return row
        return -1

    def eval_board(self, max_player, min_player):
        three_connected_max_player = self.count_three_connected(min_player, max_player) * 100
        two_connected_max_player = self.count_two_connected(min_player, max_player) * 25

        three_connected_min_player = self.count_three_connected(max_player, min_player) * 100
        two_connected_min_player = self.count_two_connected(max_player, min_player) * 15

        return three_connected_max_player + two_connected_max_player - three_connected_min_player - two_connected_min_player

    def count_three_connected(self, player, opponent):
        score = 0
        score += self.vertical_eval(opponent, player)
        score += self.horizontal_eval(opponent, player)
        score += self.positive_diagonal_eval(opponent, player)
        score += self.negative_diagonal_eval(opponent, player)
        return score

    def positive_diagonal_eval(self, opponent, player):
        score = 0
        for i in range(self.rows - 3):
            for j in range(self.columns - 3):
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == player.get_color() and \
                        self.board[i + 3][j + 3] != opponent.get_color():
                    score += 50
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 3][j + 3] == player.get_color() and \
                        self.board[i + 2][j + 2] != opponent.get_color():
                    score += 50
                if self.board[i][j] == self.board[i + 3][j + 3] == self.board[i + 2][j + 2] == player.get_color() and \
                        self.board[i + 1][j + 1] != opponent.get_color():
                    score += 50
                if self.board[i + 3][j + 3] == self.board[i + 1][j + 1] == self.board[i + 2][
                    j + 2] == player.get_color() and \
                        self.board[i][j] != opponent.get_color():
                    score += 50
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == player.get_color() and \
                        self.board[i + 3][j + 3] == opponent.get_color():
                    score += 10
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 3][j + 3] == player.get_color() and \
                        self.board[i + 2][j + 2] == opponent.get_color():
                    score += 10
                if self.board[i][j] == self.board[i + 3][j + 3] == self.board[i + 2][j + 2] == player.get_color() and \
                        self.board[i + 1][j + 1] == opponent.get_color():
                    score += 10
                if self.board[i + 3][j + 3] == self.board[i + 1][j + 1] == self.board[i + 2][
                    j + 2] == player.get_color() and \
                        self.board[i][j] == opponent.get_color():
                    score += 10
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == opponent.get_color() and \
                        self.board[i + 3][j + 3] == player.get_color():
                    score += 20
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 3][j + 3] == opponent.get_color() and \
                        self.board[i + 2][j + 2] == player.get_color():
                    score += 20
                if self.board[i][j] == self.board[i + 3][j + 3] == self.board[i + 2][j + 2] == opponent.get_color() and \
                        self.board[i + 1][j + 1] == player.get_color():
                    score += 20
                if self.board[i + 3][j + 3] == self.board[i + 1][j + 1] == self.board[i + 2][
                    j + 2] == opponent.get_color() and \
                        self.board[i][j] == player.get_color():
                    score += 20
        return score

    def vertical_eval(self, opponent, player):
        score = 0
        for i in range(self.rows):
            for j in range(self.columns - 3):
                if self.board[i][j] == self.board[i][j + 1] == \
                        self.board[i][j + 2] == player.get_color() and \
                        self.board[i][j + 3] != opponent.get_color():  # R R R ' '
                    score += 50
                if self.board[i][j] == self.board[i][j + 1] == player.get_color() and \
                        self.board[i][j + 2] != opponent.get_color() and \
                        self.board[i][j + 3] == player.get_color():  # R R ' ' R
                    score += 50
                if self.board[i][j] == self.board[i][j + 2] == player.get_color() and \
                        self.board[i][j + 1] != opponent.get_color() and \
                        self.board[i][j + 3] == player.get_color():  # R ' ' R R
                    score += 50
                if self.board[i][j] != opponent.get_color() and self.board[i][j + 2] == player.get_color() and \
                        self.board[i][j + 1] == player.get_color() and \
                        self.board[i][j + 3] == player.get_color():  # ' ' R R R
                    score += 50
                if self.board[i][j] == self.board[i][j + 1] == \
                        self.board[i][j + 2] == player.get_color() and \
                        self.board[i][j + 3] == opponent.get_color():  # R R R C
                    score += 10
                if self.board[i][j] == self.board[i][j + 1] == player.get_color() and \
                        self.board[i][j + 2] == opponent.get_color() and \
                        self.board[i][j + 3] == player.get_color():  # R R C R
                    score += 10
                if self.board[i][j] == self.board[i][j + 2] == player.get_color() and \
                        self.board[i][j + 1] == opponent.get_color() and \
                        self.board[i][j + 3] == player.get_color():  # R C R R
                    score += 10
                if self.board[i][j] == opponent.get_color() and self.board[i][j + 2] == player.get_color() and \
                        self.board[i][j + 1] == player.get_color() and \
                        self.board[i][j + 3] == player.get_color():  # C R R R
                    score += 20
                if self.board[i][j] == self.board[i][j + 1] == \
                        self.board[i][j + 2] == opponent.get_color() and \
                        self.board[i][j + 3] == player.get_color():  # C C C R
                    score += 20
                if self.board[i][j] == self.board[i][j + 1] == opponent.get_color() and \
                        self.board[i][j + 2] == player.get_color() and \
                        self.board[i][j + 3] == opponent.get_color():  # C C R C
                    score += 20
                if self.board[i][j] == self.board[i][j + 2] == opponent.get_color() and \
                        self.board[i][j + 1] == player.get_color() and \
                        self.board[i][j + 3] == opponent.get_color():  # C R C C
                    score += 20
                if self.board[i][j] == player.get_color() and self.board[i][j + 2] == opponent.get_color() and \
                        self.board[i][j + 1] == opponent.get_color() and \
                        self.board[i][j + 3] == opponent.get_color():  # R C C C
                    score += 20
        return score

    def horizontal_eval(self, opponent, player):
        score = 0
        for i in range(self.rows - 3):
            for j in range(self.columns):
                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == player.get_color() and \
                        self.board[i + 3][j] != opponent.get_color():
                    score += 50
                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 3][j] == player.get_color() and \
                        self.board[i + 2][j] != opponent.get_color():
                    score += 50
                if self.board[i][j] == self.board[i + 2][j] == self.board[i + 3][j] == player.get_color() and \
                        self.board[i + 1][j] != opponent.get_color():
                    score += 50
                if self.board[i + 2][j] == self.board[i + 1][j] == self.board[i + 3][j] == player.get_color() and \
                        self.board[i][j] != opponent.get_color():
                    score += 50

                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == player.get_color() and \
                        self.board[i + 3][j] == opponent.get_color():
                    score += 10
                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 3][j] == player.get_color() and \
                        self.board[i + 2][j] == opponent.get_color():
                    score += 10
                if self.board[i][j] == self.board[i + 2][j] == self.board[i + 3][j] == player.get_color() and \
                        self.board[i + 1][j] == opponent.get_color():
                    score += 10
                if self.board[i + 2][j] == self.board[i + 1][j] == self.board[i + 3][j] == player.get_color() and \
                        self.board[i][j] == opponent.get_color():
                    score += 10

                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == opponent.get_color() and \
                        self.board[i + 3][j] == player.get_color():
                    score += 20
                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 3][j] == opponent.get_color() and \
                        self.board[i + 2][j] == player.get_color():
                    score += 20
                if self.board[i][j] == self.board[i + 2][j] == self.board[i + 3][j] == opponent.get_color() and \
                        self.board[i + 1][j] == player.get_color():
                    score += 20
                if self.board[i + 2][j] == self.board[i + 1][j] == self.board[i + 3][j] == opponent.get_color() and \
                        self.board[i][j] == player.get_color():
                    score += 20

        return score

    def negative_diagonal_eval(self, opponent, player):
        score = 0
        for j in range(self.columns - 3):
            for i in range(3, self.rows):
                if self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 2][j + 2] == player.get_color() and \
                        self.board[i - 3][j + 3] != opponent.get_color():
                    score += 50
                if self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 3][j + 3] == player.get_color() and \
                        self.board[i - 2][j + 2] != opponent.get_color():
                    score += 50
                if self.board[i][j] == self.board[i - 3][j + 3] == self.board[i - 2][j + 2] == player.get_color() and \
                        self.board[i - 1][j + 1] != opponent.get_color():
                    score += 50
                if self.board[i - 3][j + 3] == self.board[i - 1][j + 1] == self.board[i - 2][
                    j + 2] == player.get_color() and \
                        self.board[i][j] != opponent.get_color():
                    score += 50
                if self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 2][j + 2] == player.get_color() and \
                        self.board[i - 3][j + 3] == opponent.get_color():
                    score += 10
                if self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 3][j + 3] == player.get_color() and \
                        self.board[i - 2][j + 2] == opponent.get_color():
                    score += 10
                if self.board[i][j] == self.board[i - 3][j + 3] == self.board[i - 2][j + 2] == player.get_color() and \
                        self.board[i - 1][j + 1] == opponent.get_color():
                    score += 10
                if self.board[i - 3][j + 3] == self.board[i - 1][j + 1] == self.board[i - 2][
                    j + 2] == player.get_color() and \
                        self.board[i][j] == opponent.get_color():
                    score += 10

                if self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 2][j + 2] == opponent.get_color() and \
                        self.board[i - 3][j + 3] == player.get_color():
                    score += 20
                if self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 3][j + 3] == opponent.get_color() and \
                        self.board[i - 2][j + 2] == player.get_color():
                    score += 20
                if self.board[i][j] == self.board[i - 3][j + 3] == self.board[i - 2][j + 2] == opponent.get_color() and \
                        self.board[i - 1][j + 1] == player.get_color():
                    score += 20
                if self.board[i - 3][j + 3] == self.board[i - 1][j + 1] == self.board[i - 2][
                    j + 2] == opponent.get_color() and \
                        self.board[i][j] == player.get_color():
                    score += 20
        return score

    def count_two_connected(self, player, opponent):
        score = 0
        score += self.vertical_two_eval(opponent, player)
        score += self.horizontal_two_eval(opponent, player)
        score += self.positive_diagonal_two_eval(opponent, player)
        score += self.negative_diagonal_two_eval(opponent, player)
        return score

    def vertical_two_eval(self, opponent, player):
        score = 0
        for i in range(self.rows):
            for j in range(self.columns - 2):
                if self.board[i][j] == self.board[i][j + 1] == player.get_color() and \
                        self.board[i][j + 2] != opponent.get_color():
                    score += 8
                if self.board[i][j + 2] == self.board[i][j + 1] == player.get_color() and \
                        self.board[i][j] != opponent.get_color():
                    score += 8
                if self.board[i][j + 2] == self.board[i][j] == player.get_color() and \
                        self.board[i][j + 1] != opponent.get_color():
                    score += 8

                if self.board[i][j] == self.board[i][j + 1] == player.get_color() and \
                        self.board[i][j + 2] == opponent.get_color():
                    score -= 1
                if self.board[i][j + 2] == self.board[i][j + 1] == player.get_color() and \
                        self.board[i][j] == opponent.get_color():
                    score -= 1
                if self.board[i][j + 2] == self.board[i][j] == player.get_color() and \
                        self.board[i][j + 1] == opponent.get_color():
                    score -= 1

                if self.board[i][j] == self.board[i][j + 1] == opponent.get_color() and \
                        self.board[i][j + 2] == player.get_color():
                    score += 3
                if self.board[i][j + 2] == self.board[i][j + 1] == opponent.get_color() and \
                        self.board[i][j] == player.get_color():
                    score += 3
                if self.board[i][j + 2] == self.board[i][j] == opponent.get_color() and \
                        self.board[i][j + 1] == player.get_color():
                    score += 3
        return score

    def horizontal_two_eval(self, opponent, player):
        score = 0
        for i in range(self.rows - 2):
            for j in range(self.columns):
                if self.board[i][j] == self.board[i + 1][j] == player.get_color() and \
                        self.board[i + 2][j] != opponent.get_color():
                    score += 8
                if self.board[i + 2][j] == self.board[i + 1][j] == player.get_color() and \
                        self.board[i][j] != opponent.get_color():
                    score += 8
                if self.board[i + 2][j] == self.board[i][j] == player.get_color() and \
                        self.board[i + 1][j] != opponent.get_color():
                    score += 8

                if self.board[i][j] == self.board[i + 1][j] == player.get_color() and \
                        self.board[i + 2][j] == opponent.get_color():
                    score -= 1
                if self.board[i + 2][j] == self.board[i + 1][j] == player.get_color() and \
                        self.board[i][j] == opponent.get_color():
                    score -= 1
                if self.board[i + 2][j] == self.board[i][j] == player.get_color() and \
                        self.board[i + 1][j] == opponent.get_color():
                    score -= 1

                if self.board[i][j] == self.board[i + 1][j] == opponent.get_color() and \
                        self.board[i + 2][j] == player.get_color():
                    score += 15
                if self.board[i + 2][j] == self.board[i + 1][j] == opponent.get_color() and \
                        self.board[i][j] == player.get_color():
                    score += 15
                if self.board[i + 2][j] == self.board[i][j] == opponent.get_color() and \
                        self.board[i + 1][j] == player.get_color():
                    score += 15
        return score

    def positive_diagonal_two_eval(self, opponent, player):
        score = 0
        for i in range(self.rows - 2):
            for j in range(self.columns - 2):
                if self.board[i][j] == self.board[i + 1][j + 1] == player.get_color() and \
                        self.board[i + 2][j + 2] != opponent.get_color():
                    score += 10
                if self.board[i + 2][j + 2] == self.board[i + 1][j + 1] == player.get_color() and \
                        self.board[i][j] != opponent.get_color():
                    score += 10
                if self.board[i + 2][j + 2] == self.board[i][j] == player.get_color() and \
                        self.board[i + 1][j + 1] != opponent.get_color():
                    score += 10
                if self.board[i][j] == self.board[i + 1][j + 1] == player.get_color() and \
                        self.board[i + 2][j + 2] == opponent.get_color():
                    score -= 1
                if self.board[i + 2][j + 2] == self.board[i + 1][j + 1] == player.get_color() and \
                        self.board[i][j] == opponent.get_color():
                    score -= 1
                if self.board[i + 2][j + 2] == self.board[i][j] == player.get_color() and \
                        self.board[i + 1][j + 1] == opponent.get_color():
                    score -= 1
                if self.board[i][j] == self.board[i + 1][j + 1] == opponent.get_color() and \
                        self.board[i + 2][j + 2] == player.get_color():
                    score += 15
                if self.board[i + 2][j + 2] == self.board[i + 1][j + 1] == opponent.get_color() and \
                        self.board[i][j] == player.get_color():
                    score += 15
                if self.board[i + 2][j + 2] == self.board[i][j] == opponent.get_color() and \
                        self.board[i + 1][j + 1] == player.get_color():
                    score += 15
        return score

    def negative_diagonal_two_eval(self, opponent, player):
        score = 0
        for j in range(self.columns - 2):
            for i in range(2, self.rows):
                if self.board[i][j] == self.board[i - 1][j + 1] == player.get_color() and \
                        self.board[i - 2][j + 2] != opponent.get_color():
                    score += 10
                if self.board[i - 2][j + 2] == self.board[i - 1][j + 1] == player.get_color() and \
                        self.board[i][j] != opponent.get_color():
                    score += 10
                if self.board[i][j] == self.board[i - 2][j + 2] == player.get_color() and \
                        self.board[i - 1][j + 1] != opponent.get_color():
                    score += 10

                if self.board[i][j] == self.board[i - 1][j + 1] == player.get_color() and \
                        self.board[i - 2][j + 2] == opponent.get_color():
                    score -= 1
                if self.board[i - 2][j + 2] == self.board[i - 1][j + 1] == player.get_color() and \
                        self.board[i][j] == opponent.get_color():
                    score -= 1
                if self.board[i][j] == self.board[i - 2][j + 2] == player.get_color() and \
                        self.board[i - 1][j + 1] == opponent.get_color():
                    score -= 1

                if self.board[i][j] == self.board[i - 1][j + 1] == opponent.get_color() and \
                        self.board[i - 2][j + 2] == player.get_color():
                    score += 15
                if self.board[i - 2][j + 2] == self.board[i - 1][j + 1] == opponent.get_color() and \
                        self.board[i][j] == player.get_color():
                    score += 15
                if self.board[i][j] == self.board[i - 2][j + 2] == opponent.get_color() and \
                        self.board[i - 1][j + 1] == player.get_color():
                    score += 15
        return score
