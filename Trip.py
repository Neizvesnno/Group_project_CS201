import datetime

class Trip:
    def __init__(self, station: list, bike, user):
        self.station = station
        self.bike = bike
        self.user = user
        self.is_active = True
        self.cost = 0
        self.startTime = datetime.now()
        self.endTime = None

    def take_bike(self):
        if self.user.balance < self.bike.price_per_minute * 5:
            print("Your balance is not enough")
            return 
        self.station.remove(self.bike)


    def return_bike(self):
        if not self.is_active:
            print(f"The ride've been ended in {self.endTime.strftime("%h%m:%s")}")
            return
        self.is_active = False
        self.station.append(self.bike)
        self.endTime = datetime.now()

    def calculate_cost(self):

        if self.startTime and self.endTime:
            duration = self.endTime - self.startTime
            minutes = duration.total_seconds() / 60
            self.cost = minutes * self.bike.price_per_minute

