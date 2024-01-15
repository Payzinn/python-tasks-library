class Potato:
    stadias ={0:'Отсутствует', 1:'Росток', 2:"Зелёное", 3:"Зрелая"}

    def __init__(self, index):
        self.index = index
        self.stadia = 0
    
    def grow(self):
        if self.stadia < 3:
            self.stadia += 1
        
        self.print_stadia()
        
    
    def print_stadia(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.stadias[self.stadia]))

    
    def is_ripe(self):
        if self.stadia == 3:
            return True
        
        return False

class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        
        for i_potato in self.potatoes:
            i_potato.grow()

    def is_grown(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
            
        else:
            print('Вся картошка созрела, можно собирать')


my_garden = PotatoGarden(5)
my_garden.is_grown()

for i in range(3):
    my_garden.grow_all()

my_garden.is_grown