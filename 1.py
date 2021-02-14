# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.

f1 = open('1-1.txt', 'w', encoding='utf-8')
line = input('Введите текст \n')
while line:
    f1.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

f1.close()
f1 = open('1-1.txt', 'r')
content = f1.readlines()
print(content)
f1.close()