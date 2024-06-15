class Pet:         #супер класс
    legs = 4
    tale = True

    def __str__(self):
        tale = 'да' if self.tale else 'нет'
        return "Всего ног: {}\nХвост присутствует - {}".format(self.legs, tale)
    
    def walk(self):
        print('Гуляет')


class Cat(Pet):    #под-класс
    def action(self):
        print('Мяу')

class Dog(Pet):
    def action(self):
        print('Гав')

class Frog(Pet):
    tale = False

    def action(self):
        print('Ква')

    def walk(self):
        print('Плавает')



tom = Cat()
bonie = Dog()

print(tom)
tom.walk()
tom.action()

print(bonie)
bonie.walk()
bonie.action()

frog = Frog()
print(frog)
frog.walk()
frog.action()