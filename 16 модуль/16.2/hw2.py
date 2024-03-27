from contextlib import contextmanager
from collections.abc import Iterator
import os

@contextmanager
def in_dir(path: str) -> Iterator[str]:
    cur_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    except FileNotFoundError:
        print("директория не найдена")
    finally:
        os.chdir(cur_path)


with in_dir('D:\\'):
    print(os.listdir())    