from matplotlib import pyplot as plt
from numpy import sqrt, random
from statistics import mean, stdev
from typing import List
from model import Triangle, Point, FeatureVec
from settings import Settings


class Experiment:
    sett: Settings
    points: List[FeatureVec]


    def __init__(self, s: Settings):
        self.sett = s
        self.create_points()


    # Runs the experiment twenty times with provided settings
    # Prints mean and st. dev
    # Updates the settings and runs again if need be
    def run(self, iterations=20):
        print('Experiment ', self.sett.expno, 'with settings ', self.sett.printset())
        print('running ', iterations, ' iterations')

        total: List[int] = []
        # Iterate and run the experiment X times, with a fresh dataset every time

        # total = Parallel(n_jobs=4)(delayed(process)(i) for i in range(iterations))

        for i in range(iterations):
            total.append(self.iterate_once())
            print('finished iteration ', i)

            # Calculate and print the mean and st. dev over X iterations
        mu = mean(total)
        sigma = stdev(total)
        print('total= ', total)
        print('\u03BC= ', mu)
        print('\u03C3= ', sigma)

        # Continue automatically with the next set of settings, if enabled
        if self.sett.autocontinue:
            if self.sett.next():
                self.run(iterations)

    # Run the experiment with the provided settings
    def iterate_once(self):
        # Create the pointset over which this iteration will run
        self.create_points()
        false_count: int = 0

        # Perform k-NN over ten thousand points
        for i in range(10000):
            point: FeatureVec = self.create_random()
            if self.k_nn_is_red(point) != (point.col == 'ro'):
                # Add one to the count if the point was misclassified
                false_count += 1

        return false_count

    # Performs K-NN classification over the specified point
    # Returns true if the point is red, and false otherwise
    def k_nn_is_red(self, point: FeatureVec):
        # Initialise distance list of tuples
        distances: List[(FeatureVec, int)] = []

        # Iterate over the points to assign Euclidian distances
        for fv in self.points:
            euclid: float = sqrt((fv.point.x - point.point.x) ** 2 + (fv.point.y - point.point.y) ** 2)
            distances.append((fv, euclid))

        # Sort list on second value (the distance value)
        distances.sort(key=lambda tup: tup[1])
        red: int = 0
        blue: int = 0

        # check the first k items and count how many reds vs blues there are
        for i in range(self.sett.k):
            q: tuple(FeatureVec, int) = distances[i]
            p: FeatureVec = q[0]

            if p.col == 'ro':
                red += 1
            elif p.col == 'bo':
                blue += 1

        # Return a boolean value denoting if the point is red or blue
        return red > blue

    # Create a new random feature vector
    # does not add it to the list
    def create_random(self):
        x = random.uniform(0, 10)
        y = random.uniform(0, 10)

        return FeatureVec(x, y, self.sett.triangle, 0)

    # Randomly and uniformly generates N points
    def create_points(self):
        self.points = []

        for i in range(self.sett.n):
            x = random.uniform(0, 10)
            y = random.uniform(0, 10)
            point: FeatureVec = FeatureVec(x, y, self.sett.triangle, self.sett.f)
            self.points.append(point)

    # Renders a nice-looking plot of the current experiment
    def plot(self):

        self.sett.triangle.plot(plt)

        for point in self.points:
            point.plot(plt)

        plt.xlim([0, 10])
        plt.ylim([0, 10])
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()