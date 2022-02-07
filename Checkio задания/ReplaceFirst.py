def replace_first(items: list):
    return items[1:] + items[:1]

print(list(replace_first([1, 2, 3, 4])))