# Binomial Distribution Probability

## Problem Statement

Write a Python function to calculate the probability of achieving exactly k successes in n independent Bernoulli trials, each with probability p of success, using the Binomial distribution formula.

## Input
* `n`: An integer representing the number of trials
* `k`: An integer representing the number of successes
* `p`: A float representing the probability of success on each trial (0 ≤ p ≤ 1)

## Output
* A float representing the probability, rounded to 5 decimal places

## Constraints
* `0 <= k <= n`
* `0 <= p <= 1`
* `n >= 1`

## Examples

### Example 1:
```
Input:
n = 6, k = 2, p = 0.5

Output:
0.23438

Reasoning:
Using the Binomial formula: P(X = k) = C(n,k) × p^k × (1-p)^(n-k)
P(X = 2) = C(6,2) × 0.5^2 × 0.5^4 = 15 × 0.25 × 0.0625 = 0.23438
```

### Example 2:
```
Input:
n = 10, k = 3, p = 0.3

Output:
0.26683

Reasoning:
P(X = 3) = C(10,3) × 0.3^3 × 0.7^7
P(X = 3) = 120 × 0.027 × 0.0823543 ≈ 0.26683
```

### Example 3:
```
Input:
n = 5, k = 5, p = 0.8

Output:
0.32768

Reasoning:
P(X = 5) = C(5,5) × 0.8^5 × 0.2^0 = 1 × 0.32768 × 1 = 0.32768
```

## Solution: Mathematical Formula Approach

```python
import math

def binomial_probability(n, k, p):
    combinations = math.comb(n, k)
    probability = combinations * (p**k) * (1 - p)**(n - k) 
    return round(probability, 5)
```

### Complexity Analysis

- **Time Complexity**: O(k), where k is the number of successes
  - `math.comb(n, k)` uses an optimized algorithm with O(min(k, n-k)) complexity
  - Exponentiation operations are O(log k) but typically treated as O(1) for reasonable values
  - Overall dominated by combination calculation

- **Space Complexity**: O(1)
  - Only using constant extra space for variables
  - No additional data structures needed

