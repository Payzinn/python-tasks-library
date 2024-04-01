from typing import Callable
import functools

class CountCalls:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs) -> Callable:
        self.count += 1
        print('Вызов номер: {number} \t Функция: {function}'.format(number = self.count, function = self.func.__name__))
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello")


say_hello()
say_hello()
print(say_hello.count)