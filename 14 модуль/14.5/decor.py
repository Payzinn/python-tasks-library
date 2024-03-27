import time
import functools
from typing import Callable, Any

def timer(func: Callable) -> Callable:
    """Decorator"""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        started_at = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        run = round(end - started_at, 4)
        print('Функция работала: {}'.format(run))
        return result
    return wrapped_func

@timer
def squares_sum() -> int:
    """
    Функция нахождения суммы квадратов
    для каждого N от 0 до 10000,
    где 0 <= N <= 100
    """
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**2 for i_num in range(10000)])
    return result

@timer
def cubes(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**3 for i_num in range(10000)])
    return result


print(squares_sum.__doc__)
print(squares_sum.__name__)