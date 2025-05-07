class Vehicle:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year

    def get_info(self):
        return f"{self._year} {self._brand} {self._model}"

    def move(self):
        print("The vehicle is moving.")


class Car(Vehicle):
    def move(self):
        print("Driving on the road ")


class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ")


class Boat(Vehicle):
    def move(self):
        print("Sailing on the water ")


def main():
    vehicles = [
        Car("Toyota", "Corolla", 2020),
        Plane("Boeing", "747", 2015),
        Boat("Yamaha", "242X", 2022)
    ]

    for v in vehicles:
        print(v.get_info())
        v.move()

if __name__ == "__main__":
    main()
