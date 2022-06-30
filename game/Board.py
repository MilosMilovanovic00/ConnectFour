class Board(object):
    def __init__(self):
        self._columns = 7
        self._rows = 7
        self._board = [[' ' for i in range(self._columns)] for j in range(self._rows)]

    def print_board(self):
        print("+---" * 7, end='')
        print('+')
        for i in range(self._rows):
            for j in range(self._columns):
                print("| " + self._board[i][j] + " ", end='')
            print('|')
            print("+---" * 7, end='')
            print('+')
        print("  1   2   3   4   5   6   7 ")

    def check_if_player_won(self, player):
        for i in range(self._rows):
            for j in range(self._columns - 3):
                if self._board[i][j] == self._board[i][j + 1] == self._board[i][j + 2] \
                        == self._board[i][j + 3] == player.get_color():
                    return True

        for i in range(self._rows - 3):
            for j in range(self._columns):
                if self._board[i][j] == self._board[i + 1][j] == self._board[i + 2][j] \
                        == self._board[i + 3][j] == player.get_color():
                    return True

        for i in range(self._rows - 3):
            for j in range(self._columns - 3):
                if self._board[i][j] == self._board[i + 1][j + 1] == self._board[i + 2][j + 2] \
                        == self._board[i + 3][j + 3] == player.get_color():
                    return True

        for j in range(self._columns - 3):
            for i in range(3, self._rows):
                if self._board[i][j] == self._board[i - 1][j + 1] == self._board[i - 2][j + 2] \
                        == self._board[i - 3][j + 3] == player.get_color():
                    return True

        return False

    def add_chip(self, player, column):
        for row in range(self._rows - 1, -1, -1):
            cell_value = self._board[row][column]
            if cell_value is ' ':
                self._board[row][column] = player.get_color()
                return row
        return -1
