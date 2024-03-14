from src.figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, r: float):
        if r <= 0:
            raise ValueError(f"Circle with radius {r} does not exist")
        self.r = r

    def get_area(self) -> float:
        return pi * self.r**2

    def get_perimeter(self) -> float:
        return 2 * pi * self.r
