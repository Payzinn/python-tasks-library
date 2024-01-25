class Dot:
    __x = 0
    __y = 0

    def __init__(self, x = 0, y = 0):
        self.set_y(y)
        self.set_x(x)

    def __str__(self):
        return "Координаты: x: {} y: {}".format(self.__x, self.__y)
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y


    

tochka = Dot(5,5)
tochka.set_x(7)
print(tochka)
print(tochka.get_x())