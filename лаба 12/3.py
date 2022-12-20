#Matrix17. Дана матрица размера M ? N и целое число K (1 ? K ? M). Найти сумму и произведение элементов K-й строки данной матрицы.
m = int(input())
n = int(input())
matrix = []
for i in range(m):
    mat = []
    for j in range(n):
        x = int(input())
        mat.append(x)
    matrix.append(mat)
k = int(input())
q = 1
for a in range(n):
    q = q*matrix[k][a]
    print(matrix[k][a])
print (q)
