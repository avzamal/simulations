import numpy as np
import matplotlib.pyplot as plt


def round_computations(n, r):
    return n*r*(1-n)


plt.figure(figsize=(9, 6))
n_0 = 0.3
t = np.arange(10000)
rs = np.linspace(0, 4, 150)
for r in rs:
    ns = np.zeros(t.size)
    ns[0] = n_0
    for time in t[1:]:
        ns[time] = round_computations(ns[time-1], r)
    plt.scatter(np.full(t.size, r), ns, s=0.25)

plt.xlabel('r')
plt.ylabel('Number')
plt.title('System at different r values')
plt.grid(alpha=0.3)

plt.savefig('first_plot.png', bbox_inches='tight')
#plt.show()
