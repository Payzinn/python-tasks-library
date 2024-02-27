class Ship:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return 'Модель: {}'.format(self.__model)
    
    def sail(self):
        print('Плыву по воде...') 
    

class Warship(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print('\nКорабль атакует с помощью: {}'.format(self.gun))


class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.tonnage_load = 0

    def load(self):
        print('Загружаем корабль')
        self.tonnage_load += 1
        print('Текущая загруженность {}'.format(self.tonnage_load))
    
    def unload(self):
        print('Разгружаем корабль')

        if self.tonnage_load > 0:
            self.tonnage_load -= 1
        else:
            print('На корабле нет груза')

        print('Текущая загруженность {}'.format(self.tonnage_load))


warship = Warship('Briga', 'UZI-190')

cargo = CargoShip('Newman')
cargo.load()