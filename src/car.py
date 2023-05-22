"""
basic python script to emulate a car
"""
# Level-0 code:
# * readability: poor -doesnt use functions
# * maintainability: poor,  definition and execution code is tangled up together
# * usability: poor

# describe car attributes for Alto 800
car_name = "Alto 800"
car_hp = 800
car_weight_kg = 600.54

# data structure vars
car_colors_available = ["black", "grey", "blue"]  # order matters, "ordered"
car_repair_locations = {
    "Odisha": [{"Bhubaneswar": 10}, {"Cuttack": 12}]
}  # order doesnt matter, "unordered"
car_dimensions_in_m = {"height": 1.2, "length": 3, "width": 1}


# describe car attributes for Esteem
car_name_2 = "Esteem"
car_hp_2 = 1000
car_weight_kg_2 = 700.54

# data structure vars
car_colors_available_2 = ["black", "white", "blue"]
car_repair_locations_2 = {"Odisha": [{"Bhubaneswar": 10}, {"Cuttack": 12}]}
car_dimensions_in_m_2 = {"height": 1.2, "length": 3, "width": 1}

print(*car_colors_available)
car_volume = (
    car_dimensions_in_m.get("height")
    * car_dimensions_in_m.get("length")
    * car_dimensions_in_m.get("width")
)
print(f"the volume of the car is {car_volume}m^3")

# Level-1 code:
# * readability: better -does use functions
# * maintainability: better, if definition and execution code is not tangled up together
# * usability: poor, still cannot use the code elsewhere


def print_car_colors() -> None:
    print(*car_colors_available)


def print_car_volume() -> None:
    car_volume = (
        car_dimensions_in_m.get("height")
        * car_dimensions_in_m.get("length")
        * car_dimensions_in_m.get("width")
    )
    print(f"the volume of the car is {car_volume}m^3")


def get_volume(height: float, length: float, width: float) -> float:
    car_volume = height * length * width
    print(f"the volume of the car is {car_volume}m^3")
    return car_volume


if __name__ == "__main__":
    volume_1 = get_volume(
        height=car_dimensions_in_m.get("height"),
        width=car_dimensions_in_m.get("width"),
        length=car_dimensions_in_m.get("length"),
    )
    print(f"volume={volume_1}m^3")

    volume_2 = get_volume(
        height=car_dimensions_in_m_2.get("height"),
        width=car_dimensions_in_m_2.get("width"),
        length=car_dimensions_in_m_2.get("length"),
    )
    print(f"volume={volume_2}m^3")
