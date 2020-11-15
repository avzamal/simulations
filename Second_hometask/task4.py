import numpy as np
import matplotlib.pyplot as plt

numbers = np.linspace(-10, 10, 201)
sin_numbers = np.sin(numbers)
cos_numbers = np.cos(numbers)

plt.plot(numbers, sin_numbers, label = 'sin')
plt.plot(numbers, cos_numbers, label = 'cos')
plt.legend()
plt.show()
