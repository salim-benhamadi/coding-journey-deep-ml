import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> tuple[list[float], float]:
    # Convert inputs to numpy arrays
    y_true = np.array(labels)
    W = np.array(weights)
    X = np.array(features)
    
    # Compute linear combination: z = w·x + b
    z = np.dot(X, W) + bias
    
    # Apply sigmoid activation: σ(z) = 1 / (1 + e^(-z))
    y_pred = round(1 / (1 + np.exp(-z)), 4).tolist()

    # Compute mean squared error
    mse = round(np.mean((y_true - y_pred) ** 2), 4)

    return y_pred, mse


# Time Complexity: O(m * n), where m is number of samples and n is number of features
# Space Complexity: O(m), for storing predictions and intermediate calculations