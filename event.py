import random

# Simulate rolling a die
outcome = random.randint(1, 6)

# Define the event: rolling an even number
event = outcome in [2, 4, 6]

print("Outcome of the dice roll:", outcome)
print("Event 'rolling an even number':", event)
