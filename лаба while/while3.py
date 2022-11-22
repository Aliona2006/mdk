n = int(input())
d, t, b = 1, 2, 0
a = []
while d < n:
    b = t ** 2
    if b <= n:
        a.append(b)
    t += 1
    d += 1
print(*a)