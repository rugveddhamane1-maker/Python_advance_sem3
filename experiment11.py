import pandas as pd
import numpy as np

# Generate 10 random numbers
np.random.seed(42)
numbers = np.random.randint(1, 101, size=10)

# Create a Pandas Series
series = pd.Series(numbers, index=range(1, 11))

print("Original Pandas Series:")
print(series)

# Indexing
print("\nValue at index 3:")
print(series.loc[3])

# Display first three elements
print("\nFirst three elements:")
print(series.iloc[:3])

# Filtering
print("\nNumbers greater than 50:")
print(series[series > 50])

# Statistical operations
print("\nMean:", series.mean())

print("Median:", series.median())

print("Minimum:", series.min())

print("Maximum:", series.max())