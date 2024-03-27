from typing import List

class Person:
    """ Базовый класс человек """

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def shout(self):
        print('Я - человек!')


class Employee(Person):
    """ Работник. Дочерний класс от Person """

    def __init__(self, name: str, age: int, salary: int) -> None:
        super().__init__(name, age)
        self.__salary = 20000

    def get_salary(self):
        return self.__salary
    
    def shout(self):
        print('Я - работник!')

    

class Parent(Person):
    """ Родитель. Дочериний класс от Person """

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, 100)
        self.__kids = ['Tom', 'Bob']

    def get_kids(self) -> List[str]:
        return self.__kids
    
    def shout(self):
        print('Я - родитель!')
    

class Citizen(Parent, Employee):
    """Житель - является и родителем и работником"""
    def shout(self):
        print('Я - житель!')

my_citizen = Citizen(name = 'Nikita', age=18)
print(my_citizen.get_salary())
print(my_citizen.get_kids())
print(my_citizen.shout())

print(my_citizen.__class__.__mro__)