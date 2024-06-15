class Toyota:

    def __init__(self, color = 'white', price = 0, max_speed = 0, current_speed = 0):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def info(self):
        print("Car's color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}".format(self.color, self.price, self.max_speed, self.current_speed))
    
    def change_speed(self, amount):
        self.current_speed += amount

    
car_1 = Toyota('red', 200000, 250)
car_1.change_speed(151)
car_1.info()