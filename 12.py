from random import uniform
n = int(input("размер списка: "))
summ = 0
first, second = n, n
lst = [uniform(-9, 9) for _ in range(n)]
def summa():
    global summ
    for i in range(len(lst)):
        if i % 2 !=0:
            summ=summ+lst[i]
    return summ
def summo():
    global first, second
    for b in range(len(lst)-1):
        if first == n and lst[b] < 0:
            first = b
        if second == n and lst[-b-1] < 0:
            second = b - 1
        if first and second:
            break
def zip():
    global u
    for u in range (len(lst)-1):
        if abs(lst[u]) < 1:
            lst[u] = 0
zip()
print(lst)
summa()
print("сумму элементов массива с нечетными номерами: ", summ)
summo()
print("сумму элементов массива, расположенных между первыми последним отрицательными элементами: ", sum(lst[first + 1: second]))

