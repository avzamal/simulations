import numpy as np

fib_array = np.arange(0, 125)
for i in range(2, 125):
    fib_array[i] = fib_array[i-2]+fib_array[i-1]

print(sum(fib_array[fib_array % 2 == 0]))
