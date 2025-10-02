# Poisson Distribution Probability Calculator

## Problem Statement

Write a Python function to calculate the probability of observing exactly k events in a fixed interval using the Poisson distribution formula. The function should take k (number of events) and lam (mean rate of occurrences) as inputs and return the probability rounded to 5 decimal places.

## Input
* `k`: An integer representing the number of events
* `lam`: A float representing the mean rate of occurrences (λ)

## Output
* A float representing the probability, rounded to 5 decimal places

## Constraints
* `k >= 0` (non-negative integer)
* `lam > 0` (positive real number)

## Examples

### Example 1:
```
Input:
k = 3, lam = 5

Output:
0.14037

Reasoning:
Using the Poisson formula: P(X = k) = (λ^k × e^(-λ)) / k!
P(X = 3) = (5^3 × e^(-5)) / 3! = (125 × 0.00674) / 6 ≈ 0.14037
```

### Example 2:
```
Input:
k = 0, lam = 2

Output:
0.13534

Reasoning:
P(X = 0) = (2^0 × e^(-2)) / 0! = (1 × 0.13534) / 1 = 0.13534
```

### Example 3:
```
Input:
k = 5, lam = 3

Output:
0.10082

Reasoning:
P(X = 5) = (3^5 × e^(-3)) / 5! = (243 × 0.04979) / 120 ≈ 0.10082
```

## Solution: Mathematical Formula Approach

```python
import math

def poisson_probability(k, lam):
    probability = (lam**k * math.exp(-lam)) / math.factorial(k)
    return round(probability, 5)
```

### Complexity Analysis

- **Time Complexity**: O(k), where k is the number of events
  - Computing λ^k: O(log k) using fast exponentiation, but typically O(k) for simple exponentiation
  - Computing e^(-λ): O(1) using math.exp
  - Computing k!: O(k) as factorial requires k multiplications
  - Overall: O(k)

- **Space Complexity**: O(1)
  - Only using constant extra space for the result
  - No additional data structures needed
