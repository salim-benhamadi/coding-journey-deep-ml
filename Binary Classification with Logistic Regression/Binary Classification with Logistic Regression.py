import numpy as np

# Vectorized logistic regression solution
def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
    linear_output = np.dot(X, weights) + bias
    probabilities = 1 / (1 + np.exp(-linear_output))
    predictions = np.where(probabilities >= 0.5, 1, 0)
    return predictions

# Time Complexity: O(m * n), where m is number of samples and n is number of features
# Space Complexity: O(m), for storing probabilities and predictions