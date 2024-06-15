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

    def get_name(self):
        return self.__name

    def set_age(self, age): #сеттер
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception('Недопустимый возраст')
        
class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                'Студент учится в универе {}'.format(self.university)
            )
        )
        return info
        #return 'Студент {} учится в универе {}'.format(self.get_name(), self.university)



class Employee(Person):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)
        self.company = company
        self.salary = salary

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                'Сотрудник работает в {}, з/п: {}'.format(self.company, self.salary)
            )
        )

        return info

my_student = Student('Tom', 24, 'MSU')
print(my_student)

my_employee = Employee('Vladislav', 48, 'SCP', 250000)
print(my_employee)