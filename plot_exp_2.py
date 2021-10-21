import matplotlib.pyplot as plt
import numpy as np

# x-axis (f -> 0.0 till 3.0 ). 'stop' is exclusive, so I add one more step to it.
x = np.arange(start=0, stop=0.35, step=0.05)

# averages
y = [220.35, 234.5, 370.55, 497.05, 790.1, 1246.0, 1853.5]

# standard deviations
y_err = [37.10, 42.16, 92.11, 111.38, 199.47, 216.84, 273.92]

# create figure
fig, ax = plt.subplots()

# create error bar including line
ax.errorbar(x, y, yerr=y_err, fmt='-o')

# set labels etc.
ax.set_xlabel('Fraction of outliers (f)')
ax.set_ylabel('Average misclassification')
ax.set_title('Experiment 2')

plt.show()