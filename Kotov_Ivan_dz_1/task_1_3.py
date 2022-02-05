
def transform_string(number: int) -> str:

    if number % 10 == 1:
        return f'{number} процент'
    elif number % 10 == 4:
        return f'{number} процента'
    elif number % 10 <= 9 :
        return f'{number} процентов'
    elif number % 10 <= 0:
        return  f'{number} процентов'



for n in range(1, 101):
    print(transform_string(n))


