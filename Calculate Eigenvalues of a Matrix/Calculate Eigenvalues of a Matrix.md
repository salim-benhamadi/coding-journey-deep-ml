# Calculate Eigenvalues of a Matrix

## Problem Statement

Write a Python function that calculates the eigenvalues of a 2x2 matrix. The function should return a list containing the eigenvalues, sorted from highest to lowest.

## Input
* `matrix`: A 2x2 list of floats or integers representing the input matrix

## Output
* A list of floats representing the eigenvalues sorted in descending order

## Constraints
* Input is always a 2x2 matrix
* Eigenvalues should be sorted from highest to lowest

## Examples

### Example 1:
```
Input:
matrix = [[2, 1], [1, 2]]

Output:
[3.0, 1.0]

Reasoning:
The eigenvalues of the matrix are calculated using the characteristic equation of the matrix, 
which for a 2x2 matrix is λ² - trace(A)λ + det(A) = 0, where λ are the eigenvalues.
For this matrix: trace = 2+2 = 4, det = 2*2 - 1*1 = 3
Solving λ² - 4λ + 3 = 0 gives λ = 3 and λ = 1
```

### Example 2:
```
Input:
matrix = [[4, 2], [1, 3]]

Output:
[5.0, 2.0]

Reasoning:
trace = 4+3 = 7, det = 4*3 - 2*1 = 10
Solving λ² - 7λ + 10 = 0 gives λ = 5 and λ = 2
```

## Solution 1: Characteristic Equation Approach

```python
import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    matrix_array = np.array(matrix)
    determinant = np.linalg.det(matrix_array)
    trace = np.trace(matrix_array)
    eigenvalues = np.roots([1, -trace, determinant])
    return sorted(eigenvalues.real, reverse=True)
```

### Complexity Analysis

- **Time Complexity**: O(1)
  - All operations (determinant, trace, solving quadratic) are constant time for 2x2 matrix
  - Sorting 2 elements is constant time

- **Space Complexity**: O(1)
  - Constant additional space for 2x2 operations

## Solution 2: NumPy Built-in Approach

```python
import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    matrix_array = np.array(matrix)
    eigenvalues = np.linalg.eigvals(matrix_array)
    return sorted(eigenvalues.real, reverse=True)
```

### Complexity Analysis

- **Time Complexity**: O(1)
  - NumPy's eigvals function is optimized for small matrices
  - Constant time for 2x2 matrix

- **Space Complexity**: O(1)
  - Constant additional space

