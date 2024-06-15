import random
class Person:
    def __init__(self, name, hungry_status = 50, house = True):
        self.name = name
        self.hungry_status = hungry_status
        self.house = house

    def eat(self, fridge):
        self.hungry_status += 10
        fridge.minus_food()

    def work(self, money):
        self.hungry_status -= 10
        money.salary()

    def play(self):
        self.hungry_status -= 10

    def go_market(self, fridge, money):
        fridge.plus_food()
        money.minus_money()

    def live(self, house):
        dice = random.randint(1,6)
        if self.hungry_status < 20:
            self.eat()
        elif house.get_food() < 10:
            self.go_market()
        elif house.get_money() < 50:
            self.work(house)
        elif dice == 1:
            self.work(house)
        elif dice == 2:
            self.eat()
        else:
            self.play()


        
class House:
    def __init__(self, fridge = 50, money = 0):
        self.fridge = fridge
        self.money = money

    def get_food(self):
        return self.fridge
    
    def get_money(self):
        return self.money
    
    def minus_food(self):
        self.fridge -= 10

    def plus_food(self):
        self.fridge += 10

    def salary(self):
        self.money += 10

    def minus_money(self):
        self.money -= 10


house = House()
tom = Person('Tom')
tom.live(house)