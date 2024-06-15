import random

class Warrior:
    def __init__(self):
        self.health = 100

    def __str__(self):
        return 'Здоровье: {}'.format(self.health)
    
    def attack(self, enemy):
        enemy.health -= 20


tom = Warrior()
bob = Warrior()

print(tom, bob)

while tom.health > 0 and bob.health > 0:
    random_attack = random.randint(1,2)
    

    if random_attack == 1:
        tom.attack(bob)
        print('Здоровье 2-го воина: {}'.format(bob.health))

    else:
        bob.attack(tom)
        print('Здоровье 1-го воина: {}'.format(tom.health))

if tom.health > 0:
    print('1-й выйграл')

else:
    print('2-й выйграл')