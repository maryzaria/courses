from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, x, y):
        pass


class Knight(ChessPiece):
    def can_move(self, x, y):
        x = ord(x) - 97
        x_self = ord(self.horizontal) - 97
        return abs((x_self - x) * (self.vertical - y)) == 2


class King(ChessPiece):
    def can_move(self, x, y):
        x = ord(x) - 97
        x_self = ord(self.horizontal) - 97
        return abs(x_self - x) <= 1 and abs(self.vertical - y) <= 1 and (x != x_self or y != self.vertical)


# TEST_3:
king = King('e', 3)

print(king.can_move('e', 3))
print(king.can_move('e', 4))
print(king.can_move('b', 1))