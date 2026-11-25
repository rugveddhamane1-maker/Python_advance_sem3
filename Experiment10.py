import numpy as np

# Create a one-dimensional array
arr = np.arange(1, 11)

print("Original Array:", arr)

# Slicing operations
print("First five elements:", arr[:5])

print("Elements from index 2 to 6:", arr[2:7])

print("Every second element:", arr[::2])

print("Array in reverse order:", arr[::-1])

# Statistical operations
print("Sum:", np.sum(arr))

print("Mean:", np.mean(arr))

print("Maximum:", np.max(arr))

print("Minimum:", np.min(arr))

# Broadcasting: Add 5 to every element
modified_arr = arr + 5

print("Array after adding 5:", modified_arr)