from random import shuffle


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'


class Deck:
    def __init__(self):
        self.deck = [Card(s, r) for s in '♣♢♡♠' for r in ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')]

    def shuffle(self):
        if len(self.deck) == 52:
            shuffle(self.deck)
        else:
            raise ValueError('Перемешивать можно только полную колоду')

    def deal(self):
        if len(self.deck) == 0:
            raise ValueError('Все карты разыграны')
        return self.deck.pop()

    def __str__(self):
        return f'Карт в колоде: {len(self.deck)}'


deck = Deck()

deck.deal()

try:
    deck.shuffle()
except ValueError as error:
    print(error)