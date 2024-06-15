class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Shtorm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None
        
class Air():
    def __add__(self, other):
        if isinstance(other, Fire):
            return Shtorm()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None
    

class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        else:
            None

class Earth:
    pass


class Shtorm:
    answer = 'Шторм'

class Thunder:
    answer = 'Молния'

class Dust:
    answer = 'Пыль'

class Lava:
    answer = 'Лава'

class Steam:
    answer = 'Пар'
    
class Dirt:
    answer = 'Грязь'
    


water = Water()
air = Air()
answer = water + air
print(answer.answer)

water = Water()
fire = Fire()
answer = water + fire
print(answer.answer)

water = Water()
earth = Earth()
answer = water + earth
print(answer.answer)
