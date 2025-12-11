from Shape.core.point import Point
from Shape.core.line import Line

class Shape:
    shape_type: str = "Shape"

    def __init__(self, vertices: list[Point] = None, edges: list[Line] = None):
        self.vertices = vertices if vertices else []
        self.edges = edges if edges else []
        self.inner_angles = []
        self.is_regular = False
        self.area = 0.0
        self.perimeter = 0.0

    @classmethod
    def set_shape_type(cls, shape_type: str):
        cls.shape_type = shape_type

    @classmethod
    def get_shape_type(cls) -> str:
        return cls.shape_type

    def compute_area(self) -> float:
        return self.area

    def compute_perimeter(self) -> float:
        return self.perimeter

    def compute_inner_angles(self) -> list[float]:
        return self.inner_angles
