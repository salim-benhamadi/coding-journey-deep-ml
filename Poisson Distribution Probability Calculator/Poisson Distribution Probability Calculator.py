import math

# Mathematical formula solution
def poisson_probability(k, lam):
    probability = (lam**k * math.exp(-lam)) / math.factorial(k)
    return round(probability, 5)

# Time Complexity: O(k), where k is the number of events (for factorial calculation)
# Space Complexity: O(1), only using constant extra space