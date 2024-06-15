from contextlib import contextmanager
from collections.abc import Iterable, Iterator
@contextmanager
def next_number(number: int) -> Iterator[int]:
    try:
        yield number + 1
    except ZeroDivisionError:
        print('На 0 делить нельзя!')

with next_number(-1) as next:
    print('Следующее число: {}'.format(next))
    print(10/next)