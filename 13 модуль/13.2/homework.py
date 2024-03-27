import random
n = int(input('Введите кол-во чисел: '))
numbers = [random.randint(1,100) for _ in range(n)]
print(numbers)
iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    
    except StopIteration:
        print("Конец!")
        break

    