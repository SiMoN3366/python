# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

f2 = open('2-2.txt', 'r', encoding='utf-8')
content = f2.read()
print(f'Содержимое файла: \n {content}')
f2 = open('2-2.txt', 'r', encoding='utf-8')
content = f2.readlines()
print(f'Количество строк в файле - {len(content)}')
f2 = open('2-2.txt', 'r', encoding='utf-8')
content = f2.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} строки {len(content[i])}')
f2 = open('2-2.txt', 'r', encoding='utf-8')
content = f2.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
f2.close()