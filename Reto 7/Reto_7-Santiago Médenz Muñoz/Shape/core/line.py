from math import sqrt
from Shape.core.point import Point

# -------------------- CLASE LINE -------------------- #
class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.start_point = start_point
        self.end_point = end_point
        self.length = self._calculate_length()

    def _calculate_length(self) -> float:
        dx = self.end_point.get_x() - self.start_point.get_x()
        dy = self.end_point.get_y() - self.start_point.get_y()
        return sqrt(dx**2 + dy**2)
