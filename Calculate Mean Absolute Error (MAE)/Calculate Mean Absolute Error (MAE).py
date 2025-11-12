import numpy as np

# Vectorized NumPy solution
def mae(y_true, y_pred):
    mae_result = np.mean(np.abs(y_true - y_pred))
    return round(mae_result, 3)

# Time Complexity: O(n), where n is the number of samples
# Space Complexity: O(n), for the absolute differences array