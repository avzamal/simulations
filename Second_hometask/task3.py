import numpy as np
import matplotlib.pyplot as plt


coordinates = np.zeros((100, 2))
current_coord = [0, 0]
for i in range(1, 100):
    axis = np.random.randint(0, 2)
    movement = np.random.normal()
    if axis == 0:
        current_coord[0] += movement
    else:
        current_coord[1] += movement
    coordinates[i] = current_coord

print(coordinates)
plt.plot(coordinates[..., 0], coordinates[..., 1])
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()
