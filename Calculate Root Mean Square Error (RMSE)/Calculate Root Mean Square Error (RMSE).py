import numpy as np

# Vectorized NumPy solution
def rmse(y_true, y_pred):
    rmse_result = np.sqrt(np.mean((y_true - y_pred)**2))
    return round(rmse_result, 3)

# Time Complexity: O(n), where n is the number of samples
# Space Complexity: O(n), for the squared differences array