# Calculate Covariance Matrix

## Problem Statement

Write a Python function to calculate the covariance matrix for a given set of vectors. The function should take a list of lists, where each inner list represents a feature with its observations, and return a covariance matrix as a list of lists.

## Input
* `vectors`: A list of lists where each inner list represents a feature with its observations

## Output
* A 2D list (matrix) representing the covariance matrix

## Constraints
* All inner lists (features) must have the same length
* Each feature must have at least 2 observations
* Returns sample covariance (divides by n-1)

## Examples

### Example 1:
```
Input:
vectors = [[1, 2, 3], [4, 5, 6]]

Output:
[[1.0, 1.0], [1.0, 1.0]]

Reasoning:
Feature 1: [1, 2, 3], mean = 2
Feature 2: [4, 5, 6], mean = 5
Cov(1,1) = [(1-2)² + (2-2)² + (3-2)²] / 2 = 1.0
Cov(1,2) = [(1-2)(4-5) + (2-2)(5-5) + (3-2)(6-5)] / 2 = 1.0
Cov(2,1) = 1.0 (symmetric)
Cov(2,2) = [(4-5)² + (5-5)² + (6-5)²] / 2 = 1.0
```

### Example 2:
```
Input:
vectors = [[1, 2, 3, 4], [2, 4, 6, 8], [1, 3, 5, 7]]

Output:
[[1.666, 3.333, 3.333], [3.333, 6.666, 6.666], [3.333, 6.666, 6.666]]

Reasoning:
3x3 covariance matrix for 3 features with 4 observations each.
```

### Example 3:
```
Input:
vectors = [[5, 5, 5], [10, 10, 10]]

Output:
[[0.0, 0.0], [0.0, 0.0]]

Reasoning:
Both features have no variance (all values are identical), so all covariances are 0.
```

## Solution: Nested Loop Approach

```python
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    def cov(X, Y):
        mean_x = sum(X) / len(X)
        mean_y = sum(Y) / len(Y)
        covariance_sum = 0
        for x, y in zip(X, Y):
            covariance_sum += (x - mean_x) * (y - mean_y)
        return covariance_sum / (len(X) - 1)

    n = len(vectors)
    covariance_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            covariance_matrix[i][j] = cov(vectors[i], vectors[j])

    return covariance_matrix
```

### Complexity Analysis

- **Time Complexity**: O(n² × m), where n is the number of features and m is the number of observations
  - Nested loops iterate n² times (for each pair of features)
  - Each covariance calculation processes m observations
  - Overall: O(n² × m)

- **Space Complexity**: O(n²)
  - Covariance matrix requires n × n space
  - Additional O(1) space for temporary variables