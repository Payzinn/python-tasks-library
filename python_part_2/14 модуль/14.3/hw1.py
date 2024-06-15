from typing import Callable, Any
def do_twice(func: Callable)->Callable:
    def wrapped(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapped

@do_twice
def greeting(name: str) -> None:
    print('Привет {}!'.format(name))


greeting('Tom')