class Robot:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return "Модель: {}".format(self.__model)
    

class VacuumRobot(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.trash_bin = 0

    def operate(self):
        self.trash_bin += 1
        print(f"Начинаю пылесосить {self.trash_bin}")

class WarRobot(Robot):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print(f"Защищаю военный объект с помощью: {self.gun}")

class UnderWaterRobot(WarRobot):
    def __init__(self, model, gun):
        super().__init__(model, gun)
    
    def operate(self):
        print(f'Охраняю под водой с помощью: {self.gun}')
    


vacuum = VacuumRobot('Samsung')
vacuum.operate()
print(vacuum)
war = WarRobot('Xiaomi', 'UZI-P90')
war.operate()
print(war)
underwater = UnderWaterRobot('Oppo', 'Iskander')
underwater.operate()
print(underwater)