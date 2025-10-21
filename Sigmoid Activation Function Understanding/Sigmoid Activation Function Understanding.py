import math

# Mathematical formula solution
def sigmoid(z: float) -> float:
    output = 1 / (1 + math.exp(-z))
    return round(output, 4)

# Time Complexity: O(1), constant time calculation
# Space Complexity: O(1), only using constant extra space