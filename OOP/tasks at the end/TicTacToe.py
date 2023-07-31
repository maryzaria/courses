class TicTacToe:
    def __init__(self):
        self.field = [[' '] * 3 for _ in range(3)]
        self.hod = 'X'
        self.step = 0

    def mark(self, col, row):
        if self.winner() is None:
            if self.field[col -1][row - 1] == ' ':
                self.field[col - 1][row - 1] = self.hod
                self.hod = 'O' if self.hod == 'X' else 'X'
                self.step += 1
            else:
                print('Недоступная клетка')

        else:
            print('Игра окончена')



    def winner(self):
        for row in self.field:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        for i in range(3):
            if self.field[0][i] == self.field[1][i] == self.field[2][i] != ' ':
                return self.field[0][i]
        if self.field[0][0] == self.field[1][1] == self.field[2][2] != ' ':
            return self.field[0][0]
        elif self.field[0][2] == self.field[1][1] == self.field[2][0] != ' ':
            return self.field[1][1]
        elif self.step >= 9:
            return 'Ничья'
        return None

    def show(self):
        print('\n-----\n'.join(list('|'.join(row) for row in self.field)))



# TEST_1:
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 1)
tictactoe.mark(1, 1)

tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.mark(2, 1)
tictactoe.show()