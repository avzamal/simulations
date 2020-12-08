import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def infection_func (sir, t, contact_rate, recovery_rate):
    s, i, r = sir
    s_next = -contact_rate*i*s
    i_next = contact_rate*i*s - recovery_rate*i
    r_next = recovery_rate*i
    return np.array((s_next, i_next, r_next))


s0 = 49955
i0 = 5
r0 = 0

sir0 = np.array((s0, i0, r0))
t = np.linspace(0, 100, 100)
variables_tuple = (0.000014, 0.2)
infection = integrate.odeint(func=infection_func, y0=sir0, t=t, args=variables_tuple)
susceptible = infection[:, 0]
infected = infection[:, 1]
recovered = infection[:, 2]

plt.plot(t, susceptible, label='Susceptible')
plt.plot(t, infected, label='Infected')
plt.plot(t, recovered, label='Recovered')

plt.xlabel('Time')
plt.ylabel('Size')
plt.title('Infection simulation')
plt.legend()

#plt.show()
plt.savefig('plot.png', bbox_inches='tight')