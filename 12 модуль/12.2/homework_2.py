class Human:
    __count = 0
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        Human.__count += 1

    def __str__(self):
        return 'Имя: {}\nВозраст: {}'.format(self.__name, self.__age)
    
    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise Exception('Имя должно состоять из букв')
        
    def get_age(self):
        return self.__age
    
    def get_count(self):
        return self.__count
    
    def set_age(self, age):
        if age in range(0,100):
            self.__age = age
        else:
            raise Exception('Возраст должен быть от 0 до 100')
        

Thomas  = Human('Tom', 25)
Thomas.set_age(22)
Thomas.set_name('Bob')
print(Thomas)