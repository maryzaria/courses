class Postman:
    def __init__(self):
        self.delivery_data = []
        self.houses = []
        self.flats = []

    def add_delivery(self, street, house, flat):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, nes_street):
        for street, house, flat in self.delivery_data:
            if street == nes_street and house not in self.houses:
                self.houses.append(house)
        return self.houses

    def get_flats_for_house(self, nes_street, nes_house):
        for street, house, flat in self.delivery_data:
            if street == nes_street and house == nes_house and flat not in self.flats:
                self.flats.append(flat)
        return self.flats


postman = Postman()
print(postman.delivery_data)
print(postman.get_houses_for_street('3-я ул. Строителей'))
print(postman.get_flats_for_house('3-я ул. Строителей', 25))
postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))