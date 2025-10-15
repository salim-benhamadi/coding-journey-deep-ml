import numpy as np

# Gradient descent solution

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    n, m = X.shape
    theta = np.zeros((m, 1))

    def predict(X, theta):
        return np.dot(X, theta)

    def update_weights(X, y, theta, alpha):
        predictions = predict(X, theta)
        error = predictions - y.reshape(-1, 1)  
        gradient = (1 / n) * np.dot(X.T, error)  
        theta -= alpha * gradient
        return theta
    
    for _ in range(iterations):
        theta = update_weights(X, y, theta, alpha)

    return np.round(theta, 4)

# Time Complexity: O(iterations * m * n²), where m is samples and n is features
# Space Complexity: O(n), for storing coefficients and gradients