# Transpose of a Matrix

## Problem Statement

Write a Python function that computes the transpose of a given matrix.

## Examples

### Example 1:
```
Input:
a = [[1,2,3],[4,5,6]]

Output:
[[1,4],[2,5],[3,6]]

Reasoning:
The transpose of a matrix is obtained by flipping rows and columns.
```

## Solution 1: Loop-Based Approach

```python
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    num_cols = len(a[0])
    transposed = [[] for _ in range(num_cols)]
    
    for row in a:
        for col_index in range(num_cols):
            transposed[col_index].append(row[col_index])
            
    return transposed
```

### Complexity Analysis

- **Time Complexity**: O(n * m), where n is the number of rows and m is the number of columns
  - We iterate through each element in the matrix exactly once
  - Each append operation is O(1)

- **Space Complexity**: O(n * m)
  - The transposed matrix requires the same amount of space as the original matrix
  - We create n * m new list elements

## Solution 2: NumPy-Based Approach

```python
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    import numpy as np
    
    transposed = np.array(a).T
    return transposed.tolist()
```

### Complexity Analysis

- **Time Complexity**: O(n * m), where n is the number of rows and m is the number of columns
  - Converting to NumPy array is O(n * m)
  - Transpose operation is O(n * m)
  - Converting back to list is O(n * m)

- **Space Complexity**: O(n * m)
  - NumPy array requires O(n * m) space
  - Transposed array requires O(n * m) space
  - Final list conversion requires O(n * m) space

