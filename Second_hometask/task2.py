import numpy as np

numbers = np.random.randint(0, 100, size=15)
bool_numbers = (numbers % 2) == 0
evens = numbers[bool_numbers]
bool_numbers = (numbers % 2) == 1
odds = numbers[bool_numbers]
