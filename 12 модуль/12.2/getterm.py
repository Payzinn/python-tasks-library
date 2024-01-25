class Person:
    __count = 0

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        Person.__count += 1
    
    def __str__(self):
        return "Имя: {}\tВозраст: {}".format(self.__name, self.__age)
    
    def get_age(self):
        return self.__age
    
    def get_count(self): #геттер
        return self.__count
    
    def set_age(self, age): #сеттер
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception('Недопустимый возраст')
    

misha = Person('Misha', 20)
tom = Person('Tom', 25)
new_age = 10
misha.set_age(new_age)
print(misha)