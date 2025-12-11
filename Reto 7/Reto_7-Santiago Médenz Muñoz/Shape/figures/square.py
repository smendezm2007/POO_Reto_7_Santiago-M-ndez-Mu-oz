from Shape.figures.rectangle import Rectangle
from Shape.core.decorators import timing

class Square(Rectangle):
    def __init__(self, side: float):
        self.side = side
        super().__init__(side, side)
        self.area = self.compute_area()
        self.perimeter = self.compute_perimeter()
        self.inner_angles = self.compute_inner_angles()

    @timing("square.compute_area")
    def compute_area(self) -> float:
        return self.side ** 2

    def compute_perimeter(self) -> float:
        return 4 * self.side

    def __str__(self):
        return (
            f"Square\n"
            f"Side: {self.side}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Inner Angles: {self.inner_angles}"
        )
