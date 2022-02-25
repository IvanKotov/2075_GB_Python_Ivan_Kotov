from functools import wraps


def val_checker(valid_func):
    def _checker(func):

        @wraps(func)
        def valid(x):
            if isinstance(x, valid_func) and x >= 0:
                return func(x)
            raise ValueError(f'Wrong value {x}')

        return valid

    return _checker


@val_checker(int)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3

if __name__ == '__main__':
    print(calc_cube(5))
    #print(calc_cube('ss'))