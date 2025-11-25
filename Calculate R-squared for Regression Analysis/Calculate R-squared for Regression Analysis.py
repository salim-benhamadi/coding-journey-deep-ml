import numpy as np

def r_squared(y_true, y_pred):
    y_mean = np.mean(y_true)
    SSR = np.sum((y_true - y_pred)**2)
    SST = np.sum((y_true - y_mean)**2)
    return round(1 - (SSR / SST), 3)

# Time Complexity : O(n), where n is the number of samples
# Space Complexity : O(1)