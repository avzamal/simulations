import numpy as np

n = int(input())
array = np.array([0, 0])

a = np.random.randint(1, 4, size=10)
for i in a:
    if i == 1:
        array[0] += 1
        print("We move right")
        print(array)
    elif i == 2:
        array[0] -= 1
        print("We move left")
        print(array)
    elif i == 3:
        array[1] += 1
        print("We move up")
        print(array)
    elif i == 4:
        array[1] -= 1
        print("We move down")
        print(array)

