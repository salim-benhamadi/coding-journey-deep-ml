import math

# List comprehension solution
def softmax(scores: list[float]) -> list[float]:
    exp_scores = [math.exp(score) for score in scores]
    exp_sum = sum(exp_scores)
    probabilities = [round(exp_score / exp_sum, 4) for exp_score in exp_scores]
    return probabilities

# Time Complexity: O(n), where n is the number of scores
# Space Complexity: O(n), for storing exponentials and probabilities