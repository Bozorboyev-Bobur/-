def between_markers(text: str, begin: str, end: str):
    start = text.find(begin) + 1
    finish = text.find(end)
    return text[start:finish]

print(between_markers('What is >apple<', '>', '<'))