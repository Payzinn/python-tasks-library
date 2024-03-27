class Robot:
    """ Базовый класс робота """

    def __init__(self, model, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.model = model

    def __str__(self):
        res = super().__str__()
        return res + ' {} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Я робот')



class CanFly(Robot):
    def __init__(self, *args, **kwargs) -> None:
        self.altitude = 0
        self.velocity = 0        

    def take_off(self):
        self.altitude = 100
        self.velocity = 300

    def fly(self):
        self.altitude = 5000

    def land(self):
        self.altitude = 0
        self.velocity = 0

    def operate(self):
        super().operate()
        print('Летим')

    def __str__(self):
        res = super().__str__()
        return res + ' {} высота {} скорость {}'.format(
            self.__class__.__name__, 
            self.altitude, self.velocity,
        )

class ScoutDrone(CanFly, Robot):
    def __init__(self,model) -> None:
        super().__init__(model = model)

    def operate(self):
        super().operate()
        print('Робот ведёт разведку с воздуха')


class WarDrone(CanFly, Robot):
    def __init__(self, model, gun) -> None:
        super().__init__(model = model)
        self.gun = gun
        self.model = model

    def operate(self):
        super().operate()
        print('Начинаю защиту базы при помощи {}'.format(self.gun))


ScoutDrone('Sapsan').operate()
print()
war = WarDrone('IGIL', 'Byraktar')
war.operate()
print(war)