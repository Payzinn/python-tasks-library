from collections.abc import Iterable

class Person:

    def __init__(self, name: str, age: int, friend: list) -> None:
        self.name = name
        self.friend = friend
        self.set_age(age)
    
    def __str__(self) -> str:
        return "Имя: {}\tВозраст: {}".format(self.name, self.__age)
    
    def get_age(self) -> int:
        return self.__age
    
    
    def set_age(self, age: int) -> None: #сеттер
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception('Недопустимый возраст')
        

def fibonacci(number: int) -> Iterable[int]:
    cur_val = 0
    next_val = 1
    for _ in range(number):
        yield cur_val
        cur_val, next_val = next_val, cur_val + next_val
        if cur_val > 10 ** 6:
            return
        

tom = Person(5,5,5)