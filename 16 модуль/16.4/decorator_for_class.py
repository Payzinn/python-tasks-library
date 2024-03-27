import functools
from datetime import datetime
from typing import Callable, Any
import time
def create_time(cls):
    """
    This function creates a timestamp for a new entry in the database.

    Args:
        cls (class): The class that the function is being called from.

    Returns:
        str: The timestamp for the new entry.
    """    
    @functools.wraps(cls)
    def wrapper(*args, **kwargs) -> str:
        instance = cls(*args, **kwargs)
        print('Время создания: {}'.format(datetime.utcnow()))
        return instance
    return wrapper

def timer(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        started_at = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        run = round(end - started_at, 4)
        print('Функция работала: {}'.format(run))
        return result
    return wrapped_func

def for_all_methods(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorate(cls):
        for method_name in dir(cls):
            if method_name.startswith('__') is False:
                cur_method = getattr(cls, method_name)
                decorated_method = decorator(cur_method)
                setattr(cls, method_name, decorated_method)
        return cls
    return decorate

@create_time
@for_all_methods(timer)
class Functions:
    def __init__(self, max_num) -> None:
        self.max_num = max_num

    def squares_sum(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**2 for i_num in range(self.max_num)])
        return result
    
    def cubes(self, number: int) -> int:
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**3 for i_num in range(self.max_num)])
        return result


my_func1 = Functions(max_num = 1000)
time.sleep(1)
my_func2 = Functions(max_num = 2000)
time.sleep(1)
my_func3 = Functions(max_num = 3000)


my_func1.squares_sum()
my_func1.cubes(number=2000)

