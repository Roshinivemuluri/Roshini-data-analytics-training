import random

# Define the sample space for a six-sided die
sample_space = {1, 2, 3, 4, 5, 6}

# Simulate rolling a die
outcome = random.choice(list(sample_space))

print("Sample space of rolling a die:", sample_space)
print("Outcome of the dice roll:", outcome)
