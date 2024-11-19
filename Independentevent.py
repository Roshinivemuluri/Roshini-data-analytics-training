import random

# Function to simulate a coin toss
def coin_toss():
    return random.choice(['Heads', 'Tails'])

# Function to simulate rolling a die
def roll_die():
    return random.randint(1, 6)

# Simulating both independent events
coin = coin_toss()   # Coin toss result
die = roll_die()     # Die roll result

print(f"Coin toss result: {coin}")
print(f"Die roll result: {die}")
