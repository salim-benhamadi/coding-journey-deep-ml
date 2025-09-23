# Calculate Cosine Similarity Between Vectors

## Problem Statement

In this task, you need to implement a function `cosine_similarity(v1, v2)` that calculates the cosine similarity between two vectors. Cosine similarity measures the cosine of the angle between two vectors, indicating their directional similarity.

## Input
* `v1` and `v2`: Numpy arrays representing the input vectors.

## Output
* A float representing the cosine similarity, rounded to three decimal places.

## Constraints
* Both input vectors must have the same shape.
* Input vectors cannot be empty or have zero magnitude.

## Examples

### Example 1:
```
Input:
import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
print(cosine_similarity(v1, v2))

Output:
1.0
```

## Solution

```python
import numpy as np

def cosine_similarity(v1, v2):
    magnitude_v1 = np.sqrt(np.sum(v1**2))
    magnitude_v2 = np.sqrt(np.sum(v2**2))
    dot_product = np.dot(v1, v2)
    
    similarity = dot_product / (magnitude_v1 * magnitude_v2)
    return round(similarity, 3)
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the vectors
  - Computing each magnitude: O(n) for squaring and summing
  - Computing dot product: O(n)
  - Overall: O(n) + O(n) + O(n) = O(n)

- **Space Complexity**: O(1)
  - Only scalar variables are stored
  - No additional arrays are created

