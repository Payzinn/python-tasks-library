from abc import ABC, abstractmethod


class Music:
    def play(self):
        print('Я на тебе как на войне,\nА на войне как на тебе,\nНо я устал окончен бой\nБеру портвейн иду домой\nОкончен бой, зачах огонь\nИ не разлучны мы с тобой,\nА мы с тобой, а нам с тобой\nПовезло на зло')


class Transport(ABC):
    def __init__(self, color: str, max_velocity: int) -> None:
        super().__init__()
        self._color = color
        self._max_velocity = max_velocity

    @abstractmethod
    def ride_on_water(self):
        pass

    @abstractmethod
    def ride_on_road(self):
        pass
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value: str):
        self._color = value

    @property
    def velocity(self):
        return self._max_velocity
    
    @velocity.setter
    def velocity(self, value):
        self._max_velocity = value
        


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


