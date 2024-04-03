import numpy as np
import time

# Create a large array
array_size = 1000000
arr = np.random.rand(array_size)

# NumPy operation: compute the sum of the array
start_time = time.time()
np_sum = np.sum(arr)
numpy_time = time.time() - start_time
print("NumPy sum:", np_sum)
print("NumPy time:", numpy_time)

# Regular Python for loop: compute the sum of the array
start_time = time.time()
python_sum = 0
for x in arr:
    python_sum += x
python_time = time.time() - start_time
print("Python sum:", python_sum)
print("Python time:", python_time)
