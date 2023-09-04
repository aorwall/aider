def pig_latin(text):
    py_text = ''
    for word in text.split():
        py_text += word[1:] + word[0] + 'ay' + ' '
    return py_text[:-1]