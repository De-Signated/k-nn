from typing import List, TYPE_CHECKING
from model import Triangle, Point, FeatureVec


n = 500
k = 5
f = 0
triangle: Triangle = Triangle(Point(3,3), Point(7,3), Point(7,7))
points: List[FeatureVec] = []