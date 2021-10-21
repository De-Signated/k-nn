from Experiment import Experiment
from settings import ManualSettings, AutoSettings
from model import *

def main():
    # Options for manual settings
    # If you use manual settings, make sure to specify on Experiment creation
    # By default, automatic settings are used
    n = 500
    k = 5
    f = 0.0
    triangle: Triangle = Triangle(Point(3, 3), Point(7, 3), Point(7, 7))
    manualSettings = ManualSettings(n, k, f, triangle)


    # Options for automatic settings
    # This number denotes which experiment is being carried out,
    # either 1, 2, or 3
    # These settings are automatically updated depending on the experiment number
    # and re-run the experiment until all options are exhausted
    # See settings.py for the lists of these experiment settings
    expNo = 1
    autoSettings = AutoSettings(expNo)


    # Make sure to specify the right settings with which to run the experiment!
    experiment: Experiment = Experiment(autoSettings)


    # Integer argument defines how often each experiment is repeated
    # to obtain the mean and st. dev.  Default = 20
    experiment.run(20)


    # Plots the experiment
    # If multiple experiments or iterations were run, plots the last one
    experiment.plot()


if __name__ == "__main__":
    main()