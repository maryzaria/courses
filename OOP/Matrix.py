class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self._matrix = [[self.value] * self.cols for _ in range(self.rows)]

    def get_value(self, row, col):
        return self._matrix[row][col]

    def set_value(self, row, col, value):
        self._matrix[row][col] = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.rows}, {self.cols})"

    def __str__(self):
        return '\n'.join([' '.join(list(map(str, self._matrix[i]))) for i in range(self.rows)])

    def __pos__(self):
        return Matrix(self.rows, self.cols, self.value)

    def _new_matrix(self, rows, cols, sign=1, is_round=False, n=None):
        new_matrix = Matrix(self.rows, self.cols)
        for row in range(rows):
            for col in range(cols):
                new_matrix.set_value(row, col, sign * self.get_value(row, col))
                if is_round:
                    new_matrix.set_value(row, col, round(self.get_value(row, col), n))
        return new_matrix

    def __neg__(self):
        return self._new_matrix(self.rows, self.cols, sign=-1)

    def __invert__(self):
        new_m = Matrix(self.cols, self.rows)
        for col in range(self.cols):
            for row in range(self.rows):
                new_m.set_value(col, row, self.get_value(row, col))
        return new_m

    def __round__(self, n=None):
        return self._new_matrix(self.rows, self.cols, is_round=True, n=n)

# TEST_7:
matrix = Matrix(5, 10)

floats = [[7125.900408, 633.354471, -9237.8575119, 2865.3825158, 5509.2609336, 8712.260779, 8317.523947, 2512.4736075,
           -3087.5496014, 3861.68814],
          [-7852.451832, 376.465911, -8142.7867326, -6921.8371407, 3735.7516227, -3322.8019034, 7115.79968,
           -8949.9313078, -7032.4347679, -5217.8236385],
          [-7817.9657992, -4319.716346, -1038.6294521, -2959.8970273, -9263.5713405, 9358.607686, 1429.6576196,
           -9484.68116, 639.6343972, 3444.9938213],
          [-2844.2405153, -2078.2441427, 6812.1367017, 112.3910618, -1116.8662449, 5042.7026276, -5981.6930342,
           4370.9173164, -8851.7648474, 8990.6896422],
          [90.8102435, 5256.6137481, -9743.8477321, -131.5501688, -5920.5976176, 4963.8336619, -4907.3622526,
           8531.2015615, -244.3630074, 3421.8817151]]

for r in range(5):
    for c in range(10):
        matrix.set_value(r, c, floats[r][c])

# print(matrix)
# print()
print(~matrix)
# print(round(matrix, 2))