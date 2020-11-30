import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def lotka_computation(hpp, t, b1=2, d1=1, b2=1.5, d2=1, b3=0.5, d3=1):
    h, p, p2 = hpp
    host_next = b1 * h - d1 * h * p
    predator_next = b2 * h * p - d2 * p * p2
    predator_2_next = b3 * p * p2 - d3 * p2
    return np.array((host_next, predator_next, predator_2_next))


h0 = 10
p0 = 10
p2_0 = 1
hpp0 = np.array([h0, p0, p2_0])
t = np.linspace(0, 5, 100)
host_predator_sizes = integrate.odeint(func=lotka_computation, y0=hpp0, t=t)
hosts = host_predator_sizes[:, 0]
predators = host_predator_sizes[:, 1]
predators_2 = host_predator_sizes[:, 2]
plt.plot(t, hosts, label='Hosts')
plt.plot(t, predators, label='Predators')
plt.plot(t, predators_2, label='Predators_2')
plt.grid()
plt.xlabel('Time')
plt.ylabel('Size')
plt.title('Three populations simulation')
plt.legend()

#plt.show()
plt.savefig('Fourth_plot.png', bbox_inches='tight')
