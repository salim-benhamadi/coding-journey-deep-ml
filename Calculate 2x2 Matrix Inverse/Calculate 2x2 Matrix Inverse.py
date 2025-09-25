import numpy as np 

# NumPy solution
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    matrix_array = np.array(matrix)
    determinant = np.linalg.det(matrix_array)
    if determinant:
        return np.linalg.inv(matrix_array).tolist()
    return None

# Time Complexity: O(1), constant time for 2x2 matrix operations
# Space Complexity: O(1), constant space for 2x2 matrix


# Manual calculation solution
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    determinant = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    if determinant:
        inv_det = 1/determinant
        return [[inv_det*matrix[1][1], -inv_det*matrix[0][1]],
                [-inv_det*matrix[1][0], inv_det*matrix[0][0]]]
    return None

# Time Complexity: O(1), constant time for 2x2 matrix operations
# Space Complexity: O(1), constant space for 2x2 matrix