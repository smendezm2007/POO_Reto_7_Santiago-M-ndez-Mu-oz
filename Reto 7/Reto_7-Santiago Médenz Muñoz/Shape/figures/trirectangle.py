from math import sqrt, acos, atan, degrees
from Shape.figures.triangle import Triangle
from Shape.core.decorators import timing

class Trirectangle(Triangle):
    def __init__(self, a: float, b: float):
        c = sqrt(a**2 + b**2)
        super().__init__(a, b, c)
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.inner_angles = self.compute_inner_angles()

    @timing("trirectangle.compute_area")
    def compute_area(self) -> float:
        return (self.a * self.b) / 2

    def compute_inner_angles(self) -> list[float]:
        return [
            90.0,
            degrees(atan(self.b / self.a)),
            degrees(atan(self.a / self.b)),
        ]

    def __str__(self):
        return (
            f"Trirectangle\n"
            f"Sides: a={self.a}, b={self.b}, c={self.c}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Angles: {self.inner_angles}"
        )
