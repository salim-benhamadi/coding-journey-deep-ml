# Reshape Matrix

## Problem Statement

Write a Python function that reshapes a given matrix into a specified shape. If it can't be reshaped, return back an empty list `[]`.

## Input
* `a`: A 2D list of integers or floats representing the input matrix
* `new_shape`: A tuple of two integers representing the desired shape (rows, columns)

## Output
* A 2D list representing the reshaped matrix, or an empty list if reshaping is not possible

## Constraints
* The total number of elements must remain the same for successful reshaping
* If reshaping is impossible, return empty list `[]`

## Examples

### Example 1:
```
Input:
a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)

Output:
[[1, 2], [3, 4], [5, 6], [7, 8]]

Reasoning:
The given matrix is reshaped from 2x4 to 4x2.
```

### Example 2:
```
Input:
a = [[1,2,3],[4,5,6]], new_shape = (4, 2)

Output:
[]

Reasoning:
Cannot reshape a 2x3 matrix (6 elements) into 4x2 (8 elements).
```

## Solution: Using NumPy

```python
import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    
    a = np.array(a)
    if new_shape[0]*new_shape[1] == a.size:
        reshaped_matrix = np.reshape(a, new_shape)
        return reshaped_matrix.tolist()
    else:
        return []
```

### Complexity Analysis

- **Time Complexity**: O(m × n), where m and n are the dimensions of the matrix
  - Converting to numpy array and reshaping both require processing all elements
  - Converting back to list also processes all elements

- **Space Complexity**: O(m × n)
  - Additional space needed for numpy array and output list
  - Space proportional to the size of the input matrix