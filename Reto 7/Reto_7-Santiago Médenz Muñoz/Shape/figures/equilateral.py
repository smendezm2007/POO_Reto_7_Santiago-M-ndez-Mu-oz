from math import sqrt, acos, atan, degrees
from Shape.figures.triangle import Triangle
from Shape.core.decorators import timing

class Equilateral(Triangle):
    def __init__(self, side: float):
        self.side = side
        super().__init__(side, side, side)
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.inner_angles = self.compute_inner_angles()

    @timing("equilateral.compute_area")
    def compute_area(self) -> float:
        return (sqrt(3) / 4) * (self.side ** 2)

    def compute_perimeter(self) -> float:
        return 3 * self.side

    def compute_inner_angles(self) -> list[float]:
        return [60, 60, 60]

    def __str__(self):
        return (
            f"Equilateral Triangle\n"
            f"Side: {self.side}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Inner Angles: {self.inner_angles}"
        )
