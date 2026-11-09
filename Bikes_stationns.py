class Station:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number}'


class Bike:
    def __init__(self, number, type, station):
        self.number = number
        self.type = type
        self.station = station
        self.price_per_minute = 5 if type == "electro" else 2
