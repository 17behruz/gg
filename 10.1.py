def create_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if i < n - 1:
            matrix[i][i] = (i + 1) * (i + 2)
        else:
            matrix[i][i] = n * (n + 1)
    return matrix

# Пример использования
n = 4
matrix = create_matrix(n)
for row in matrix:
    print(row)
