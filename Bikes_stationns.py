class Station(Bike):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number}


class Bike:
    def __init__(self, number, type, station):
        self.number = number
        self.type = type
        self.station = station

    def price(self):
        if self.price_per_minute:
            return 5
        else:
            return 2
