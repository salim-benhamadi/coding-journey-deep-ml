# Matrix times Matrix

## Problem Statement

Multiply two matrices together (return -1 if shapes of matrix don't align), i.e. C = A⋅B

## Input
* `a`: A 2D list of integers or floats representing the first matrix
* `b`: A 2D list of integers or floats representing the second matrix

## Output
* A 2D list representing the matrix multiplication result, or -1 if multiplication is not possible

## Constraints
* For matrix multiplication to be valid, the number of columns in matrix A must equal the number of rows in matrix B
* If shapes don't align, return -1

## Examples

### Example 1:
```
Input:
A = [[1,2],[2,4]], B = [[2,1],[3,4]]

Output:
[[8, 9],[16, 18]]

Reasoning:
Row 1: 1*2 + 2*3 = 8; 1*1 + 2*4 = 9
Row 2: 2*2 + 4*3 = 16; 2*1 + 4*4 = 18
```

### Example 2:
```
Input:
A = [[1,2], [2,4]], B = [[2,1], [3,4], [4,5]]

Output:
-1

Reasoning:
The length of the rows of A (2) does not equal the column length of B (2), but B has 3 rows.
Matrix A is 2x2 and matrix B is 3x2, so multiplication is not possible.
```

## Solution 1: NumPy Approach

```python
def matrixmul(a: list[list[int|float]], b: list[list[int|float]]) -> list[list[int|float]]:
    import numpy as np
    matrix_a = np.array(a)
    matrix_b = np.array(b)
    if matrix_a.shape[1] == matrix_b.shape[0]:
        return np.matmul(matrix_a, matrix_b).tolist()
    return -1
```

### Complexity Analysis

- **Time Complexity**: O(m × n × p), where m, n, p are matrix dimensions
  - Matrix A: m × n, Matrix B: n × p, Result: m × p
  - NumPy uses optimized algorithms for matrix multiplication

- **Space Complexity**: O(m × p)
  - Space needed for the result matrix of dimensions m × p

## Solution 2: Manual Calculation Approach

```python
def matrixmul(a: list[list[int|float]], b: list[list[int|float]]) -> list[list[int|float]]:
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    
    if cols_a != rows_b:
        return -1
    
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    
    return result
```

### Complexity Analysis

- **Time Complexity**: O(m × n × p), where m, n, p are matrix dimensions
  - Triple nested loops: outer two for result matrix dimensions, inner for dot product
  - Each element of result matrix requires n multiplications and additions

- **Space Complexity**: O(m × p)
  - Additional space for result matrix
  - No extra space for computation (in-place calculation)

