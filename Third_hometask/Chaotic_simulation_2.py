import numpy as np
import matplotlib.pyplot as plt


def round_computations(n, r):
    return n*r*(1-n)


n_0 = 0.3
t = np.arange(10000)
rs = np.linspace(0, 4, 120)
plt.figure(figsize=(11, 6))
plt.xlabel('r')
plt.ylabel('Number')
plt.title('System at different r values, t > 1000')
plt.grid(alpha=0.3)
for r in rs:
    ns = np.zeros(t.size)
    ns[0] = n_0
    for time in t[1:]:
        ns[time] = round_computations(ns[time-1], r)
    ns_part = ns[1000:]
    plt.scatter(np.full(ns_part.size, r), ns_part, s=0.00001)
plt.savefig('second_plot.png', bbox_inches = 'tight')
#plt.show()