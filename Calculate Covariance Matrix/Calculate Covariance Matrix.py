# Nested loop solution
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    def cov(X, Y):
        mean_x = sum(X) / len(X)
        mean_y = sum(Y) / len(Y)
        covariance_sum = 0
        for x, y in zip(X, Y):
            covariance_sum += (x - mean_x) * (y - mean_y)
        return covariance_sum / (len(X) - 1)

    n = len(vectors)
    covariance_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            covariance_matrix[i][j] = cov(vectors[i], vectors[j])

    return covariance_matrix

# Time Complexity: O(n² * m), where n is number of features and m is number of observations
# Space Complexity: O(n²), for the covariance matrix