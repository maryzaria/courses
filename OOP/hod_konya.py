class Knight:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.color = color
        self.digit_col = 'abcdefgh'.index(self.col) + 1

    def get_char(self):
        return 'N'

    def can_move(self, col, row):
        col = 'abcdefgh'.index(col) + 1
        return abs(self.digit_col - col) * abs(self.row - row) == 2

    def move_to(self, col_x, row_y):
        if self.can_move(col_x, row_y):
            self.col = col_x
            self.row = row_y
            self.digit_col = 'abcdefgh'.index(self.col) + 1

    def draw_board(self):
        for row in range(8, 0, -1):
            for col in 'abcdefgh':
                if self.can_move(col, row):
                    print('*', end='')
                elif col == self.col and row == self.row:
                    print(self.get_char(), end='')
                else:
                    print('.', end='')
            print()



knight = Knight('c', 3, 'white')

print(knight.col, knight.row, knight.digit_col)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
# print(knight.col, knight.row)


knight.draw_board()