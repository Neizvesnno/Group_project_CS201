from datetime import timedelta

from Bikes_stationns import Bike, Station
from Client import Client
from Trip import Trip

data_set = {
    "stations": {1: "Станція А", 2: "Станція Б"},
    "bikes": [
        ("KB1001", "regular", 1),
        ("KB1002", "electro", 1),
        ("KB1003", "regular", 1),
        ("KB1004", "regular", 1),
        ("KB2001", "electro", 2),
    ],
    "clients": [
        ("Оля", 300),
        ("Тарас", 100),
    ],
    "rides": [
        {"client": "Тарас", "bike": "KB2001", "from_station": 2, "to_station": 1, "minutes": 15},
        {"client": "Оля", "bike": None, "from_station": 2, "to_station": 1, "minutes": 0},
        {"client": "Оля", "bike": "KB1002", "from_station": 1, "to_station": 2, "minutes": 20},
        {"client": "Тарас", "bike": "KB1001", "from_station": 1, "to_station": 2, "minutes": 10},
    ],
    "expected": {
        "balances": {"Оля": 200, "Тарас": 5},
        "revenue": 195,
        "bikes_on_station": {1: 3, 2: 2},
    },
}


def build_world(data):
    station_objects = {station_id: Station(station_id) for station_id in data["stations"]}
    stations = {station_id: [] for station_id in data["stations"]}
    bikes = {}
    for number, kind, station_id in data["bikes"]:
        bike = Bike(number, kind, station_objects[station_id])
        bikes[number] = bike
        stations[station_id].append(bike)
    clients = {
        name: Client(client_id, name, balance)
        for client_id, (name, balance) in enumerate(data["clients"], start=1)
    }
    return stations, bikes, clients


def run_ride(ride, stations, bikes, clients):
    client = clients[ride["client"]]
    source = stations[ride["from_station"]]
    target = stations[ride["to_station"]]

    if not source:
        return "empty_station", None
    bike = bikes[ride["bike"]] if ride["bike"] else source[0]
    if bike not in source:
        return "bike_not_here", None

    trip = Trip(source, bike, client)
    if not trip.take_bike():
        return "refused", None

    trip.start_time -= timedelta(minutes=ride["minutes"], seconds=-30)
    trip.return_bike(target)
    return "ok", trip


def print_report(stations, station_names, revenue):
    print("Звіт:")
    for station_id, bikes_here in stations.items():
        numbers = ", ".join(bike.number for bike in bikes_here) or "порожньо"
        print(f"{station_names[station_id]}: {len(bikes_here)} велосипедів ({numbers})")
    print(f"Заробили загалом: {round(revenue, 2)} грн")


def main():
    stations, bikes, clients = build_world(data_set)
    names = data_set["stations"]
    revenue = 0

    print("Поїздки:")
    for ride in data_set["rides"]:
        who = ride["client"]
        status, trip = run_ride(ride, stations, bikes, clients)
        if status == "ok":
            revenue += trip.cost
            print(f"{who}: {trip.bike.number}, {names[ride['from_station']]} -> "
                  f"{names[ride['to_station']]}, {ride['minutes']} хв, "
                  f"сплатив {round(trip.cost, 2)} грн")
        elif status == "empty_station":
            print(f"{who}: на станції «{names[ride['from_station']]}» немає велосипедів")
        elif status == "bike_not_here":
            print(f"{who}: велосипеда {ride['bike']} немає на станції "
                  f"«{names[ride['from_station']]}»")
        else:
            print(f"{who}: взяти велосипед не вдалося (можливо, не вистачає грошей)")

    print("\nБаланси клієнтів:")
    for client in clients.values():
        print(f"{client.name}: {round(client.balance, 2)} грн")
    print()
    print_report(stations, names, revenue)

    expected = data_set["expected"]
    for name, balance in expected["balances"].items():
        assert round(clients[name].balance, 2) == balance, f"баланс {name}"
    assert round(revenue, 2) == expected["revenue"], "виручка мережі"
    for station_id, count in expected["bikes_on_station"].items():
        assert len(stations[station_id]) == count, f"велосипедів на станції {station_id}"
    print("\nУсі перевірки пройдені.")


if __name__ == "__main__":
    main()