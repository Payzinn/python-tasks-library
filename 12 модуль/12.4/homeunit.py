class Unit:
    def __init__(self, health):
        self.__health = health
    
    def set_hp(self, amount):
        self.__health = amount

    def get_hp(self):
        return self.__health
    
    def get_damage(self, amount):
        self.set_hp(self.get_hp() - 0) 

class Soldier(Unit):
    def get_damage(self, amount):
        self.set_hp(self.get_hp() - amount)


class Person(Unit):
    def get_damage(self, amount):
        self.set_hp(self.get_hp() - amount * 2)


sold = Soldier(100)
print(sold.get_hp())
sold.get_damage(25)
print(sold.get_hp())

print('Гражданский')
person = Person(100)
print(person.get_hp())
person.get_damage(25)
print(person.get_hp())