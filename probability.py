import random

# Simulate rolling a die
def roll_die():
    return random.randint(1, 6)

# Probability of rolling a 4
def probability_of_4(rolls=1000):
    count_4 = 0
    for _ in range(rolls):
        if roll_die() == 4:
            count_4 += 1
    return count_4 / rolls

# Run the simulation
prob = probability_of_4()
print(f"Estimated probability of rolling a 4: {prob}")
