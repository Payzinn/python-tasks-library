class Toyota:
    color = 'red'
    price = 1e6
    max_speed = 200
    current_speed = 0
    
    def info(self):
        print("Car's color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}".format(self.color, self.price, self.max_speed, self.current_speed))
    
    def change_speed(self, amount):
        self.current_speed += amount


car_1 = Toyota()

car_1.info()
car_1.change_speed(155)
car_1.info()