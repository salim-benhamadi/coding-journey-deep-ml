# Convert Vector to Diagonal Matrix

## Problem Statement

Write a Python function to convert a 1D numpy array into a diagonal matrix. The function should take in a 1D numpy array x and return a 2D numpy array representing the diagonal matrix.

## Examples

### Example 1:
```
Input:
x = np.array([1, 2, 3])
output = make_diagonal(x)
print(output)

Output:
[[1. 0. 0.]
 [0. 2. 0.]
 [0. 0. 3.]]

Reasoning:
The input vector [1, 2, 3] is converted into a diagonal matrix where the elements of the vector form the diagonal of the matrix.
```

## Solution 1: Using Identity Matrix Multiplication

```python
import numpy as np

def make_diagonal(x):
    vector_length = len(x)
    return np.eye(vector_length) * x
```

### Complexity Analysis

- **Time Complexity**: O(n²), where n is the length of the input vector
  - Creating the identity matrix with np.eye() is O(n²)
  - Element-wise multiplication with the vector is O(n²) (broadcasting across the matrix)

- **Space Complexity**: O(n²)
  - The identity matrix requires O(n²) space
  - The resulting diagonal matrix requires O(n²) space

## Solution 2: Using np.diag()

```python
import numpy as np

def make_diagonal(x):
    return np.diag(x)
```

### Complexity Analysis

- **Time Complexity**: O(n²), where n is the length of the input vector
  - np.diag() creates an n×n matrix with the vector elements on the diagonal

- **Space Complexity**: O(n²)
  - The resulting diagonal matrix requires O(n²) space

## Solution 3: Manual Matrix Construction

```python
import numpy as np

def make_diagonal(x):
    vector_length = len(x)
    diagonal_matrix = np.zeros((vector_length, vector_length))
    
    for i in range(vector_length):
        diagonal_matrix[i, i] = x[i]
        
    return diagonal_matrix
```

### Complexity Analysis

- **Time Complexity**: O(n²), where n is the length of the input vector
  - Creating the zero matrix is O(n²)
  - Setting diagonal elements is O(n)
  - Overall: O(n²)

- **Space Complexity**: O(n²)
  - The zero matrix and resulting diagonal matrix require O(n²) space

