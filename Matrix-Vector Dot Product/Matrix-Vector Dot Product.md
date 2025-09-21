# Matrix-Vector Dot Product

## Problem Statement

Write a Python function that computes the dot product of a matrix and a vector. The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. 

A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. For example, an n x m matrix requires a vector of length m.

## Examples

### Example 1:
```
Input:
a = [[1, 2], [2, 4]], b = [1, 2]

Output:
[5, 10]

Reasoning:
Row 1: (1 * 1) + (2 * 2) = 1 + 4 = 5
Row 2: (2 * 1) + (4 * 2) = 2 + 8 = 10
```

## Solution 1: Loop-Based Approach

```python
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    num_cols = len(a[0])
    
    if num_cols != len(b):
        return -1
        
    result = []
    
    for row in a:
        row_products = []
        for col_index in range(num_cols):
            row_products.append(row[col_index] * b[col_index])
        result.append(sum(row_products))
        
    return result
```

### Complexity Analysis

- **Time Complexity**: O(n * m), where n is the number of rows and m is the number of columns
  - We iterate through each element in the matrix once
  - For each row, we perform m multiplications and one sum operation

- **Space Complexity**: O(n * m)
  - We store intermediate products for each row before summing
  - The result vector requires O(n) space
  - Total space includes the temporary row_products lists

## Solution 2: NumPy-Based Approach

```python
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    import numpy as np
    
    num_cols = len(a[0])
    
    if num_cols != len(b):
        return -1
    
    result = np.sum(np.array(a) * np.array(b), axis=1)
    return list(result)
```

### Complexity Analysis

- **Time Complexity**: O(n * m), where n is the number of rows and m is the number of columns
  - NumPy operations are vectorized and optimized but still process each element
  - Broadcasting and element-wise multiplication is O(n * m)
  - Sum along axis=1 is O(n * m)

- **Space Complexity**: O(n * m)
  - NumPy arrays require space to store the matrix and vector
  - Intermediate array from element-wise multiplication requires O(n * m) space
  - Final result requires O(n) space

