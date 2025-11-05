import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    scores_array = np.array(scores)
    max_score = np.max(scores_array)
    
    shifted_scores = scores_array - max_score
    log_sum_exp = np.log(np.sum(np.exp(shifted_scores)))
    log_softmax_output = shifted_scores - log_sum_exp
    
    return log_softmax_output

# Time Complexity: O(n), where n is the length of scores
# Space Complexity: O(n), for storing the output array