import numpy as np

n = int(input())
array1 = np.arange(1, n+1)
array2 = np.ones(n)

result_array = array2/array1
print(sum(result_array))