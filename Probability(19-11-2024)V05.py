import random

# Function to simulate drawing two marbles from a bag
def draw_two_marbles():
    # Bag with 3 red marbles and 2 blue marbles
    bag = ['Red', 'Red', 'Red', 'Blue', 'Blue']
    
    # First draw
    first_draw = random.choice(bag)
    bag.remove(first_draw)  # Remove the first marble
    
    # Second draw
    second_draw = random.choice(bag)
    
    return first_draw, second_draw

# Run the simulation
first, second = draw_two_marbles()

print(f"First draw: {first}")
print(f"Second draw: {second}")
