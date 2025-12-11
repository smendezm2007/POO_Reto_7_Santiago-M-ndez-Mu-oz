from Shape.figures.rectangle import Rectangle
from Shape.figures.square import Square
from Shape.figures.isosceles import Isosceles
from Shape.figures.equilateral import Equilateral
from Shape.figures.scalene import Scalene
from Shape.figures.trirectangle import Trirectangle

if __name__ == "__main__":
    figures = [
        Rectangle(5, 15),
        Square(6),
        Isosceles(15, 7),
        Equilateral(9),
        Scalene(6, 7, 8),
        Trirectangle(7, 9)
    ]

    for i in figures:
        print(i)
        print("---------------------------------------------")
