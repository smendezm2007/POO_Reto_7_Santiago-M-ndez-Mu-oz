from math import sqrt, acos, atan, degrees
from Shape.figures.triangle import Triangle
from Shape.core.decorators import timing

class Isosceles(Triangle):
    def __init__(self, equal_side: float, base: float):
        self.equal_side = equal_side
        self.base = base
        super().__init__(equal_side, equal_side, base)
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.inner_angles = self.compute_inner_angles()

    @timing("isosceles.compute_area")
    def compute_area(self) -> float:
        height = sqrt(self.equal_side**2 - (self.base / 2)**2)
        return (self.base * height) / 2

    def compute_perimeter(self) -> float:
        return 2 * self.equal_side + self.base

    def compute_inner_angles(self) -> list[float]:
        height = sqrt(self.equal_side**2 - (self.base / 2)**2)
        vertex_angle = degrees(2 * acos(height / self.equal_side))
        base_angle = (180 - vertex_angle) / 2
        return [base_angle, base_angle, vertex_angle]

    def __str__(self):
        return (
            f"Isosceles Triangle\n"
            f"Equal Side: {self.equal_side}, Base: {self.base}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Inner Angles: {self.inner_angles}"
        )
