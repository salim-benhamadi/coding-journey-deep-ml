# Conditional solution
def leaky_relu(z: float, alpha: float = 0.01) -> float:
    return z if z > 0 else alpha * z

# Time Complexity: O(1), constant time comparison
# Space Complexity: O(1), only using constant extra space