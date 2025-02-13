import numpy as np

def generate_matrix():
    size = 10
    matrix = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if j == size - i - 1:
                matrix[i][j] = i
            elif i == 0:
                matrix[i][j] = j + 1
            elif j == size - 1:
                matrix[i][j] = size - i - 1
    return matrix

matrix = generate_matrix()
print(matrix)