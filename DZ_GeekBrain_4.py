# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = input("Введите число: ")
a = 0
for i in n:
    while int(i) > a:
        a = int(i)
print(a)
