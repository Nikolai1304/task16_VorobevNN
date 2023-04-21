# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

N = abs(int(input("Введите число N: ")))
temps = []

for i in range(N): 
    temp = random.randint(0, N)
    temps.append(temp)
print(*temps)

X = int(input("Введите число X: "))

my_list = []
for i in range(0,N):
    A = X - temps[i]
    if A<0:
        A = A*(-1)
    i+=1
    my_list.append(A)
    #print(my_list) 
# print(my_list[2]) #просто проверял, что выводит на печать

for i in range(N):
    min = temps[0]
    if my_list[i]<my_list[i+1]:
        min = temps[i]
        i+=1
        print(min)
  
#НЕ РАБОТАЕТ. В интернете видел решение, просто хотелось по своему
# доделать. Мысль была такая - сначала создаем список из разницы 
# введенного значения Х и элементами списка N, затем выбираем минимальное.
# Получается какая то ерунда в итоге
  
  
# for i in my_list:
#     if my_list[i]<= my_list[0]:
#         min = my_list[i]
#         my_list[0] = my_list[i]
#         i+=1
#         print(min)
    
    

    
    
    # if A <= B:
    #     A = temps[i]
    #     temps[i] = temps[i+1]
    #     temps[i+1] = temps[i+2]
    # else:
    #     A = temps[i+1]
    #     temps[i] = temps[i+1]
    #     temps[i+1] = temps[i+2]
                 
    # print(A)

