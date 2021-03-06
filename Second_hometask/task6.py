import numpy as np
import matplotlib.pyplot as plt


xs1 = np.arange(0, 10, 0.01)
xs2 = np.arange(0, 10, 0.1)
xs3 = np.arange(0, 10, 1)
xs4 = np.arange(0, 10, 2)

fig, axes = plt.subplots(ncols=2, nrows=2, figsize = (8.5,8.5))
axes[0, 0].plot(xs1, xs1**2, label='step = 0.01')
axes[0, 0].legend()
axes[0, 0].grid()
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('Y')
axes[0, 1].plot(xs2, xs2**2, label='step = 0.1')
axes[0, 1].legend()
axes[0, 1].grid()
axes[0, 1].set_xlabel('X')
axes[0, 1].set_ylabel('Y')
axes[1, 0].plot(xs3, xs3**2, label='step = 1')
axes[1, 0].legend()
axes[1, 0].grid()
axes[1, 0].set_xlabel('X')
axes[1, 0].set_ylabel('Y')
axes[1, 1].plot(xs4, xs4**2, label='step = 2')
axes[1, 1].legend()
axes[1, 1].grid()
axes[1, 1].set_xlabel('X')
axes[1, 1].set_ylabel('Y')
plt.show()
