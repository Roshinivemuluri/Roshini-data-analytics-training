import random

# Simulate a discrete random variable (a dice roll)
def roll_die():
    return random.randint(1, 6)  # Returns a random value between 1 and 6

# Simulate rolling the die 10 times
rolls = [roll_die() for _ in range(10)]

print("Die rolls:", rolls)
