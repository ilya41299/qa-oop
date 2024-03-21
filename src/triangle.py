from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError(f"Triangle with sides {a}, {b}, {c} does not exist")
        self.a = a
        self.b = b
        self.c = c

    def get_area(self) -> float:
        half_perimetr = self.get_perimeter() / 2
        return sqrt(
            half_perimetr
            * (half_perimetr - self.a)
            * (half_perimetr - self.b)
            * (half_perimetr - self.c)
        )

    def get_perimeter(self) -> float:
        return self.a + self.b + self.c
