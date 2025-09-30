import numpy as np

# NumPy solution using characteristic equation
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    matrix_array = np.array(matrix)
    determinant = np.linalg.det(matrix_array)
    trace = np.trace(matrix_array)
    eigenvalues = np.roots([1, -trace, determinant])
    return sorted(eigenvalues.real, reverse=True)

# Time Complexity: O(1), constant time for 2x2 matrix operations
# Space Complexity: O(1), constant space for 2x2 matrix


# NumPy built-in solution
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    matrix_array = np.array(matrix)
    eigenvalues = np.linalg.eigvals(matrix_array)
    return sorted(eigenvalues.real, reverse=True)

# Time Complexity: O(1), constant time for 2x2 matrix operations
# Space Complexity: O(1), constant space for 2x2 matrix