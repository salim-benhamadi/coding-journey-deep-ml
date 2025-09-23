import numpy as np


# Solution 1: Using np.dot()


def calculate_dot_product(vec1, vec2) -> float:
    """
    Calculate the dot product of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    """
    return np.dot(vec1, vec2)


# Time Complexity : O(n), where n is the length of the vectors
# Space Complexity : O(1)


# Solution 2: Using Element-wise Multiplication and Sum

def calculate_dot_product(vec1, vec2) -> float:
    """
    Calculate the dot product of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    """
    return np.sum(vec1 * vec2)

# Time Complexity : O(n), where n is the length of the vectors
# Space Complexity : O(n)

