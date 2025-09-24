import numpy as np

# Using numpy
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:

    matrix_array = np.array(a)
    try:
        reshaped_matrix = np.reshape(matrix_array, new_shape)
    except:
        return []
    return reshaped_matrix.tolist()

# Time Complexity: O(m * n), where m and n are dimensions of the matrix
# Space Complexity: O(m * n)