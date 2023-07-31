class Pet:
    pets = []

    def __init__(self, name):
        self.name = name
        Pet.pets.append(self)

    @classmethod
    def first_pet(cls):
        try:
            return cls.pets[0]
        except IndexError:
            return None

    @classmethod
    def last_pet(cls):
        try:
            return cls.pets[-1]
        except IndexError:
            return None

    @classmethod
    def num_of_pets(cls):
        return len(cls.pets)




# TEST_1:
print(Pet.first_pet())
print(Pet.last_pet())
print(Pet.num_of_pets())