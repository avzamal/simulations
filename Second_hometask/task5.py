import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 30)
p_0 = 10
r = 0.8
p = p_0 * np.e**(r*t)

plt.plot(t, p)
plt.show()
