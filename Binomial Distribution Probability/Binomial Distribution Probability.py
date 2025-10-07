import math

# Mathematical formula solution
def binomial_probability(n, k, p):
    combinations = math.comb(n, k)
    probability = combinations * (p**k) * (1 - p)**(n - k) 
    return round(probability, 5)

# Time Complexity: O(k), where k is the number of successes (for combination calculation)
# Space Complexity: O(1), only using constant extra space