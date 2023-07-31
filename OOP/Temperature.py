class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)

    def __str__(self):
        return f'{round(self.temperature, 2)}°C'

    def to_fahrenheit(self):
        return (self.temperature * 9 + 32 * 5) / 5

    @classmethod
    def from_fahrenheit(cls, tf):
        return cls(5 / 9 * (tf - 32))


t = Temperature.from_fahrenheit(41)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())