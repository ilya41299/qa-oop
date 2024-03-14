import random
import math
from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")


class BaseDataGenerator(ABC, Generic[T]):
    @abstractmethod
    def generate_data(self) -> T:
        ...


class CorrectIntGenerator(BaseDataGenerator[int]):
    def generate_data(self) -> int:
        return random.randint(1, 100)


class IncorrectIntGenerator(BaseDataGenerator[int]):
    def generate_data(self) -> int:
        return random.randint(-100, 0)


class CorrectFloatGenerator(BaseDataGenerator[float]):
    def generate_data(self) -> float:
        return random.uniform(1, 100)


class IncorrectFloatGenerator(BaseDataGenerator[float]):
    def generate_data(self) -> float:
        return random.uniform(-100, 0)


class BaseFigureGenerator(ABC, Generic[T]):
    def __init__(self, generator: BaseDataGenerator[T]) -> None:
        super().__init__()
        self.generator = generator

    @abstractmethod
    def generate_figure(self) -> tuple[list[T], float, float]:
        ...


class SquareGenerator(BaseFigureGenerator, Generic[T]):
    def generate_figure(self) -> tuple[list[T], float, float]:
        a = self.generator.generate_data()
        area = a**2
        perimeter = 4 * a
        return [a], area, perimeter


class RectangleGenerator(BaseFigureGenerator, Generic[T]):
    def generate_figure(self) -> tuple[list[T], float, float]:
        a, b = self.generator.generate_data(), self.generator.generate_data()
        area = a * b
        perimeter = 2 * (a + b)
        return [a, b], area, perimeter


class CircleGenerator(BaseFigureGenerator, Generic[T]):
    def generate_figure(self) -> tuple[list[T], float, float]:
        r = self.generator.generate_data()
        area = math.pi * r**2
        perimeter = 2 * math.pi * r
        return [r], area, perimeter


class TriangleGenerator(BaseFigureGenerator, Generic[T]):
    def generate_figure(self) -> tuple[list[T], float, float]:
        a, b = self.generator.generate_data(), self.generator.generate_data()
        angle_c = random.randint(1, 90)
        c = math.sqrt((a * a) + (b * b) - 2 * a * b * math.cos(angle_c / 180 * math.pi))
        perimeter = a + b + c
        half_perimetr = perimeter / 2
        area = math.sqrt(
            half_perimetr
            * (half_perimetr - a)
            * (half_perimetr - b)
            * (half_perimetr - c)
        )
        return [a, b, c], area, perimeter
