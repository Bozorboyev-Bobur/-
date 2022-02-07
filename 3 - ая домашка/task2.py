# Задание №2
# Описание:
# Ограничения: 10 строк кода
# Ваш друг живет в многоэтажном жилом доме. Вы знаете его номер квартиры (apartment), общее количество квартир в доме (total) и этажность дома (floors). 
# Условия:
# apartment > 0 (номер квартиры должен больше нуля)
# apartment <= total (номер квартиры должен быть меньше общего количества квартир)
# floors > 0 (этажность дома должна быть больше нуля)
# total % floors = 0 (количество квартир гарантированно делится на количество этажей) 
# У дома только 1 подъезд. Нумерация квартир начинается с 1 этажа и идет вверх. Например, если в 10-этажке есть 120 квартир, то квартиры 1-12 будут расположены на первом этаже, квартиры 13-24 - на втором этаже и т.д. Вам нужно посчитать, на каком этаже находится квартира вашего друга.
# Входные данные:
# Три числа, ввод которых производится отдельно: 
# Количество квартир (total)
# Количество этажей (floors)
# Номер квартиры вашего друга (apartment)
# Вывод: Номер этажа
# Пример 1: 
# Входные данные:
# 120
# 10
# 15
# Вывод: 2


apartment = int(input('Enter the apartment number: '))
total = int(input('Enter the total number of apartments in the house: '))
floors = int(input('Enter the number of floors of the house: '))

if apartment > 0 and apartment <= total and floors > 0 and total % floors == 0:
    floor = apartment // (total / floors)
    if apartment == total: print(floors)
    elif apartment % (total / floors) == 0: print(floor)
    else:
        friend_floor = floor + 1
        print(friend_floor)
else: print('Error')