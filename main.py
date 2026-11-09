data_set = {
    # Станції
    "stations": {1: "Станція А", 2: "Станція Б"},

    # Велосипеди
    "bikes": [
        ("KB1001", "regular", 1),
        ("KB1002", "electric", 1),
        ("KB1003", "regular", 1),
        ("KB1004", "regular", 1),
        ("KB2001", "electric", 2),
    ],

    # Клієнти
    "clients": [
        ("Оля", 300),
        ("Тарас", 100),
    ],

    # Поїздки
    "rides": [
        # Тарас забирає єдиний велосипед зі станції 2 і вона залишається порожньою
        {"client": "Тарас", "bike": "KB2001", "from_station": 2, "to_station": 1, "minutes": 15},
        # Оля намагається взяти велосипед зі станції 2, де вже нічого немає
        {"client": "Оля", "bike": None, "from_station": 2, "to_station": 1, "minutes": 0},
        # Оля бере електричний велосипед зі станції 1 і повертає на станцію 2
        {"client": "Оля", "bike": "KB1002", "from_station": 1, "to_station": 2, "minutes": 20},
        # Тарас бере звичайний велосипед зі станції 1 і повертає на станцію 2
        {"client": "Тарас", "bike": "KB1001", "from_station": 1, "to_station": 2, "minutes": 10},
    ],

    "expected": {
        "balances": {"Оля": 200, "Тарас": 5},
        # 300 - 100 і 100 - 75 - 20
        "revenue": 195,
        # 75 + 100 + 20
        "bikes_on_station": {1: 3, 2: 2},
        # на станції 1: KB1003, KB1004, KB2001
    },
}


def main():
    print()


if __name__ == "__main__":
    main()