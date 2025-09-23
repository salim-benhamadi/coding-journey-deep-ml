## Solution 1: Loop-Based Approach

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    num_cols = len(a[0])
    transposed = [[] for _ in range(num_cols)]
    
    for row in a:
        for col_index in range(num_cols):
            transposed[col_index].append(row[col_index])
            
    return transposed

# Time Complexity : O(n * m), where n is the number of rows and m is the number of columns
# Space Complexity : O(n * m)

## Solution 2: NumPy-Based Approach

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    import numpy as np
    
    transposed = np.array(a).T
    return transposed.tolist()

# Time Complexity : O(n * m), where n is the number of rows and m is the number of columns
# Space Complexity : O(n * m)