# Define the total number of cards in a standard deck
total_cards = 52

# Define the number of red cards (hearts + diamonds)
red_cards = 26  # 13 hearts + 13 diamonds

# Define the number of hearts (which are red)
hearts = 13

# Conditional Probability P(Heart|Red) = P(Heart and Red) / P(Red)
P_heart_given_red = hearts / red_cards

# Output the result
print("The conditional probability of drawing a heart given that the card is red is:", P_heart_given_red)