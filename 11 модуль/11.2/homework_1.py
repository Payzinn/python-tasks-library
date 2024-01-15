import random
class Toyota:
    color = 'red'
    price = 1e6
    max_speed = 200
    current_speed = 0

car_1 = Toyota()
car_2 = Toyota()
car_3 = Toyota()

print(Toyota.price)

def car_func(*args):
    for car in args:
        car.current_speed = random.randint(0,200)
        print(car.current_speed)

car_func(car_1, car_2, car_3)



# car_1.current_speed = random.randint(0,200)
# print(car_1.current_speed)
# car_2.current_speed = random.randint(0,200)
# print(car_1.current_speed)
# car_3.current_speed = random.randint(0,200)
# print(car_1.current_speed)