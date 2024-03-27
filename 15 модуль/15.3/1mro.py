from abc import ABC, abstractmethod

class Figure(ABC):
    """
    Абстрактный базовый класс Фигура

    Args and attrs:
        posx (int): координата X
        posy (int): координата Y
        length (int): длина фигуры
        width (int): ширина фигуры
    """
    def __init__(self, posx: int, posy: int, length: int, width: int) -> None:
        self.posx = posx
        self.posy = posy
        self.length = length
        self.width = width

    @abstractmethod
    def move(self, posx: int, posy: int) -> None:
        self.posx = posx
        self.posy = posy

class ResizableMixin:
    def resize(self, length: int, width: int):
        self.length = length
        self.width = width

class Rectangle(Figure, ResizableMixin):
    """Прямоугольник"""
    def move(self, posx: int, posy: int) -> None:
        return super().move(posx, posy)

class Square(Figure, ResizableMixin):
    """Квадрат"""
    def __init__(self, posx: int, posy: int, size: int) -> None:
        super().__init__(posx, posy, size, size)

    def move(self, posx: int, posy: int) -> None:
        return super().move(posx, posy)

rect_1 = Rectangle(posx=10, posy=20, length=5, width=6)
rect_2 = Rectangle(posx=30, posy=40, length=10, width=11)
square_1 = Square(posx=30, posy=40, size=7)

for figure in [rect_1, rect_2, square_1]:
    new_size_x = figure.length * 2
    new_size_y = figure.width * 2
    figure.resize(new_size_x, new_size_y)



test = Rectangle(1, 1, 1, 1)
test_2 = Square(1, 1, 1)