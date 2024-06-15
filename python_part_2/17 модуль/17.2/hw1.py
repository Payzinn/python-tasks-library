from typing import Callable
import functools
def decorator(func: Callable)->Callable:
    counter = 0
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        #global counter
        nonlocal counter
        result = func(*args, **kwargs)
        counter += 1
        print('Функция была вызвана {} раз'.format(counter))
        return result

    return wrapped

counter = 0

@decorator
def hello(name: str) -> str:
    print('Hello {}'.format(name))


hello('nick')
hello('vicka')