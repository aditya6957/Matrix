def make_zeros(n_rows: int, n_columns: int):
    matrix = []
    for i in range(n_rows):
        matrix.append([0] * n_columns)
    return matrix
print(make_zeros(2, 2))