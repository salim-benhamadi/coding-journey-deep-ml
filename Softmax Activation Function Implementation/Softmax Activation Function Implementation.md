# Softmax Activation Function Implementation

## Problem Statement

Write a Python function that computes the softmax activation for a given list of scores. The function should return the softmax values as a list, each rounded to four decimal places.

## Input
* `scores`: A list of floats representing the input scores

## Output
* A list of floats representing the softmax probabilities, rounded to 4 decimal places

## Constraints
* All inputs are real numbers
* The output should sum to approximately 1.0 (allowing for rounding errors)

## Examples

### Example 1:
```
Input:
scores = [1, 2, 3]

Output:
[0.0900, 0.2447, 0.6652]

Reasoning:
e^1 = 2.7183, e^2 = 7.3891, e^3 = 20.0855
Sum = 30.1929
Softmax: [2.7183/30.1929, 7.3891/30.1929, 20.0855/30.1929] = [0.0900, 0.2447, 0.6652]
```

### Example 2:
```
Input:
scores = [0, 0, 0]

Output:
[0.3333, 0.3333, 0.3333]

Reasoning:
All scores are equal, so each gets equal probability (1/3).
```

### Example 3:
```
Input:
scores = [10, 20, 30]

Output:
[0.0, 0.0, 1.0]

Reasoning:
Large differences in scores cause the largest value to dominate.
The exponential of 30 is much larger than 10 or 20.
```

## List Comprehension Approach

```python
import math

def softmax(scores: list[float]) -> list[float]:
    exp_scores = [math.exp(score) for score in scores]
    exp_sum = sum(exp_scores)
    probabilities = [round(exp_score / exp_sum, 4) for exp_score in exp_scores]
    return probabilities
```

### Complexity Analysis

- **Time Complexity**: O(n), where n is the number of scores
  - First pass: compute exponentials for all scores
  - Second pass: sum all exponentials
  - Third pass: divide each by sum and round
  - Overall: O(n)

- **Space Complexity**: O(n)
  - Storing exponentials: O(n)
  - Storing probabilities: O(n)

