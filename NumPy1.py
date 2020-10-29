import numpy as np

n = int(input())
array = np.arange(1, n+1)
result_array = np.zeros(n-1)

for i in range(n-1):
    result_array[i] = abs((array[i]**2+array[i+1]**2)-(array[i]+array[i+1])**2)

print(result_array)