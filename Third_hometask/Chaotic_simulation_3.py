import numpy as np
import matplotlib.pyplot as plt


def round_computations(n, r):
    return n*r*(1-n)


n_0 = 0.3
t = np.arange(10000)
rs = np.linspace(3.4, 4, 60)
plt.figure(figsize=(11, 6))
plt.xlabel('r')
plt.ylabel('Number')
plt.title('System at different r values, t > 1000, zoomed from x = 3.5 to x = 4')
plt.grid(alpha=0.3)
plt.xlim(3.49,4.01)
plt.xticks(np.linspace(3.5, 4, 11))
for r in rs:
    ns = np.zeros(t.size)
    ns[0] = n_0
    for time in t[1:]:
        ns[time] = round_computations(ns[time-1], r)
    ns_part = ns[1000:]
    plt.scatter(np.full(ns_part.size, r), ns_part, s=0.00001)
plt.savefig('fourth_plot.png', bbox_inches='tight')
plt.show()