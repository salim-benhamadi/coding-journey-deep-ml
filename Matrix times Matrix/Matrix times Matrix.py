# NumPy solution
def matrixmul(a: list[list[int|float]], b: list[list[int|float]]) -> list[list[int|float]]:
    import numpy as np
    matrix_a = np.array(a)
    matrix_b = np.array(b)
    if matrix_a.shape[1] == matrix_b.shape[0]:
        return np.matmul(matrix_a, matrix_b).tolist()
    return -1

# Time Complexity: O(m * n * p), where m, n, p are matrix dimensions
# Space Complexity: O(m * p), for the result matrix


# Manual calculation solution
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

# Time Complexity: O(m * n * p), where m, n, p are matrix dimensions
# Space Complexity: O(m * p), for the result matrix