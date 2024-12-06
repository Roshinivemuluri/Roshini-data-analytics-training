import random

# Function to simulate a continuous random variable (height between 4.5 and 6.5 feet)
def random_height():
    return round(random.uniform(4.5, 6.5), 2)  # Returns a random float between 4.5 and 6.5

# Simulate random height 10 times
heights = [random_height() for _ in range(10)]

print("Random heights:", heights)
