"""
basic python script to emulate a car at level-2
"""
# Level-3 code:
# * readability: better than level-2, much better than level-1
# * maintainability: improved, because class attributes and methods are separate. Breathing space
# * usability: usable, can import/inherit classes and also extend


class Car:
    def __init__(
        self,
        brand: str,
        model: str,
        hp: int,
        dimensions_in_m: dict,
        weight_kg: float = None,
        colors_available: list = None,
        repair_locations: dict = None,
    ):
        """
        return a car dict for given attributes

        :param brand: str | brand of car
        :param model: str | model of car
        :param hp: float | power of car in hp
        :param dimensions_in_m: dict | e.g. {"height": 1.2, "length": 3, "width": 1}
        :param weight_kg: float | (optional) in kg
        :param colors_available: list | colors available
        :param repair_locations: dict | e.g. {"Odisha": [{"Bhubaneswar": 10}, {"Cuttack": 12}]}
        :return: dict | containing attributes of car
        """
        self.name = f"{brand} {model}"
        self.hp = hp
        self.dimensions_in_m = dimensions_in_m
        self.weight_kg = weight_kg
        self.colors_available = colors_available
        self.repair_locations = repair_locations
        self.volume = self.get_volume_of_car()
        self.density = self.get_density_of_car()

    def get_volume_of_car(self) -> float:
        height = self.dimensions_in_m.get("height")
        length = self.dimensions_in_m.get("length")
        width = self.dimensions_in_m.get("width")
        return self.get_volume(height=height, length=length, width=width)

    def get_density_of_car(self) -> float:
        if self.weight_kg:
            return self.weight_kg / self.volume
        print("no weight given")
        return 0

    @staticmethod
    def get_volume(height: float, length: float, width: float) -> float:
        volume = height * length * width
        print(f"the volume of the object is {volume}m^3")
        return volume


class AltoCar(Car):
    def __init__(self, model: str, hp: int):
        super().__init__(
            brand="alto",
            model=model,
            hp=hp,
            dimensions_in_m={"height": 1.2, "length": 3, "width": 1},
        )
        self.volume = self.volume + 1


if __name__ == "__main__":
    car_alto_800 = Car(
        brand="alto",
        model="800",
        hp=800,
        dimensions_in_m={"height": 1.2, "length": 3, "width": 1},
    )
    print(car_alto_800)
    car_volume_alter = car_alto_800.volume
    car_volume = car_alto_800.get_volume_of_car()
    random_volume = car_alto_800.get_volume(1, 1, 1)

    alto_car = AltoCar(model="neu", hp=800)
    print(alto_car)
