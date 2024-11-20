import math

# Multiplication Rule: Total ways to choose one item from each group
def multiplication_rule(m, n):
    return m * n

# Addition Rule: Total ways to choose one item from either group
def addition_rule(m, n):
    return m + n

# Factorial Rule: Number of ways to arrange 'n' objects
def factorial_rule(n):
    return math.factorial(n)

# Combination Rule: Number of ways to choose 'r' items from 'n' items
def combination_rule(n, r):
    return math.comb(n, r)

# Permutation Rule: Number of ways to arrange 'r' items from 'n' items
def permutation_rule(n, r):
    return math.perm(n, r)

# Example usage
m, n = 3, 4
print(f"Multiplication Rule: {multiplication_rule(m, n)}")
print(f"Addition Rule: {addition_rule(m, n)}")
print(f"Factorial Rule (4!): {factorial_rule(4)}")
print(f"Combination Rule (5 choose 2): {combination_rule(5, 2)}")
print(f"Permutation Rule (4 P 2): {permutation_rule(4, 2)}")