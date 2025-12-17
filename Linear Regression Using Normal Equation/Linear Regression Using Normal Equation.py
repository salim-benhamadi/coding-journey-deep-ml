import numpy as np

# Normal equation solution
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    y = np.array(y)
    
    # Normal equation: theta = (X^T * X)^(-1) * X^T * y
    theta = np.linalg.inv(X.T @ X) @ X.T @ y
    
    # Round to 4 decimal places
    theta = np.round(theta, 4)
    
    return theta.tolist()

# Time Complexity: O(n^2 * m + n^3), where n is number of features and m is number of samples
# Space Complexity: O(n^2), for storing X^T * X matrix