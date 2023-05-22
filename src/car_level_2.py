"""
basic python script to emulate a car at level-2
"""
# Level-2 code:
# * readability: better than level-1
# * maintainability:better than level-1, possibility of tangling up of definitions
# * usability: same as level-1


def get_car(
    name: str,
    hp: int,
    dimensions_in_m: dict,
    weight_kg: float = None,
    colors_available: list = None,
    repair_locations: dict = None,
) -> dict:
    """
    return a car dict for given attributes

    :param name: str | name of car
    :param hp: float | power of car in hp
    :param dimensions_in_m: dict | e.g. {"height": 1.2, "length": 3, "width": 1}
    :param weight_kg: float | (optional) in kg
    :param colors_available: list | colors available
    :param repair_locations: dict | e.g. {"Odisha": [{"Bhubaneswar": 10}, {"Cuttack": 12}]}
    :return: dict | containing attributes of car
    """
    car_name = name
    car_hp = hp
    car_weight_kg = weight_kg
    car_colors_available = colors_available
    car_dimensions_in_m = dimensions_in_m
    car_repair_locations = repair_locations
    return {
        "car_name": car_name,
        "car_hp": car_hp,
        "car_weight_kg": car_weight_kg,
        "car_colors_available": car_colors_available,
        "car_dimensions_in_m": car_dimensions_in_m,
        "car_repair_locations": car_repair_locations,
    }


def get_volume_of_car(car: dict) -> float:
    car_dimensions = car.get("car_dimensions_in_m")
    height = car_dimensions.get("height")
    length = car_dimensions.get("length")
    width = car_dimensions.get("width")
    return get_volume(height=height, length=length, width=width)


def get_volume(height: float, length: float, width: float) -> float:
    volume = height * length * width
    print(f"the volume of the object is {volume}m^3")
    return volume


if __name__ == "__main__":
    car_alto_800 = get_car(
        name="alto 800",
        hp=800,
        dimensions_in_m={"height": 1.2, "length": 3, "width": 1},
    )
    print(car_alto_800)
    car_volume = get_volume_of_car(car=car_alto_800)
    print(car_volume)
