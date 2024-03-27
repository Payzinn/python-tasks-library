import time
from typing import Callable, Any

def timer(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        started_at = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        run = round(end - started_at, 4)
        print('Функция работала: {} секунд(ы)'.format(run))
        return result
    return wrapped_func

def logging(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        print('\nВызывается функция: {} \tПозиционные аргументы: {} \tИменнованые аргументы: {}'.format(func.__name__, args, kwargs))
        result = func(*args, **kwargs)
        print('Функция завершила работу.')
        return result
    return wrapped_func

@logging
@timer
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**2 for i_num in range(10000)])
    return result

@timer
@logging
def cubes(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**3 for i_num in range(10000)])
    return result



my_sum = squares_sum()
print(my_sum)
my_cubes = cubes(200)
print(my_cubes)