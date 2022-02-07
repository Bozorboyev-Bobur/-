def split_pairs(a:str):
    num = []
    sum = ''
    i = 2
    if len(a)%2 != 0:
        a = a+'_'
    
    for x in a:
        sum = sum + x
        i -= 1
        if i == 0:
            i = 2
            num.append(sum)
            sum = ''
    return num 

print(list(split_pairs('abcd')))