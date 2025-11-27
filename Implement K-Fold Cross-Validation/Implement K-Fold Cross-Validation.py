import numpy as np

# K-fold split generation solution
def k_fold_cross_validation(X: np.ndarray, y: np.ndarray, k=5, shuffle=True):
    """
    Implement k-fold cross-validation by returning train-test indices.
    """
    n = len(X)
    indices = np.arange(n)
    
    if shuffle:
        np.random.shuffle(indices)
    
    fold_size = n // k
    folds = []
    
    for i in range(k):
        test_start = i * fold_size
        test_end = (i + 1) * fold_size if i < k - 1 else n  
        
        test_indices = indices[test_start:test_end]
        train_indices = np.concatenate((indices[:test_start], indices[test_end:]))
        
        folds.append((train_indices.tolist(), test_indices.tolist()))
    
    return folds

# Time Complexity: O(n * k), where n is number of samples and k is number of folds
# Space Complexity: O(n), for storing indices and fold splits