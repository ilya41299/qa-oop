## ООП на практике

### Цель:

Научиться писать код в ООП стиле

### Описание:

Создать базовый класс геометрической фигуры (Figure). 

Реализовать классы геометрических фигур Треугольник, Прямоугольник, Квадрат, Круг (Triangle, Rectangle, Square, Circle).
- Каждый класс должен располагаться в отдельном файле с соответствующим названием (например, `class Triangle` => `triangle.py`).
- Все файлы с классами должны находиться в директории `src/` в корне репозитория.
- Каждая фигура должна иметь методы для вычисления площади(`get_area()`) и периметра(`get_perimeter()`)
- Треугольник должен задаваться тремя сторонами, если треугольник создать нельзя, то выбрасывать ошибку `raise ValueError`.

Все вычисляемые свойства должны вычисляться по формулам для соответствующих геометрических фигур (никакого хардкода значений).

Каждая фигура должна реализовать метод `add_area(figure)` который должен принимать другую геометрическую фигуру и возвращать сумму площадей этих фигур.

Если в метод передана не геометрическая фигура, то нужно выбрасывать ошибку `raise ValueError`.

Пример работы с одним из классов фигуры:

```shell
>>> square = Square(10) # Так создаем квадрат со стороной 10
>>> square.area
100
>>> triangle = Triangle(13, 14, 15) # Так создаем треугольник со сторонами 13, 14, 15
>>> triangle.area
84
>>> triangle.add_area(square)
184
```