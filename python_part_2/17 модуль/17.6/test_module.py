def func():
    print('Я функция func() из тест модуля')

if __name__ == '__main__':
    print('Здесь какой-то код')
    func()
else:
    print('Импортирован модуль ', __name__)
    