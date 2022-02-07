# Задание №1
# Ограничения: 10 строк кода
# Описание:
# Вам даётся текущее время (часы и минуты) и значение дельты(разницы) в часах(может быть любым целым числом). Вам необходимо вывести время в дельта-часах от текущего времени в виде единой строки в формате ЧЧ:ММ.
# Входные данные:
# Три числа, ввод которых производится отдельно - часы, минуты и дельта.
# Вывод:
# Строка в 24-часовом формате ЧЧ:ММ. Часы и минуты должны быть двухзначными числами, например ночное время 2 часа 5 минут, то вывод должен быть 02:05. Вам нужно реализовать вывод в консоль без использования форматированных строк! Использовать только, что проходили на уроке!
# Пример 1: 
# Входные данные:
# 13
# 29 
# 2 
# Вывод: 15:29
# Пример 2:
# Входные данные: 
# 15
# 2
# -17
# Вывод: 22:02 
# Пример 3:
# Входные данные:
# 0
# 0 
# 48
# Вывод: 00:00



hrs = int(input('Enter hours: '))
mins = int(input('Enter minutes: '))
delta = int(input('Enter delta hours: '))

if hrs >= 0 and 0 <= mins <= 59:
    new_hrs = (hrs + delta) % 24
    if new_hrs <= 9: new_hrs = '0' + str(new_hrs)
    if mins <= 9: mins = '0' + str(mins)
    print(f'{new_hrs}:{mins}')
else: print('Error')