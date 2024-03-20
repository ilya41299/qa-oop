from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a: float, b: float):
        if a <= 0 or b <= 0:
            raise ValueError(f"Rectangle with sides {a}, {b} does not exist")
        self.a = a
        self.b = b

    def get_area(self) -> float:
        return self.a * self.b

    def get_perimeter(self) -> float:
        return 2 * (self.a + self.b)
