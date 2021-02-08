# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.

def my_func(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)

my_func(name= 'Roman', surname='Frolov', year=1985, city='Spb', email='sa2rolru@gmail.com', phone='8-937-xxx-1812')