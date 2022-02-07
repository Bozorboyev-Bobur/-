def max_digit(number: int):
    number = list(str(number))
    number = [eval(x) for x in number]
    return max(number)

print(max_digit(0))