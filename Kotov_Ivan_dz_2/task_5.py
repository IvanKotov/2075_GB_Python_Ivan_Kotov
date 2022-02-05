from random import uniform
import math

def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    str_out = []
    for i in list_in:
        i = i * 100
        int_num = math.floor(i // 100)
        div_rem = math.floor(i % 100)
        if int_num < 10:
            int_num = f'0{int_num}'
        elif div_rem < 10:
            div_rem = f'{div_rem}0'
        str_out.append(f'{int_num} руб {div_rem} коп')
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    return list_in


# зафиксируйте здесь информацию по исходному списку my_list
print(id(my_list))
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(id(my_list))
print(result_2)


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_out = sorted(list_in, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_out = sorted(list_in, reverse=True)
    return list_out[0:5]


result_4 = check_five_max_elements(my_list)
print(result_4)