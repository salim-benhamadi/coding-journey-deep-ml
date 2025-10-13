# Normal Distribution PDF Calculator

## Problem Statement

Write a Python function to calculate the probability density function (PDF) of the normal distribution for a given value, mean, and standard deviation. The function should use the mathematical formula of the normal distribution to return the PDF value rounded to 5 decimal places.

## Input
* `x`: A float representing the value at which to evaluate the PDF
* `mean`: A float representing the mean (μ) of the distribution
* `std_dev`: A float representing the standard deviation (σ) of the distribution (σ > 0)

## Output
* A float representing the probability density value, rounded to 5 decimal places

## Constraints
* `std_dev > 0` (standard deviation must be positive)
* All inputs are real numbers

## Examples

### Example 1:
```
Input:
x = 16, mean = 15, std_dev = 2.04

Output:
0.17342

Reasoning:
Using the normal distribution PDF formula:
f(x) = (1 / (σ√(2π))) × e^(-(x-μ)²/(2σ²))
f(16) = (1 / (2.04√(2π))) × e^(-(16-15)²/(2×2.04²))
f(16) ≈ 0.17342
```

### Example 2:
```
Input:
x = 0, mean = 0, std_dev = 1

Output:
0.39894

Reasoning:
This is the standard normal distribution at x = 0.
f(0) = (1 / √(2π)) × e^0 = 1 / √(2π) ≈ 0.39894
```

### Example 3:
```
Input:
x = 10, mean = 12, std_dev = 3

Output:
0.10648

Reasoning:
f(10) = (1 / (3√(2π))) × e^(-(10-12)²/(2×3²))
f(10) ≈ 0.10648
```

## Solution: Mathematical Formula Approach

```python
import math

def normal_pdf(x, mean, std_dev):
    coefficient = 1 / math.sqrt(2 * math.pi * std_dev**2)
    exponent = math.exp(-(x - mean)**2 / (2 * std_dev**2))
    pdf_value = coefficient * exponent
    return round(pdf_value, 5)
```

### Complexity Analysis

- **Time Complexity**: O(1)
  - All operations (sqrt, exp, arithmetic) are constant time
  - No loops or iterations

- **Space Complexity**: O(1)
  - Only using constant extra space for variables
  - No additional data structures needed
