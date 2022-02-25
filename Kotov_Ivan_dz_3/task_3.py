def thesaurus(*args) -> dict:
    '''Формирует словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
    '''
    dict_out = {}
    for word in args:
        dict_value = dict_out.setdefault(word[0], list())
        if word not in dict_value:
            dict_value.append(word)
            dict_out[word[0]] = dict_value
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))