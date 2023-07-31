class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, items=()):
        self.items = items if items else []

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)

    def remove(self, name):
        self.items = [item for item in self.items if item.name != name]

    def __str__(self):
        return '\n'.join([str(item) for item in self.items])


# TEST_4:
shopping_cart = ShoppingCart([Item('Banana', 100), Item('Apple', 120), Item('Orange', 110), Item('Tomato', 180), Item('Cucumber', 150)])

shopping_cart.add(Item('Banana', 100))
print(shopping_cart)
print(shopping_cart.total())

shopping_cart.remove('Banana')
print(shopping_cart)
print(shopping_cart.total())