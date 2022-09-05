# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def del_words_with_str_from_text(text, str):
    list_of_words = text.replace(',', ' ,').replace(
        '.', ' .').replace('!', ' !').replace('?', ' ?').split(' ')
    for s in range(0, len(list_of_words)):
        if s < len(list_of_words) and list_of_words[s].find(str) != -1:
            list_of_words.remove(list_of_words[s])
            s -= 1
    str_of_words = ' '.join(list_of_words).replace(' ,', ',').replace(
        ' .', '.').replace(' !', '!').replace(' ?', '?') + ' '
    i = 0
    while i < len(str_of_words) - 1:
        if (str_of_words[i] == ',' or str_of_words[i] == '.' or str_of_words[i] == '?' or str_of_words[i] == '!') and str_of_words[i + 1] != ' ':
            str_of_words = str_of_words[:i + 1] + str_of_words[i + 2:]
            i = i - 1

        if i == 0 and (str_of_words[i] == ',' or str_of_words[i] == ' ' or str_of_words[i] == '.' or str_of_words[i] == '?' or str_of_words[i] == '!'):
            str_of_words = str_of_words[1:]
            i = i - 1
        i += 1

    return str_of_words


print(del_words_with_str_from_text('Фбв олв абвол абв. Ьабв, бабв?', 'абв'))
print(del_words_with_str_from_text(
    'Фбабв, олв варрп! Абвол абв. Ьабв, бабв?', 'абв'))
