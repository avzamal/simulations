import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(-5, 5)
y1 = xs**2
y2 = np.full(50, np.pi)
plt.plot(xs, y1, label='x^2')
plt.plot(xs, y2, label='Pi')
plt.fill_between(xs, np.max(y1), y1, color='b')
plt.fill_between(xs, y2, y1, color='w')
plt.show()
