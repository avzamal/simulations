import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def infection_func(sirv, t, contact_rate, recovery_rate, vaccination):
    s, i, r, v = sirv
    s_next = -contact_rate * i * s - vaccination
    i_next = contact_rate * i * s - recovery_rate * i
    r_next = recovery_rate * i
    v_next = vaccination
    return np.array((s_next, i_next, r_next, v_next))


s0 = 99999
i0 = 1
r0 = 0
v0 = 0
Re = 3.26  # effective reproductive number
D = 14  # duration of illness
vaccination = 50 # people per time unit
recovery_rate = 1/D
contact_rate = (Re / s0) / D
sirv0 = np.array((s0, i0, r0, v0))
t = np.linspace(0, 600, 1000)
plt.figure(figsize=(14, 6))
сolors_in_plot = ['blue', 'orange', 'green', 'red']
linestyles = ['-', '--', '-.', ':']
vaccination_labels = ['without vaccination', 'with vaccination']
for i in range(0, 4):
    contact_rate_var = contact_rate * (1 - 0.2 * i)
    for j in range(0, 2):
        variables_tuple = (contact_rate_var, recovery_rate, vaccination*j)
        infection = integrate.odeint(func=infection_func, y0=sirv0, t=t, args=variables_tuple)
        susceptible = infection[:, 0]
        infected = infection[:, 1]
        recovered = infection[:, 2]
        vaccinated = infection[:, 3]
        plt.plot(t, infected,
                 label=f"Contact rate = {100 * round(1 - 0.2 * i, 1)}%, {vaccination_labels[j]}",
                 linestyle=linestyles[j], color=сolors_in_plot[i])


plt.xlabel('Time')
plt.ylabel('Size')
# plt.xlim(20, 150)
plt.title('Infected people dependence on contact rate and vaccination')
plt.legend()

# plt.show()
plt.savefig('Infected people dependence on contact rate and vaccination.png', bbox_inches='tight')
