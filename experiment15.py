import gc
import tracemalloc

# Define a class
class Demo:
    pass


# Function to create circular references
def create_objects():
    objects = []

    for i in range(10):
        a = Demo()
        b = Demo()

        a.other = b
        b.other = a

        objects.append(a)
        objects.append(b)

    return objects


# Start memory tracking
tracemalloc.start()

# Display garbage collection information
print("Garbage Collection Enabled:", gc.isenabled())
print("Garbage Collection Threshold:", gc.get_threshold())

# Create circular reference objects
items = create_objects()

print("\nCreated 10 pairs of circular objects.")

# Delete external references
del items

# Check memory before garbage collection
current, peak = tracemalloc.get_traced_memory()

print("\nMemory Before Garbage Collection:")
print("Current Memory:", current, "bytes")
print("Peak Memory:", peak, "bytes")

# Perform manual garbage collection
collected = gc.collect()

# Check memory after garbage collection
current, peak = tracemalloc.get_traced_memory()

print("\nManual Garbage Collection Completed")
print("Objects Collected:", collected)

print("\nMemory After Garbage Collection:")
print("Current Memory:", current, "bytes")
print("Peak Memory:", peak, "bytes")

# Disable garbage collection
gc.disable()
print("\nGarbage Collection Enabled:", gc.isenabled())

# Enable garbage collection
gc.enable()
print("Garbage Collection Enabled:", gc.isenabled())

# Stop memory tracking
tracemalloc.stop()