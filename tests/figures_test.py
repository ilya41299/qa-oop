import pytest
from src import Circle, Rectangle, Square, Triangle

from .conftest import (
    CorrectIntGenerator,
    CorrectFloatGenerator,
    IncorrectIntGenerator,
    IncorrectFloatGenerator,
    CircleGenerator,
    SquareGenerator,
    RectangleGenerator,
    TriangleGenerator,
)


@pytest.mark.parametrize(
    "generator",
    [
        CorrectIntGenerator,
        CorrectFloatGenerator,
    ],
)
@pytest.mark.parametrize(
    ("figure", "figure_generator"),
    [
        (Square, SquareGenerator),
        (Rectangle, RectangleGenerator),
        (Circle, CircleGenerator),
        (Triangle, TriangleGenerator),
    ],
)
def test_get_perimeter(figure, generator, figure_generator):
    sides, _, perimeter = figure_generator(generator()).generate_figure()
    test_figure = figure(*sides)
    assert test_figure.get_perimeter() == perimeter, f"Correct perimeter {perimeter}"


@pytest.mark.parametrize(
    "generator",
    [
        CorrectIntGenerator,
        CorrectFloatGenerator,
    ],
)
@pytest.mark.parametrize(
    ("figure", "figure_generator"),
    [
        (Square, SquareGenerator),
        (Rectangle, RectangleGenerator),
        (Circle, CircleGenerator),
        (Triangle, TriangleGenerator),
    ],
)
def test_get_area(figure, generator, figure_generator):
    sides, area, _ = figure_generator(generator()).generate_figure()
    test_figure = figure(*sides)
    assert test_figure.get_area() == area, f"Correct area {area}"


@pytest.mark.parametrize(
    "generator",
    [
        CorrectIntGenerator,
        CorrectFloatGenerator,
    ],
)
@pytest.mark.parametrize(
    ("figure_1", "figure_generator_1"),
    [
        (Square, SquareGenerator),
        (Rectangle, RectangleGenerator),
        (Circle, CircleGenerator),
        (Triangle, TriangleGenerator),
    ],
)
@pytest.mark.parametrize(
    ("figure_2", "figure_generator_2"),
    [
        (Square, SquareGenerator),
        (Rectangle, RectangleGenerator),
        (Circle, CircleGenerator),
        (Triangle, TriangleGenerator),
    ],
)
def test_add_area(
    figure_1, figure_2, generator, figure_generator_1, figure_generator_2
):
    sides_1, area_1, _ = figure_generator_1(generator()).generate_figure()
    sides_2, area_2, _ = figure_generator_2(generator()).generate_figure()
    test_figure_1 = figure_1(*sides_1)
    test_figure_2 = figure_2(*sides_2)
    assert (
        test_figure_1.add_area(test_figure_2) == area_1 + area_2
    ), f"Correct area {area_1+area_2}"


@pytest.mark.parametrize(
    "generator",
    [
        IncorrectIntGenerator,
        IncorrectFloatGenerator,
    ],
)
@pytest.mark.parametrize(
    ("figure", "figure_generator"),
    [
        (Square, SquareGenerator),
        (Rectangle, RectangleGenerator),
        (Circle, CircleGenerator),
        (Triangle, TriangleGenerator),
    ],
)
def test_negative_init_figure(figure, generator, figure_generator):
    sides, _, _ = figure_generator(generator()).generate_figure()
    with pytest.raises(ValueError):
        figure(*sides)
