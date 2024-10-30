from numpy import random
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr1))

print("------------------------------")
arr2 = np.array([1, 2, 3, 4, 5])

random.shuffle(arr2)

print(arr2)