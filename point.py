from typing import Self
import math

class Vector():
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __add__(self, point: Self) -> Self:
        return Vector(self.x + point.x, self.y + point.y)

    def __sub__(self, point: Self) -> Self:
        return Vector(self.x - point.x, self.y - point.y)

    def __mul__(self, scalar: int) -> Self:
        return Vector(self.x * scalar, self.y * scalar)

    def __div__(self, scalar: int) -> Self | None:
        if scalar != 0:
            return Vector(self.x // scalar, self.y // scalar)
        return None

    def __truediv__(self, scalar: int) -> Self | None:
        return self.__div__(scalar)

    def __eq__(self, point: Self) -> bool:
        if self.x == point.x and self.y == point.y:
            return True
        else:
            return False

    def copy(self) -> Self:
        return Vector(self.x, self.y)

    def asTuple(self) -> tuple[int, int]:
        return self.x, self.y

    def magnitude(self, point: Self) -> int:
        vec = self.__sub__(point)
        return int(math.sqrt((vec.x ** 2) + (vec.y ** 2)))

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
