import datetime
import math


class Trip:
    def __init__(self, station: list, bike, user):
        self.station = station
        self.bike = bike
        self.user = user

        self.is_active = False
        self.cost = 0

        self.start_time = None
        self.end_time = None

    def take_bike(self):
        # Не можна повторно почати вже активну поїздку
        if self.is_active:
            return False

        # Перевіряємо, чи є велосипед на станції
        if self.bike not in self.station:
            return False

        # Перевіряємо, чи вистачить коштів хоча б на 5 хвилин
        if self.user.balance < self.bike.price_per_minute * 5:
            return False

        self.station.remove(self.bike)

        self.start_time = datetime.datetime.now()
        self.is_active = True

        return True

    def return_bike(self, destination_station=None):
        # Не можна завершити неактивну поїздку
        if not self.is_active:
            return False

        self.end_time = datetime.datetime.now()

        # Обчислюємо вартість поїздки
        self.calculate_cost()

        # Списуємо кошти з балансу користувача
        self.user.balance -= self.cost

        # Якщо станцію не вказано, повертаємо велосипед на початкову
        if destination_station is None:
            destination_station = self.station

        # Повертаємо велосипед на станцію призначення
        if self.bike not in destination_station:
            destination_station.append(self.bike)

        self.is_active = False

        return True

    def calculate_cost(self):
        if self.start_time is None or self.end_time is None:
            return 0

        duration = self.end_time - self.start_time

        # Кожна розпочата хвилина оплачується як повна
        minutes = math.ceil(duration.total_seconds() / 60)

        self.cost = minutes * self.bike.price_per_minute

        return self.cost
