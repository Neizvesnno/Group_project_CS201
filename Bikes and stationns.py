class Bike:
    def __init__(self, number, price_per_minute):
        self.number = number
        self.price_per_minute = price_per_minute #False - це звичайний (3), а True - електро (5)

    def price(self):
        if self.price_per_minute:
            return 5
        else:
            return 3

    def __str__(self):
        return f'{self.number} {self.price_per_minute}'