import math

# Mathematical formula solution
def normal_pdf(x, mean, std_dev):
    coefficient = 1 / math.sqrt(2 * math.pi * std_dev**2)
    exponent = math.exp(-(x - mean)**2 / (2 * std_dev**2))
    pdf_value = coefficient * exponent
    return round(pdf_value, 5)

# Time Complexity: O(1), constant time calculation
# Space Complexity: O(1), only using constant extra space