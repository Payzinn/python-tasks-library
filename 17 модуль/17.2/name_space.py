def f3():
    def f4():
        # global number
        nonlocal number
        number = 10
        print('f4 = {}'.format(number))

    number = 30
    print('number f3 = {}'.format(number))
    f4()
    print('number f3 = {}'.format(number))
    

number = 100

print('global number = {}'.format(number))
f3()
print('global number = {}'.format(number))
