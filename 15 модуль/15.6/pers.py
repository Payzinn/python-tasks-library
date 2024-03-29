class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return 'Имя: {}\tВозраст: {}'.format(self._name, self._age)
    
    @property
    def age(self):
        return self._age
    

    @age.setter
    def age(self, age):
        if age > 0 and age < 100:
            self._age = age
        else:
            raise Exception("Недопустимый возраст")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name
        return self._name
    
tom = Person("Tom", 25)
print(tom)
tom.age = 99
tom.name = 'vok'
print(tom.age)
print(tom)