import time
from typing import Callable, Any, Optional
import functools

def timer_with_precision(_func: Optional[Callable] = None,*, precision: int = 5) -> Callable:
    def timer_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            started_at = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            run = round(end - started_at, precision)
            print('Функция работала: {}'.format(run))
            return result
        return wrapped_func
    if _func is None:
        return timer_decorator
    else:
        return timer_decorator(_func)
@timer_with_precision()
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**2 for i_num in range(10000)])
    return result

@timer_with_precision(precision=2)
def cubes(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**3 for i_num in range(10000)])
    return result



my_sum = squares_sum()
print(my_sum)
my_cubes = cubes(200)
print(my_cubes)