import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib.offsetbox import AnchoredText

def lotka_computation(hp, t, b1=0.1, b2=0.1, d1=0.1, d2=0.1):
    h, p = hp
    host_next = b1 * h - d1 * h * p
    predator_next = b2 * h * p - d2 * p
    return np.array((host_next, predator_next))


def lotka_computation_with_cannibalism(hp, t, b1=0.1, b2=0.1, d1=0.1, d2=0.1, cannibalism = 2):
    h, p = hp
    host_next = b1 * h - d1 * h * p
    predator_next = b2 * h * p - d2 * (np.e ** (-np.sqrt(h)) * cannibalism) * p
    return np.array((host_next, predator_next))


h0 = 10
p0 = 10
hp0 = np.array([h0, p0])
t = np.linspace(0,1000,1000)
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15,7))
fig.suptitle('Population size simulation', fontsize=12)
functions = [lotka_computation, lotka_computation_with_cannibalism]
function_names = ['Without cannibalism', 'With cannibalism']
for i in range(2):
    host_predator_sizes = integrate.odeint(func=functions[i], y0=hp0, t=t)
    hosts = host_predator_sizes[:, 0]
    predators = host_predator_sizes[:, 1]
    axes[i].plot(t, hosts, label='Hosts')
    axes[i].plot(t, predators, label='Predators')

    at = AnchoredText(f"{function_names[i]}",
                      prop=dict(size=7), frameon=True,
                      loc='upper center',
                      )
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    axes[i].add_artist(at)
    axes[i].grid()
fig.text(0.5, 0.06, 'Time', ha='center', va='center')
fig.text(0.1, 0.5, 'Size', ha='center', va='center', rotation='vertical')
handles, labels = axes[i].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper left')
#plt.show()
plt.savefig('Second_plot.png', bbox_inches='tight')


