def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    sep_list = [i.split() for i in list_in]

    names = []
    for i in sep_list:
        names.append(i[-1])
    print(sep_list)

    list_out = []
    for i in names:
        list_out.append(f'Привет, {i.capitalize()}!')


    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
