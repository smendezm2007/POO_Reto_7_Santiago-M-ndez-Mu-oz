from math import sqrt

# -------------------- CLASE POINT -------------------- #
class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float):
        self._y = value

    def get_x(self) -> float:
        return self._x

    def set_x(self, x: float):
        self._x = x

    def get_y(self) -> float:
        return self._y

    def set_y(self, y: float):
        self._y = y

    def compute_distance(self) -> float:
        return sqrt(self._x**2 + self._y**2)

