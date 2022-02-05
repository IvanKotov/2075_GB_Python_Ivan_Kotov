def sum_list_1(dataset: list) -> int:
    sum_cub_1 = 0
    for i in range(len(dataset)):
        sum_numbers = 0
        number = dataset[i]
        #print(number)
        while number != 0:
            sum_numbers = sum_numbers + number % 10
            number = number // 10
        if sum_numbers % 7 == 0:
            sum_cub_1 = dataset[i]
    return sum_cub_1


def sum_list_2(dataset: list) -> int:
    sum_cub_2 = 0
    for i in range(len(dataset)):
        sum_numbers_2 = 0
        number_2 = dataset[i]
        #print(number_2)
        while number_2 != 0:
            sum_numbers_2 = sum_numbers_2 + number_2 % 10
            number_2 = number_2 // 10
        if sum_numbers_2 % 7 == 0:
            sum_cub_2 = dataset[i]

    return sum_cub_2

def sum_list_3(dataset: list) -> int:
    sum_cub_3 = 0
    for i in range(len(dataset)):
        dataset[i] = dataset[i] + 17
        sum_numbers_3 = 0
        number_3 = dataset[i]
        while number_3 != 0:
            sum_numbers_3 = sum_numbers_3 + number_3 % 10
            number_3 = number_3 // 10
        if sum_numbers_3 % 7 == 0:
            sum_cub_3 = dataset[i]

    return sum_cub_3
my_list = []
for cub_x in range(1, 1001, 2):
    my_list.append(cub_x ** 3)
#print(my_list)
my_list_2 = []
for cub_y in range(1, 1001, 2):
    my_list_2.append(cub_y ** 3 + 17)
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list_2)
print(result_2)
result_3 = sum_list_3(my_list)
print(result_3)