def remove_all_before(items, border):
     if border not in items:
        return items
     else:
        x = items.index(border)
        return items[x:]

print(list(remove_all_before([1, 2, 3, 4, 5], 3)))