from typing import Callable, Any, Optional
import functools

def repeat(amount: int):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            for i in range(amount-1):
                func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapped_func
    return decorator

@repeat(3)
def greeting():
    print ("Hello")


greeting()