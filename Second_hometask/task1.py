import numpy as np
import matplotlib.pyplot as plt


xs = np.linspace(-np.pi, np.pi, 20)
sin_xs = np.sin(xs)

plt.scatter(xs, sin_xs)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()

