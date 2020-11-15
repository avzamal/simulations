import numpy as np
import matplotlib.pyplot as plt

xs = (np.random.rand(20)*2-1)*np.pi
sin_xs = np.sin(xs)

plt.scatter(xs, sin_xs)
plt.show()

