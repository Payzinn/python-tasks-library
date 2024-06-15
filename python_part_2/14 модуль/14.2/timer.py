import time
from typing import Callable, Any

def timer(func: Callable, *args, **kwargs) -> Any:
    started_at = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    run = round(end - started_at, 4)
    print('Функция работала: {}'.format(run))
    return result

def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**2 for i_num in range(10000)])
    return result

def cubes(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**3 for i_num in range(10000)])
    return result



my_result = timer(squares_sum)
print(my_result)
my_cube = timer(cubes, 200)
print(my_cube)