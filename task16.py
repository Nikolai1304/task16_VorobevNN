# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

N = abs(int(input("Введите число N: ")))
temps = []

for i in range(N): 
    temp = random.randint(1, N)
    temps.append(temp)
print(*temps)

X = int(input("Введите число X: "))
count = 0

for i in range(N):
    if X == temps[i]:
        count+=1
        
print(count)

# вроде работает