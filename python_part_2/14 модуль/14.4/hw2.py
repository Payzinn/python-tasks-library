from typing import Callable, Dict

PLUGINS: Dict[str, Callable] = dict()

def decorator(func: Callable) -> Callable:
    PLUGINS[func.__name__] = func
    return func

@decorator
def greeting():
    print('Hello')

@decorator
def bye():
    print('bye')

print(PLUGINS)