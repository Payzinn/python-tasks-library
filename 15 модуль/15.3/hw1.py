from abc import ABC, abstractmethod


class Music:
    def play(self):
        print('Я на тебе как на войне,\nА на войне как на тебе,\nНо я устал окончен бой\nБеру портвейн иду домой\nОкончен бой, зачах огонь\nИ не разлучны мы с тобой,\nА мы с тобой, а нам с тобой\nПовезло на зло')


class Transport(ABC):

    @abstractmethod
    def ride_on_water(self):
        pass

    @abstractmethod
    def ride_on_road(self):
        pass



class Car(Transport):
    
    def ride_on_road(self):
        print('Едем по земле')





class Boat(Transport):

    def ride_on_water(self):
        print('Плыву по воде')


class Amphibian(Car, Boat, Music):
    pass


amph_transport = Amphibian()
amph_transport.ride_on_road()
amph_transport.ride_on_water()
amph_transport.play()


