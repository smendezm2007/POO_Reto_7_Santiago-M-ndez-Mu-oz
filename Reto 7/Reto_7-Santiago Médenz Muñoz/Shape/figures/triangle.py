from Shape.figures.base_shape import Shape
from Shape.core.decorators import timing

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.inner_angles = self.compute_inner_angles()

    @timing("triangle.compute_area")
    def compute_area(self) -> float:
        return (self.a * self.b) / 2

    def compute_perimeter(self) -> float:
        return self.a + self.b + self.c

    def compute_inner_angles(self) -> list[float]:
        return [60.0, 60.0, 60.0]

    def __str__(self):
        return (
            f"Triangle\n"
            f"Sides: a={self.a}, b={self.b}, c={self.c}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Angles: {self.inner_angles}"
        )
