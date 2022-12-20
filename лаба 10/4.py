#Func9. Описать функцию Even(K) логического типа, возвращающую True, если целый параметр K является четным, и False в противном случае.
# С ее помощью найти количество четных чисел в наборе из 10 целых чисел.
def Even(K):
    if K % 2 == 0:
        return True
    else:
        return False
counter = 0
for i in range(10):
    K = int(input())
    if Even(K) is True:
        counter += 1
print (counter)