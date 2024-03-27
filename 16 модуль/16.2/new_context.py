import time
from contextlib import contextmanager
from collections.abc import Iterator

# class Timer:
#     def __init__(self) -> None:
#         print('Время работы кода')
#         self.start = None

#     def __enter__(self) -> 'Timer':
#         self.start = time.time()
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
#         print(time.time() - self.start)
#         # if exc_type is TypeError:
#         #     return True
#         return True

@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except Exception as e:
        print(type(e), ('Поймано исключение.'))
    finally:
        print(time.time() - start)

with timer() as t1:
    print('Первая часть')
    val_1 = 100 * 100 ** 100000
    val_1 += "abc"
with timer() as t2:
    print('Вторая часть')
    val_2 = 200 * 200 ** 100000
with timer() as t3:
    print('Третья часть')
    val_3 = 300 * 300 ** 100000