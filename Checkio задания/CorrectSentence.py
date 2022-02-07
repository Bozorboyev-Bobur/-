def correct_sentence(text: str):
    if text[0].islower():
        text = text[0].upper() + text[1:]
    if text[-1] != '.':
        text += '.'
    return text

print(correct_sentence("greetings, friends"))
