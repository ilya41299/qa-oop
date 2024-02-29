from figure import Figure


class Square(Figure):
    def __init__(self, a: float):
        if a <= 0:
            raise ValueError(f"Square with sides {a} does not exist")
        self.a = a

    def get_area(self) -> float:
        return self.a**2

    def get_perimeter(self) -> float:
        return 4 * self.a
