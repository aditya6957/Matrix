def zero_matrix(n_rows: int, n_columns: int):
        matrix = []
        for i in range(n_rows):
            matrix.append([0] * n_columns)
        return matrix

R1 = int(input("Enter number of rows for first matrix"))
C1 = int(input("Enter number of columns for first matrix"))
M1 = [[int(input()) for x in range (C1)] for y in range(R1)]
for i in range(R1):
    for j in range(C1):
        print(M1[i][j], end = " ")
    print()

R2 = int(input("Enter number of rows for second matrix"))
C2 = int(input("Enter number of columns for second matrix"))
M2 = [[int(input()) for x in range (C2)] for y in range(R2)]
for i in range(R2):
    for j in range(C2):
        print(M1[i][j], end = " ")
    print()

if C1 != R2:
    print("Multiplication is not possible")
else:
    result = zero_matrix(C1, R2)
    for i in range(len(M1)): 
        for j in range(len(M2[0])): 
            for k in range(len(M2)): 
                result[i][j] += M1[i][k] * M2[k][j] 
print("The Resultant Matrix Is ::>")
for r in result: 
   print(r) 