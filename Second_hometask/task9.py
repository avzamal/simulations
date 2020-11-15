import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib.offsetbox import AnchoredText


# I added temperature factor

def population_dynamics(n, t, r, k, temp):
    return r*(1.05 ** (-abs(temp-37)))*n*(1-n/k)

# Block with population size counting
n_0 = 10
k = 100
t = np.linspace(0, 100, 100)
r = 0.2
temp = 37
population_sizes00 = integrate.odeint(func=population_dynamics, y0=n_0, t=t, args=(r, k, temp))

temp = 30
population_sizes01 = integrate.odeint(func=population_dynamics, y0=n_0, t=t, args=(r, k, temp))

temp = 10
population_sizes02 = integrate.odeint(func=population_dynamics, y0=n_0, t=t, args=(r, k, temp))

# Block with plots
fig, axes = plt.subplots(nrows=1, ncols=3)
fig.suptitle('Population size simulation', fontsize=12)
axes[0].plot(t, population_sizes00, label='temp = 37 Celsius')
axes[0].legend()
axes[0].grid()

at = AnchoredText("Population grows with a max speed",
                  prop=dict(size=5), frameon=True,
                  loc='lower left',
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
axes[0].add_artist(at)

axes[1].plot(t, population_sizes01, label='temp = 30 Celsius')
axes[1].legend()
axes[1].grid()
at = AnchoredText("Population grows with a lower speed",
                  prop=dict(size=5), frameon=True,
                  loc='lower left',
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
axes[1].add_artist(at)

axes[2].plot(t, population_sizes02, label='temp = 10 Celsius')
axes[2].legend()
axes[2].grid()
at = AnchoredText("Population grows with low speed",
                  prop=dict(size=5), frameon=True,
                  loc='lower left',
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
axes[2].add_artist(at)


plt.show()
