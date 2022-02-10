def matrix(m,n):
    o=[]
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input("Enter o[i][j]"))
        row.append(inp)
    return o

def sum(A,B):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(B)):
            row.append(A[i][j]+B[i][j])
        output.append(row)
    return output

m = int(input("Enter number of rows"))
n = int(input("Enter number of columns"))

print("Enter matrix A")
A = matrix(m, n)
print(A)

print("Enter matrix B")
B= matrix(m, n)
print(B)

s = sum(A, B)
print(s)

