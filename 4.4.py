import random as r
def first():
    #1
    nums = [x for x in range(1,101) if x % 10 == 0]
    new_nums = nums[:]
    new_nums[3] = 0
    print(new_nums[2:8])
    print(nums[2:8])

def second(): 
    #2
    nums = [x for x in range(1,101) if x % 10 == 0]
    new_nums = nums[:]
    new_nums[3] = 0
    print(nums[2:8:2])

def third():
    #3
    nums = [x for x in range(1,101) if x % 10 == 0]
    new_nums = nums[:]
    new_nums[3] = 0
    print(nums[::-1])

def fourth():
    #4
    def is_palindrome(num_list):
        reversed_list = num_list[::-1]
        if num_list == reversed_list:
            return True
        else:
            return False
        
    nums = int(input('Количество чисел: '))
    digits = []
    for _ in range(nums):
         ask = int(input('Число: '))
         digits.append(ask)

    answer = []

    for i in range(0, len(digits)):
        if is_palindrome(digits[i:len(digits)]):
            answer = digits[:i]
            answer.reverse()
            break

    print(f'Исходный список {digits}')
    print(f'Нужно чисел для палиндрома {len(answer)}')
    print(f'Сами числа {answer}')

#HomeTask

def one():

    original_prices = [r.randint(-15, 20) for i in range(5)]
    new_prices = original_prices[:]
    for i in range(len(original_prices)):
        if new_prices[i] < 0:
            new_prices[i] = 0
    print("Мы потеряли: ", abs(sum(original_prices) - sum(new_prices)))


def two():
    nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
    print(f"1: {nums[:5]}")
    print(f"2: {nums[:-2]}")
    print(f"3: {nums[::2]}")
    print(f'4: {nums[1::2]}')
    print(f'5: {nums[::-1]}')
    print(f'6: {nums[::-2]}')

def three():
    n = int(input("Введите количество чисел N: "))
    numbers = [r.randint(-10, 10) for _ in range(n)]
    a = r.randint(0, len(numbers) - 2)
    b = r.randint(a + 1, len(numbers) - 1)
    print(numbers, a, b)
    numbers = numbers[:a] + numbers[b + 1:]
    print(numbers)

three()
