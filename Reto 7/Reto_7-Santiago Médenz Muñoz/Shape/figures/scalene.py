from math import sqrt, acos, atan, degrees
from Shape.figures.triangle import Triangle
from Shape.core.decorators import timing

class Scalene(Triangle):
    def __init__(self, a: float, b: float, c: float):
        super().__init__(a, b, c)
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.inner_angles = self.compute_inner_angles()

    @timing("scalene.compute_area")
    def compute_area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def compute_inner_angles(self) -> list[float]:
        A = degrees(acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)))
        B = degrees(acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c)))
        C = 180 - A - B
        return [A, B, C]

    def __str__(self):
        return (
            f"Scalene Triangle\n"
            f"Sides: a={self.a}, b={self.b}, c={self.c}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Angles: {self.inner_angles}"
        )
