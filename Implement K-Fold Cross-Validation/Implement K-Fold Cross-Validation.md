# Implement K-Fold Cross-Validation

## Problem Statement

Implement a function to generate train and test splits for K-Fold Cross-Validation. Your task is to divide the dataset into k folds and return a list of train-test indices for each fold.

## Input
* `X`: A numpy array containing feature data
* `y`: A numpy array containing labels
* `k`: An integer representing the number of folds (default: 5)
* `shuffle`: A boolean indicating whether to shuffle data (default: True)

## Output
* A list of k tuples, where each tuple contains (train_indices, test_indices) as lists

## Constraints
* `k > 0` and `k <= n` where n is the number of samples
* Each sample appears in exactly one test set
* Each sample appears in k-1 training sets

## Examples

### Example 1:
```
Input:
X = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([0,1,2,3,4,5,6,7,8,9])
k = 5
shuffle = False

Output:
[([2, 3, 4, 5, 6, 7, 8, 9], [0, 1]), 
 ([0, 1, 4, 5, 6, 7, 8, 9], [2, 3]), 
 ([0, 1, 2, 3, 6, 7, 8, 9], [4, 5]), 
 ([0, 1, 2, 3, 4, 5, 8, 9], [6, 7]), 
 ([0, 1, 2, 3, 4, 5, 6, 7], [8, 9])]

Reasoning:
With 10 samples and k=5, each fold has 2 test samples.
Fold 1: test [0,1], train [2-9]
Fold 2: test [2,3], train [0,1,4-9]
Fold 3: test [4,5], train [0-3,6-9]
Fold 4: test [6,7], train [0-5,8-9]
Fold 5: test [8,9], train [0-7]
```

### Example 2:
```
Input:
X = np.array([0,1,2,3,4])
y = np.array([0,1,2,3,4])
k = 3
shuffle = False

Output:
[([1, 2, 3, 4], [0]), 
 ([0, 2, 3, 4], [1]), 
 ([0, 1], [2, 3, 4])]

Reasoning:
With 5 samples and k=3:
Fold 1: 1 test sample [0]
Fold 2: 1 test sample [1]
Fold 3: 3 test samples [2,3,4] (last fold gets remainder)
```

### Example 3:
```
Input:
X = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,4,5,6])
k = 2
shuffle = False

Output:
[([3, 4, 5, 6], [1, 2]), 
 ([1, 2], [3, 4, 5, 6])]

Reasoning:
With 6 samples and k=2, each fold has 3 test samples.
```

## Solution: K-Fold Split Generation Approach

```python
import numpy as np

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
```

### Complexity Analysis

- **Time Complexity**: O(n × k), where n is the number of samples and k is the number of folds
  - Shuffling (optional): O(n)
  - Creating k folds: O(k)
  - For each fold, concatenating train indices: O(n)
  - Overall: O(n × k)

- **Space Complexity**: O(n)
  - Storing indices array: O(n)
  - Storing all folds with train/test splits: O(n × k) but dominated by O(n) per fold
  - Overall: O(n)