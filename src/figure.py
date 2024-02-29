from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    def area(self) -> float:
        return self.get_area()

    @property
    def perimeter(self) -> float:
        return self.get_perimeter()

    @abstractmethod
    def get_area(self) -> float:
        """Calculate figur area"""

    @abstractmethod
    def get_perimeter(self) -> float:
        """Calculate figur perimeter"""

    def add_area(self, other_figure: "Figure") -> float:
        """Sum of area this and other figur"""
        if not isinstance(other_figure, Figure):
            raise ValueError("Argument not figure")
        return self.get_area() + other_figure.get_area()
