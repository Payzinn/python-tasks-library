import functools
from typing import Callable, Any, Optional
import time

def decorator(_func: Optional[Callable] = None,*,seconds: int = 2):
    def wrapped_decor(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            time.sleep(seconds)
            func(*args, **kwargs)
        
        return wrapped_func
    if _func is None:
        return wrapped_decor
    else:
        return wrapped_decor(_func)
    
@decorator(seconds=5)
def greeting():
    print ("Hello")


greeting()