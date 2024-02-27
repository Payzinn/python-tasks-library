class CanFly:
    def __init__(self):
        self.height = 0
        self.velocity = 0
    
    def __str__(self):
        return 'Высота: {}\tСкорость: {}'.format(self.height, self.velocity)

    def start_fly(self):
        pass
    
    def fly(self):
        pass

    def land(self):
        self.height = 0
        self.velocity = 0


class Butterfly(CanFly):
    def start_fly(self):
        self.height = 1
        print('Высота: {}'.format(self.height))
    
    def fly(self):
        self.velocity = 0.1
        print('Скорость: {}'.format(self.velocity))



class Rocket(CanFly):
    def start_fly(self):
        self.height = 500
        self.velocity = 1000
        print('Высота: {} \tСкорость {}'.format(self.height, self.velocity))
     
    def land(self):
        self.height = 0
        print('Высота: {}'.format(self.height))
        self.detonate()
    
    def detonate(self):
        print('Кабум...')


babochka = Butterfly()
babochka.start_fly()
babochka.fly()

print('\nРакета')
iskander = Rocket()
iskander.start_fly()
iskander.land()

    

    