"""
here we put utils related to dimensions
"""

def get_volume(height: float, length: float, width: float) -> float:
    volume = height * length * width
    print(f"the volume of the object is {volume}m^3")
    return volume