from typing import List
from model import Triangle, Point, FeatureVec
from abc import abstractmethod

class Settings:
    expno: int
    n: int
    k: int
    f: float
    triangle:Triangle
    autocontinue: bool

    @abstractmethod
    def next(self):
        pass

    def printset(self):
        return f'n = {self.n}; k = {self.k}; f = {self.f}\n' \
                 f'{self.triangle.printset()}'

class ManualSettings(Settings):

    # Manual settings are initalised by passing the arguments
    # Certain settings are given default values
    def __init__(self, n: int, k: int, f: float, t: Triangle):
        self.expno = 0
        self.autocontinue = False
        self.n = n
        self.k = k
        self.f = f
        self.triangle = t


    def next(self):
        return False

    def printset(self):
        return 'Manual: ' + super().printset()



class AutoSettings(Settings):

    # These lists define what the next value of n, f, and the triangle respectively should be
    # to facilitate automatic continuation
    ns: List[int] = [100, 200, 300, 400, 500, 600, 700, 800]
    fs: List[float] = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
    ts: List[Triangle] =   [Triangle(Point(3, 3), Point(7, 3), Point(7, 7)),
                            Triangle(Point(3, 3), Point(7, 3), Point(8, 7)),
                            Triangle(Point(3, 3), Point(7, 3), Point(9, 7)),
                            Triangle(Point(2, 3), Point(6, 3), Point(7, 7)),
                            Triangle(Point(2, 3), Point(6, 3), Point(8, 7)),
                            Triangle(Point(2, 3), Point(6, 3), Point(9, 7)),
                            Triangle(Point(1, 3), Point(5, 3), Point(7, 7)),
                            Triangle(Point(1, 3), Point(5, 3), Point(8, 7)),
                            Triangle(Point(1, 3), Point(5, 3), Point(9, 7))]


    # Values are initiated as either default values, or the first item in the respective list
    # These lists are popped to facilitate automatic continuation
    def __init__(self, expno:int):
        self.expno = expno
        self.k = 5
        self.autocontinue = True
        self.n = 500
        self.f = 0.0
        self.triangle = Triangle(Point(3, 3), Point(7, 3), Point(7, 7))

        if expno == 1:
            self.n = self.ns.pop(0)

        elif expno == 2:
            self.f = self.fs.pop(0)

        elif expno == 3:
            self.triangle = self.ts.pop(0)


    # If there are still items in the respective lists, we pop them and continue
    # the boolean returned denotes whether or not the settings have changed
    def next(self):
        if self.expno == 1:
            if self.ns:
                self.n = self.ns.pop(0)
                return True
            else: return False

        elif self.expno == 2:
            if self.fs:
                self.f = self.fs.pop(0)
                return True
            else: return False

        elif self.expno == 3:
            if self.ts:
                self.triangle = self.ts.pop(0)
                return True
            else: return False

    def printset(self):
        return 'Auto: ' + super().printset()