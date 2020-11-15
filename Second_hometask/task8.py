import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib.offsetbox import AnchoredText


def population_dynamics(n, t, r, k):
    return r*n*(1-n/k)


# Block with population size counting
n_0 = 10
k = 100
t = np.linspace(0, 100, 100)
r = 0.2
population_sizes00 = integrate.odeint(func=population_dynamics, y0=n_0, t=t, args=(r, k))

r = 0
population_sizes01 = integrate.odeint(func=population_dynamics, y0=n_0, t=t, args=(r, k))

r = -0.2
population_sizes02 = integrate.odeint(func=population_dynamics, y0=n_0, t=t, args=(r, k))

n_0 = 100
k = 10
r = 0.2
population_sizes10 = integrate.odeint(func=population_dynamics, y0=n_0, t=t, args=(r, k))

r = 0
population_sizes11 = integrate.odeint(func=population_dynamics, y0=n_0, t=t, args=(r, k))

n_0 = 100
r = -0.2
population_sizes12 = integrate.odeint(func=population_dynamics, y0=n_0, t=t, args=(r, k))

# Block with plots
fig, axes = plt.subplots(nrows=2, ncols=3, figsize = (15,7))
fig.suptitle('Population size simulation', fontsize=12)
axes[0, 0].plot(t, population_sizes00, label='K > N0, r > 0')
axes[0, 0].legend()

at = AnchoredText("Population grows up to a constant level",
                  prop=dict(size=5), frameon=True,
                  loc='center',
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
axes[0, 0].add_artist(at)
axes[0, 0].grid()
axes[0, 0].set_xlabel('Time')
axes[0, 0].set_ylabel('Size')

axes[0, 1].plot(t, population_sizes01, label='K > N0, r = 0')
axes[0, 1].legend()

at = AnchoredText("Population stays at a constant level",
                  prop=dict(size=5), frameon=True,
                  loc='lower center',
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
axes[0, 1].add_artist(at)
axes[0, 1].grid()
axes[0, 1].set_xlabel('Time')
axes[0, 1].set_ylabel('Size')

axes[0, 2].plot(t, population_sizes02, label='K > N0, r < 0')
axes[0, 2].legend()

at = AnchoredText("Population decrease up to 0",
                  prop=dict(size=5), frameon=True,
                  loc='center',
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
axes[0, 2].add_artist(at)
axes[0, 2].grid()
axes[0, 2].set_xlabel('Time')
axes[0, 2].set_ylabel('Size')

axes[1, 0].plot(t, population_sizes10, label='K < N0, r > 0')
axes[1, 0].legend()

at = AnchoredText("Population rapidly decrease to a constant level",
                  prop=dict(size=5), frameon=True,
                  loc='center',
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
axes[1, 0].add_artist(at)
axes[1, 0].grid()
axes[1, 0].set_xlabel('Time')
axes[1, 0].set_ylabel('Size')

axes[1, 1].plot(t, population_sizes11, label='K < N0, r = 0')
axes[1, 1].legend()

at = AnchoredText("Population stays at a constant level",
                  prop=dict(size=5), frameon=True,
                  loc='lower center',
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
axes[1, 1].add_artist(at)
axes[1, 1].grid()
axes[1, 1].set_xlabel('Time')
axes[1, 1].set_ylabel('Size')

axes[1, 2].plot(t, population_sizes12, label='K < N0, r < 0')
axes[1, 2].legend()

at = AnchoredText("r and (1-n/k) are negative, so it looks strange",
                  prop=dict(size=5), frameon=True,
                  loc='center',
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
axes[1, 2].add_artist(at)
axes[1, 2].grid()
axes[1, 2].set_xlabel('Time')
axes[1, 2].set_ylabel('Size')

plt.show()
