
def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    list_in.insert(1, '"')
    list_in.insert(3, '"')
    list_in.insert(5, '"')
    list_in.insert(7, '"')
    list_in.insert(12, '"')
    list_in.insert(14, '"')
    #print(' '.join(map(str, list_in)))
   # print(list_in)

    str_out = ''

    for i in list_in:
        if ord(i[0]) >= 48 and ord(i[0]) <= 57 and len(i) == 1:
            i = f'0{i[0]}'
        if ord(i[0]) == 43 or ord(i[0]) == 45:
            i = f'{i[0]}0{i[1]}'
        str_out += i + ' '
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)


