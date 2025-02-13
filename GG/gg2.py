def sum_matrix_halves(matrix):
    N, M = matrix.shape
    left_half = matrix[:, :M//2]
    right_half = matrix[:, M//2:]

    sum_left = np.sum(left_half, axis=0)
    sum_even_right = np.sum(right_half[:, ::2], axis=0)

    return sum_left, sum_even_right

sum_left, sum_even_right = sum_matrix_halves(matrix)
print("Суммы столбцов левой половины:", sum_left)
print("Суммы четных столбцов правой половины:", sum_even_right)