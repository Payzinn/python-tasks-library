import random as r

def first():
    squares_odds = [x**2 for x in range (10) if x % 2 != 0]
    squares_cubes = [(x**2 if x % 2 != 0 else x**3) for x in range (10)]
    print(squares_cubes)
    print(squares_odds)

def second():
    squad_1 = [r.randint(50,80) for _ in range (10)]
    squad_2 = [r.randint(30,60) for _ in range (10)]
    squad_3_condition = [("Погиб" if squad_1[i_damage] + squad_2[i_damage]> 100 
                          else 'Выжил') 
                          for i_damage in range(10)]
    
    print(f'Урон первого отряда:{squad_1} ')
    print(f'Урон второго отряда:{squad_2} ')
    print(f'Состояние третьего отряда:{squad_3_condition} ')


#HomeTask

def one():
    a = r.randint(2,21)
    b = r.randint(2,21)
    even_nums = [x for x in range(a,b) if x % 2 == 0]
    print(even_nums)

def two():
    original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
    new_prices = [(x if x > 0 else 0) for x in original_prices]
    print(new_prices)

