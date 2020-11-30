import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib.offsetbox import AnchoredText


def lotka_computation(hp, t, b1=1, d1=1, b2=1, d2=1):
    h, p = hp
    host_next = b1 * h - d1 * h * p
    predator_next = b2 * h * p - d2 * p
    return np.array((host_next, predator_next))


h0 = 10
p0 = 10
hp0 = np.array([h0, p0])
t = np.linspace(0,1000,1000)
fig, axes = plt.subplots(nrows=4, ncols=5, figsize=(15,7))
fig.suptitle('Population size simulation', fontsize=12)
variables_names = ['Birth rate hosts', 'Death rate hosts', 'Birth rate predators', 'Death rate predators']
for i in range(4):
    variables = [0.1, 0.1, 0.1, 0.1]
    for j in range(5):
        variables[i] = 0.04 + (j+1) * 0.02
        variables_tuple = tuple(variables)
        host_predator_sizes = integrate.odeint(func=lotka_computation, y0=hp0, t=t, args=variables_tuple)
        hosts = host_predator_sizes[:,0]
        predators = host_predator_sizes[:,1]
        axes[i, j].plot(t, hosts, label='Hosts')
        axes[i, j].plot(t, predators, label='Predators')

        at = AnchoredText(f"{variables_names[i]} = {round(variables[i], 2)}",
                          prop=dict(size=7), frameon=True,
                          loc='upper center',
                          )
        at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
        axes[i, j].add_artist(at)
        axes[i, j].grid()
fig.text(0.5, 0.06, 'Time', ha='center', va='center')
fig.text(0.1, 0.5, 'Size', ha='center', va='center', rotation='vertical')
handles, labels = axes[i, j].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper left')
#plt.show()
plt.savefig('first_plot.png', bbox_inches='tight')


