def remove_char(text, char):
    return text.replace(char, '')

def replace_char(text, old_char, new_char):
    return text.replace(old_char, new_char)

def count_char(text, char):
    return text.count(char)

# Пример использования
text = "hello world"
print(remove_char(text, 'l'))
print(replace_char(text, 'o', '0'))
print(count_char(text, 'l'))
