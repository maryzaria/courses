from functools import total_ordering


@total_ordering
class RomanNumeral:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number}'

    def __int__(self):
        return RomanNumeral.roman_to_int(self.number)

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) == int(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) > int(other)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            n = self.__int__() + other.__int__()
            return RomanNumeral(RomanNumeral.int_to_roman(n))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            n = int(self) - int(other)
            return RomanNumeral(RomanNumeral.int_to_roman(n))
        return NotImplemented

    @staticmethod
    def roman_to_int(number):
        roman_int = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
                     'D': 500, 'CM': 900, 'M': 1000}
        res = 0
        rom_num = number
        while len(rom_num) > 0:
            if rom_num[0:2] in roman_int:
                res += roman_int[rom_num[0:2]]
                rom_num = rom_num[2:]
            else:
                res += roman_int[rom_num[0]]
                rom_num = rom_num[1:]
        return res

    @staticmethod
    def int_to_roman(number):
        int_roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
                     10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
                     100: 'C', 400: 'CD',  500: 'D', 900: 'CM', 1000: 'M'}
        res = ''
        for n in sorted(int_roman, reverse=True):
            while number >= n:
                res += int_roman[n]
                number -= n
        return res

# TEST_4:
a = RomanNumeral('X')
b = RomanNumeral('X')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# TEST_5:
number = RomanNumeral('MXL') + RomanNumeral('MCDVIII') - RomanNumeral('I')

print(number)
print(int(number))

# TEST_6:
number = RomanNumeral('I') + RomanNumeral('II') + RomanNumeral('III') - RomanNumeral('V')

print(number)
print(int(number))

# TEST_7:
romans1 = ['I', 'X', 'L', 'IV', 'IX', 'XLV', 'CXXIV', 'MCMXCIV']
romans2 = ['I', 'V', 'L', 'VI', 'XI', 'XXV', 'CDXLVIII', 'MCMXCI']

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) + RomanNumeral(y)
    print(number, int(number))

# TEST_8:
romans1 = ['III', 'X', 'L', 'C', 'M', 'XXV', 'XC', 'MMMCMXXXV']
romans2 = ['II', 'V', 'X', 'L', 'D', 'IV', 'VIII', 'MCMXCIV']

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) - RomanNumeral(y)
    print(number, int(number))

# TEST_9:
romans = ['I', 'IV', 'IX', 'XII', 'XXV', 'XLV', 'LXIX', 'XC', 'CDXLVIII']

for num in romans:
    print(RomanNumeral(num), int(RomanNumeral(num)))