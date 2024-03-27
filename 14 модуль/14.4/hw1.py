from typing import Callable, Any

def decorator(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        print("</----------\>")
        result = func(*args, **kwargs)
        print('<\______/>')
        return result
    return wrapped_func

@decorator
def sandwich(*args):
    for ingridient in args:
        print("  {}".format(ingridient))

sandwich('помидор', "сыр", "огурчики","котлета")