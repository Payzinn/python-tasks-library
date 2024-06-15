def first():
    def add_num(seq, number):
        seq = list(seq)
        for i_num in range(len(seq)):
            seq[i_num] += number
        return seq

    origin_tuple = (3, 1, 4, 1, 5)
    changed_tuple = add_num(origin_tuple, 5)
    print(origin_tuple)
    print(changed_tuple)

def second():
    nums = (10, 20, 30, 40)
    print(nums.index(30))
    some_list = [1,1,1]
    some_tuple = tuple(some_list)
    print(some_tuple)
    bums = (10,20,30, some_list)
    print(bums)

def three():
    user = 'Vova', 'Petrov', 25
    name, surname, age = user
    print(name, surname, age)


def fourth():
    def get_user():
        name = 'Bob'
        surname = 'Ivanov'
        age = 20
        return name, surname, age

    user = get_user()
    print(user)

#Home Task
import random as r
def one():
    def generate_tuple(a, b, c):
        return tuple([r.randint(a,b) for _ in range(c)])
    
    first = generate_tuple(0, 5, 10)
    second = generate_tuple(-5, 0, 10)
    print('first: {} \nsecond: {}'.format(
        first,
        second))
    
    third = first + second
    print('Объединенный кортеж: {}'.format(third))

    nulls = third.count(0)
    print('Кол-во 0: {}'.format(nulls))

import math
def two():#Площадь цилиндра

    def cylinder(r,h):
        side = 2*math.pi * r * h
        full = side + 2 * math.pi * r**2
        return side, full
    
    radius_input = int(input('Введите радиус: '))
    height_input = int(input("Введите высоту: "))
    first, second = cylinder(radius_input, height_input)
    print('Площадь боковой поверхности: {}\nПолная площадь: {}'.format(first,second))
    

def three():

    def change(nums):
        index = r.randint(0, 5) % len(nums)
        value = r.randint(100, 1000)
        nums = list(nums)
        nums[index] = value
        return tuple(nums), value

    my_nums = 1, 2, 3, 4, 5
    new_nums, rand_val = change(my_nums)
    print(new_nums, rand_val)

    new_nums_2, rand_val_2 = change(new_nums)
    rand_val += rand_val_2
    print(new_nums_2, rand_val_2)

three()