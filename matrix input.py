def new_matrix(row: int, col: int):
    matrix = [[int(input()) for x in range (col)] for y in range(row)]
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end = " ")
        return matrix

m1 = new_matrix(2, 2)
print(m1)
