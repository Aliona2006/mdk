#Matrix7. Дана матрица размера M ? N и целое число K (1 ? K ? M). Вывести элементы K-й строки данной матрицы.
m = int(input())
n = int(input())
matrix = []
for i in range(m):
    line = []
    for j in range(n):
        x = int(input())
        line.append(x)
    matrix.append(line)
k = int(input())
print (matrix[k])