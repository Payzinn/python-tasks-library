class Pet:         #супер класс

    TOTAL_SOUNDS = 0


    def __init__(self) -> None:
        self.__legs = 4
        self.__tale = True

    def __str__(self):
        tale = 'да' if self.__tale else 'нет'
        return "Всего ног: {} Хвост присутствует - {}".format(self.__legs, tale)


class Cat(Pet):
    @classmethod
    def action(cls) -> None:
        cls.TOTAL_SOUNDS += 1
        print(cls.TOTAL_SOUNDS)
        print('Мяу')

class Dog(Pet):

    @classmethod
    def action(cls) -> None:
        cls.TOTAL_SOUNDS += 1
        print(cls.TOTAL_SOUNDS)
        print('Гав')



Cat.action()
cat = Cat()
cat.action()
cat.action()