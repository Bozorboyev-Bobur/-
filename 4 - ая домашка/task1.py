# Задание №1
# Написать сортировку 4 чисел.


num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
num3 = int(input('Enter 3th number: '))
num4 = int(input('Enter 4th number: '))


# if -----------------------------------------------------------------------

# if num1 < num2 < num3 < num4: print(num1, num2, num3, num4)
# if num1 < num2 < num4 < num3: print(num1, num2, num4, num3)
# if num1 < num4 < num2 < num3: print(num1, num4, num2, num3)
# if num1 < num4 < num3 < num2: print(num1, num4, num3, num2)
# if num1 < num3 < num4 < num2: print(num1, num3, num4, num2)
# if num1 < num3 < num2 < num4: print(num1, num3, num2, num4)

# if num2 < num1 < num3 < num4: print(num2, num1, num3, num4)
# if num2 < num3 < num1 < num4: print(num2, num3, num1, num4)
# if num2 < num3 < num4 < num1: print(num2, num3, num4, num1)
# if num2 < num4 < num3 < num1: print(num2, num4, num3, num1)
# if num2 < num4 < num1 < num3: print(num2, num4, num1, num3)
# if num2 < num1 < num4 < num3: print(num2, num1, num4, num3)

# if num3 < num1 < num2 < num4: print(num3, num1, num2, num4)
# if num3 < num2 < num1 < num4: print(num3, num2, num1, num4)
# if num3 < num2 < num4 < num1: print(num3, num2, num4, num1)
# if num3 < num4 < num2 < num1: print(num3, num4, num2, num1)
# if num3 < num4 < num1 < num2: print(num3, num4, num1, num2)
# if num3 < num1 < num4 < num2: print(num3, num1, num4, num2)

# if num4 < num1 < num2 < num3: print(num4, num1, num2, num3)
# if num4 < num2 < num1 < num3: print(num4, num2, num1, num3)
# if num4 < num2 < num3 < num1: print(num4, num2, num3, num1)
# if num4 < num3 < num2 < num1: print(num4, num3, num2, num1)
# if num4 < num3 < num1 < num2: print(num4, num3, num1, num2)
# if num4 < num1 < num3 < num2: print(num4, num1, num3, num2)

# if num1 == num2 == num3 == num4: print(num1, num2, num3, num4)




# max, min and for ------------------------------

numbers = [num1, num2, num3, num4]
result = []
for i in range(len(numbers)):
    result.append(min(numbers))
    numbers.remove(min(numbers))
print(result)