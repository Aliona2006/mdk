#Matrix1. Даны целые положительные числа M и N.
# Сформировать целочисленную матрицу размера M ? N, у которой все элементы I-й строки имеют значение 10·I (I = 1, …, M).
m = int(input())
n = int(input())
a = []
for j in range(m):
    mat = []
    for i in range(1,n+1):
        mat.append(10*i)
    a.append(mat)
for i in a:
    print (*i)