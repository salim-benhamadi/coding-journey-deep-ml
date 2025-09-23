import numpy as np

# Solution 1: Using Identity Matrix Multiplication


def make_diagonal(x):
    vector_length = len(x)
    return np.eye(vector_length) * x



# Time Complexity : O(n²), where n is the length of the input vector
# Space Complexity : O(n²)


# Solution 2: Using np.diag()

def make_diagonal(x):
    return np.diag(x)


# Time Complexity : O(n²), where n is the length of the input vector
# Space Complexity : O(n²)

# Solution 3: Manual Matrix Construction

def make_diagonal(x):
    vector_length = len(x)
    diagonal_matrix = np.zeros((vector_length, vector_length))
    
    for i in range(vector_length):
        diagonal_matrix[i, i] = x[i]
        
    return diagonal_matrix

# Time Complexity : O(n²), where n is the length of the input vector
# Space Complexity : O(n²)
