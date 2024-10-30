import numpy as np 

arr1  = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2), axis=0)
arrr = np.stack((arr1, arr2), axis=0)
print(arr1)
print(arr2)
print(arr)
print("-----------------------")
print(arrr)