# Solution 1: Loop-Based Approach

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

# Time Complexity : O(n * m), where n is the number of rows and m is the number of columns
# Space Complexity : O(n * m)

# Solution 2: NumPy-Based Approach

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    import numpy as np
    
    num_cols = len(a[0])
    
    if num_cols != len(b):
        return -1
    
    result = np.sum(np.array(a) * np.array(b), axis=1)
    return list(result)


# Time Complexity : O(n * m), where n is the number of rows and m is the number of columns
# Space Complexity : O(n * m)