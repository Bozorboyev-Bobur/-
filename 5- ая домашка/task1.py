# Написать обработку ошибки для программы.
# Условие: 
# Пользователь вводить целые числа. Должна произойти ошибка, если введённое число нечетное.
# Реализовать способом
# try…except 
# if…else


# №1
# while True:
#     try:
#         numOfIntegers = int(input('Enter number of integers: '))
#         if numOfIntegers < 2: raise ValueError('The number of integers must be more than 1')
#         else: break
#     except ValueError as ve: print(ve)

# while True:
#     try:
#         for i in range(1, numOfIntegers + 1):
#             num = int(input(f'Enter {i} integer: '))
#             if num % 2 != 0: raise ValueError("The numbers don't have to be odd")
#         else: break
#     except ValueError as ve: print(ve)


# №2
while True:
    numOfIntegers = int(input('Enter number of integers: '))
    if numOfIntegers < 2:
        print('The number of integers must be more than 1')
    else: break

for i in range(1, numOfIntegers + 1):
    while True:
        num = int(input(f'Enter {i} integer: '))
        if num % 2 != 0:
            print("The numbers don't have to be odd")
        
        else: break