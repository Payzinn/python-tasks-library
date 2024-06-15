class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, word: str):
        if isinstance(word, str):
            self.__name = word
        else:
            raise NameError('Имя должно состоять из букв')

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age: int) -> int:
        if age > 0 and age <= 100:
            self.__age = age
            return self.__age
        else:
            raise ValueError('Недопустимый возраст')

    def __repr__(self) -> str:
        return f"({self.name}, {self.age})"

first = Person('Perry', 25)
second = Person('Vika', 17)
third = Person('Nick', 18)
humans = [first, second, third]

print(humans)
humans.sort(key = lambda human: human.age)
print(humans)
humans.sort(key = lambda human: -human.age)
print(humans)