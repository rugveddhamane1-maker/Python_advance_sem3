import threading

# Function to print numbers
def print_numbers():
    print("\nThread 1: Printing Numbers")
    for i in range(1, 6):
        print(i)

# Function to calculate squares
def print_squares():
    print("\nThread 2: Calculating Squares")
    for i in range(1, 6):
        print(i * i)

# Function to calculate cubes
def print_cubes():
    print("\nThread 3: Calculating Cubes")
    for i in range(1, 6):
        print(i * i * i)


# Create three threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_squares)
t3 = threading.Thread(target=print_cubes)

print("Starting Threads...")

# Start all threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to complete
t1.join()
t2.join()
t3.join()

print("\nAll threads completed successfully!")