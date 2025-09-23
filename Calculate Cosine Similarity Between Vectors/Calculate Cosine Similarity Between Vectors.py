import numpy as np

def cosine_similarity(v1, v2):
    magnitude_v1 = np.sqrt(np.sum(v1**2))
    magnitude_v2 = np.sqrt(np.sum(v2**2))
    dot_product = np.dot(v1, v2)
    
    similarity = dot_product / (magnitude_v1 * magnitude_v2)
    return round(similarity, 3)

# Time Complexity : O(n), where n is the length of the vectors
# Space Complexity : O(1)
