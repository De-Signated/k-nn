from matplotlib import pyplot as plt
import numpy as np
from math import sqrt

from settings import *
from model import *


def main():
    init_plot()
    results: List[bool] = []

    for i in range(10000):
        #generate a random point
        x = np.random.uniform(0, 10)
        y = np.random.uniform(0, 10)

        point: FeatureVec = FeatureVec(x,y,triangle,0)

        #perform k-NN
        isRed: bool = k_nn(point)

        results.append(isRed == (point.col == 'ro'))

    false_count: int = 10000 - sum(results)
    print(false_count)


def init_plot():

    triangle.plot(plt)

    for i in range(n):
        x = np.random.uniform(0, 10)
        y = np.random.uniform(0, 10)
        point: FeatureVec = FeatureVec(x, y, triangle, f)
        points.append(point)
        point.plot(plt)

    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.show()


#returns true if the point is red, and false otherwise
def k_nn(point: FeatureVec):
    distances: List[(FeatureVec, int)] = []

    for fv in points:
        euclid: float = sqrt((fv.point.x - point.point.x) ** 2 + (fv.point.y - point.point.y) ** 2)
        distances.append((fv, euclid))

    distances.sort(key=lambda tup: tup[1])
    red: int = 0
    blue: int = 0

    for i in range(5):
        q: (FeatureVec, int) = distances[i]
        p: FeatureVec = q[0]

        if p.col == 'ro':
            red += 1
        elif p.col == 'bo':
            blue += 1

    return red > blue

if __name__ == "__main__":
    main()