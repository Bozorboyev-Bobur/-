def beginning_zeros(number: str):
    result = 0
    for n in number:
        if int(n) == 0:
            result += 1
        else:
            return result
    return result

print(beginning_zeros('100'))