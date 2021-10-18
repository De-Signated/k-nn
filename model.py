from dataclasses import dataclass
import numpy as np


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Triangle:
    a: Point
    b: Point
    c: Point

    def sign(self, p1: Point, p2: Point, p3: Point):
        return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

    def point_inside(self, point: Point):
        d1 = self.sign(point, self.a, self.b)
        d2 = self.sign(point, self.b, self.c)
        d3 = self.sign(point, self.c, self.a)

        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

        return not (has_neg and has_pos)

    def plot(self, plt):
        x = [self.a.x, self.b.x, self.c.x, self.a.x]
        y = [self.a.y, self.b.y, self.c.y, self.a.y]
        plt.plot(x, y)


class FeatureVec:
    point: Point
    col: str

    def __init__(self, x, y, triangle: Triangle, f: float):
        self.point = Point(x, y)
        if triangle.point_inside(self.point):
            self.col = 'bo'
        else:
            self.col = 'ro'

        if np.random.random() < f:
            self.flip()

    def flip(self):
        if self.col == 'bo':
            self.col = 'ro'

        elif self.col == 'ro':
            self.col = 'bo'

    def plot(self, plt):
        plt.plot(self.point.x, self.point.y, self.col)
