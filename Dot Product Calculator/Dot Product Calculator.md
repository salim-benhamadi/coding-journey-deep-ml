# Dot Product Calculator

## Problem Statement

Write a Python function to calculate the dot product of two vectors. The function should take two 1D NumPy arrays as input and return the dot product as a single number.

## Examples

### Example 1:
```
Input:
vec1 = np.array([1, 2, 3]), vec2 = np.array([4, 5, 6])

Output:
32

Reasoning:
The function calculates the dot product by multiplying corresponding elements of the two vectors and summing the results. For vec1 = [1, 2, 3] and vec2 = [4, 5, 6], the result is (1 * 4) + (2 * 5) + (3 * 6) = 32.
```

## Solution 1: Using np.dot()

```python
import numpy as np

def calculate_dot_product(vec1, vec2) -> float:
    """
    Calculate the dot product of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    """
    return np.dot(vec1, vec2)
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the vectors
  - The np.dot() function iterates through all elements once
  - Each multiplication and addition is O(1)

- **Space Complexity**: O(1)
  - No additional arrays are created
  - Only the result value is stored

## Solution 2: Using Element-wise Multiplication and Sum

```python
import numpy as np

def calculate_dot_product(vec1, vec2) -> float:
    """
    Calculate the dot product of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    """
    return np.sum(vec1 * vec2)
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the vectors
  - Element-wise multiplication creates an intermediate array in O(n)
  - np.sum() iterates through the intermediate array in O(n)
  - Overall: O(n) + O(n) = O(n)

- **Space Complexity**: O(n)
  - Element-wise multiplication creates an intermediate array of size n
  - This array is then summed and discarded

