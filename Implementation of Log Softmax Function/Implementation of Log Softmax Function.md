# Implementation of Log Softmax Function

## Problem Statement

In machine learning and statistics, the softmax function is a generalization of the logistic function that converts a vector of scores into probabilities. The log-softmax function is the logarithm of the softmax function, and it is often used for numerical stability when computing the softmax of large numbers.

Given a 1D numpy array of scores, implement a Python function to compute the log-softmax of the array.

## Input
* `scores`: A list or 1D array of numerical scores

## Output
* A numpy array containing the log-softmax values

## Constraints
* Input contains real numbers
* Output values are always negative or zero

## Examples

### Example 1:
```
Input:
scores = [1, 2, 3]

Output:
array([-2.4076, -1.4076, -0.4076])

Reasoning:
max = 3
shifted = [1-3, 2-3, 3-3] = [-2, -1, 0]
sum(exp(shifted)) = exp(-2) + exp(-1) + exp(0) ≈ 1.5031
log_sum_exp = log(1.5031) ≈ 0.4076
log_softmax = [-2 - 0.4076, -1 - 0.4076, 0 - 0.4076]
            = [-2.4076, -1.4076, -0.4076]
```

### Example 2:
```
Input:
scores = [0, 0, 0]

Output:
array([-1.0986, -1.0986, -1.0986])

Reasoning:
All equal scores result in uniform log-probabilities.
log(1/3) ≈ -1.0986 for each element.
```

### Example 3:
```
Input:
scores = [10, 20, 30]

Output:
array([-20.0000, -10.0000, -0.0000])

Reasoning:
Large values demonstrate numerical stability.
The largest value (30) gets log-softmax close to 0.
```

### Example 4:
```
Input:
scores = [1.0, 2.0]

Output:
array([-1.3133, -0.3133])

Reasoning:
Two-element case with simple calculation.
```

## Solution: Numerically Stable Approach

```python
import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    scores_array = np.array(scores)
    max_score = np.max(scores_array)
    
    shifted_scores = scores_array - max_score
    log_sum_exp = np.log(np.sum(np.exp(shifted_scores)))
    log_softmax_output = shifted_scores - log_sum_exp
    
    return log_softmax_output
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the length of scores
  - Finding max: O(n)
  - Subtraction: O(n)
  - Exponential and sum: O(n)
  - Final subtraction: O(n)
  - Overall: O(n)

- **Space Complexity**: O(n)
  - Storing shifted scores: O(n)
  - Storing output: O(n)

