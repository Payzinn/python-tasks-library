from typing import Callable, Dict

PLUGINS: Dict[str, Callable] = dict()

def register(func: Callable):
    """Регистрирует функцию как плагин"""
    PLUGINS[func.__name__] = func
    return func

@register
def greeting(name: str)->str:
    return "Hello {}".format(name)

@register
def bye(name: str)->str:
    return "Bye {}".format(name)

print(PLUGINS)
#print(greeting('TOM'))