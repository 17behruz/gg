def remove_max_element(matrix):
    n = len(matrix)
    max_val = -1
    max_pos = (0, 0)

    for i in range(n):
        for j in range(n):
            if abs(matrix[i][j]) > max_val:
                max_val = abs(matrix[i][j])
                max_pos = (i, j)

    new_matrix = np.delete(matrix, max_pos[0], axis=0)
    new_matrix = np.delete(new_matrix, max_pos[1], axis=1)

    return new_matrix


new_matrix = remove_max_element(matrix)
print(new_matrix)