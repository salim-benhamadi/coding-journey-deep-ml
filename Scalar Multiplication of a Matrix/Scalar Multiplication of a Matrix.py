# NumPy solution
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    import numpy as np
    return (np.array(matrix) * scalar).tolist()

# Time Complexity: O(m * n), where m and n are dimensions of the matrix
# Space Complexity: O(m * n)


# Loop solution
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    result = [[matrix[i][j] for j in range(len(matrix[i]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] *= scalar
    return result

# Time Complexity: O(m * n), where m and n are dimensions of the matrix  
# Space Complexity: O(m * n)