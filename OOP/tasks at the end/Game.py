from random import randint


class Cell:
    def __init__(self, rows, cols, mines=False, open=False, neighbours=0):
        self.row = rows
        self.col = cols
        self.mine = mines
        self.open = open
        self.neighbours = neighbours

    def __repr__(self):
        return f'Cell({self.row}, {self.col}, {self.mine})'


class Game:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = self.fill_board()

    def show(self):
        print('\n-----\n'.join(list('|'.join(map(str, row)) for row in self.board)))

    def fill_board(self):
        board = [[Cell(i, j) for i in range(self.cols)] for j in range(self.rows)]

        for _ in range(self.mines):
            i = randint(0, self.rows - 1)
            j = randint(0, self.cols - 1)
            board[i][j].mine = True

        for r in range(self.rows):
            for c in range(self.cols):
                total = 0
                for i, j in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    if 0 <= r + i < self.rows and 0 <= c + j < self.cols and board[r + i][c + j].mine:
                        total += 1
                board[r][c].neighbours = total

        return board

# # TEST_4:
# game = Game(10, 8, 14)
#
# for c in (0, -1):
#     for r in range(1, game.rows - 1):
#         cell = game.board[r][c]
#         print(0 <= cell.neighbours <= 5, type(cell))





game = Game(5, 15, 40)
# # print(game.board)
game.show()
