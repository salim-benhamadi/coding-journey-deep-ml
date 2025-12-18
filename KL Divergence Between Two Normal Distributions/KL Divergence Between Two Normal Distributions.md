# KL Divergence Between Two Normal Distributions

## Problem Statement

Your task is to compute the Kullback Leibler (KL) divergence between two normal distributions. KL divergence measures how one probability distribution differs from a second, reference probability distribution.

Write a function `kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q)` that calculates the KL divergence between two normal distributions.

The function should return the KL divergence as a floating point number.

## Input
* `mu_p`: Mean of distribution P
* `sigma_p`: Standard deviation of distribution P
* `mu_q`: Mean of distribution Q
* `sigma_q`: Standard deviation of distribution Q

## Output
* A float representing the KL divergence from P to Q

## Constraints
* All parameters are real numbers
* Standard deviations must be positive (sigma_p > 0, sigma_q > 0)
* KL divergence is always non-negative

## Examples

### Example 1:
```
Input:
mu_p = 0.0
sigma_p = 1.0
mu_q = 1.0
sigma_q = 1.0

Output:
0.5

Reasoning:
The KL divergence between the normal distributions P and Q with parameters 
μ_P = 0.0, σ_P = 1.0 and μ_Q = 1.0, σ_Q = 1.0 is 0.5.
```

### Example 2:
```
Input:
mu_p = 0.0
sigma_p = 1.0
mu_q = 0.0
sigma_q = 1.0

Output:
0.0

Reasoning:
Identical distributions have KL divergence of 0.
```

### Example 3:
```
Input:
mu_p = 1.0
sigma_p = 2.0
mu_q = 2.0
sigma_q = 3.0

Output:
≈ 0.0849

Reasoning:
Different means and standard deviations result in non-zero KL divergence.
```

### Example 4:
```
Input:
mu_p = 0.0
sigma_p = 1.0
mu_q = 0.0
sigma_q = 2.0

Output:
≈ -0.1931

Reasoning:
When sigma_q > sigma_p, the log term becomes negative.
Note: KL divergence can be negative in intermediate calculations but final result is always non-negative when properly computed.
```

## Solution: Mathematical Formula Approach

```python
import numpy as np

def kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q):
    return np.log(sigma_q / sigma_p) + (sigma_p**2 + (mu_p - mu_q)**2) / (2 * sigma_q**2) - 0.5
```

### Complexity Analysis

- **Time Complexity**: O(1)
  - All operations (log, division, exponentiation) are constant time
  - No loops or iterations

- **Space Complexity**: O(1)
  - Only using constant extra space for the calculation
  - No additional data structures