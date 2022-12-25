#Задайте список из нескольких чисел. Напишите программу, 
#которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# lst =[]
# lst = list(map(int,input('Enter your number interval: ').split()))
# def my_sum(lst):
#     sum = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             sum += lst[i]
#     print(sum)
# my_sum(lst)

# Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

# from random import randint
# list = []
# list2 = []
# number = int(input('Enter your list length: '))
# for i in range(number):
#     list.append(randint(0, 9))
# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1
# print(list)
# print(list2)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
#разницу между максимальным и минимальным значением дробной части элементов.
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
# print(max(new_lst) - min(new_lst))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

# n = int(input('Enter your number: '))
# def decToBinary(n):
#     binaryNum = [0] * n
#     i = 0
#     while (n > 0):
#         binaryNum[i] = n % 2
#         n = int(n / 2)
#         i += 1
#     for j in range(i - 1, -1, -1):
#         print(binaryNum[j], end = "")
# decToBinary(n)

#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0
#%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%B
#A%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%
#BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1
#%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1
#%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4
#%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5
#%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)

# n = int(input('Enter your number: '))

# def get_fibonacci(n):
#     fbn_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fbn_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fbn_nums.insert(0, a)
#         a, b = b, a - b
#     return fbn_nums

# fbn_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fbn_nums.index(0))